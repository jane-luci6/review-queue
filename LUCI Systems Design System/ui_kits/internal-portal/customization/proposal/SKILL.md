---
name: luci-proposal
description: >-
  Customize the LUCI Proposal for a specific client LED wall project.
  Use when scoping a COB LED display installation: cover, COB technology overview,
  scope, coordination, per-pitch design specs, fee schedule, per-installation
  estimates, terms, and the close page are editable; LUCI branding, COB advantage
  boilerplate, gallery layout, and spec schema stay locked.
---

# Proposal · customization

Post-survey proposal for LED wall installations. **~13 pages (US Letter, variable)** — cover, then five numbered sections: §1 Project overview (dark), §2 Built on COB (dark, spans the COB advantage + project gallery), §3 Scope of work (spans scope + coordination + per-pitch design specs), §4 Fee schedule & payment terms (estimates first — one estimate page per LED installation, flowing across pages — then payment milestones + fine print), §5 Terms & warranty, then a close page (Next step + contacts — no signature block). **Page count is not fixed** — spec pages and estimate pages are added or removed to match the project; all trailing page numbers and footers shift accordingly. Source master: `proposal.html` in this folder (build copy from `ui_kits/sales/`).

**Section numbering rule:** a section number appears only on the first page of that section (the band big-numeral + title). Continuation pages within the same section carry a `.led-subhead` instead — no repeated number. In the default 13-page layout, §3's number lives on page 5; pages 6–8 use subheads ("Coordination & Training", "Design Specifications — <pitch>"). §4's number lives on page 9 (Estimate 01 opener). Estimate 02 on p10 and Payment Terms on p11 are subheads — no repeated §4 number. §5's number lives on page 12 (Terms). **These page numbers shift when spec or estimate pages are added/removed** — always reference by section, not by absolute page number.

Also read: `../_brand/SKILL.md` — especially **Efficient customization (read this first)**, **Continuous page packing**, **Source fidelity**, **Totals span the full page width**, **Logo + pattern**, and **PDF export — gradient + mask flattening**. This is a populate-in-place job; never rebuild.

## Click-to-edit (Mike) vs agent edits

**Mike can click and type any text in the document.** Edit mode unlocks every text leaf (including former “boilerplate” pages). Fonts, colors, and layout stay on CSS classes — change words only; never strip `doc-edit` / `data-studio` / structural wrappers.

**What stays non-editable (images only):** LUCI wordmark on the cover (`.doc-cover__logo`) and the close-page LUCI logo (`.doc-close__logo`). Client logo is still click-to-swap.

**Agent rules (unchanged discipline):** prefer `[data-studio]` selector edits; do not rebuild sections; do not invent fine-print; after Mike types in the preview, **Save** (or write the live DOM back to the same working file) before the next agent pass. Brand/voice still applies to any copy the agent authors.

**Save / PDF toolbar:** **Save** overwrites the working file via the LUCI dev server's `POST /__save` (no file picker, no Downloads artifact). **Copy HTML** puts the full document on the clipboard. **Download PDF** renders via `POST /__pdf` (headless Chrome — never `window.print()`, which crashes Cursor's in-editor browser) and downloads the PDF. See `../_brand/SKILL.md` → **PDF export — gradient + mask flattening** for why gradients/masks are flattened automatically.

## Voice

Match LUCI's voice on every line you write or rewrite. Full contract: `../_brand/SKILL.md` → **Voice & tone**. Canonical source: LUCI Messaging Guide (`ui_kits/review/messaging/messaging-guide.html`). Cover-page goal rewrites: `ui_kits/internal-portal/skills/cover-page-customization.md`.

