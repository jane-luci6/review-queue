#!/usr/bin/env python3
"""Pack SOW sections and line items across pages with continuous flow.

Replaces the ad-hoc packing logic that was re-derived every session.

Usage:
  # SOW mode — element-level packing for .upg-scope blocks
  python3 scripts/pack-content.py <html> --mode sow \
      --start-page 3 --end-page 5 --url http://127.0.0.1:8771/clients/foo.html

  # Line-items mode — group-level packing for .be-price-group blocks
  python3 scripts/pack-content.py <html> --mode lineitems \
      --start-page 6 --end-page 14 --url http://127.0.0.1:8771/clients/foo.html

  # Dry run (show the plan, don't write)
  python3 scripts/pack-content.py <html> --mode sow --dry-run ...

  # Write the repacked HTML back to the file
  python3 scripts/pack-content.py <html> --mode sow --write ...

Requirements: Google Chrome in /Applications, dev server running at --url.
"""
from __future__ import annotations
import argparse, json, os, re, subprocess, sys, tempfile, pathlib

PAGE_HEIGHT = 1056
PAGE_OVERHEAD = 240
CONTENT_BUDGET = PAGE_HEIGHT - PAGE_OVERHEAD

# Footer page-number patterns (kept in sync with scripts/check-footers.py).
_PAGE_PATTERN = re.compile(
    r'(?:<!-- PAGE[^>]*-->\s*\n\s*)?<section class="doc-page[^>]*>.*?</section>', re.S)
_FOOTER_PATTERN = re.compile(
    r'<span class="doc-foot__page[^"]*"[^>]*>(\d+)</span>')
_MANGLE_TELLS = ('<span cla<span', 'div&gt;', '<span=""', 'class=doc-foot')


def verify_footers(html):
    """Return a list of footer-integrity issues in the packed HTML.

    Run after every --write so a broken renumber is caught immediately, not
    in the PDF. Mirrors scripts/check-footers.py — kept inline here because
    Python can't import a hyphenated module name.
    """
    pages = list(_PAGE_PATTERN.finditer(html))
    if not pages:
        return []  # non-paged document — footer check doesn't apply
    nums = []
    blocks = []
    for m in pages:
        block = m.group(0)
        blocks.append(block)
        fm = _FOOTER_PATTERN.search(block)
        nums.append(int(fm.group(1)) if fm else None)
    first_idx = next((i for i, n in enumerate(nums) if n is not None), None)
    if first_idx is None:
        return []  # paged but no numbered footers — nothing to verify
    last_idx = max(i for i, n in enumerate(nums) if n is not None)
    issues = []
    expected = nums[first_idx]
    for i, block in enumerate(blocks):
        idx = i + 1
        comment = block.split('-->', 1)[0] + '-->' if block.startswith('<!--') else '<!-- (no PAGE comment) -->'
        if any(tell in block for tell in _MANGLE_TELLS):
            issues.append(f"page {idx}: mangled footer markup ({comment.strip()})")
        if i < first_idx or i > last_idx:
            continue
        n = nums[i]
        if n is None:
            issues.append(f"page {idx}: missing .doc-foot__page number ({comment.strip()})")
        elif n != expected:
            issues.append(f"page {idx}: footer says '{n:02d}' but expected '{expected:02d}' ({comment.strip()})")
        expected += 1
    return issues

def find_chrome():
    for c in ["/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
             "/Applications/Chromium.app/Contents/MacOS/Chromium",
             "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
             "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"]:
        if os.path.isfile(c):
            return c
    return None

# ── Measurement ────────────────────────────────────────────────────────────

