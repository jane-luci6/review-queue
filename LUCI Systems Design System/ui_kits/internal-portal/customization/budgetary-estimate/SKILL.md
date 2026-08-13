---
name: luci-budgetary-estimate
description: >-
  Customize the LUCI Budgetary Estimate for a specific client. Use when quoting
  scoped endpoint counts and line items after the client has received the
  Capabilities document.
---

# Budgetary estimate — customization

Scoped, line-itemed pre-quote estimate. **6 pages (US Letter)** — professional follow-on to the Capabilities doc. Source master: `budgetary-estimate.html` in this folder (build copy from `ui_kits/sales/`).

**Workflow:** see `../_brand/SKILL.md` — two-folder architecture, create workspace, dev server, fit check, page packing, voice, PDF export. This file covers only the template-specific page map and editable regions.

Voice: see `../_brand/SKILL.md` → Voice & tone.

## When to use

After the client has received the **Capabilities document** and leadership needs endpoint counts, line-item pricing, and tier sheet before onsite final quote.

### Workflow notes (template-specific)

- **Pages 1–2 from Mike/Mark context** — cover property name, phase framing, and the page-2 "Prepared for…" intro come from what Mike/Mark tell you (or the portal form). Edit those regions directly; do not rebuild the locked "What LUCI is" block on page 2.
- **Page 4 line items from the uploaded spreadsheet** — Mike/Mark attach an `.xlsx` of the proposal line items. Run `scripts/ingest-budgetary-lineitems.py` to convert it to the page-4 markup, paste it in. If it overflows, run `scripts/pack-content.py --mode lineitems` to repack across pages (see `../_brand/SKILL.md` → Continuous page packing).
- **Page 6 tiers** — move `be-tier-chip--selected` to the tier you're pricing this job at, and edit the discount % / price inline for any customer-specific discount.

---

## Page 4 line items — Excel ingestion

Mike/Mark upload an `.xlsx` of the proposal line items. Convert it to the page-4 markup with `scripts/ingest-budgetary-lineitems.py`:

```bash
# from the working folder (~/Desktop/LUCI Docs/<client-name>/)
python3 scripts/ingest-budgetary-lineitems.py path/to/line-items.xlsx
# write the groups HTML to a file to paste from:
python3 scripts/ingest-budgetary-lineitems.py path/to/line-items.xlsx --out /tmp/be-rows.html
# if the rows overflow one page, emit full page-04 + "continued" page shells:
python3 scripts/ingest-budgetary-lineitems.py path/to/line-items.xlsx --split --out /tmp/be-pages.html
```

**Expected spreadsheet shape** (header row; column names are flexible / case-insensitive):

| Group | MFG | Item | Description | Qty | Unit Price | Subtotal |
|-------|-----|------|-------------|-----|------------|----------|
| LUCI Software | LUCI | LUCI OS | Operating System Software… | 1 | 35112 | |
| LUCI Video & Control Hardware | LG | LG STB-6500 | IPTV Set Top Box Receiver… | 50 | 174.90 | |

- **Group / Category / System / Section** → the group label.
- **Subtotal is optional** — computed as `Qty × Unit Price` when the column is missing.
- A row with **Qty 0** renders a `—` subtotal (matches the placeholder endpoint rows).
- The script prints a **row count, group count, grand total, and an estimated line-item stack height** against an 8.5in per-page budget, and tells you whether the rows fit one page or need a second.

**When it overflows one page:**

