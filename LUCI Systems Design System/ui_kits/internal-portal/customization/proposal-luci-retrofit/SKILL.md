---
name: luci-proposal-retrofit
description: >-
  Customize the LUCI Proposal (LUCI Retrofit) for a specific client. Use when
  proposing a full LUCI platform installation — endpoint licensing, integration
  hardware, professional services, and a scope of work. Built from the Budgetary
  Estimate with endpoint pricing removed and a full SOW added before line items.
---

# Proposal — LUCI Retrofit · customization

Full LUCI platform proposal. **~8 pages (US Letter, variable)** — cover, overview (What LUCI is), review of scope, scope of work (included / not-included + coordination & training), line items, investment summary, and close (next step — no endpoint pricing tiers). Source master: `proposal-luci-retrofit.html` in this folder (build copy from `ui_kits/sales/`).

**This is the Budgetary Estimate + a scope of work, minus the endpoint pricing tiers.** The BE's page 4 (line items), page 5 (investment summary), and page 6 (close) are preserved; the BE's endpoint pricing tier chips are removed. Two SOW pages are inserted between the review of scope and the line items.

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
- **Subtraction over addition.** Lead with what LUCI removes, not what it adds.
- **Institutions, not adjectives.** Describe what the platform does for the enterprise, not how it feels.
- **Discretion over display.** No client names or percentage claims in public materials.
- **Register:** SOW/proposal = 3rd person, factual, narrative where it aids clarity. No marketing register in technical scope.

## Portal URL workflow (primary)

**Preview URL:** `http://10.10.1.17:8081/internal-portal/customization/proposal-luci-retrofit/proposal-luci-retrofit.html`

When Mike pastes this URL into Cursor chat:

1. Read this `SKILL.md` and `../_brand/SKILL.md` before any edits.
2. Copy master from `LUCI Systems Design System/ui_kits/sales/proposal-luci-retrofit.html` to `ui_kits/sales/<client>-proposal-luci-retrofit.html`.
3. Customize cover, overview, scope, SOW, line items, investment, and close per regions below.
4. Do **not** edit the HTML file on the VM deploy folder (overwritten on deploy).

See also: `../CURSOR.md`, `AGENTS.md` in this folder.

### Open the rendered preview in the editor (automatic)

After customizing, **automatically open the rendered client HTML in Cursor's in-editor (Glass) browser — not the HTML source** — without being asked:

1. **Start the LUCI dev server** rooted at **`LUCI Systems Design System/`**: `python3 ui_kits/internal-portal/customization/luci-dev-server.py` from that root (run as a background process). It serves the project on `http://127.0.0.1:8771` and accepts `POST /__save` so the edit bar's Save button writes typed edits back to the working file.
2. Verify: `curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:8771/ui_kits/sales/<client>-proposal-luci-retrofit.html` → `200`.
3. Open `http://127.0.0.1:8771/ui_kits/sales/<client>-proposal-luci-retrofit.html` in Cursor's in-editor browser via the `cursor-app-control` MCP `open_resource` tool (URI = that URL). Do **not** use a `file://` URI.

Click highlighted editable text and type; save the file when done.

## When to use

After a capabilities review and demo where the client needs a written proposal with scope of work, line items, and investment summary for a full LUCI platform installation (video and audio endpoints, integration hardware, professional services). **Not for LED wall projects** — use the Proposal - LED template for those.

## Page map — editable vs locked

*Page numbers below reflect the default 8-page layout. They shift if line items overflow to a second page — always reference by section name, not absolute page number.*

| Page | Section | Canvas | Status |
|------|---------|--------|--------|
| **1** | Cover | Light + navy hero band | **EDITABLE** (kicker, display, sub, client summary, prepared-for, client logo) |
| **2** | Overview — What LUCI is | Dark band | **EDITABLE** (intro text); **LOCKED** identity diagram + feature cards (boilerplate) |
| **3** | Review of scope | Dark band | **EDITABLE** (scope categories, endpoint counts, descriptions, bridge text, footnote) |
| **4** | §3 Scope of work — Included / Not included | Light | **EDITABLE** (all list items, callout body); **LOCKED** section number + title |
| **5** | §3 Scope of work — Coordination & training (cont.) | Light | **EDITABLE** (obligations list, punch-list body); **LOCKED** PM/training feature cards |
| **6** | Proposal — Line items | Dark band | **EDITABLE** (all line items, qty, cost, subtotals, group labels, deck text) |
| **7** | Investment summary | Dark band | **EDITABLE** (all summary values, total, CapEx/OpEx split); **LOCKED** `.be-delivers` marketing grid |
| **8** | Close — Next step | Dark band | **EDITABLE** (next-step body, contact name/email); **LOCKED** structure + LUCI company info |

### Variable page counts

- **Line items (page 6):** if the spreadsheet has more rows than fit on one page, the estimate spills onto a continuation page. Add a "continues on the following page" note; the continuation page reuses the same section header but does **not** add a second total.
- **SOW pages (4–5):** add or remove SOW continuation pages if the scope requires more detail (e.g., phasing, IDF/rack scope). Use subheads, not repeated section numbers.

---

## Editable regions by section

### Cover (page 1) — `.doc-page--cover`

| Element | Selector / class |
|---------|-----------------|
| Kicker | `.doc-cover__kicker` (default: "Proposal") |
| Display headline | `.doc-cover__display` (keep `<em>` for client short name) |
| Sub copy | `.doc-cover__sub` |
| Client summary | `.doc-cover__summary-text` |
| Client logo | `.doc-cover__client` (`src` + `alt`) |
| LUCI logo | `.doc-cover__logo` — **locked** (brand) |

### Overview (page 2) — `.doc-page--overview`

