---
name: luci-proposal-upgrade
description: >-
  Customize the LUCI Services Order Form (Upgrade) for a specific client. Use
  when an existing client is adding endpoint licenses and hardware to their
  existing LUCI platform. Simple 3-page order form: cover (client info, MSA
  reference, invoicing), line items (software, hardware, professional services),
  and scope of work.
---

# Proposal — Upgrade · customization

Simple services order form for existing clients adding endpoints/hardware to their LUCI platform. **3 pages (US Letter, variable)** — cover (client info, MSA reference, customer invoice information, invoicing terms), line items (software, hardware, professional services + totals), and scope of work (numbered items + assumptions). Source master: `proposal-upgrade.html` in this folder (build copy from `ui_kits/sales/`).

**This is for existing clients who already have a Master Purchase & Services Agreement (MSA) in place.** The cover references the existing MSA. No capabilities overview, no demo, no walkthrough — the client knows LUCI and is expanding.

Also read: `../_brand/SKILL.md` — especially **Efficient customization** and **Combine endpoint pricing into one line item**. Mike can click-edit any text (fonts/colors stay on CSS). Populate-in-place; never rebuild.

## Click-to-edit (Mike) vs agent edits

**Mike can click and type any text in the document.** Edit mode unlocks every text leaf. Fonts, colors, and layout stay on CSS classes — change words only; never strip `doc-edit` / `contenteditable` / structural wrappers.

**What stays non-editable (images only):** LUCI wordmark on the cover (`.doc-cover__logo`). Client logo is click-to-swap.

**Agent rules:** prefer `[data-studio]` selector edits (where present) or class-based edits; do not rebuild sections; do not invent fine-print; after Mike types in the preview, **Save** (or write the live DOM back to the same working file) before the next agent pass. Brand/voice still applies to any copy the agent authors.

**Save / PDF toolbar:** **Save** overwrites the working file when the browser supports the file picker (otherwise downloads `<title>.html` — Mike should save over the same path, not a new `-edited` copy). **Copy HTML** puts the full document on the clipboard. **Download PDF** opens the print dialog (Save as PDF, US Letter).

**Fit check (mandatory after content edits):** pages are fixed US Letter with `overflow: hidden` — overflow clips silently in print. After any content edit, verify no page overflows (see `../_brand/SKILL.md` → fit check).

## Voice

Match LUCI's voice on every line you write or rewrite. Full contract: `../_brand/SKILL.md` → **Voice & tone**. Canonical source: LUCI Messaging Guide (`ui_kits/review/messaging/messaging-guide.html`).

- **Engine and verbs — not layers.** Never use *layer* as a noun for LUCI. Lead with **orchestration engine** / **LUCI orchestrates…**; rotate to *runs, operates, integrates, consolidates, refines*.
- **Always write A/V** — never "AV" or "A-V" (body, headlines, labels, captions, alt text, diagrams).
- **Declarative, not promotional.** State facts; no "revolutionize / transform / empower / absurdly simple."
- **Register:** SOW/proposal = 3rd person, factual, narrative where it aids clarity. No marketing register in technical scope.

## Portal URL workflow (primary)

**Preview URL:** `http://10.10.1.17:8081/internal-portal/customization/proposal-upgrade/proposal-upgrade.html`

When Mike pastes this URL into Cursor chat:

1. Read this `SKILL.md` and `../_brand/SKILL.md` before any edits.
2. Copy master from `LUCI Systems Design System/ui_kits/sales/proposal-upgrade.html` to `ui_kits/sales/<client>-proposal-upgrade.html`.
3. Customize cover, line items, and scope of work per regions below.
4. Do **not** edit the HTML file on the VM deploy folder (overwritten on deploy).

See also: `../CURSOR.md`, `AGENTS.md` in this folder.

## When to use

When an existing LUCI client wants to add endpoint licenses, hardware, or professional services to their existing platform. The client already has an MSA — this is an order form under that agreement, not a new proposal. **Not for new clients** — use Proposal - LED or Proposal - LUCI Retrofit for those.

## Page map — editable vs locked

*Page numbers below reflect the default 3-page layout. They shift if line items overflow to a second page — always reference by section name, not absolute page number.*

| Page | Section | Canvas | Status |
|------|---------|--------|--------|
| **1** | Cover | Light + navy hero band | **EDITABLE** (kicker, display, sub, order summary, MSA reference, customer invoice info, invoicing terms, client logo) |
| **2** | Line items | Dark band | **EDITABLE** (all line items, qty, cost, subtotals, group labels, summary values, total) |
| **3** | Scope of work | Dark band | **EDITABLE** (all scope items, assumptions text) |

