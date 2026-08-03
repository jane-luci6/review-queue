---
name: luci-proposal-retrofit
description: >-
  Customize the LUCI Proposal (LUCI Retrofit) for a specific client. Use when
  proposing a full LUCI platform installation — endpoint licensing, integration
  hardware, professional services, and the full 8-page scope of work. Built from
  the Budgetary Estimate with endpoint pricing removed and the full standalone
  SOW template inserted before line items. ~15 pages (variable).
---

# Proposal — LUCI Retrofit · customization

Full LUCI platform proposal. **~15 pages (US Letter, variable)** — cover (with date), overview (What LUCI is), review of scope, **full 8-page scope of work** (from the standalone SOW template), line items, investment summary, **payment terms**, and close (next step — no endpoint pricing tiers). Source master: `proposal-luci-retrofit.html` in this folder (build copy from `ui_kits/sales/`).

**This is the Budgetary Estimate + the full standalone Scope of Work, minus the endpoint pricing tiers.** The BE's line items, investment summary, and close are preserved; the BE's endpoint pricing tier chips are removed. The full 8-page SOW (pages 4–11) is inserted between the review of scope and the line items, using the standalone SOW template's content and CSS classes (`scope-of-work.css`).

Also read: `../_brand/SKILL.md` — especially **Efficient customization**, **Continuous page packing**, **Source fidelity**, **Totals span the full page width**, **Logo + pattern**, **Combine endpoint pricing into one line item**, and **PDF export — gradient + mask flattening**. Mike can click-edit any text (fonts/colors stay on CSS). Populate-in-place; never rebuild.

## Click-to-edit (Mike) vs agent edits

**Mike can click and type any text in the document.** Edit mode unlocks every text leaf. Fonts, colors, and layout stay on CSS classes — change words only; never strip `doc-edit` / `contenteditable` / structural wrappers.

**What stays non-editable (images only):** LUCI wordmark on the cover (`.doc-cover__logo`). Client logo is click-to-swap.

**Agent rules:** prefer `[data-studio]` selector edits (where present) or class-based edits; do not rebuild sections; do not invent fine-print; after Mike types in the preview, **Save** (or write the live DOM back to the same working file) before the next agent pass. Brand/voice still applies to any copy the agent authors.

**Save / PDF toolbar:** **Save** overwrites the working file via the LUCI dev server's `POST /__save` (no file picker, no Downloads artifact). **Copy HTML** puts the full document on the clipboard. **Download PDF** renders via `POST /__pdf` (headless Chrome — never `window.print()`, which crashes Cursor's in-editor browser) and downloads the PDF. See `../_brand/SKILL.md` → **PDF export — gradient + mask flattening** for why gradients/masks are flattened automatically.

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
2. Copy master to `clients/<client>-proposal-luci-retrofit.html` using `scripts/prepare-client-doc.sh ui_kits/sales/proposal-luci-retrofit.html clients/<client>-proposal-luci-retrofit.html` (adjusts all relative paths automatically). Do **not** manually copy to `ui_kits/sales/` — client files live in the top-level `clients/` folder.
3. Customize cover, overview, scope, SOW, line items, investment, and close per regions below.
4. Do **not** edit the HTML file on the VM deploy folder (overwritten on deploy).

See also: `../CURSOR.md`, `AGENTS.md` in this folder.

### Open the rendered preview in the editor (automatic)

After customizing, **automatically open the rendered client HTML in Cursor's in-editor (Glass) browser — not the HTML source** — without being asked:

1. **Start the LUCI dev server** rooted at **`LUCI Systems Design System/`**: `python3 ui_kits/internal-portal/customization/luci-dev-server.py` from that root (run as a background process). It serves the project on `http://127.0.0.1:8771` and accepts `POST /__save` so the edit bar's Save button writes typed edits back to the working file.
2. Verify: `curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:8771/clients/<client>-proposal-luci-retrofit.html` → `200`.
3. Open `http://127.0.0.1:8771/clients/<client>-proposal-luci-retrofit.html` in Cursor's in-editor browser via the `cursor-app-control` MCP `open_resource` tool (URI = that URL). Do **not** use a `file://` URI.