| Element | Selector / class |
|---------|-----------------|
| Band title / deck | `.doc-page-band__title` / `.doc-page-band__deck` |
| Intro text | `.be-intro__text` |
| Identity diagram | `.cap-identity` — **locked** (canonical asset) |
| Feature cards | `.cap-feature-card` — **locked** (boilerplate) |

### Review of scope (page 3) — `.doc-page--scope`

| Element | Selector / class |
|---------|-----------------|
| Band title / deck | `.doc-page-band__title` / `.doc-page-band__deck` |
| Bridge text | `.be-scope-bridge` |
| Scope rows | `.be-scope__cat`, `.be-scope__count`, `.be-scope__desc`, `.be-scope__tag` |
| Tally numbers | `.be-scope-tally__num` |
| Footnote | `.be-scope-footnote` |

### Scope of work (page 4) — `.doc-page--led-scope`

| Element | Selector / class |
|---------|-----------------|
| Section number | `.sow-band-bignum` (default: "03") |
| Section title | `.doc-page-band__title` (default: "Scope of Work") |
| Included head | `.led-check-panel__head` (first panel) |
| Included items | `.led-check-list` `<li>` elements (first panel) |
| Excluded head | `.led-check-panel__head` (second panel) |
| Excluded items | `.led-check-list--exclude` `<li>` elements (second panel) |
| Callout body | `.led-callout__body` |

### Coordination & training (page 5) — `.doc-page--led-coordination`

| Element | Selector / class |
|---------|-----------------|
| Subhead | `.led-subhead` (default: "Coordination & Training") |
| Feature cards | `.led-feature-card__name`, `.led-feature-card__body` — **locked** (PM/training boilerplate) |
| Obligations head | `.led-check-panel__head` |
| Obligations items | `.led-check-list` `<li>` elements |
| Punch-list label | `.led-callout__label` |
| Punch-list body | `.led-callout__body` |

### Line items (page 6) — `.doc-page--proposal`

Populate from the uploaded spreadsheet via `scripts/ingest-budgetary-lineitems.py` (same as the BE). The emitted `be-price-group` / `be-price-row` markup drops straight into the `.be-price` container. Each cell is `contenteditable` for word-level tweaks in preview. **No auto-math** — subtotals come from the spreadsheet; if you hand-edit a qty or unit price, recompute that row's subtotal yourself.

**One continuous table, one total.** Never split line items into sub-sections with separate sub-totals. If rows exceed one page, spill onto a continuation page.

**Only include rows that are in Mike's spreadsheet.** If the spreadsheet has a Sales Tax row, add it. If it doesn't, don't invent one. Same for freight, travel, or any other row.

**Combine endpoint pricing into one line item.** LUCI OS endpoint licenses must appear as a **single line item** referencing the **total number of endpoints** — never split by video/audio/etc. (See `../_brand/SKILL.md` → Pricing.)

### Investment summary (page 7) — `.doc-page--investment`

| Element | Selector / class |
|---------|-----------------|
| Summary values | `.be-summary__value`, `.be-summary__total-value`, `.be-split__value` |
| Delivers grid | `.be-delivers` — **locked** (marketing outcomes) |

### Close (page 8) — `.doc-page--investment-close`

| Element | Selector / class |
|---------|-----------------|
| Band title | `.doc-page-band__title` (default: "A property that gets simpler as it grows.") |
| Next-step body | `.be-close__body` |
| Contact name | `.be-close__name` (first instance) |
| Contact email | `.be-close__link` (first instance) |
| LUCI company info | `.be-close__name` / `.be-close__addr` / `.be-close__link` (second instance) — **locked** |

**No endpoint pricing tiers on this page.** The BE's tier chips (`.be-tier-chip`) are removed from this template. Per-endpoint pricing stays in the Budgetary Estimate only.

**No signature block.** The close page uses the BE's contact block (next step + rep + LUCI company info) — no signature lines, no date lines, no "accepted by" fields.

---

## Do not

- **Locked regions** (identity diagram + feature cards on page 2; `.be-delivers` marketing grid on page 7; PM/training feature cards on page 5; LUCI logo on cover; LUCI company info on close) — **no changes of any kind**, including color, styling, or CSS. Run the pre-edit gate in `.cursor/rules/luci-doc-customization.mdc` first.
- Add endpoint pricing tiers — this is the Proposal, not the Budgetary Estimate. Endpoint pricing stays in the BE.
- Add a signature block, signature lines, or "accepted by" fields — the close page is a contact block, not a sign-off.
- Split endpoint pricing into separate video/audio line items — combine into one row with the total endpoint count.
- Add "Addressed to" or similar labels to the cover.
- Use opaque JPEG client logos on the cover (white box artifact) — use transparent PNG/SVG.
- Invent hardware specs or pricing not supported by Mike's spreadsheet.
- Add marketing language to technical scope — stay factual and scoping-focused.

---

## Common tasks

**New LUCI platform proposal from site notes**
1. Cover (p1): client org, display `<em>` short name, prepared-for, client summary, client logo.
2. Overview (p2): update intro text to reference the specific property and phase.
3. Review of scope (p3): set scope categories, endpoint counts, and descriptions per the site survey.
4. SOW — Included / Not included (p4): rewrite the included and excluded lists to match the project scope.
5. SOW — Coordination & training (p5): update client obligations and punch-list text per the contract.
6. Line items (p6): populate from Mike's spreadsheet via `ingest-budgetary-lineitems.py`; split to a continuation page if it overflows.
7. Investment summary (p7): reconcile totals against the line items.
8. Close (p8): set the next-step body and contact name/email.

**Update `<title>`** in `<head>` to reflect client/project name.
