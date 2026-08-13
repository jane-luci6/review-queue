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

# A page section: the `<!-- PAGE ... -->` comment + the <section class="doc-page...">…</section>.
PAGE_PATTERN = re.compile(
    r'<!-- PAGE[^>]*-->\s*\n\s*<section class="doc-page[^>]*>.*?</section>',
    re.S,
)
# A clean footer page-number span, with or without the edit-bar's doc-edit attrs.
FOOTER_PATTERN = re.compile(
    r'<span class="doc-foot__page(?:\s+doc-edit)?"\s*(?:contenteditable="true"\s*)?>(\d+)</span>'
)
# Mangle tells — any of these near a footer means the markup is broken.
MANGLE_TELLS = ('<span cla<span', 'div&gt;', '<span=""', 'class=doc-foot')


def _extract_pages(html):
    """Return list of (page_index, comment_text, section_html, footer_num_or_None, mangled_bool)."""
    pages = []
    for i, m in enumerate(PAGE_PATTERN.finditer(html), 1):
        block = m.group(0)
        comment = block.split('-->', 1)[0] + '-->'
        fm = FOOTER_PATTERN.search(block)
        footer_num = int(fm.group(1)) if fm else None
        mangled = any(tell in block for tell in MANGLE_TELLS)
        pages.append((i, comment, block, footer_num, mangled))
    return pages


def check(html_text, quiet=False):
    pages = _extract_pages(html_text)
    errors = []
    if not pages:
        return ["No .doc-page sections found."]

    expected = 2  # page 1 is the cover (no footer); numbering starts at 02
    for idx, comment, block, footer_num, mangled in pages:
        if mangled:
            errors.append(f"page {idx}: mangled footer markup ({comment.strip()})")
        if footer_num is None:
            # Cover (page 1) legitimately has no footer; any later page without one is an error.
            if idx == 1:
                continue
            errors.append(f"page {idx}: missing .doc-foot__page number ({comment.strip()})")
        else:
            if footer_num != expected:
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
    # Now renumber every footer span (clean or edit-bar-saved) sequentially from 02.
    counter = {'n': 1}

    def renum(m):
        counter['n'] += 1
        n = counter['n']
        # preserve whether the span carries the edit-bar attrs
        if 'doc-edit' in m.group(0):
            cls = 'doc-foot__page doc-edit'
            extra = ' contenteditable="true"'
        else:
            cls = 'doc-foot__page'
            extra = ''
        return f'<span class="{cls}"{extra}>{n:02d}</span>'

    html_text = FOOTER_PATTERN.sub(renum, html_text)
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
