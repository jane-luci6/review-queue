#!/usr/bin/env python3
"""Verify page-footer integrity in a sales/customization document.

Catches the "little details" that string-transform passes (pack-content
renumbering, edit-bar saves, manual sed edits) can silently drop or mangle:
  - a .doc-page section with no .doc-foot__page number,
  - a footer number that's missing, duplicated, or out of sequence,
  - mangled footer markup (e.g. `<span cla<span`, `div&gt;`).

Run after every pack-content pass, after any edit-bar save, and before PDF
export. Exits 0 if every page has a clean, sequential footer; 1 otherwise.

Usage:
  python3 scripts/check-footers.py <html>            # check + report
  python3 scripts/check-footers.py <html> --quiet    # exit code only
  python3 scripts/check-footers.py <html> --fix     # renumber footers in place
"""
import argparse
import re
import sys
from pathlib import Path

# A page section: an optional `<!-- PAGE ... -->` comment + the
# <section class="doc-page...">…</section>. The comment is optional because some
# templates (proposal.html, scope-of-work.html) omit it and use the section alone.
PAGE_PATTERN = re.compile(
    r'(?:<!-- PAGE[^>]*-->\s*\n\s*)?<section class="doc-page[^>]*>.*?</section>',
    re.S,
)
# A clean footer page-number span. Allow arbitrary extra attributes (contenteditable,
# data-studio="auto-doc-foot-page-NN", etc.) between the class and the >.
FOOTER_PATTERN = re.compile(
    r'<span class="doc-foot__page[^"]*"[^>]*>(\d+)</span>'
)
# Mangle tells — any of these near a footer means the markup is broken.
MANGLE_TELLS = ('<span cla<span', 'div&gt;', '<span=""', 'class=doc-foot')


def _extract_pages(html):
    """Return list of (page_index, comment_text, section_html, footer_num_or_None, mangled_bool)."""
    pages = []
    for i, m in enumerate(PAGE_PATTERN.finditer(html), 1):
        block = m.group(0)
        if block.startswith('<!--'):
            comment = block.split('-->', 1)[0] + '-->'
        else:
            comment = '<!-- (no PAGE comment) -->'
        fm = FOOTER_PATTERN.search(block)
        footer_num = int(fm.group(1)) if fm else None
        mangled = any(tell in block for tell in MANGLE_TELLS)
        pages.append((i, comment, block, footer_num, mangled))
    return pages


def check(html_text, quiet=False):
    pages = _extract_pages(html_text)
    errors = []
    if not pages:
        # Non-paged document (e.g. sales deck, standalone HTML) — the footer
        # check doesn't apply. Not an error.
        if not quiet:
            print("no .doc-page sections — non-paged document, footer check skipped.")
        return []

    nums = [p[3] for p in pages]
    first_idx = next((i for i, n in enumerate(nums) if n is not None), None)
    if first_idx is None:
        # Paged doc with no footer numbers anywhere — unusual; skip rather than
        # block (the footer check has nothing to verify).
        if not quiet:
            print(f"pages: {len(pages)}  | footers found: 0  | (no numbered pages — skipped)")
        return []

    last_idx = max(i for i, n in enumerate(nums) if n is not None)
    expected = nums[first_idx]
    for i, (idx, comment, block, footer_num, mangled) in enumerate(pages):
        if mangled:
            errors.append(f"page {idx}: mangled footer markup ({comment.strip()})")
        # Pages before the first numbered page (cover / front matter) and after
        # the last numbered page (close) legitimately have no footer.
        if i < first_idx or i > last_idx:
            continue
        if footer_num is None:
            errors.append(f"page {idx}: missing .doc-foot__page number ({comment.strip()})")
        elif footer_num != expected:
            errors.append(
                f"page {idx}: footer says '{footer_num:02d}' but expected '{expected:02d}' "
                f"({comment.strip()})"
            )
        expected += 1

    if not quiet:
        max_num = max((p[3] for p in pages if p[3] is not None), default=0)
        print(f"pages: {len(pages)}  | footers found: "
              f"{sum(1 for p in pages if p[3] is not None)}  | last number: {max_num:02d}")
        if errors:
            print(f"\n✗ {len(errors)} footer issue(s):")
            for e in errors:
                print(f"  - {e}")
        else:
            print("✓ all page footers present, clean, and sequential.")
    return errors


def fix(html_text):
    """Renumber every .doc-foot__page span sequentially from 02, leaving markup intact.

    Also repairs the known mangle (`<span cla<span…>NN</span>div&gt;`) back to a
    clean span before renumbering. Returns the repaired+renumbered HTML.
    """
    # Repair the mangled footer pattern first:
    #   <span cla<span="" class="doc-foot__page doc-edit" contenteditable="true">NN</span>div&gt;
    # back to a clean span + closing </div> (the </section> stays where it was).
    repair = re.compile(
        r'<span cla<span="" class="doc-foot__page doc-edit" contenteditable="true">(\d+)</span>div&gt;\n(\s*)</div></section>'
    )
    html_text = repair.sub(
        r'<span class="doc-foot__page doc-edit" contenteditable="true">\1</span>\n\2</div>\n    </section>',
        html_text,
    )
    # Now renumber every footer span (clean or edit-bar-saved) sequentially,
    # starting from the first footer number already in the doc — this preserves
    # each template's numbering convention (e.g. capabilities starts at 04).
    # We only swap the digits, leaving every attribute (class, contenteditable,
    # data-studio="auto-doc-foot-page-NN", …) untouched.
    renum_pattern = re.compile(r'(<span class="doc-foot__page[^"]*"[^>]*>)(\d+)(</span>)')
    first_match = renum_pattern.search(html_text)
    counter = {'n': (int(first_match.group(2)) - 1) if first_match else 1}

    def renum(m):
        counter['n'] += 1
        return f"{m.group(1)}{counter['n']:02d}{m.group(3)}"

    html_text = renum_pattern.sub(renum, html_text)
    return html_text


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("html", help="Path to the HTML file to check")
    ap.add_argument("--quiet", action="store_true", help="No report; just exit code")
    ap.add_argument("--fix", action="store_true",
                    help="Renumber footers in place (repairs mangle + resequences)")
    args = ap.parse_args()

    path = Path(args.html)
    if not path.is_file():
        sys.exit(f"File not found: {path}")
    html = path.read_text(encoding="utf-8", errors="replace")

    if args.fix:
        fixed = fix(html)
        path.write_text(fixed, encoding="utf-8")
        print(f"Rewrote footers in: {path}")
        # re-check after fixing
        errors = check(fixed, quiet=args.quiet)
        sys.exit(1 if errors else 0)

    errors = check(html, quiet=args.quiet)
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