MEASURE_JS = r"""
(() => {
  const doc = iframe.contentDocument;
  if (!doc) return {error: "no iframe document"};
  const allPages = [...doc.querySelectorAll('.doc-page')];
  const targetPages = allPages.slice(START_PAGE - 1, END_PAGE);
  const elements = [];
  for (const page of targetPages) {
    for (const block of page.querySelectorAll('.upg-scope')) {
      for (const child of block.children) {
        const st = doc.defaultView.getComputedStyle(child);
        const mt = parseFloat(st.marginTop) || 0;
        const mb = parseFloat(st.marginBottom) || 0;
        const h = Math.ceil(child.getBoundingClientRect().height + mt + mb);
        let type = 'text';
        if (child.classList.contains('upg-scope__title')) type = 'title';
        else if (child.classList.contains('upg-scope__label')) type = 'label';
        else if (child.classList.contains('upg-scope__sub')) type = 'sub';
        else if (child.classList.contains('upg-scope__subsub')) type = 'subsub';
        else if (child.tagName === 'UL' || child.tagName === 'OL') type = 'list';
        elements.push({type, html: child.outerHTML, height: h,
                       text: child.textContent.trim().slice(0, 80)});
      }
    }
    for (const group of page.querySelectorAll('.be-price-group')) {
      const label = group.querySelector('.be-price-group__label');
      elements.push({type: 'group', html: group.outerHTML,
                     height: Math.ceil(group.getBoundingClientRect().height),
                     text: label ? label.textContent.trim() : ''});
    }
    const summary = page.querySelector('.be-p5-numbers') || page.querySelector('.be-summary');
    if (summary) {
      elements.push({type: 'totals', html: summary.outerHTML,
                     height: Math.ceil(summary.getBoundingClientRect().height),
                     text: 'Investment Summary'});
    }
  }
  return {elements, totalPages: allPages.length};
})()
"""

def measure_elements(url, start_page, end_page):
    chrome = find_chrome()
    if not chrome:
        sys.exit("No Chrome found in /Applications.")
    js = MEASURE_JS.replace("START_PAGE", str(start_page)).replace("END_PAGE", str(end_page))
    wrapper_dir = tempfile.mkdtemp(prefix="pack-")
    wrapper = os.path.join(wrapper_dir, "measure.html")
    wrapper_html = f"""<!DOCTYPE html><html><head><meta charset="utf-8">
<style>html,body{{margin:0;padding:0;background:#fff;}}</style>
</head><body>
<iframe id="doc" style="width:816px;height:30000px;border:0;"></iframe>
<script>
const iframe = document.getElementById('doc');
let done = false;
const poll = () => {{
  try {{
    const doc = iframe.contentDocument;
    if (!doc || !doc.querySelector('.doc-page')) {{ setTimeout(poll, 200); return; }}
    const result = {js};
    document.title = '__RESULTS__' + JSON.stringify(result) + '__END__';
    done = true;
  }} catch(e) {{ document.title = '__ERROR__' + e.message + '__END__'; done = true; }}
}};
iframe.onload = () => setTimeout(poll, 500);
iframe.src = {url!r};
setTimeout(() => {{ if (!done) document.title = '__ERROR__timeout__END__'; }}, 20000);
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
        sys.exit("Measurement timed out.")
    m = re.search(r'__RESULTS__.*?__END__|__ERROR__.*?__END__', proc.stdout, re.S)
    if not m:
        sys.exit("Measurement: no results captured.")
    inner = m.group(0)
    if inner.startswith("__ERROR__"):
        sys.exit(f"Measurement ERROR: {inner[8:-6]}")
    return json.loads(inner[11:-6])

# ── Packing ────────────────────────────────────────────────────────────────

def pack_elements(elements, budget=CONTENT_BUDGET):
    """Greedily pack elements into pages. Returns list of pages (each a list of elems)."""
    pages = []
    current = []
    current_h = 0

    for elem in elements:
        elem_h = elem["height"]

        # Totals exception: break to new page before totals unless they fit
        if elem["type"] == "totals":
            if current and current_h + elem_h > budget:
                pages.append(current)
                current = []
                current_h = 0
            current.append(elem)
            current_h += elem_h
            continue

        # Don't strand a section title alone at the bottom
        if elem["type"] in ("title", "label", "sub") and current_h + elem_h + 40 > budget:
            if current:
                pages.append(current)
                current = []
                current_h = 0

        # Greedy: if this element doesn't fit, start a new page
        if current and current_h + elem_h > budget:
            pages.append(current)
            current = []
            current_h = 0

        current.append(elem)
        current_h += elem_h

    if current:
        pages.append(current)
    return pages

# ── HTML generation ────────────────────────────────────────────────────────

def get_footer_label(html):
    m = re.search(r'class="doc-foot">\s*<span>(.*?)</span>', html, re.S)
    return m.group(1).strip() if m else "LUCI Systems &middot; Proposal"

def make_sow_page(elements, page_num, footer_label, is_continued):
    title = ('Scope of <span class="doc-page-band__accent doc-page-band__accent--gold">work, continued.</span>'
             if is_continued else
             'Scope of <span class="doc-page-band__accent doc-page-band__accent--gold">work.</span>')
    blocks = []
    current_block = []
    for elem in elements:
        if elem["type"] in ("title", "label"):
            if current_block:
                blocks.append(current_block)
            current_block = [elem]
        else:
            if is_continued and not current_block and elem["type"] == "text":
                pass
            current_block.append(elem)
    if current_block:
        blocks.append(current_block)

    body_parts = []
    for block in blocks:
        body_parts.append('      <div class="upg-scope">')
        for elem in block:
            body_parts.append(f"        {elem['html']}")
        body_parts.append("      </div>")

    body = "\n".join(body_parts)
    comment = f"<!-- PAGE {page_num:02d} · SCOPE OF WORK{' (CONTINUED)' if is_continued else ''} -->"
    return f"""    {comment}
    <section class="doc-page doc-page--band doc-page--proposal">
      <header class="doc-page-band">
        <div class="doc-page-band__top">
          <p class="doc-page-band__kicker">Proposal</p>
        </div>
        <h2 class="doc-page-band__title doc-edit" contenteditable="true">{title}</h2>
      </header>

