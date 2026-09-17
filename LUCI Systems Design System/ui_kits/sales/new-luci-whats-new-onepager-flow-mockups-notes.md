# New LUCI What’s New one-pager — flow mockups

**Built:** 17 September 2026 · GLM · from `new-luci-whats-new-onepager-flows.md`

Three true 8.5×11 letter-size HTML mockups, one per flow. Each is a **single locked sheet** — not a scroll-tall page pretending to be a one-pager.

## How to open each file

Open in a browser (or Cursor's in-editor preview). The screen view shows the sheet centered on a grey desk surround; **Print → Save as PDF (US Letter, margins: None)** is the deliverable view.

| Flow | File | Open |
|---|---|---|
| A — The control arc | `new-luci-whats-new-onepager-flow-a.html` | browser / Preview → Print → Letter |
| B — Three decisions | `new-luci-whats-new-onepager-flow-b.html` | browser / Preview → Print → Letter |
| C — Promise, proof, path | `new-luci-whats-new-onepager-flow-c.html` | browser / Preview → Print → Letter |

All three link `../../assets/fonts/luci-brand-fonts.css` (static Inter / Space Grotesk / Syncopate — no Google Fonts) and the LUCI white wordmark from `assets/logos/`. They are self-contained — no shared `sales-document.css` dependency — so each can be moved or handed off independently.

## One-line diff between the flows

- **A — The control arc:** one descending column — announcement → partnership bridge → three pillars stacked top-to-bottom (each: benefit sentence, then features as a compact proof line) → compact CTA with the 3-step path. Reads as a single vertical narrative; pillars are **not** equal columns.
- **B — Three decisions:** a question-and-answer rhythm — theme + release-shift, then the **three operator questions** sit in the first-read field, and each question **resolves into its pillar** below (Q above, A beneath, features as evidence) → partnership line → CTA. Reads as decision → resolution, three times.
- **C — Promise, proof, path:** a two-depth structure — theme + partnership, then a **horizontal promise index** (the three pillar names in a row), then a **vertical proof ledger** beneath (same pillar order, one benefit + features per row) → a distinct "Your path to New LUCI" close. The pillars appear **twice at different depths** — first as a memorable index, then as ordered proof.

## What every flow holds (locked content)

- **Theme:** Putting the power of programming in your hands
- **Partnership:** more control; LUCI still supports — never implies less support
- **Three pillars + features (features as proof lines, not the lead):**
  1. Control the room — Venue panels · Staging · Audio group control
  2. Control your view — Customizable interface · Live map flexibility · Video/LED wall layout sync
  3. Control your security — Audit trails · Live monitoring · Sign-in & session · In-product support
- **Off-page:** Add any endpoint · Display model catalog · Upgrade Guide body · download CTAs
- **Placeholders:** `[RELEASE DATE]`, `[NAME]` / `[TITLE]` / `[EMAIL]` / `[PHONE]` for the contact CTA

## Print check tip

Before sending to Jane, open each file and **Print → Save as PDF** with:
- **Paper size:** US Letter
- **Margins:** None (the `@page { size: letter; margin: 0 }` rule handles it)
- **Scale:** 100% (do not "fit to page" — the sheet is already exactly 8.5×11)
- **Background graphics:** ON (so the navy masthead, mint bars, and circuit texture render)

Verify in the PDF:
1. The page is exactly one sheet — no trailing blank page, no clipped content.
2. The navy masthead and mint 4px bottom rule print (not white).
3. The dark CTA/path band at the bottom prints navy with mint accents.
4. Feature proof chips read cleanly; the `·` separators are mint.
5. `[RELEASE DATE]` and `[NAME]` placeholders are visible (Jane fills these per send).

If a flow overflows on print, do **not** trim copy — the sheet is locked at 8.5×11 with `overflow: hidden`, so overflow is silently clipped. Open in the browser and inspect; if content collides with the footer, tighten spacing (not copy) in that file's embedded `<style>`.
