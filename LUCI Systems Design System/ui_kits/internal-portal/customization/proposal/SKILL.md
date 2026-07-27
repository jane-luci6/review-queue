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

Post-survey proposal for LED wall installations. **14 pages (US Letter)** — cover, contents, then five numbered sections: §1 Project overview (dark), §2 Built on COB (dark, spans the COB advantage + project gallery), §3 Scope of work (spans scope + coordination + per-pitch design specs), §4 Fee schedule (spans the milestones + one estimate page per LED installation), §5 Terms & warranty, then a close page (Next step + contacts — no signature block). Source master: `proposal.html` in this folder (build copy from `ui_kits/sales/`).

**Section numbering rule:** a section number appears only on the first page of that section (the band big-numeral + title). Continuation pages within the same section carry a `.led-subhead` instead — no repeated number. So §3's number lives on page 6 only; pages 7–9 use subheads ("Coordination & Training", "Design Specifications — <pitch>"). Same for §4 (number on p10; estimates on p11–12 are subheads).

Also read: `../_brand/SKILL.md`

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

1. Start a local server rooted at **`LUCI Systems Design System/`** (not `ui_kits/sales/`) so `../../assets/` relative paths resolve to the canonical assets folder: `python3 -m http.server 8771 --bind 127.0.0.1` from that root.
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