{body}

      <div class="doc-foot">
        <span>{footer_label}</span>
        <span class="doc-foot__page">{page_num:02d}</span>
      </div>
    </section>"""

def make_lineitem_page(elements, page_num, footer_label, is_continued, is_totals):
    if is_totals:
        title = 'Investment <span class="doc-page-band__accent doc-page-band__accent--gold">summary.</span>'
    elif is_continued:
        title = 'Line items, <span class="doc-page-band__accent doc-page-band__accent--gold">continued.</span>'
    else:
        title = 'Line <span class="doc-page-band__accent doc-page-band__accent--gold">items.</span>'

    groups = [e for e in elements if e["type"] == "group"]
    totals = [e for e in elements if e["type"] == "totals"]

    body_parts = ['      <div class="be-price">']
    body_parts.append('        <div class="be-price__head">')
    body_parts.append('          <span>MFG</span><span>Item</span><span>Description</span>'
                      '<span class="be-col--num">Qty</span>'
                      '<span class="be-col--num">Cost ea</span>'
                      '<span class="be-col--num">Subtotal</span>')
    body_parts.append('        </div>')
    for g in groups:
        body_parts.append(f"        {g['html']}")
    body_parts.append("      </div>")
    for t in totals:
        body_parts.append(f"      {t['html']}")

    body = "\n".join(body_parts)
    label = "LINE ITEMS TOTALS" if is_totals else "LINE ITEMS" + (" (CONTINUED)" if is_continued else "")
    comment = f"<!-- PAGE {page_num:02d} · {label} -->"
    return f"""    {comment}
    <section class="doc-page doc-page--band doc-page--proposal">
      <header class="doc-page-band">
        <div class="doc-page-band__top">
          <p class="doc-page-band__kicker">Proposal</p>
        </div>
        <h2 class="doc-page-band__title doc-edit" contenteditable="true">{title}</h2>
      </header>

