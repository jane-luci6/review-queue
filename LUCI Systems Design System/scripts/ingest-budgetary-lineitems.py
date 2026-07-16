#!/usr/bin/env python3
"""Ingest a budgetary-estimate line-item spreadsheet and emit the page-4 HTML.

Mike/Mark drop an .xlsx of the proposal line items. This script reads it,
groups rows by the Group/Category column, computes subtotals (Qty x Unit Price
when no Subtotal column is supplied), and emits the `be-price-group` /
`be-price-row` markup that drops straight into the page-4 `be-price` container
(after the `be-price__head` column-label row).

It also estimates the line-item stack height and tells you whether the rows fit
one page or need a second proposal page. With `--split` it emits two complete
`doc-page--proposal` sections (page 04 + a "continued" page 05) so the agent
only has to paste them in and renumber the trailing page footers.

Expected spreadsheet shape (header row, column names are flexible / case-
insensitive — see COL_SYNONYMS below):

  Group        | MFG  | Item       | Description               | Qty | Unit Price | Subtotal
  LUCI Software| LUCI | LUCI OS    | Operating System Software | 1   | 35112      |
  LUCI Software| LUCI | LUCI Endp… | Video — IPTV …            | 50  | 399        |

- Group / Category / System / Section all map to the group label.
- Subtotal is optional — computed as Qty x Unit Price when absent.
- A row with Qty 0 renders a "—" subtotal (matches the template's placeholder
  endpoint rows).

Usage:
  python3 scripts/ingest-budgetary-lineitems.py <input.xlsx>
  python3 scripts/ingest-budgetary-lineitems.py <input.xlsx> --sheet Sheet2
  python3 scripts/ingest-budgetary-lineitems.py <input.xlsx> --out rows.html
  python3 scripts/ingest-budgetary-lineitems.py <input.xlsx> --split --out pages.html
"""
from __future__ import annotations

import argparse
import html
import math
import re
import sys
from pathlib import Path

try:
    import openpyxl
except ImportError:
    sys.exit("openpyxl is required:  pip3 install openpyxl")


# Header synonyms (lowercased, stripped). First match wins per role.
COL_SYNONYMS = {
    "group":    ["group", "category", "system", "section", "phase"],
    "mfg":      ["mfg", "manufacturer", "mfr", "brand", "vendor", "make"],
    "item":     ["item", "product", "model", "sku", "name", "part"],
    "desc":     ["description", "desc", "details", "spec", "specs", "notes"],
    "qty":      ["qty", "quantity", "count", "qty ea", "ea"],
    "unit":     ["unit price", "cost ea", "unit", "price", "cost", "each", "rate", "unit cost"],
    "subtotal": ["subtotal", "ext", "extended", "line total", "total", "amount"],
}

# Per-page height budget for the line-item stack (inches). The band header +
# column-label row + footer eat ~2in on a Letter page, leaving ~8.5in for
# groups + rows. Rows that wrap their description cost more.
PAGE_BUDGET_IN = 8.5
ROW_BASE_IN = 0.30        # one-line row
ROW_PER_EXTRA_LINE_IN = 0.18
DESC_CHARS_PER_LINE = 48
GROUP_LABEL_IN = 0.34


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", str(s).strip().lower())


def find_columns(header_row):
    """Map role -> column index from a header row."""
    mapping = {}
    for idx, cell in enumerate(header_row):
        key = norm(cell)
        if not key:
            continue
        for role, syns in COL_SYNONYMS.items():
            if role in mapping:
                continue
            if key in syns:
                mapping[role] = idx
    return mapping


def find_header_row(ws, max_scan=12):
    """Return (row_index, col_mapping) for the first row that looks like a header."""
    for r in range(1, min(max_scan, ws.max_row) + 1):
        row = [ws.cell(r, c).value for c in range(1, ws.max_column + 1)]
        mapping = find_columns(row)
        # A header needs at least Item + Qty to be plausible.
        if "item" in mapping and "qty" in mapping:
            return r, mapping
    return None, {}


def parse_money(v):
    """Return (float_or_None, raw_str). Accepts numbers, '$1,234.00', '1234', blanks."""
    if v is None:
        return None, ""
    if isinstance(v, (int, float)):
        return float(v), str(v)
    s = str(v).strip()
    if not s:
        return None, ""
    cleaned = re.sub(r"[$,\s]", "", s)
    try:
        return float(cleaned), s
    except ValueError:
        return None, s


def parse_qty(v):
    if v is None:
        return None, ""
    if isinstance(v, (int, float)):
        f = float(v)
        return f, (str(int(f)) if f.is_integer() else str(f))
    s = str(v).strip()
    if not s:
        return None, ""
    try:
        f = float(re.sub(r"[,\s]", "", s))
        return f, (str(int(f)) if f.is_integer() else str(f))
    except ValueError:
        return None, s