Click highlighted editable text and type; save the file when done.

## When to use

After a capabilities review and demo where the client needs a written proposal with scope of work, line items, and investment summary for a full LUCI platform installation (video and audio endpoints, integration hardware, professional services). **Not for LED wall projects** — use the Proposal - LED template for those.

## Page map — editable vs locked

*Page numbers below reflect the default 15-page layout. They shift if SOW content or line items overflow to additional pages — always reference by section name, not absolute page number.*

| Page | Section | Canvas | Status |
|------|---------|--------|--------|
| **1** | Cover | Light + navy hero band | **EDITABLE** (kicker, display, sub, client summary, **date**, prepared-for, client logo) |
| **2** | Overview — What LUCI is | Dark band | **EDITABLE** (intro text); **LOCKED** identity diagram + feature cards (boilerplate) |
| **3** | Review of scope | Dark band | **EDITABLE** (scope categories, endpoint counts, descriptions, bridge text, footnote) |
| **4** | §1 Project Intent + §2 Guiding Principles | Light (SOW band) | **EDITABLE** (all text); **LOCKED** section numbers |
| **5** | §3 Project Phasing + §4 System Scope (4.1) | Light (SOW band) | **EDITABLE** (all text); **LOCKED** section numbers |
| **6** | §4 System Scope cont. (4.2–4.4: IPTV, encoders, audio) | Light (SOW band) | **EDITABLE** (all text); **LOCKED** section numbers |
| **7** | §4 System Scope cont. (4.5–4.6: network, remote access) | Light (SOW band) | **EDITABLE** (all text); **LOCKED** section numbers |
| **8** | §5 IDF / Rack Scope (5.1–5.4) | Light (SOW band) | **EDITABLE** (all text); **LOCKED** section numbers |
| **9** | §5 IDF / Rack Scope cont. (5.5–5.6) | Light (SOW band) | **EDITABLE** (all text); **LOCKED** section numbers |
| **10** | §6 Deliverables + §7 Assumptions/Constraints/Exclusions | Light (SOW band) | **EDITABLE** (all text); **LOCKED** section numbers |
| **11** | §8 Open Items to Confirm | Light (SOW band) | **EDITABLE** (all text); **LOCKED** section numbers |
| **12** | Proposal — Line items | Dark band | **EDITABLE** (all line items, qty, cost, subtotals, group labels, deck text) |
| **13** | Investment summary | Dark band | **EDITABLE** (all summary values, total, CapEx/OpEx split); **LOCKED** `.be-delivers` marketing grid |
| **14** | Payment terms | Light (LED-fee style) | **EDITABLE** (all milestone percentages, labels, due descriptions, notes) |
| **15** | Close — Next step | Dark (capabilities-doc style) | **EDITABLE** (kicker, headline, next-step body, contact name/email); **LOCKED** LUCI logo + company info |

### Variable page counts

- **SOW pages (4–11):** the 8 SOW pages mirror the standalone Scope of Work template. Add or remove SOW continuation pages if the scope requires more or less detail (e.g., fewer IDF pages, additional phasing). Use subheads (`.sow-subsection-title`), not repeated section numbers. The SOW uses `scope-of-work.css` classes — do not mix in `led-*` classes from the LED proposal. **SOW content flows continuously** — sections, subsections, line items, and bullets may break across page boundaries; do not force section-start page breaks or leave large gaps (see `../_brand/SKILL.md` → Continuous page packing).
- **Line items (page 12):** if the spreadsheet has more rows than fit on one page, the estimate spills onto a continuation page. Add a "continues on the following page" note; the continuation page reuses the same section header but does **not** add a second total.

---

## Editable regions by section

### Cover (page 1) — `.doc-page--cover`

