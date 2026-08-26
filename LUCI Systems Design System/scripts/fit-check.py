#!/usr/bin/env python3
"""Fit check: measure natural height of each .doc-page in an HTML doc via headless Chrome.

Usage:
  python3 scripts/fit-check.py <html-file>
  python3 scripts/fit-check.py <html-file> --url http://127.0.0.1:8771/clients/foo.html

Pages are locked to US Letter (8.5x11in = 1056px) with overflow:hidden, so
scrollHeight returns the fixed height, not the true content height. This script
temporarily overrides height/overflow to measure the natural content height,
then reports overflow (+px over 1056) and underfill (px under 1056).

Exit codes: 0 = all pages fit, 1 = overflow detected, 2 = measurement error.
"""
import argparse, os, re, subprocess, sys, tempfile, pathlib, json

PROBE_JS = r"""
(() => {
  const pages = [...document.querySelectorAll('.doc-page')];
  return pages.map((p, i) => {
    const s = {h: p.style.height, mh: p.style.minHeight, o: p.style.overflow, jc: p.style.justifyContent};
    Object.assign(p.style, {height:'auto', minHeight:'0', overflow:'visible', justifyContent:'flex-start'});
    const nat = Math.round(p.getBoundingClientRect().height);
    Object.assign(p.style, s);
    const isDesign = p.classList.contains('doc-page--cover') || p.classList.contains('doc-page--close');
    const titleEl = p.querySelector('.doc-page-band__title, h2');
    const title = titleEl ? titleEl.textContent.trim().slice(0, 60) : '';
    const footEl = p.querySelector('.doc-foot__page');
    const foot = footEl ? footEl.textContent.trim() : '';
    return {
      page: i + 1,
      foot: foot,
      nat: nat,
      over: nat - 1056,
      under: 1056 - nat,
      design: isDesign,
      title: title
    };
  });
})()
"""

def find_chrome():
    for c in [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Chromium.app/Contents/MacOS/Chromium",
        "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
        "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser",
    ]:
        if os.path.isfile(c):
            return c
    return None


# The probe runs inside the document itself. An earlier implementation loaded the
# document into an iframe from a file:// wrapper; iframe.onload never fired under
# headless Chrome's virtual time, so every run reported "_timeout_" and exited 2.
# That silent failure is why clipped pages shipped unnoticed. Injecting directly
# avoids the iframe and the same-origin problem entirely.
_INJECT = """
<script>
(() => {
  const emit = () => {
    try {
      const results = %s;
      document.title = '__RESULTS__' + JSON.stringify(results) + '__END__';
    } catch (e) {
      document.title = '__ERROR__' + e.message + '__END__';
    }
  };
  const go = () => {
    // Fonts change line-wrapping, so measuring before they load understates height.
    const ready = document.fonts && document.fonts.ready
      ? document.fonts.ready
      : Promise.resolve();
    ready.then(() => setTimeout(emit, 600));
  };
  if (document.readyState === 'complete') go();
  else window.addEventListener('load', go);
})();
</script>
""" % PROBE_JS


def _run_probe(html_text, work_dir, label):
    """Inject the probe into html_text, render it, and return the parsed results.

    work_dir must be the directory the document's relative asset paths resolve
    against, so the temp copy sees the same CSS and fonts as the real file.
    """
    chrome = find_chrome()
    if not chrome:
        print("No Chrome found in /Applications.", file=sys.stderr)
        return None
    if "</body>" in html_text:
        html_text = html_text.replace("</body>", _INJECT + "</body>", 1)
    else:
        html_text += _INJECT
    tmp = pathlib.Path(work_dir) / f"_fitcheck_{os.getpid()}_{label}"
    tmp.write_text(html_text)
    try:
        proc = subprocess.run(
            [chrome, "--headless=new", "--disable-gpu", "--no-sandbox",
             "--hide-scrollbars", "--virtual-time-budget=20000",
             "--run-all-compositor-stages-before-draw",
             "--dump-dom", tmp.as_uri()],
            capture_output=True, text=True, timeout=90)
    except subprocess.TimeoutExpired:
        print("Fit check timed out.", file=sys.stderr)
        return None
    finally:
        tmp.unlink(missing_ok=True)
    m = re.search(r'__RESULTS__(.*?)__END__|__ERROR__(.*?)__END__', proc.stdout, re.S)
    if not m:
        print("Fit check: no results captured (is .doc-page present?).", file=sys.stderr)
        return None
    if m.group(2) is not None:
        print(f"Fit check ERROR: {m.group(2)}", file=sys.stderr)
        return None
    return json.loads(m.group(1))


def measure_via_url(url):
    """Measure pages served by the dev server.

    The document is fetched and rewritten with a <base href> so its relative
    asset paths keep resolving against the server while the probe runs locally.
    """
    import urllib.request, urllib.parse
    try:
        with urllib.request.urlopen(url, timeout=20) as r:
            html = r.read().decode("utf-8", "replace")
    except Exception as e:
        print(f"Fit check: could not fetch {url} ({e}).", file=sys.stderr)
        return None
    base = urllib.parse.urljoin(url, ".")
    tag = f'<base href="{base}">'
    if "<head>" in html:
        html = html.replace("<head>", "<head>\n" + tag, 1)
    else:
        html = tag + html
    return _run_probe(html, tempfile.mkdtemp(prefix="fitcheck-"), "url.html")


def measure_via_file(html_path):
    """Measure pages by rendering the file in place (relative assets resolve)."""
    return _run_probe(html_path.read_text(), html_path.parent, html_path.name)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("html", help="Path to the HTML file to check")
    ap.add_argument("--url", default=None,
                    help="Dev server URL (e.g. http://127.0.0.1:8771/clients/foo.html). "
                         "Use this when the file is served by the dev server (CSS/fonts resolve).")
    args = ap.parse_args()

    html_path = pathlib.Path(args.html).resolve()
    if not html_path.is_file():
        sys.exit(f"file not found: {html_path}")

    if args.url:
        results = measure_via_url(args.url)
    else:
        results = measure_via_file(html_path)

    if results is None:
        sys.exit(2)

    print(f"=== Fit check: {html_path.name} ===")
    any_overflow = False
    for d in results:
        over = d["over"]
        under = d["under"]
        design = d["design"]
        if over > 0:
            status = f"OVERFLOW (+{over}px)"
            any_overflow = True
        elif design:
            status = "OK (design page — empty space expected)"
        elif under > 200 and not design:
            status = f"UNDERFILL ({under}px empty)"
        else:
            status = "OK"
        print(f"  page {d['page']:02d} [foot:{d['foot']:>4s}] nat={d['nat']:5d}px  {status}  {d['title']}")
    print(f"=== (1056px = US Letter height limit) ===")
    if any_overflow:
        print("\n*** OVERFLOW DETECTED — run pack-content.py to repack ***")
        sys.exit(1)
    else:
        print("\nAll pages fit.")

if __name__ == "__main__":
    main()
