#!/usr/bin/env python3
"""Fit check: measure natural height of each .doc-page in an HTML doc via headless Chrome."""
import subprocess, tempfile, os, sys, re, pathlib

if len(sys.argv) < 2:
    print("Usage: python3 fit-check.py <html-file>"); sys.exit(1)

html_path = pathlib.Path(sys.argv[1]).resolve()
if not html_path.is_file():
    print("File not found:", html_path); sys.exit(1)

wrapper_dir = tempfile.mkdtemp(prefix="fitcheck-")
wrapper = os.path.join(wrapper_dir, "fit-check.html")

doc_uri = html_path.as_uri()

wrapper_html = f"""<!DOCTYPE html><html><head><meta charset="utf-8">
<style>html,body{{margin:0;padding:0;background:#fff;}}</style>
</head><body>
<iframe id="doc" style="width:816px;height:30000px;border:0;"></iframe>
<script>
const iframe = document.getElementById('doc');
iframe.onload = () => {{
  try {{
    const doc = iframe.contentDocument;
    const pages = doc.querySelectorAll('.doc-page');
    const results = [];
    pages.forEach((p, i) => {{
      const nat = p.scrollHeight;
      const title = (p.querySelector('.doc-page-band__title, h2') || {{}}).textContent || '';
      const page = (p.querySelector('.doc-foot__page') || {{}}).textContent || '';
      const status = nat <= 1056 ? 'OK' : 'OVERFLOW (+' + (nat - 1056) + ')';
      results.push((i+1) + ' [foot:' + page + '] nat=' + nat + ' ' + status + '  ' + title.trim().slice(0,50));
    }});
    document.title = '__RESULTS__' + results.join('|||') + '__END__';
  }} catch(e) {{ document.title = '__ERROR__' + e.message + '__END__'; }}
}};
iframe.src = {doc_uri!r};
</script>
</body></html>"""

with open(wrapper, "w") as f:
    f.write(wrapper_html)

chrome = None
for c in ["/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
         "/Applications/Chromium.app/Contents/MacOS/Chromium"]:
    if os.path.isfile(c):
        chrome = c; break
if not chrome:
    print("No Chrome found."); sys.exit(1)

try:
    proc = subprocess.run(
        [chrome, "--headless", "--disable-gpu", "--no-sandbox",
         "--virtual-time-budget=10000", "--run-all-compositor-stages-before-draw",
         "--dump-dom", wrapper],
        capture_output=True, text=True, timeout=60)
    out = proc.stdout
except subprocess.TimeoutExpired:
    print("Fit check timed out."); sys.exit(2)

m = re.search(r'__RESULTS__.*?__END__|__ERROR__.*?__END__', out, re.S)
if not m:
    print("Fit check: no results captured (page may not have finished loading).")
    print("--- stderr tail ---")
    print(proc.stderr[-500:] if proc.stderr else "(empty)")
    sys.exit(2)

inner = m.group(0)
if inner.startswith("__ERROR__"):
    print("Fit check ERROR:", inner[len("__ERROR__"):-len("__END__")]); sys.exit(3)

results = inner[len("__RESULTS__"):-len("__END__")].split("|||")
print("=== Fit check:", html_path.name, "===")
any_overflow = False
for r in results:
    print(r)
    if "OVERFLOW" in r:
        any_overflow = True
print("=== (1056px = US Letter height limit) ===")
if any_overflow:
    print("\n*** OVERFLOW DETECTED — needs repacking ***")
    sys.exit(1)
else:
    print("\nAll pages fit.")