| Element | Selector / class |
|---------|-----------------|
| Kicker | `.doc-cover__kicker` (default: "Proposal") |
| Display headline | `.doc-cover__display` (keep `<em>` for client short name) |
| Sub copy | `.doc-cover__sub` |
| Client summary | `.doc-cover__summary-text` |
| Date | `.doc-cover__date` (format: "Month DD, YYYY") |
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

### Scope of Work (pages 4–11) — SOW template classes

The SOW pages use the standalone Scope of Work template's CSS classes (`scope-of-work.css`). All text is editable; section numbers (`.sow-band-bignum`) and band kickers are locked structure.

When Mike provides a source SOW, **mirror its verbiage and structure** (headers, narrative vs bullets, section order) and dress it in the SOW branded classes. Pack continuously across pages — sections may break mid-way with “(continued)”. See `../_brand/SKILL.md` → Continuous page packing and Source fidelity.

| Element | Selector / class |
|---------|-----------------|
| Section band number | `.sow-band-bignum` — **locked** (01–08) |
| Band kicker | `.doc-page-band__kicker` |
| Band title | `.doc-page-band__title` |
| Section head text | `.doc-section-head__text` |
| Subsection title | `.sow-subsection-title` |
| List label | `.sow-list-label` |
| Scope list items | `.sow-scope-list` `<li>` elements (variants: `--checks`, `--bullets`, `--ledger`) |
| Function items | `.doc-fn__label`, `.doc-fn__text` |
| Scope block | `.sow-scope-block` |
| Takeaway / open items | `.doc-takeaway`, `.sow-open-items` |
| Note | `.sow-note` |

**SOW page breakdown (default — shifts with content):**
- **Page 4 (§1–2):** Project Intent + Guiding Principles
- **Page 5 (§3–4.1):** Project Phasing + System Scope intro
- **Page 6 (§4.2–4.4):** IPTV upgrade, local content ingestion, audio modernization
- **Page 7 (§4.5–4.6):** Network overhaul, secure remote access
- **Page 8 (§5.1–5.4):** IDF/Rack scope (main casino, ISP ingest, hotel IPTV, sportsbook)
- **Page 9 (§5.5–5.6):** IDF/Rack scope cont. (spa, meeting/conferencing)
- **Page 10 (§6–7):** Deliverables + Assumptions/Constraints/Exclusions
- **Page 11 (§8):** Open Items to Confirm

**These page boundaries are defaults, not fixed.** SOW content flows continuously — sections, subsections, line items, and bullets may break across page boundaries. If content shifts (more or less scope detail), repack greedily and renumber footers. Do not force a section to start on a new page when it would fit at the bottom of the current one.

### Line items (page 12) — `.doc-page--proposal`

Populate from the uploaded spreadsheet via `scripts/ingest-budgetary-lineitems.py` (same as the BE). The emitted `be-price-group` / `be-price-row` markup drops straight into the `.be-price` container. Each cell is `contenteditable` for word-level tweaks in preview. **No auto-math** — subtotals come from the spreadsheet; if you hand-edit a qty or unit price, recompute that row's subtotal yourself.

**One continuous table, one total.** Never split line items into sub-sections with separate sub-totals. If rows exceed one page, spill onto a continuation page.

**Pack greedily; totals break unless they fit.** Keep groups/rows on the same page when they fit. Put a page break **before** the summary/totals unless the **full** totals block fits on the last line-item page. See `../_brand/SKILL.md` → Continuous page packing.

**Source fidelity + branded dress.** Mirror the spreadsheet’s labels, order, and structure; apply `.be-price*` branded formatting. See `../_brand/SKILL.md` → Source fidelity.

**Totals span full page width.** `.be-summary` / `.be-summary__total` (and `.be-p5-numbers`) must be full content width — never `max-width: 48ch`. See `../_brand/SKILL.md` → Totals span the full page width.

**Only include rows that are in Mike's spreadsheet.** If the spreadsheet has a Sales Tax row, add it. If it doesn't, don't invent one. Same for freight, travel, or any other row.