- **Engine and verbs — not layers.** Never use *layer* as a noun for LUCI. Lead with **orchestration engine** / **LUCI orchestrates…**; rotate to *runs, operates, integrates, consolidates, refines*.
- **Always write A/V** — never "AV" or "A-V" (body, headlines, labels, captions, alt text, diagrams).
- **Declarative, not promotional.** State facts; no "revolutionize / transform / empower / absurdly simple." Stay factual and scoping-focused — no marketing language in technical scope.
- **Subtraction over addition.** Lead with what LUCI removes (variables, vendors, interfaces, refresh cycles), not what it adds.
- **Institutions, not adjectives.** Describe what the platform does for the enterprise, not how it feels.
- **Discretion over display.** No client names or percentage claims in public materials.
- **Retired terms:** absurdly simple / easy to use / intuitive · revolutionize / transform / empower · best-in-class / game-changing · owner's rep (use LUCI FDE / embedded team) · *layer* for LUCI.
- **Verbatim lines:** tagline, sub-tagline, and value-prop boilerplate — use as written, do not paraphrase.
- **Register:** SOW/proposal = 3rd person, factual, narrative where it aids clarity. No marketing register in technical scope.

## Portal URL workflow (primary)

**Preview URL:** `http://10.10.1.17:8081/internal-portal/customization/proposal/proposal.html`

When Mike pastes this URL into Cursor chat:

1. Read this `SKILL.md` and `../_brand/SKILL.md` before any edits.
2. Copy master from `LUCI Systems Design System/ui_kits/sales/proposal.html` to `ui_kits/sales/<client>-proposal.html`.
3. Customize cover, scope, specs, fee, estimates, terms, and close per this skill — preserve CSS classes.
4. Do **not** edit the HTML file on the VM deploy folder (overwritten on deploy).

See also: `../CURSOR.md`, `AGENTS.md` in this folder.

### Open the rendered preview in the editor (automatic)

After customizing, **automatically open the rendered client HTML in Cursor's in-editor (Glass) browser — not the HTML source** — without being asked:

1. **Start the LUCI dev server** rooted at **`LUCI Systems Design System/`** (not `ui_kits/sales/`) so `../../assets/` relative paths resolve to the canonical assets folder: `python3 ui_kits/internal-portal/customization/luci-dev-server.py` from that root (run as a background process). It serves the project on `http://127.0.0.1:8771` and accepts `POST /__save` so the edit bar's Save button writes typed edits back to the working file.
2. Verify: `curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:8771/ui_kits/sales/<client>-proposal.html` → `200`.
3. Open `http://127.0.0.1:8771/ui_kits/sales/<client>-proposal.html` in Cursor's in-editor browser via the `cursor-app-control` MCP `open_resource` tool (URI = that URL). Do **not** use a `file://` URI — that opens the HTML source, not the rendered doc. Do **not** root the server in `ui_kits/sales/` — the cover logo and `../../assets/` paths will 404.

Click highlighted editable text and type; save the file when done. User fallback if the pane doesn't appear: `Cmd+Shift+P` → "Simple Browser: Show" → paste the localhost URL.

## When to use

After a site survey or discovery for an LED wall project (casino sportsbook, center-bar tower, casino-floor ribbon, facade, etc.) where the client needs a written scope with COB technology context, per-pitch specs, pricing milestones, and per-installation estimates.

## Workflow

1. Open the **portal preview** (URL above) or copy that URL into Cursor chat.
2. Provide: project title, client org, basis (survey/meeting notes), pixel pitch(s) featured, and one line-items set per LED installation.
3. Save the **client version** in luci-design under `ui_kits/sales/<client>-proposal.html` — not over the master.
4. Preview → Print/Save as PDF (US Letter).

---

## Page map — editable vs locked

*Page numbers below reflect the default 13-page layout. They shift when spec or estimate pages are added or removed — always reference by section name, not absolute page number.*