{body}

      <div class="doc-foot">
        <span>{footer_label}</span>
        <span class="doc-foot__page">{page_num:02d}</span>
      </div>
    </section>"""

# ── Splicing ────────────────────────────────────────────────────────────────

def replace_pages(html, start_page, end_page, new_pages_html):
    """Replace pages start_page..end_page with new_pages_html, renumber footers + comments."""
    page_pattern = r'    <!-- PAGE \d+[^>]*-->\n    <section class="doc-page.*?</section>'
    all_pages = list(re.finditer(page_pattern, html, re.S))
    if len(all_pages) < end_page:
        sys.exit(f"Document has {len(all_pages)} pages, but end_page is {end_page}")
    start_idx = start_page - 1
    end_idx = end_page - 1
    before = html[:all_pages[start_idx].start()]
    after = html[all_pages[end_idx].end():]
    result = before + new_pages_html + after
    page_num = 1
    def foot_repl(m):
        nonlocal page_num
        s = f"{page_num:02d}"
        page_num += 1
        # preserve the edit-bar's doc-edit/contenteditable attrs if present, so
        # renumbering still works after a preview edit + save (the edit bar adds
        # `doc-edit" contenteditable="true"` to footers; the old regex skipped them
        # and the numbering silently drifted).
        if 'doc-edit' in m.group(0):
            return f'<span class="doc-foot__page doc-edit" contenteditable="true">{s}</span>'
        return f'<span class="doc-foot__page">{s}</span>'
    result = re.sub(
        r'<span class="doc-foot__page(?:\s+doc-edit)?"\s*(?:contenteditable="true"\s*)?>\d+</span>',
        foot_repl, result)
    page_num = 1
    def comment_repl(m):
        nonlocal page_num
        s = f"<!-- PAGE {page_num:02d}"
        page_num += 1
        return s
    result = re.sub(r'<!-- PAGE \d+', comment_repl, result)
    return result

# ── Main ────────────────────────────────────────────────────────────────────

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("html", help="Path to the HTML file to repack")
    ap.add_argument("--mode", choices=["sow", "lineitems"], required=True,
                    help="sow = .upg-scope blocks (element-level); lineitems = .be-price-group blocks")
    ap.add_argument("--start-page", type=int, required=True, help="First page number to repack")
    ap.add_argument("--end-page", type=int, required=True, help="Last page number to repack")
    ap.add_argument("--url", required=True,
                    help="Dev server URL of the document (e.g. http://127.0.0.1:8771/clients/foo.html)")
    ap.add_argument("--dry-run", action="store_true", help="Show the plan, don't write")
    ap.add_argument("--write", action="store_true", help="Write repacked HTML back to the file")
    args = ap.parse_args()

    html_path = pathlib.Path(args.html).resolve()
    if not html_path.is_file():
        sys.exit(f"file not found: {html_path}")

    print(f"Measuring elements from pages {args.start_page}-{args.end_page} via {args.url}...")
    data = measure_elements(args.url, args.start_page, args.end_page)

    elements = data.get("elements", [])
    if not elements:
        sys.exit("No content elements found in the specified page range.")

    print(f"  Found {len(elements)} elements, total height {sum(e['height'] for e in elements)}px")

    pages = pack_elements(elements)
    print(f"  Packed into {len(pages)} pages (budget {CONTENT_BUDGET}px/page):")
    for i, p in enumerate(pages):
        types = [e["type"] for e in p]
        h = sum(e["height"] for e in p)
        has_totals = "totals" in types
        print(f"    page {i+1}: {len(p)} elements, {h}px {'[TOTALS]' if has_totals else ''}")

    if args.dry_run:
        print("\n--dry-run: not writing. Re-run with --write to apply.")
        return

    footer_label = get_footer_label(html_path.read_text())
    new_pages = []
    for i, page_elems in enumerate(pages):
        is_continued = i > 0
        is_totals = any(e["type"] == "totals" for e in page_elems)
        page_num = args.start_page + i
        if args.mode == "sow":
            new_pages.append(make_sow_page(page_elems, page_num, footer_label, is_continued))
        else:
            new_pages.append(make_lineitem_page(page_elems, page_num, footer_label, is_continued, is_totals))

    new_pages_html = "\n\n".join(new_pages)
    html = html_path.read_text()
    result = replace_pages(html, args.start_page, args.end_page, new_pages_html)

    if args.write:
        html_path.write_text(result)
        print(f"\nWrote repacked HTML to {html_path}")
        print(f"  Pages {args.start_page}-{args.end_page} replaced with {len(pages)} packed pages.")
        print(f"  Footers + comments renumbered.")
        # Auto footer-integrity check — catches a broken renumber before it
        # reaches the PDF. Run check-footers.py --fix if this flags anything.
        issues = verify_footers(result)
        if issues:
            print(f"\n⚠ FOOTER INTEGRITY CHECK FAILED ({len(issues)} issue(s)):")
            for i in issues:
                print(f"  - {i}")
            print("  Run: python3 scripts/check-footers.py <html> --fix")
        else:
            print("  ✓ footer integrity check passed.")
        print(f"  Run fit-check.py to verify, then hard-refresh the preview.")
    else:
        print(f"\nPreview (first 500 chars of new page HTML):")
        print(new_pages_html[:500])
        print(f"\nRe-run with --write to apply to {html_path.name}")

if __name__ == "__main__":
    main()