**Combine endpoint pricing into one line item.** LUCI OS endpoint licenses must appear as a **single line item** referencing the **total number of endpoints** — never split by video/audio/etc. (See `../_brand/SKILL.md` → Pricing.)

### Investment summary (page 13) — `.doc-page--investment`

| Element | Selector / class |
|---------|-----------------|
| Summary values | `.be-summary__value`, `.be-summary__total-value`, `.be-split__value` |
| Delivers grid | `.be-delivers` — **locked** (marketing outcomes) |

### Payment terms (page 14) — `.doc-page--led-fee`

Standard payment terms page (light canvas, LED-fee style milestones). Defaults to multimedia equipment terms: 50% deposit upon award, 50% pre-shipment (second 50% due on final piece shipping date with tracking info provided), balance upon final acceptance. Quote valid for 30 days.

| Element | Selector / class |
|---------|-----------------|
| Subhead | `.led-subhead` (default: "Payment Terms") |
| Milestone percentage | `.led-fee-mile__pct` (e.g. "50%", "Remaining") |
| Milestone label | `.led-fee-mile__label` |
| Milestone due description | `.led-fee-mile__due` |
| Notes / validity | `.led-fee-notes` `<p>` (30-day validity, USD, sales tax note) |

### Close (page 15) — `.doc-page--close`

Capabilities-doc-style close page (dark, circuit texture, LUCI wordmark logo, Syncopate headline).

| Element | Selector / class |
|---------|-----------------|
| LUCI logo | `.doc-close__logo` — **locked** (brand) |
| Kicker | `.doc-eyebrow--mint` (default: "Next step") |
| Headline | `.doc-close__head` (keep `<em>` for the display phrase) |
| Next-step body | `.doc-close__body` |
| Contact name | `.doc-close__name` (first instance, in `.doc-close__rep`) |
| Contact email | `.doc-close__rep` `<a>` (first instance) |
| LUCI company info | `.doc-close__company` (name, address, phone, URL) — **locked** |

**No endpoint pricing tiers on this page.** The BE's tier chips (`.be-tier-chip`) are removed from this template. Per-endpoint pricing stays in the Budgetary Estimate only.

**No signature block.** The close page uses the capabilities-doc-style contact block (LUCI wordmark + Syncopate headline + two-column contacts) — no signature lines, no "accepted by" fields. The proposal date lives on the cover (`.doc-cover__date`); payment terms live on page 14 (`.doc-page--led-fee`).

---

## Do not

- **Locked regions** (identity diagram + feature cards on page 2; `.be-delivers` marketing grid on page 13; SOW section numbers `.sow-band-bignum`; LUCI logo on cover; LUCI company info on close) — **no changes of any kind**, including color, styling, or CSS. Run the pre-edit gate in `.cursor/rules/luci-doc-customization.mdc` first.
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
1. Cover (p1): client org, display `<em>` short name, prepared-for, client summary, **date** (`.doc-cover__date` — format "Month DD, YYYY"), client logo.
2. Overview (p2): update intro text to reference the specific property and phase.
3. Review of scope (p3): set scope categories, endpoint counts, and descriptions per the site survey.
4. SOW pages (p4–11): rewrite the 8 SOW pages to match the project scope — project intent, guiding principles, phasing, system scope (platform, IPTV, encoders, audio, network, remote access), IDF/rack scope, deliverables, assumptions/constraints/exclusions, and open items. Adapt from the standalone SOW template content. **Pack continuously** — sections, subsections, line items, and bullets may break across page boundaries (see `../_brand/SKILL.md` → Continuous page packing).
5. Line items (p12): populate from Mike's spreadsheet via `ingest-budgetary-lineitems.py`; split to a continuation page if it overflows.
6. Investment summary (p13): reconcile totals against the line items.
7. Payment terms (p14): verify milestone percentages, labels, and due descriptions match the deal terms; update the 30-day validity date reference if needed.
8. Close (p15): set the next-step body and contact name/email.

**Update `<title>`** in `<head>` to reflect client/project name.