def fmt_money(f):
    if f is None:
        return None
    return f"${f:,.2f}"


def esc(s):
    return html.escape(str(s), quote=False)


def row_height_in(desc):
    if not desc:
        return ROW_BASE_IN
    lines = max(1, math.ceil(len(str(desc)) / DESC_CHARS_PER_LINE))
    return ROW_BASE_IN + (lines - 1) * ROW_PER_EXTRA_LINE_IN


def read_rows(ws, header_row, cols):
    """Yield dicts of parsed row data in sheet order."""
    for r in range(header_row + 1, ws.max_row + 1):
        get = lambda role: ws.cell(r, cols[role] + 1).value if role in cols else None
        group = get("group")
        item = get("item")
        # Stop at a fully blank row (trailing whitespace). A row with no item
        # but a group label is still skipped.
        if group is None and item is None:
            blank = all(
                (ws.cell(r, c).value in (None, "", " "))
                for c in range(1, ws.max_column + 1)
            )
            if blank:
                continue
            # non-blank but missing item + group -> skip silently
            continue
        qty_f, qty_s = parse_qty(get("qty"))
        unit_f, unit_s = parse_money(get("unit"))
        sub_f, sub_s = parse_money(get("subtotal"))
        # Compute subtotal if missing.
        if sub_f is None and qty_f is not None and unit_f is not None:
            sub_f = qty_f * unit_f
        yield {
            "group": (str(group).strip() if group is not None else "Other"),
            "mfg": (str(get("mfg")).strip() if get("mfg") is not None else ""),
            "item": (str(item).strip() if item is not None else ""),
            "desc": (str(get("desc")).strip() if get("desc") is not None else ""),
            "qty_s": qty_s,
            "unit_s": (fmt_money(unit_f) if unit_f is not None else unit_s),
            "sub_s": ("—" if (qty_f == 0) else (fmt_money(sub_f) if sub_f is not None else sub_s)),
            "_h": row_height_in(get("desc")),
        }


def group_rows(rows):
    """Group rows by the Group column, preserving first-appearance order."""
    groups = {}
    order = []
    for r in rows:
        g = r["group"]
        if g not in groups:
            groups[g] = []
            order.append(g)
        groups[g].append(r)
    return [(g, groups[g]) for g in order]


def render_row(r):
    return (
        '        <div class="be-price-row">\n'
        f'          <span class="be-price__mfg" contenteditable="true">{esc(r["mfg"])}</span>\n'
        f'          <span class="be-price__item" contenteditable="true">{esc(r["item"])}</span>\n'
        f'          <span class="be-price__desc" contenteditable="true">{esc(r["desc"])}</span>\n'
        f'          <span class="be-price__num doc-edit" contenteditable="true">{esc(r["qty_s"])}</span>\n'
        f'          <span class="be-price__num doc-edit" contenteditable="true">{esc(r["unit_s"])}</span>\n'
        f'          <span class="be-price__num be-price__subtotal doc-edit" contenteditable="true">{esc(r["sub_s"])}</span>\n'
        '        </div>'
    )


def render_groups(grouped, indent=""):
    out = []
    for label, rows in grouped:
        out.append(f'{indent}<div class="be-price-group">')
        out.append(f'{indent}  <p class="be-price-group__label">{esc(label)}</p>')
        for r in rows:
            out.append(indent + "  " + render_row(r))
        out.append(f'{indent}</div>')
    return "\n".join(out)


def estimate_height_in(grouped):
    h = 0.0
    for _label, rows in grouped:
        h += GROUP_LABEL_IN
        for r in rows:
            h += r["_h"]
    return h


def page_band(title_html, deck, page_num, body):
    return (
        '    <section class="doc-page doc-page--band doc-page--proposal">\n'
        '      <header class="doc-page-band">\n'
        '        <div class="doc-page-band__top">\n'
        '          <p class="doc-page-band__kicker">Proposal</p>\n'
        '        </div>\n'
        f'        <h2 class="doc-page-band__title">{title_html}</h2>\n'
        f'        <p class="doc-page-band__deck">{deck}</p>\n'
        '      </header>\n'
        '\n'
        '      <div class="be-price">\n'
        '        <div class="be-price__head">\n'
        '          <span>MFG</span><span>Item</span><span>Description</span>'
        '<span class="be-col--num">Qty</span><span class="be-col--num">Cost ea</span>'
        '<span class="be-col--num">Subtotal</span>\n'
        '        </div>\n'
        f'{body}\n'
        '      </div>\n'
        '\n'
        '      <div class="doc-foot">\n'
        '        <span>LUCI Systems &middot; Budgetary estimate</span>\n'
        f'        <span class="doc-foot__page">{page_num:02d}</span>\n'
        '      </div>\n'
        '    </section>'
    )