| Page | Section | Canvas | Status |
|------|---------|--------|--------|
| **1** | Cover | Dark | **EDITABLE** (see exceptions below) |
| **2** | Contents | Light | **EDITABLE** (section titles + page numbers) |
| **3** | §1 Project overview | Dark | **EDITABLE** (deck, intent/approach/outcome/standard narrative, scope list, 4 stat values, pairing callout) |
| **4** | §2 Built on COB — The COB Advantage (part 1 of 2) | Dark | **LOCKED** (advantage tiles, NovaStar architecture, 4 stat tiles) — boilerplate |
| **5** | §2 Built on COB — Project Gallery (part 2 of 2, no repeated §2 header) | Dark | **EDITABLE** photos + captions (Mike swaps images); **LOCKED** layout |
| **6** | §3 Scope of work | Light | **EDITABLE** (included / not-included lists); **LOCKED** process paragraph |
| **7** | §3 Scope of work — Coordination & training (cont.) | Light | **EDITABLE** (client obligations, punch-list line); **LOCKED** PM/training boilerplate |
| **8** | §3 Scope of work — Design specifications, pitch 1 (cont.) | Light | **EDITABLE** (all spec values + pitch in subhead); **LOCKED** spec row labels |
| **9** | §3 Scope of work — Design specifications, pitch 2 (cont.) | Light | **EDITABLE** (all spec values + pitch in subhead); **LOCKED** spec row labels |
| **10** | §4 Fee schedule & payment terms | Light | **EDITABLE** (milestone %, labels, due-when, tariff note); **LOCKED** structure + USD/30-day boilerplate |
| **11** | §4 Fee schedule — Estimate 01 (cont.) | Light | **EDITABLE** (all line items, qty, rate, amount, total, estimate #, date, name) |
| **12** | §4 Fee schedule — Estimate 02 (cont., clone per install) | Light | **EDITABLE** — clone this page for each additional LED installation |
| **13** | §5 Terms & warranty | Light | **EDITABLE** (warranty duration); **LOCKED** 4-column warranty boilerplate |
| **14** | Close (Next step + contacts) | Dark | **EDITABLE** (next-step body, contact name/email); **LOCKED** structure + LUCI company info |

### Variable page counts

- **Spec pages (8–9):** one page per pixel pitch in the project, all under §3 (subheads, no repeated section number). Add or remove `.doc-page--led-specs` sections to match the number of pitches.
- **Estimate pages (11–12):** one page per LED installation, all under §4 (subheads, no repeated section number). Clone the estimate section for each installation; renumber trailing page footers (`doc-foot__page`) only — do **not** add a `sow-band-bignum` to continuation pages (the section number lives on the section opener only). Update the Contents page (p2) page numbers to match.

### Cover exceptions (page 1 — do not change)

| Element | Why locked |
|---------|------------|
| `.doc-cover__logo` (LUCI logo image) | Brand |
| "Prepared by" value remains **LUCI Systems, LLC** unless Jane directs otherwise | Standard attribution |

Everything else on the cover with `doc-edit` / `contenteditable="true"` is editable.

---

## Editable regions by section

### Cover (page 1) — `.doc-page--cover`

| Element | Selector | What to change |
|---------|----------|----------------|
| Display headline | `.doc-cover__display` | "Proposal" + client short name in `<em>` |
| Project title | `[data-studio="project-title"]` | Full project name line |
| Prepared for | `[data-studio="prepared-for"]` | Client organization |
| Basis | `[data-studio="basis"]` | Survey notes, meetings, source documents |
| Client logo | `.doc-cover__client` (`[data-studio="client-logo"]`) | Replace `src` and `alt` |

### Contents (page 2) — `.doc-page--led-toc`

- Section titles (`.led-toc__title`) and page numbers (`.led-toc__pg`) — editable. Update page numbers when pages are added/removed.
- **No Agreement row** — the close page (p14) sits outside the numbered TOC. Do not add an Agreement/signature row back.
- Plain off-white page — no circuit/pattern overlay (keeps dotted leaders clean).

### Project overview (page 3, dark) — `.doc-page--led-overview`

- Deck (`.led-band-deck`) — editable; white, left-justified
- Two-column layout (`.led-overview-cols`): left = "The intent" / "The approach" / "The outcome" / "The standard" narrative blocks (`.doc-section-head__text`); right = "Scope at a glance" list (`.led-overview-scope`) + pairing callout (`.led-pairing`) + section-pointer note (`.led-overview-note`) — all editable
- 4 stat values in `.led-stat-strip` (`.led-stat__num`) — editable (gold numerals)

### §2 Technology Overview — The COB Advantage (page 4, part 1 of 2, dark) — `.doc-page--led-advantage` — LOCKED

The section title "Technology Overview" (`.doc-page-band__title`) names §2; "The COB Advantage" is the Syncopate `.led-subhead` directly beneath it, then the deck. The 6 advantage tiles, NovaStar architecture paragraph, and 4 stat tiles are standard COB/NovaStar facts. If a future project uses a different processor brand or non-COB panels, flag for a Jane-approved override rather than a Mike edit.

### §2 Technology Overview — Project Gallery (page 5, part 2 of 2, dark) — `.doc-page--led-gallery`

No repeated §2 header on this page — "Project Gallery" is the `.led-subhead` anchoring the continuation. Deck is white, left-justified.

| Element | Selector | What to change |
|---------|----------|----------------|
| Gallery photos | `[data-studio="gallery-img-1"]` … `[data-studio="gallery-img-4"]` | Replace `src` and `alt` on each `<img>` |
| Captions | `.led-gallery-cell__cap` | Edit caption text (bold lead-in + descriptor) |

Layout (2×2 grid) stays locked.

### §3 Scope of work (page 6) — `.doc-page--led-scope`

- Included / not-included lists inside soft check panels (`.led-check-panel`) — editable
- **Locked:** the "certified technicians / design vetting / kickoff" process callout

### §3 Scope of work — Coordination & training (page 7, cont.) — `.doc-page--led-coordination`

- Client obligations list inside soft check panel — editable
- Punch-list & acceptance line — editable
- **Locked:** PM + training boilerplate (the two `.doc-teams` rows)

### §3 Scope of work — Design specifications (pages 8–9, cont.) — `.doc-page--led-specs`

- Pitch in the subhead (`[data-studio="spec-pitch-N"]`) — editable
- All `.led-spec-row__value` cells — editable
- **Locked:** the `.led-spec-row__label` schema (Pixel Pitch, Panel Size, Resolution, Brightness, etc.)

### §4 Fee schedule & payment terms (page 10) — `.doc-page--led-fee`

- Milestone percentages (`.led-fee-mile__pct`), labels, and due-when lines — editable
- Tariff note text — editable
- **Locked:** structure + the "All prices in USD / valid 30 days" boilerplate

### §4 Fee schedule — Estimates (pages 11–12, cont.) — `.doc-page--led-estimate`

- Estimate name (`[data-studio="estimate-N-name"]`), number, date — editable
- All line items: mfg, item, description, qty, rate, amount — editable (`.doc-edit`)
- Estimate total (`[data-studio="estimate-N-total"]`) — editable
- **No auto-math** — recompute subtotals/totals by hand if you edit a qty or rate.
- Clone the section for each additional LED installation; renumber footers + update Contents page numbers.

### §5 Terms & warranty (page 13) — `.doc-page--led-terms`

- Warranty duration line (`.led-warranty-duration` span) — editable
- **Locked:** the 4-column warranty grid (covered / void-if / service / not-covered) + extended-warranty paragraph

### Close (page 14) — `.doc-page--led-signoff` (dark, navy + circuit texture)

- Next-step body (`.led-close__body`) — editable
- Contact name + email (`.led-close__name` / `.led-close__link` in the "Your contact" column) — editable
- **Locked:** close-page structure, LUCI company info (name/address/phone/web), and the navy circuit-texture band
- **No signature block** — this is a close page, not an agreement/signature page. Do not re-add signature fields.

All editable content uses `class="doc-edit" contenteditable="true"`. When editing HTML directly, preserve those classes.

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
- Add inline font styles or unclassed elements that bypass the typography table above.
- Add marketing language to technical scope — stay factual and scoping-focused.
- Invent hardware specs or pricing not supported by client notes.
- Use opaque JPEG client logos on the cover (white box artifact) — use transparent PNG/SVG.

---

## Common tasks

**New LED project from site notes**
1. Cover (p1): project title, prepared-for, basis, logo, display `<em>` name.
2. Contents (p2): confirm section titles + page numbers match the final page count.
3. §1 Project overview (p3): rewrite the intent/approach/outcome/standard narrative; set the 4 stat values to the proposed panel's pitch / angle / lifespan / IP.
4. §3 Scope of work — Design specifications (p8–9): set spec values per pixel pitch; add/remove spec pages to match the number of pitches (subheads, no repeated §3 number).
5. §4 Fee schedule (p10): set fee milestones per contract.
6. §4 Fee schedule — Estimates (p11+): one estimate page per LED installation — populate line items, qty, rate, amount, total (subheads, no repeated §4 number).
7. §5 Terms & warranty (p13): set warranty duration per contract.
8. Close (p14): set the next-step body + the contact name/email (no signature block).

**Update `<title>`** in `<head>` to reflect client/project name.


