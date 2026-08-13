#!/usr/bin/env python3
"""LUCI dev server — serves the project folder and accepts:
  POST /__save  — write edited HTML back to the working file on disk
  POST /__pdf   — render that HTML to PDF via scripts/render-pdf.sh (headless
                  Chrome). Never uses window.print() — that crashes Cursor's
                  in-editor browser.

Run from the project root:  python3 luci-dev-server.py
Listens on 127.0.0.1:8771 (localhost only — never exposed to the network).

The edit bar's "Save" button POSTs the serialized DOM here; this script
writes it to the file on disk so Cursor (the agent) reads the latest version
on the next pass — no prompting required.
"""

import http.server
import json
import os
import re
import datetime
import socketserver
import subprocess
import sys
import tempfile
from pathlib import Path
from urllib.parse import unquote

PORT = 8771
ROOT = Path.cwd().resolve()
SCRIPT_DIR = Path(__file__).resolve().parent
# Bump when endpoints/behavior change — edit bar checks GET /__health.
SERVER_VERSION = 3
SERVER_FEATURES = ('save', 'pdf')


def _check_pdf_deps():
    """Check whether the PDF render pipeline has its dependencies.
    Returns a dict with 'chrome' (bool), 'pil' (bool), and 'chrome_path' (str|None)."""
    chrome_paths = [
        '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
        '/Applications/Chromium.app/Contents/MacOS/Chromium',
        '/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge',
        '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser',
    ]
    chrome_path = None
    for p in chrome_paths:
        if Path(p).exists():
            chrome_path = p
            break
    try:
        from PIL import Image  # noqa: F401
        import numpy  # noqa: F401
        has_pil = True
    except ImportError:
        has_pil = False
    return {'chrome': bool(chrome_path), 'pil': has_pil, 'chrome_path': chrome_path}


# PDF filename convention: "<ClientName>-<DocType> <M+D+YY>.pdf"
# e.g. "Elwha River Casino-Proposal-LUCI-Retrofit 81326" (Aug 13 '26).
# Longest doc-type slug first so "proposal-luci-retrofit" wins over "proposal".
_DOC_TYPE_DISPLAY = [
    ('proposal-luci-retrofit', 'Proposal-LUCI-Retrofit'),
    ('capabilities-document', 'Capabilities-Document'),
    ('budgetary-estimate', 'Budgetary-Estimate'),
    ('proposal-upgrade', 'Proposal-Upgrade'),
    ('scope-of-work', 'Scope-of-Work'),
    ('sales-deck', 'Sales-Deck'),
    ('proposal', 'Proposal-LED'),
]


def _pdf_display_name(html_path):
    """Build the convention PDF filename: <ClientName>-<DocType> <M+D+YY>.pdf

    ClientName is read from the document <title> — the customization templates
    set it as "LUCI — <Doc> · <Client>" (newer) or "<Client> — <Doc>" (older);
    we prefer the text after the last '·', then the text before the first ' — '
    when that left side isn't "LUCI", and finally fall back to title-casing the
    client slug. DocType is the longest known doc-type suffix of the HTML stem,
    mapped to its display name. The date is today's export date — month and day
    without leading zeros (e.g. 81326 = Aug 13 '26).
    """
    stem = html_path.stem  # <client-slug>-<doc-type>
    doc_type = None
    client_slug = stem
    for slug, display in _DOC_TYPE_DISPLAY:
        marker = '-' + slug
        if stem.endswith(marker) and len(stem) > len(marker):
            doc_type = display
            client_slug = stem[:-len(marker)]
            break
    if doc_type is None:
        doc_type = stem  # unknown doc-type — use the stem verbatim

    # Client name from <title> (authoritative); fallback to slug title-case.
    client_name = None
    try:
        html = html_path.read_text(encoding='utf-8', errors='replace')
        m = re.search(r'<title>(.*?)</title>', html, re.S)
        if m:
            title = m.group(1).strip()
            if '·' in title:
                client_name = title.split('·')[-1].strip()
            elif ' — ' in title:
                left = title.split(' — ')[0].strip()
                if left and left != 'LUCI':
                    client_name = left
    except Exception:
        pass
    if not client_name:
        client_name = ' '.join(w.capitalize() for w in client_slug.split('-') if w)

    now = datetime.date.today()
    date_str = f"{now.month}{now.day}{str(now.year)[2:]}"
    return f"{client_name}-{doc_type} {date_str}.pdf"


class LUCIDevHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    # Edit-bar assets, served from the customization folder in the project.
    EDIT_BAR_CSS = '/ui_kits/internal-portal/customization/luci-doc-edit.css'
    EDIT_BAR_JS = '/ui_kits/internal-portal/customization/luci-doc-edit.js'

    def end_headers(self):
        # Allow the edit bar (same origin) to POST; harmless on localhost.
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        # Edit-bar JS/CSS must never stick in Glass cache — stale copies still
        # called window.print() and crashed Cursor.
        path = unquote(getattr(self, 'path', '').split('?', 1)[0])
        if path.endswith(('luci-doc-edit.js', 'luci-doc-edit.css')):
            self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
            self.send_header('Pragma', 'no-cache')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(204)
        self.end_headers()

    def do_GET(self):
        path = unquote(self.path.split('?', 1)[0].split('#', 1)[0])
        if path == '/__health':
            deps = _check_pdf_deps()
            self._json(200, {
                'ok': True,
                'version': SERVER_VERSION,
                'features': list(SERVER_FEATURES),
                'pdf': True,
                'save': True,
                'pdfDeps': deps,
            })
            return

        # Intercept HTML responses so the edit bar (Save / Copy HTML / Download
        # PDF) is always present in the preview, regardless of whether the
        # working file on disk currently links luci-doc-edit.{css,js}. The
        # edit bar's serializeHtml() strips these tags before saving, so the
        # working file stays clean — but every serve re-injects them. This is
        # what keeps the buttons from disappearing after Cursor re-renders.
        if path.endswith('/'):
            path = path + 'index.html'
        # Normalize the path (resolve .. but do NOT follow symlinks yet) so
        # the security check sees the literal path within ROOT. Symlinks
        # (e.g. ui_kits/ → OneDrive/ui_kits/) are followed by the OS when
        # the file is actually read — the check just needs to confirm the
        # requested URL path is within the project root.
        import os as _os
        raw_path = ROOT / path.lstrip('/')
        norm_path = Path(_os.path.normpath(str(raw_path)))
        try:
            norm_path.relative_to(ROOT)
        except ValueError:
            self.send_error(403, 'Path outside project root')
            return
        fs_path = norm_path

        if fs_path.is_file() and fs_path.suffix.lower() == '.html':
            try:
                html = fs_path.read_text(encoding='utf-8')
            except Exception as e:
                self.send_error(500, str(e))
                return
            body = self._inject_edit_bar(html).encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.send_header('Content-Length', str(len(body)))
            self.send_header('Cache-Control', 'no-cache, must-revalidate')
            self.end_headers()
            self.wfile.write(body)
            return

        # Fall back to default static serving for non-HTML assets.
        super().do_GET()

    def _inject_edit_bar(self, html):
        # Only inject into actual LUCI sales docs (contain a doc page section).
        # Skip portal index pages, skill files rendered as HTML, etc.
        if 'doc-page' not in html and 'doc-cover' not in html:
            return html
        # Skip if the file already links the edit bar (e.g. a master that
        # already has them — don't double-inject).
        if 'luci-doc-edit.css' in html and 'luci-doc-edit.js' in html:
            return html
        # Cache-bust so Glass/Simple Browser always picks up edit-bar fixes.
        js_tag = '<script src="%s?v=5"></script>' % self.EDIT_BAR_JS
        css_tag = '<link rel="stylesheet" href="%s?v=5">' % self.EDIT_BAR_CSS
        head_close = html.rfind('</head>')
        if head_close != -1:
            return html[:head_close] + css_tag + js_tag + html[head_close:]
        # No </head> — inject before </body> as a fallback.
        body_close = html.rfind('</body>')
        if body_close != -1:
            return html[:body_close] + js_tag + html[body_close:]
        return html + js_tag

    def do_POST(self):
        path = unquote(self.path.split('?', 1)[0])
        if path == '/__save':
            self._handle_save()
            return
        if path == '/__pdf':
            self._handle_pdf()
            return
        self.send_error(404, 'Not found')

    def _handle_save(self):
        length = int(self.headers.get('Content-Length', 0))
        raw = self.rfile.read(length) if length else b''
        try:
            data = json.loads(raw)
            rel_path = data.get('path', '')
            html = data.get('html', '')
        except (json.JSONDecodeError, AttributeError):
            self._json(400, {'error': 'Invalid JSON body'})
            return

        if not rel_path or not html:
            self._json(400, {'error': 'Missing "path" or "html"'})
            return

        # Strip leading slash, normalize (no symlink follow), confirm inside ROOT.
        rel = unquote(rel_path).lstrip('/')
        target = Path(os.path.normpath(str(ROOT / rel)))
        try:
            target.relative_to(ROOT)
        except ValueError:
            self._json(403, {'error': 'Path outside project root'})
            return

        try:
            target.write_text(html, encoding='utf-8')
        except Exception as e:
            self._json(500, {'error': str(e)})
            return

        self._json(200, {'ok': True, 'path': str(target)})

    def _find_render_script(self):
        # Prefer scripts next to the design-system root that owns this server
        # file, then fall back to cwd (Mike's per-job folder may mirror it).
        candidates = [
            SCRIPT_DIR.parents[2] / 'scripts' / 'render-pdf.sh',  # …/LUCI Systems Design System
            ROOT / 'scripts' / 'render-pdf.sh',
            ROOT / 'LUCI Systems Design System' / 'scripts' / 'render-pdf.sh',
        ]
        for c in candidates:
            if c.is_file():
                return c
        return None

    def _handle_pdf(self):
        """Render the on-disk HTML to PDF via headless Chrome — never print()."""
        length = int(self.headers.get('Content-Length', 0))
        raw = self.rfile.read(length) if length else b''
        try:
            data = json.loads(raw) if raw else {}
            rel_path = data.get('path', '') or ''
        except (json.JSONDecodeError, AttributeError):
            self._json(400, {'error': 'Invalid JSON body'})
            return

        if not rel_path:
            self._json(400, {'error': 'Missing "path"'})
            return

        rel = unquote(rel_path).lstrip('/')
        html_path = Path(os.path.normpath(str(ROOT / rel)))
        try:
            html_path.relative_to(ROOT)
        except ValueError:
            self._json(403, {'error': 'Path outside project root'})
            return

        if not html_path.is_file() or html_path.suffix.lower() != '.html':
            self._json(404, {'error': 'HTML file not found: %s' % rel})
            return

        render = self._find_render_script()
        if not render:
            self._json(500, {
                'error': 'scripts/render-pdf.sh not found. Run the LUCI dev server from the design-system project root.'
            })
            return

        # Pre-flight: check Chrome before running the pipeline.
        deps = _check_pdf_deps()
        if not deps['chrome']:
            self._json(500, {
                'error': 'Google Chrome (or Chromium/Edge/Brave) not found in /Applications. '
                         'Install Google Chrome to generate PDFs.'
            })
            return

        # Write PDF beside a temp dir so we never leave export debris in sales/.
        out_name = _pdf_display_name(html_path)
        tmp_dir = Path(tempfile.mkdtemp(prefix='luci-pdf-'))
        out_pdf = tmp_dir / out_name

        try:
            # render-pdf.sh expects to run with its design-system root context
            # (prepare-sales-pdf-assets.py lives next to it). cwd = script's parent.parent
            ds_root = render.parent.parent
            env = os.environ.copy()
            proc = subprocess.run(
                ['bash', str(render), str(html_path), str(out_pdf)],
                cwd=str(ds_root),
                env=env,
                capture_output=True,
                text=True,
                timeout=180,
            )
            if proc.returncode != 0 or not out_pdf.is_file():
                err = (proc.stderr or proc.stdout or 'render-pdf.sh failed').strip()
                self._json(500, {'error': err[-800:]})
                return

            pdf_bytes = out_pdf.read_bytes()
        except subprocess.TimeoutExpired:
            self._json(500, {'error': 'PDF render timed out (180s). Try again or ask Cursor to render it.'})
            return
        except Exception as e:
            self._json(500, {'error': str(e)})
            return
        finally:
            try:
                for p in tmp_dir.iterdir():
                    p.unlink(missing_ok=True)
                tmp_dir.rmdir()
            except Exception:
                pass

        self.send_response(200)
        self.send_header('Content-Type', 'application/pdf')
        self.send_header('Content-Disposition', 'attachment; filename="%s"' % out_name)
        self.send_header('Content-Length', str(len(pdf_bytes)))
        self.send_header('Cache-Control', 'no-store')
        self.end_headers()
        self.wfile.write(pdf_bytes)

    def _json(self, code, payload):
        body = json.dumps(payload).encode('utf-8')
        self.send_response(code)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt, *args):
        # Quieter logging — just method + path, not the full stderr spam.
        sys.stderr.write("  %s %s\n" % (args[0], args[1]))


class ThreadingServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    daemon_threads = True
    allow_reuse_address = True


def main():
    if not (ROOT / 'ui_kits').exists() and not (ROOT / 'assets').exists():
        print('Warning: no ui_kits/ or assets/ in current folder.', file=sys.stderr)
        print('   Run this from the project root that contains both.', file=sys.stderr)

    server = ThreadingServer(('127.0.0.1', PORT), LUCIDevHandler)
    print('LUCI dev server -> http://127.0.0.1:%d' % PORT)
    print('  Serving: %s' % ROOT)
    print('  Version: %s' % SERVER_VERSION)
    print('  Health:        GET  /__health')
    print('  Save endpoint: POST /__save')
    print('  PDF endpoint:  POST /__pdf  (headless Chrome — safe in Cursor)')
    print('  Ctrl+C to stop.')
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\nStopping.')
        server.shutdown()


if __name__ == '__main__':
    main()