### Variable page counts

- **Line items (page 2):** if the table has more rows than fit on one page, the estimate spills onto a continuation page. Add a "continues on the following page" note; the continuation page reuses the same section header but does **not** add a second total.
- **Scope of work (page 3):** add or remove scope items as needed. Use numbered subheads (`.sow-subsection-title`), not repeated section numbers.

---

## Editable regions by section

### Cover (page 1) — `.doc-page--cover`

| Element | Selector / class |
|---------|-----------------|
| Kicker | `.doc-cover__kicker` (default: "Services Order Form") |
| Display headline | `.doc-cover__display` (keep `<em>` for accent phrase) |
| Sub copy | `.doc-cover__sub` |
| Order summary | `.doc-cover__summary-text` (includes project name, date, MSA reference) |
| Client logo | `.doc-cover__client` (`src` + `alt`) |
| LUCI logo | `.doc-cover__logo` — **locked** (brand) |
| Invoice customer | `[data-studio="invoice-customer"]` |
| Invoice site | `[data-studio="invoice-site"]` |
| Invoice address | `[data-studio="invoice-address"]` |
| Invoice city/state/zip | `[data-studio="invoice-cszip"]` |
| Invoice contact | `[data-studio="invoice-contact"]` |
| Invoice phone/email | `[data-studio="invoice-phone"]` |
| Invoicing terms | `.doc-cover__summary-text` (last summary block) |

### Line items (page 2) — `.doc-page--proposal`

Populate from the uploaded spreadsheet via `scripts/ingest-budgetary-lineitems.py` (same as the BE). The emitted `be-price-group` / `be-price-row` markup drops straight into the `.be-price` container. Each cell is `contenteditable` for word-level tweaks in preview. **No auto-math** — subtotals come from the spreadsheet; if you hand-edit a qty or unit price, recompute that row's subtotal yourself.

**One continuous table, one total.** Never split line items into sub-sections with separate sub-totals. If rows exceed one page, spill onto a continuation page.

**Only include rows that are in Mike's spreadsheet.** If the spreadsheet has a Sales Tax row, add it. If it doesn't, don't invent one. Same for freight, travel, or any other row.

**Combine endpoint pricing into one line item.** LUCI OS endpoint licenses must appear as a **single line item** referencing the **total number of endpoints** — never split by video/audio/etc. (See `../_brand/SKILL.md` → Pricing.)

| Element | Selector / class |
|---------|-----------------|
| Band title / deck | `.doc-page-band__title` / `.doc-page-band__deck` |
| Group labels | `.be-price-group__label` |
| Line item cells | `.be-price__mfg`, `.be-price__item`, `.be-price__desc`, `.be-price__num`, `.be-price__subtotal` |
| Summary labels | `.be-summary__label` |
| Summary values | `.be-summary__value`, `.be-summary__total-value` |

### Scope of work (page 3) — `.doc-page--terms`

| Element | Selector / class |
|---------|-----------------|
| Band title / deck | `.doc-page-band__title` / `.doc-page-band__deck` |
| Scope item title | `.sow-subsection-title` |
| Scope item body | `.doc-section-head__text` |
| Assumptions label | `.sow-list-label` |
| Assumptions body | `.doc-section-head__text` (last block) |

---

## Do not

- **Locked regions** (LUCI logo on cover) — **no changes of any kind**, including color, styling, or CSS. Run the pre-edit gate in `.cursor/rules/luci-doc-customization.mdc` first.
- Add endpoint pricing tiers — this is a simple order form, not a budgetary estimate.
- Add a capabilities overview, demo, or walkthrough content — the client already knows LUCI.
- Add "Addressed to" or similar labels to the cover.
- Use opaque JPEG client logo on the cover (white box artifact) — use transparent PNG/SVG.
- Invent hardware specs or pricing not supported by Mike's spreadsheet.
- Add marketing language to scope of work — stay factual and scoping-focused.

---

## Common tasks

**New upgrade order from client request**
1. Cover (p1): set kicker, display `<em>`, sub copy, order summary (project name, date, MSA reference), customer invoice info, invoicing terms, client logo.
2. Line items (p2): populate from Mike's spreadsheet via `ingest-budgetary-lineitems.py`; split to a continuation page if it overflows.
3. Scope of work (p3): rewrite the numbered scope items and assumptions to match the project scope.
4. Update `<title>` in `<head>` to reflect client/project name.
