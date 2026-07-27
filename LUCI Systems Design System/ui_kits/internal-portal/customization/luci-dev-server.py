#!/usr/bin/env python3
"""LUCI dev server — serves the project folder and accepts POST /__save
to write edited HTML back to the working file on disk.

Run from the project root:  python3 luci-dev-server.py
Listens on 127.0.0.1:8771 (localhost only — never exposed to the network).

The edit bar's "Save" button POSTs the serialized DOM here; this script
writes it to the file on disk so Cursor (the agent) reads the latest version
on the next pass — no prompting required.
"""

import http.server
import json
import socketserver
import sys
from pathlib import Path
from urllib.parse import unquote

PORT = 8771
ROOT = Path.cwd().resolve()


class LUCIDevHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def end_headers(self):
        # Allow the edit bar (same origin) to POST; harmless on localhost.
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(204)
        self.end_headers()

    def do_POST(self):
        if self.path != '/__save':
            self.send_error(404, 'Not found')
            return

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

        # Strip leading slash, resolve, and confirm it stays inside ROOT.
        rel = unquote(rel_path).lstrip('/')
        target = (ROOT / rel).resolve()
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
    print('  Save endpoint: POST /__save')
    print('  Ctrl+C to stop.')
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\nStopping.')
        server.shutdown()


if __name__ == '__main__':
    main()