- Use `scripts/pack-content.py --mode lineitems` to repack the line-item groups across pages with continuous flow (greedy packing, totals exception, footer renumbering). See `../_brand/SKILL.md` -> Continuous page packing for the command.
- The old `--split` flag on `ingest-budgetary-lineitems.py` still works for a simple two-page split, but `pack-content.py` is the preferred tool -- it handles arbitrary page counts, the totals exception, and renumbers footers automatically.
- Verify the split by running `scripts/fit-check.py`, then rendering the PDF (via the dev server's `POST /__pdf` or `scripts/render-pdf.sh`). If a single group is too tall to fit a page, subdivide it into two `be-price-group` blocks with split labels (e.g. "LUCI Video & Control Hardware (1/2)").

If the spreadsheet’s column names don’t map (the script errors with `missing required column(s)`), either rename the headers in the .xlsx or pass an adapted copy — the script’s `COL_SYNONYMS` table lists the accepted names.

---

## Page map — editable vs locked

| Page | Section | Status |
|------|---------|--------|
| **1** | Cover | **EDITABLE** |
| **2** | Introduction + What LUCI is (mint-bar intro, identity diagram, 6 feature cards) | **EDITABLE** (intro statement); **LOCKED** identity diagram + feature cards |
| **3** | Review of scope | **EDITABLE** (bridge line, scope rows) |
| **4** | Proposal line items | **EDITABLE** (populate from Excel via `ingest-budgetary-lineitems.py`; auto-splits to a continued page if it overflows) |
| **5** | Investment summary + what it delivers | **EDITABLE** (totals); **LOCKED** delivers marketing grid |
| **6** | Endpoint pricing + next steps/close | **EDITABLE** (tier cells incl. discount, close body/contact); **highlight offered tier** with `be-tier-chip--selected` |

---

## Editable regions

### Cover (page 1) — `.doc-page--cover`

| Element | What to change |
|---------|----------------|
| `.doc-cover__kicker`, `.doc-cover__display`, `.doc-cover__sub` | Headline stack |
| `.doc-cover__summary-text` | Property name + phase framing |
| `.doc-cover__date` | Proposal/estimate date (format: "Month DD, YYYY") |
| `.doc-cover__client` | Client logo (`src`, `alt`) — use a transparent **vector (SVG) or high-res PNG**; for a band spot, prefer the brand's white/reversed logo so it renders crisp on navy (see *Logo cleanup for dark backgrounds* in `skills/cover-page-customization.md`). Click the logo in preview to swap it, or drag an image file onto it. |
| `.doc-page--cover` (`logo-pos--X`) | **Logo placement** — add one of `logo-pos--bottom-left` (default), `logo-pos--band`, `logo-pos--band-right`, `logo-pos--bottom-right`. Mike can also tap a "Logo spot" chip in the edit bar to change it live. See `skills/cover-page-customization.md` → *Logo placement* for the spot table + default-picking + white-logo handling + logo cleanup for dark backgrounds. |

Do **not** change `.doc-cover__logo` (LUCI).

**Full cover flow (company name + goals rewrite + logo):** when the client
provides a company name, plain-language goals, and a logo, follow
`internal-portal/skills/cover-page-customization.md` — it defines the designated
placement areas and the rewrite contract (goals → business-audience overview in
LUCI voice). That skill also lists the gaps in the current Studio form (the goals
field has no inject target; there's no rewrite step; the name only hits the
summary bold, not the headline or page-2 intro).

**Logo placement handoff (tell Mike):** after placing the client logo, always tell
Mike where it sits and that he can move it — e.g., *"Client logo placed bottom-left
on the cover. Tap a **Logo spot** chip in the top edit bar (Band / Band-right /
Bottom-right) if you'd rather it elsewhere."* Pick the default per
`skills/cover-page-customization.md` → *Logo placement*. Don't ask him to choose
upfront — place a sensible default and let him adjust in one tap.

### Introduction + What LUCI is (page 2) — `.doc-page--overview`

The navy band (`doc-page-band`) carries the page title and a short deck. Below it:

| Element | What to change |
|---------|----------------|
| `.be-intro__text` | “Prepared for…” statement — property name, phase, budgetary framing |

**Locked on page 2:** `.be-why` — the “What LUCI is” sub-head, the canonical identity diagram (`cap-identity`), and the six feature cards (`cap-feature-card`). These mirror the brochure/capabilities “What LUCI is” page and stay consistent across documents.

### Review of scope (page 3) — `.doc-page--scope`

| Element | What to change |
|---------|----------------|
| `.be-scope-bridge` | Line tying estimate to endpoint counts |
| `.be-scope__cat`, `.be-scope__count`, `.be-scope__desc` | Scope categories and counts |

### Proposal (page 4) — `.doc-page--proposal`

Populate from the uploaded spreadsheet via `scripts/ingest-budgetary-lineitems.py` (see “Page 4 line items — Excel ingestion” above). The emitted `be-price-group` / `be-price-row` markup drops straight into the `.be-price` container, after the `.be-price__head` column-label row. Each cell is `contenteditable` (mfg/item/desc + qty/cost/subtotal) for word-level tweaks in preview. **No auto-math in the page** — subtotals come from the spreadsheet (or are computed by the script when the Subtotal column is missing); if you hand-edit a qty or unit price in preview, recompute that row’s subtotal yourself.

**Combine endpoint pricing into one line item.** LUCI OS endpoint licenses must appear as a **single line item** with the **total endpoint count as the quantity** and the **per-endpoint price as the cost-ea** (e.g. qty 38 × $420/ea = $15,960) — never split out by video, audio, or other sub-categories. If Mike’s spreadsheet has them combined, mirror that. If a previous AI run split them into separate video/audio/etc. rows, combine them back into one row with the total endpoint count as the quantity. The label should match Mike’s spreadsheet (e.g. “LUCI OS & Endpoint Licenses” or “LUCI OS — Annual Partnership”) — do not invent a different label.

**Pack greedily; totals break unless they fit.** Keep groups/rows on the same page when they fit. Put a page break **before** the investment summary/totals unless the **full** totals block fits on the last line-item page (or the template already separates investment onto its own page). See `../_brand/SKILL.md` → Continuous page packing.

**Source fidelity + branded dress.** Mirror the spreadsheet’s labels, order, and structure; apply `.be-price*` branded formatting. See `../_brand/SKILL.md` → Source fidelity.

**Totals span full page width.** `.be-summary` / `.be-summary__total` / `.be-summary-split` (and `.be-p5-numbers`) must be full content width — never `max-width: 48ch`. See `../_brand/SKILL.md` → Totals span the full page width.

### Investment summary (page 5) — `.doc-page--investment`

| Element | What to change |
|---------|----------------|
| `.be-summary__value`, `.be-summary__total-value`, `.be-split__value` | Totals |

**Locked:** `.be-delivers` (marketing outcomes grid — 6 verb-led outcomes)

### Endpoint pricing + close (page 6) — `.doc-page--pricing`

| Element | What to change |
|---------|----------------|
| `.be-tier-chip` | Tier pricing cells — qty, discount %, and price are all `contenteditable`; edit inline for a customer-specific discount |
| `.be-tier-chip--selected` | **Highlight the tier you’re pricing this job at.** Move this class to the offered chip — it renders a mint fill, mint outline, mint numerals, and a “Your tier” tag. Default in the master is the 100-endpoint tier |
| `.be-close__body`, contact name/email | Next step + rep |

---

## Do not

- **Locked regions** (page 2 identity diagram + feature cards; `.be-delivers` marketing grid) — **no changes of any kind**, including color, styling, spacing, or CSS, not just copy. If asked to change a locked region, do NOT edit first — flag the lock and ask whether to override (local-only vs canonical) before making any change.
- Split endpoint pricing into separate video/audio line items — combine into one row with the total endpoint count as the quantity.
- Re-add full LUCI story pages from the old 10-page template.
- Edit locked `.be-delivers` marketing copy without Jane’s approval.
- Change diagram/screenshot assets on page 2 without Jane’s approval.
- Use opaque JPEG client logos on the cover (white box artifact).

---

**Update `<title>`** in `<head>` to reflect client/project name.
