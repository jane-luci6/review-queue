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

def measure_via_url(url):
    """Measure pages by navigating headless Chrome to a URL (dev server must be running)."""
    chrome = find_chrome()
    if not chrome:
        print("No Chrome found in /Applications.", file=sys.stderr)
        return None
    wrapper_dir = tempfile.mkdtemp(prefix="fitcheck-")
    wrapper = os.path.join(wrapper_dir, "fit-check.html")
    wrapper_html = f"""<!DOCTYPE html><html><head><meta charset="utf-8">
<style>html,body{{margin:0;padding:0;background:#fff;}}</style>
</head><body>
<iframe id="doc" style="width:816px;height:30000px;border:0;"></iframe>
<script>
const iframe = document.getElementById('doc');
const poll = () => {{
  try {{
    const doc = iframe.contentDocument;
    if (!doc || !doc.querySelector('.doc-page')) {{ setTimeout(poll, 200); return; }}
    const results = {PROBE_JS.replace('document', 'doc')};
    document.title = '__RESULTS__' + JSON.stringify(results) + '__END__';
  }} catch(e) {{ document.title = '__ERROR__' + e.message + '__END__'; }}
}};
iframe.onload = poll;
iframe.src = {url!r};
setTimeout(() => {{ if (!document.title.startsWith('__')) document.title = '__ERROR__timeout__END__'; }}, 15000);
</script>
</body></html>"""
    with open(wrapper, "w") as f:
        f.write(wrapper_html)
    try:
        proc = subprocess.run(
            [chrome, "--headless=new", "--disable-gpu", "--no-sandbox",
             "--virtual-time-budget=20000", "--run-all-compositor-stages-before-draw",
             "--dump-dom", wrapper],
            capture_output=True, text=True, timeout=45)
    except subprocess.TimeoutExpired:
        print("Fit check timed out.", file=sys.stderr)
        return None
    m = re.search(r'__RESULTS__.*?__END__|__ERROR__.*?__END__', proc.stdout, re.S)
    if not m:
        print("Fit check: no results captured.", file=sys.stderr)
        return None
    inner = m.group(0)
    if inner.startswith("__ERROR__"):
        print(f"Fit check ERROR: {inner[8:-6]}", file=sys.stderr)
        return None
    return json.loads(inner[11:-6])

def measure_via_file(html_path):
    """Measure pages by loading the file directly in an iframe."""
    chrome = find_chrome()
    if not chrome:
        print("No Chrome found in /Applications.", file=sys.stderr)
        return None
    doc_uri = html_path.as_uri()
    wrapper_dir = tempfile.mkdtemp(prefix="fitcheck-")
    wrapper = os.path.join(wrapper_dir, "fit-check.html")
    wrapper_html = f"""<!DOCTYPE html><html><head><meta charset="utf-8">
<style>html,body{{margin:0;padding:0;background:#fff;}}</style>
</head><body>
<iframe id="doc" style="width:816px;height:30000px;border:0;"></iframe>
<script>
const iframe = document.getElementById('doc');
const poll = () => {{
  try {{
    const doc = iframe.contentDocument;
    if (!doc || !doc.querySelector('.doc-page')) {{ setTimeout(poll, 200); return; }}
    const results = {PROBE_JS.replace('document', 'doc')};
    document.title = '__RESULTS__' + JSON.stringify(results) + '__END__';
  }} catch(e) {{ document.title = '__ERROR__' + e.message + '__END__'; }}
}};
iframe.onload = poll;
iframe.src = {doc_uri!r};
setTimeout(() => {{ if (!document.title.startsWith('__')) document.title = '__ERROR__timeout__END__'; }}, 15000);
</script>
</body></html>"""
    with open(wrapper, "w") as f:
        f.write(wrapper_html)
    try:
        proc = subprocess.run(
            [chrome, "--headless=new", "--disable-gpu", "--no-sandbox",
             "--virtual-time-budget=20000", "--run-all-compositor-stages-before-draw",
             "--dump-dom", wrapper],
            capture_output=True, text=True, timeout=45)
    except subprocess.TimeoutExpired:
        print("Fit check timed out.", file=sys.stderr)
        return None
    m = re.search(r'__RESULTS__.*?__END__|__ERROR__.*?__END__', proc.stdout, re.S)
    if not m:
        print("Fit check: no results captured.", file=sys.stderr)
        return None
    inner = m.group(0)
    if inner.startswith("__ERROR__"):
        print(f"Fit check ERROR: {inner[8:-6]}", file=sys.stderr)
        return None
    return json.loads(inner[11:-6])

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