| Page | Section | Canvas | Status |
|------|---------|--------|--------|
| **1** | Cover | Dark | **EDITABLE** (see exceptions below) |
| **2** | §1 Project overview | Dark | **EDITABLE** (deck, intent/approach/outcome/standard narrative, scope list, 4 stat values, pairing callout) |
| **3** | §2 Built on COB — The COB Advantage (part 1 of 2) | Dark | **LOCKED** (advantage tiles, NovaStar architecture, 4 stat tiles) — boilerplate |
| **4** | §2 Built on COB — Project Gallery (part 2 of 2, no repeated §2 header) | Dark | **EDITABLE** photos + captions (Mike swaps images); **LOCKED** layout |
| **5** | §3 Scope of work | Light | **EDITABLE** (included / not-included lists); **LOCKED** process paragraph |
| **6** | §3 Scope of work — Coordination & training (cont.) | Light | **EDITABLE** (client obligations, punch-list line); **LOCKED** PM/training boilerplate |
| **7** | §3 Scope of work — Design specifications, pitch 1 (cont.) | Light | **EDITABLE** (all spec values + pitch in subhead); **LOCKED** spec row labels |
| **8** | §3 Scope of work — Design specifications, pitch 2 (cont.) | Light | **EDITABLE** (all spec values + pitch in subhead); **LOCKED** spec row labels |
| **9** | §4 Fee schedule & payment terms — Estimate 01 (section opener) | Light | **EDITABLE** (all line items, qty, rate, amount, total, estimate #, date, name) |
| **10** | §4 Fee schedule — Estimate 02 (cont., clone per install) | Light | **EDITABLE** — clone this page for each additional LED installation |
| **11** | §4 Fee schedule — Payment Terms (cont.) | Light | **EDITABLE** (milestones + all fine print: USD note + tariff) |
| **12** | §5 Terms & warranty | Light | **EDITABLE** (warranty duration); **LOCKED** 4-column warranty boilerplate |
| **13** | Close (Next step + contacts) | Dark | **EDITABLE** (next-step body, contact name/email); **LOCKED** structure + LUCI company info |

### Variable page counts

- **Spec pages (7–8):** one page per pixel pitch in the project, all under §3 (subheads, no repeated section number). Add or remove `.doc-page--led-specs` sections to match the number of pitches.
- **Estimate pages (9+):** one estimate per LED installation, all under §4 (subheads, no repeated section number). Each estimate flows continuously across as many pages as its line items need — add a "continues on the following page" note when an estimate spans pages. Clone the estimate section for each installation; renumber trailing page footers (`doc-foot__page`) only — do **not** add a `sow-band-bignum` to continuation pages. Payment Terms (p11) is also a §4 continuation page (subhead, no number).

### Cover exceptions (page 1 — do not change)

| Element | Why locked |
|---------|------------|
| `.doc-cover__logo` (LUCI logo image) | Brand |
| "Prepared by" value remains **LUCI Systems, LLC** unless Jane directs otherwise | Standard attribution |

Everything else on the cover with `doc-edit` / `contenteditable="true"` is editable.

---

## Editable regions by section

**Every variable field carries a `data-studio` attribute.** Locate by `[data-studio="…"]` and replace the text node (or `src`/`alt`/`href`) only. Do not rewrite a whole `<section>` to change a value. Preserve `class="doc-edit" contenteditable="true"` on every hooked field.

### Cover (page 1) — `.doc-page--cover`

| Element | Selector |
|---------|----------|
| Display headline | `[data-studio="cover-display"]` |
| Project title | `[data-studio="project-title"]` |
| Label / Prepared for | `[data-studio="label-prepared-for"]` / `[data-studio="prepared-for"]` |
| Label / Prepared by | `[data-studio="label-prepared-by"]` / `[data-studio="prepared-by"]` |
| Label / Basis | `[data-studio="label-basis"]` / `[data-studio="basis"]` |
| Label / Date | `[data-studio="label-date"]` / `[data-studio="proposal-date"]` |
| Client logo | `[data-studio="client-logo"]` (`src` + `alt`) |

**Proposal date:** the master shows "Today" as a placeholder; a small inline script stamps the current date on load (only while the placeholder is still "Today"). When generating a client proposal, **replace "Today" with the issue date** (e.g. "July 27, 2026") as a static value — a real date persists and the script leaves it alone.


### Project overview (page 2) — `.doc-page--led-overview`

| Element | Selector |
|---------|----------|
| Title / deck | `overview-title` / `overview-deck` |
| Narratives | `overview-intent` · `overview-approach` · `overview-outcome` · `overview-standard` |
| Scope list | `overview-scope-1` … `overview-scope-6` |
| Pairing / note | `overview-pairing` / `overview-note` |
| Stats | `overview-stat-1` … `overview-stat-4` |

### §2 Technology Overview — COB Advantage (page 3)

Mike may click-edit any text here. Hooks: `tech-title`, `tech-cob-subhead`, `tech-cob-deck`, `tech-stat-1`…`4`, plus auto-* on advantage tiles / arch paragraph. **Agent:** treat as brand boilerplate — only change when Mike asks; do not invent alternate tech claims.

### §2 Project Gallery (page 4)

| Element | Selector |
|---------|----------|
| Subhead / deck | `gallery-subhead` / `gallery-deck` |
| Photos | `gallery-img-1` … `gallery-img-4` (`src` + `alt`) |
| Captions | `gallery-cap-1` … `gallery-cap-4` |

Layout (2×2) stays locked.

**Section title follows the photos Mike uploads:** if Mike provides design renderings of the proposed install, title the section “Design Renderings” (subhead + deck). If Mike provides photos of past installations, title it “Project Gallery.” Match the subhead and deck copy to whichever Mike provides.

### §3 Scope of work (page 5)

| Element | Selector |
|---------|----------|
| Title | `scope-title` |
| Included head / items | `scope-included-head` · `scope-included-1` … `scope-included-8` |
| Excluded head / items | `scope-excluded-head` · `scope-excluded-1` … `scope-excluded-5` |

**Locked:** certified-technicians / kickoff process callout.

### §3 Coordination & training (page 6)

| Element | Selector |
|---------|----------|
| Subhead | `coord-subhead` |
| Obligations | `obligations-head` · `obligation-1` … `obligation-5` |
| Punch list | `punch-list` |

**Locked:** PM + training boilerplate rows.

### §3 Design specifications (pages 7–8)

| Element | Selector |
|---------|----------|
| Subhead / pitch | `spec-N-subhead` / `spec-pitch-N` |
| Values | `spec-N-display-model`, `spec-N-pixel-pitch`, `spec-N-panel-size`, `spec-N-resolution-panel`, `spec-N-brightness`, `spec-N-contrast-ratio`, `spec-N-refresh-rate`, `spec-N-color-depth`, `spec-N-viewing-angle`, `spec-N-power-consumption`, `spec-N-lifespan`, `spec-N-ip-rating`, `spec-N-operating-temp`, `spec-N-video-processor` |
| Note | `spec-N-note` |

**Locked:** `.led-spec-row__label` schema. N = pitch page (1, 2, …).

### §4 Fee schedule — Payment Terms (page 11, continuation)

| Element | Selector |
|---------|----------|
| Subhead | `payment-terms-subhead` |
| Milestone N | `fee-mile-N-pct` · `fee-mile-N-label` · `fee-mile-N-due` (N = 1–3) |
| Fine print | `fee-note-usd` · `fee-note-tariff` |

**Everything on this page is editable**, including fine print. Structure (stack of milestones) stays.

**Populate from Mike’s input — not a fixed template.** Most proposals show dollar amounts per milestone ($77,145.11 / $65,145.11 / …); some show percentages (50% / 50% / Remaining). Use whichever Mike provides. If Mike gives dollar amounts, include a one-line description of what’s in each milestone (equipment vs. professional services vs. balance). Reconcile the milestones to the estimate total in the fine print.

### §4 Fee schedule — Estimates (pages 9–10, section opener)

| Element | Selector |
|---------|----------|
| Subhead / name / # / date / total | `estimate-N-subhead` · `estimate-N-name` · `estimate-N-num` · `estimate-N-date` · `estimate-N-total` |
| Line row R | `estimate-N-row-R-mfg` · `-item` · `-desc` · `-qty` · `-rate` · `-amount` |
| Footnote | `estimate-N-footnote` |

**No auto-math** — recompute amount/total by hand when qty or rate changes. Clone the estimate section for more installs; keep the `estimate-N-…` numbering consecutive.

**One estimate = one continuous table = one total.** Never split an estimate into sub-sections (e.g. “hardware” / “cabling” / “services”) with separate sub-totals. The spreadsheet Mike uploads has everything summed together — the proposal mirrors that: one table, one “Project total” at the end. If the line items exceed one page, the estimate spills onto the next page (add a “continues on the following page” note at the bottom of the first page); the continuation page reuses the same estimate # and date with a descriptive subhead (e.g. “Source, Rack & Services”) but does **not** add a second total.

**Pack greedily; totals break unless they fit.** Keep the next block of rows on the same page when it fits. Put a page break **before** the project total unless the **full** total block fits on the last estimate page. See `../_brand/SKILL.md` → Continuous page packing.

**Source fidelity + branded dress.** Mirror the spreadsheet’s labels, order, and structure; apply the estimate’s branded formatting. See `../_brand/SKILL.md` → Source fidelity.

**Totals span full page width.** Estimate / project total rows must span the full content width of the page — never constrain the total block to a narrow `max-width` (e.g. 48ch). See `../_brand/SKILL.md` → Totals span the full page width.

**Only include rows that are in Mike’s spreadsheet.** If the spreadsheet has a Sales Tax row, add it as a line item. If it doesn’t, don’t invent one. Same for freight, travel, or any other row — the estimate mirrors the spreadsheet exactly, no added and no removed rows.

**Combine endpoint pricing into one line item.** LUCI OS endpoint licenses must appear as a **single line item** referencing the **total number of endpoints** — never split out by video, audio, or other sub-categories. If Mike’s spreadsheet has them combined, mirror that. If a previous AI run split them into separate video/audio/etc. rows, combine them back into one row with the total endpoint count. The label should match Mike’s spreadsheet (e.g. “LUCI OS & Endpoint Licenses” or “LUCI OS — Annual Partnership”) — do not invent a different label.

### §5 Terms & warranty (page 12)

| Element | Selector |
|---------|----------|
| Title | `terms-title` |
| Duration | `warranty-duration` |

**Locked:** 4-column warranty grid + extended-warranty paragraph.

### Close (page 13)

| Element | Selector |
|---------|----------|
| Head / body | `close-head` / `close-body` |
| Contact | `close-contact-name` / `close-contact-email` |

**Locked:** structure, LUCI company block, navy circuit band. **No signature block.**

When editing HTML directly, preserve `doc-edit` / `contenteditable` / `data-studio` on every field.

---

## Typography & font styling (required)

Fonts are applied by **CSS classes**, not inline styles. When customizing copy, **change text only** — preserve every wrapper element and its classes so headers stay Space Grotesk, body copy stays Inter, and display moments stay Syncopate. This keeps header and copy sizes/colors/formatting consistent across documents even when the words change.

| Role | Element / class | Font | Do |
|------|-----------------|------|-----|
| Cover display | `.doc-cover__display` | Syncopate | Edit words only; keep `<em>` for client short name |
| Cover meta labels | `.doc-eyebrow` | Space Grotesk | Edit label text only |
| Cover meta values | `.sow-meta__value` | Inter | Edit value text only |
| Section headers | `.doc-page-band__title` | Space Grotesk 700 | Edit title text; keep one line where possible |
| Dark-page headers | `.led-dark-head__title` | Space Grotesk 700 | Edit title text only |
| Dark-page kickers | `.led-dark-head__kicker` | Space Grotesk | Edit kicker text only |
| Stat numerals (light) | `.led-stat__num` | Space Grotesk | Edit value only |
| Stat labels | `.led-stat__label` | Space Grotesk | Locked schema — do not edit |
| Advantage names | `.led-advantage__name` | Space Grotesk | Locked boilerplate |
| Advantage bodies | `.led-advantage__body` | Inter | Locked boilerplate |
| Spec labels | `.led-spec-row__label` | Space Grotesk | Locked schema — do not edit |
| Spec values | `.led-spec-row__value` | Space Grotesk | Edit value only |
| Fee percentages | `.led-fee-mile__pct` | Space Grotesk | Edit value only |
| Estimate line items | `.led-price__mfg`, `.led-price__item` | Space Grotesk | Edit text only |
| Estimate descriptions | `.led-price__desc` | Inter | Edit text only |
| Estimate numerals | `.led-price__num` | Space Grotesk | Edit value only |
| Warranty column heads | `.led-terms-col__head` | Space Grotesk | Locked boilerplate |
| Warranty list items | `.led-terms-col li` | Inter | Locked boilerplate |
| Body paragraphs | `.doc-section-head__text` | Inter | Edit paragraph text only |
| List items | `.sow-scope-list li` | Inter | Edit item text; use `<strong>` for lead terms |

### Rules when adding or rewriting content

1. **Never** add inline `font-family`, `font-size`, or `font-weight` — the linked stylesheets own typography.
2. **Never** replace a styled element with a plain `<p>` or `<div>` — duplicate the markup pattern from a neighboring item (same classes).
3. **New list items** must use `<li class="doc-edit" contenteditable="true">…</li>` inside the existing `<ul class="sow-scope-list …">`.
4. **New estimate rows** must use the `.led-price-row` grid with the same 6-column `grid-template-columns` and `.doc-edit` cells.
5. **New spec rows** must use `<div class="led-spec-row"><dt class="led-spec-row__label">…</dt><dd class="led-spec-row__value doc-edit" contenteditable="true">…</dd></div>`.
6. **Do not** strip `doc-edit` or `contenteditable="true"` from elements you modify.
7. Linked stylesheets and `<head>` font links must not be removed or swapped.

If preview shows wrong fonts after an edit, the HTML structure was likely broken — restore the original classes from the master copy.

---

## Copy guidance

- Use **specific panel models, pixel pitches, processor models, and installation locations** from site notes.
- Keep the spec schema labels intact — only values change per panel model.
- Estimate pages: one per LED installation; clone and renumber. No auto-math — recompute totals by hand.
- Fee milestones: match the contract terms (default 50/50/remaining).
- Warranty duration: match the contract (default 2-year comprehensive).
- Match tone: operational, factual, scoping-focused. No marketing register in technical scope.

---

## Do not

- **Locked pages/regions** (page 3 COB advantage + architecture; page 12 warranty grid; spec schema labels; cover LUCI logo; document CSS/structure; page footers; band big numerals; LUCI contact line) are **locked — no changes of any kind, including color, styling, or CSS.** If asked to change one, do NOT edit first — flag it and ask whether to override (local-only vs canonical) before making any change.
- Change LUCI cover logo or document CSS/structure.
- Remove page footers (`.doc-foot`) or band big numbers (`.sow-band-bignum`).
- Manually edit the footer text span (`.doc-foot > span:first-child`) — it is auto-synced to the cover’s project title (`project-title`) by an inline script. To change the footer, change the project title on the cover; the footers update automatically. Page numbers (`.doc-foot__page`) are still manual.
- Add inline font styles or unclassed elements that bypass the typography table above.
- Add marketing language to technical scope — stay factual and scoping-focused.
- Invent hardware specs or pricing not supported by client notes.
- Use opaque JPEG client logos on the cover (white box artifact) — use transparent PNG/SVG.

---

## Common tasks

**New LED project from site notes**
1. Cover (p1): project title, prepared-for, basis, logo, display `<em>` name, and **stamp the proposal date** (replace the "Today" placeholder with the issue date).
2. §1 Project overview (p2): rewrite the intent/approach/outcome/standard narrative; set the 4 stat values to the proposed panel's pitch / angle / lifespan / IP.
3. §3 Scope of work — Design specifications (p7–8): set spec values per pixel pitch; add/remove spec pages to match the number of pitches (subheads, no repeated §3 number).
4. §4 Fee schedule — Payment Terms (p11): set fee milestones per contract.
5. §4 Fee schedule — Estimates (p9+): one estimate per LED installation — populate line items, qty, rate, amount, total (subheads, no repeated §4 number). Let each estimate flow across pages if line items exceed one page.
6. §5 Terms & warranty (p12): set warranty duration per contract.
7. Close (p13): set the next-step body + the contact name/email (no signature block).

**Update `<title>`** in `<head>` to reflect client/project name.