def split_groups(grouped, budget=PAGE_BUDGET_IN):
    """Partition groups into page buckets that each fit `budget` inches."""
    buckets = []
    cur = []
    cur_h = 0.0
    for label, rows in grouped:
        block_h = GROUP_LABEL_IN + sum(r["_h"] for r in rows)
        # If a single group is bigger than a page, it still rides on its own
        # bucket (the agent can subdivide further if needed).
        if cur and cur_h + block_h > budget:
            buckets.append(cur)
            cur = []
            cur_h = 0.0
        cur.append((label, rows))
        cur_h += block_h
    if cur:
        buckets.append(cur)
    return buckets


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("xlsx", help="Path to the line-item .xlsx file")
    ap.add_argument("--sheet", default=None, help="Sheet name (default: first sheet)")
    ap.add_argument("--out", default=None, help="Write emitted HTML to this file")
    ap.add_argument("--split", action="store_true",
                    help="Emit two complete doc-page--proposal sections when the rows overflow one page")
    ap.add_argument("--budget", type=float, default=PAGE_BUDGET_IN,
                    help=f"Per-page line-item height budget in inches (default {PAGE_BUDGET_IN})")
    args = ap.parse_args(argv)

    src = Path(args.xlsx)
    if not src.exists():
        sys.exit(f"file not found: {src}")

    wb = openpyxl.load_workbook(src, data_only=True, read_only=True)
    ws = wb[args.sheet] if args.sheet else wb[wb.sheetnames[0]]

    header_row, cols = find_header_row(ws)
    if not header_row:
        sys.exit("could not find a header row (need at least an 'Item' and 'Qty' column)")

    missing = [r for r in ("item", "qty") if r not in cols]
    if missing:
        sys.exit(f"missing required column(s): {missing}. "
                 f"Detected columns: { {k: ws.cell(header_row, v+1).value for k,v in cols.items()} }")

    rows = list(read_rows(ws, header_row, cols))
    if not rows:
        sys.exit("no data rows found after the header")

    grouped = group_rows(rows)
    total_h = estimate_height_in(grouped)
    n_rows = len(rows)
    n_groups = len(grouped)
    grand = 0.0
    for r in rows:
        # recompute a numeric grand total where possible
        try:
            if r["sub_s"] not in ("—", "", None):
                grand += float(re.sub(r"[$,\s]", "", r["sub_s"]))
        except ValueError:
            pass

    # ---- report -------------------------------------------------------------
    print(f"sheet:        {ws.title}")
    print(f"header row:   {header_row}")
    print(f"columns:      " + ", ".join(f"{k}={ws.cell(header_row, v+1).value}" for k, v in sorted(cols.items(), key=lambda kv: kv[1])))
    print(f"groups:       {n_groups}")
    print(f"line items:   {n_rows}")
    print(f"est. height:  {total_h:.2f} in  (page budget {args.budget:.2f} in)")
    if grand:
        print(f"grand total:  {fmt_money(grand)}")

    needs_split = total_h > args.budget
    if needs_split:
        print(f"\n⚠  Rows overflow one page (~{math.ceil(total_h / args.budget)} pages of line items).")
        if args.split:
            print("   --split is on: emitting full proposal page sections below.")
        else:
            print("   Re-run with --split to get two complete doc-page--proposal sections,")
            print("   then renumber the trailing page footers (+1) and the SKILL page map.")
    else:
        print("\n✓  Rows fit one page — paste the groups below into page 04's .be-price container.")

    # ---- emit ---------------------------------------------------------------
    if args.split and needs_split:
        buckets = split_groups(grouped, args.budget)
        pages = []
        for i, bucket in enumerate(buckets):
            if i == 0:
                title = 'Line <span class="doc-page-band__accent doc-page-band__accent--gold">items.</span>'
                deck = ("Budgetary pricing by manufacturer and item &mdash; LUCI software, video and "
                        "control hardware, and professional services. Figures are confirmed on site "
                        "before a final quote.")
                pageno = 4
            else:
                title = ('Line items, <span class="doc-page-band__accent doc-page-band__accent--gold">'
                         'continued.</span>')
                deck = (f"Continued from page {4 + i - 1:02d} &mdash; remaining line items by "
                        "manufacturer and item.")
                pageno = 4 + i
            body = render_groups(bucket, indent="        ")
            pages.append(page_band(title, deck, pageno, body))
        out_html = "\n\n".join(pages)
    else:
        out_html = render_groups(grouped, indent="      ")

    print("\n" + "=" * 72)
    print(out_html)
    print("=" * 72)

    if args.out:
        Path(args.out).write_text(out_html + "\n", encoding="utf-8")
        print(f"\nwrote {args.out}")


if __name__ == "__main__":
    main()
