---
name: luci-brand
description: >-
  LUCI brand guardrails for customizing sales documents. Apply whenever editing
  capabilities documents, scope of work, budgetary estimates, or other LUCI
  marketing HTML templates.
---

# LUCI brand — document customization

Shared rules for all LUCI sales document customization. Read the template-specific `SKILL.md` first for editable vs locked pages; this file governs **how** edits look and read.

---

## Efficient customization (read this first)

This is a **populate-in-place** job, not a rebuild. Never regenerate the document from scratch. Locked regions must come through **byte-identical**. The master template already has the layout, CSS, textures, fonts, and locked copy — your job is to stamp client values into the existing file.

**House-wide (every Customization Studio document):** Mike can click and type **any text**. Fonts, colors, and layout stay on CSS classes — change words only. Only LUCI logo images stay non-editable. Efficiency rules below apply to **every** template (Proposal - LED, Budgetary estimate, Scope of work, Capabilities, Sales deck, and future Proposal - LUCI Retrofit / Proposal - Upgrade).

Burning millions of tokens on discovery, rebuilds, accessibility snapshots, or rewriting whole `<section>`s is a failure mode. Parse the request → touch only what changed → verify.

### 1. One project folder — never spawn copies

Each client document lives in **one** dedicated folder for the life of that job. All skills, CSS, fonts, logos, textures, and the HTML stay there. Do **not** create a second folder, a `-edited.html` sibling that becomes the new source of truth, or a parallel “build output” path.

**When Mike names a folder** (e.g. `IP Biloxi Proposal`):

```
<project>/                          ← e.g. Desktop/LUCI Docs/IP Biloxi Proposal/
  ui_kits/sales/
    <client>-<doc>.html             ← THE working file (only one)
    sales-document.css
    <template>.css                  ← only the CSS the master already links
  ui_kits/internal-portal/customization/
    luci-doc-edit.css
    luci-doc-edit.js
    luci-dev-server.py             ← ALWAYS overwrite from originals; Save + PDF
    <template>/SKILL.md             ← copy from portal/master skill
    _brand/SKILL.md
  assets/fonts/                     luci-brand-fonts.css
  assets/logos/                     luci-full-white.png (+ client logo)
  assets/textures/                  ONLY files the master CSS/HTML references
  inputs/                           spreadsheet, SOW, logo uploads (optional)
```

Mirror the portal’s relative paths (`../../assets/…`, sibling CSS). **Serve with the LUCI dev server** — run `python3 ui_kits/internal-portal/customization/luci-dev-server.py` from `<project>/` (the agent starts it as a background process). It serves the project root on `http://127.0.0.1:8771` and accepts `POST /__save` + `POST /__pdf`. Never root the server at `ui_kits/sales/` or textures/logos 404 and the circuit pattern “doesn’t load.”

**Always refresh the preview tooling before every server start (mandatory for Mike):** overwrite — do not skip if present —

- `ui_kits/internal-portal/customization/luci-dev-server.py`
- `ui_kits/internal-portal/customization/luci-doc-edit.js`
- `ui_kits/internal-portal/customization/luci-doc-edit.css`

— from the current portal/luci-design `customization/` originals. Stale copies lack `POST /__pdf` and break Download PDF. Then restart the server from that refreshed path.

If this tree does not exist yet: create it and fetch the exact master HTML + linked CSS + referenced assets from the portal (or luci-design) in **one batch**. Do not discover assets by trial and error. Do **not** pull extra stylesheets the master does not already link (e.g. do not add `scope-of-work.css` into a budgetary/proposal client — it overrides `.doc-page-band` and strips navy headers + circuit texture).

### 2. Edit by selector — never by rewrite

- Locate variable fields by `[data-studio="…"]` (or the template skill’s listed selectors) and replace the **text node / attribute only**.
- Do **not** re-emit a whole `<section>` to change values inside it.
- Do **not** invent fine-print, freight/travel disclaimers, “Addressed to” labels, or extra legal language that is not in the master or Mike’s source files.
- Do **not** edit shared stylesheets. Client-only layout overrides go in a commented `<style>` block in the client HTML `<head>`, scoped to a page class — and only after confirming a locked-region override with the user.

### 3. Same file forever — typed edits + agent edits

- The working file is `<client>-<doc>.html` in that project folder. Every agent pass edits **that same path**.
- Browser “Copy updated HTML” / “Download HTML” produce a **download artifact** (`*-edited.html`). That is **not** the source of truth. If Mike typed in the preview, the agent must **write the live DOM (or the copied HTML) back into the same working file** before any further prompt — otherwise typed edits are lost and Cursor works from a stale disk copy.
- Never treat a Downloads/`*-edited.html` file as the new master.

### 4. Preview and verify — no accessibility snapshots

Browser accessibility snapshots return the entire document tree and waste tokens. Use only:

- `browser_take_screenshot` for visual checks
- CDP `Runtime.evaluate` for measurement / fit checks

Pages are locked to fixed US Letter (8.5×11in, 1056px height) with `height: var(--page-h)` and `overflow: hidden` — **on screen and in print**. Pages cannot stretch or shrink beyond the printable area. Overflow **clips silently** (and visibly, on screen) so you catch it during editing, not in the PDF. A fit check is **mandatory** after any content edit:

```js
(() => [...document.querySelectorAll('.doc-page')].map((p,i) => {
  const s = {h:p.style.height, m:p.style.minHeight,
             o:p.style.overflow, j:p.style.justifyContent};
  Object.assign(p.style, {height:'auto', minHeight:'0',
                          overflow:'visible', justifyContent:'flex-start'});
  const nat = p.getBoundingClientRect().height;
  Object.assign(p.style, s);
  return {page: i+1, over: Math.round(nat - 1056)};
}).filter(r => r.over > 0))()
```

Anything with `over > 0` is clipped. **Trim copy or split to a new `.doc-page`** — do not change page height. Do not let Mike’s extra rows of typed text push a page past letter size unnoticed.

### Continuous page packing — SOW + line items (mandatory)

Fill each content page as far as it will go before opening a new one. **Do not invent page breaks.** This applies to **Scope of Work** sections and **line-item** tables alike.

- Pack **greedily** while natural height stays ≤ 1056px. If there is room for another partial section / group / rows, use it.
- **Sections and groups may break across a page boundary.** Start the next page with a "(continued)" title/label and keep going. Do **not** force a whole section onto the next page just because only 2–3 sections fit on the current one, and do **not** leave large empty space when more content would fit.
- **SOW continuous flow (locked):** the Scope of Work flows continuously across pages with no forced section-start page breaks. Page breaks may occur **anywhere** — between sections, mid-section (a subsection's body can start on one page and continue on the next), between line items, between bullet points, or mid-subsection. Subsections can cross a page boundary. The only rule: pack greedily, renumber footers, and keep going. Do not strand a section header alone at the bottom of a page with its content on the next — if the header + at least one line of body don't fit, move the header to the next page.
- After packing, renumber `.doc-foot__page` and page comments sequentially. Drop empty continuation pages.

**Line items — totals exception:** follow the same greedy packing for all line-item **rows and groups**. Then:

- Put a **page break before the investment summary / totals** unless the **full** totals block fits on the last line-item page with the final rows (fit check ≤ 1056px).
- If the full totals do not fit, move **only the totals** to the next page (full content width). Do **not** strand a leftover group alone on a page just to keep it with the totals — keep that group with the prior line items when it fits.

### Totals span the full page width (mandatory)

`.be-summary`, `.be-summary__total`, `.be-summary-split`, and their wrapper (e.g. `.be-p5-numbers`) must span the **full content width** of the page. **Never** set `max-width: 48ch` (or any narrow measure) on those elements — not in CSS, not as an inline style. Labels left, amounts right, row edge-to-edge with the line-item table above.

### Source fidelity — SOW + line items (mandatory)

When Mike provides a source SOW (Word/PDF) or a line-item spreadsheet, the destination document must **mirror the source’s content and structure**, then dress it in the destination’s brand:

- **Carry through:** exact verbiage (modulo LUCI house voice fixes like “A/V”), section/sub-section headers, narrative vs bullet structure, list nesting, group labels, row order, and categories. Two Ballroom sections in the source → two Ballroom sections in the doc. Bullets in the source → bullets in the doc.
- **Do not:** rewrite, condense, reorganize, invent sections, drop bullets into paragraphs (or the reverse), or make scoping/pricing assumptions the source does not support.
- **Do apply:** the destination document’s branded formatting — fonts, colors, hairlines, mint markers, `.upg-scope*` / `.be-price*` classes, etc. Source structure + destination design.
- **Scope:** this contract is required for **SOW** and **line items**. Other sections may have template-specific exceptions (locked marketing pages, etc.) — follow the per-template `SKILL.md`.

### 5. Pricing must be verified, not eyeballed

After any pricing / qty / rate edit, reconcile totals. Known trap: a grand total can be a live formula while milestone cells stay hardcoded and drift. Reconcile milestones against the verified total. Prefer a small verify script when one ships with the template; otherwise compute and state the check in your summary. **Never silently change numbers that Mike already confirmed.**

**The spreadsheet is the source of truth for line-item content** (same fidelity rule as above). Mirror its categories, order, and breakout exactly — do not combine rows, split rows, or invent categories that are not in the spreadsheet. If the spreadsheet has a "Shipping" row, include it; if it doesn't, don't add one. If it has a "Sales Tax" row, include it; if it doesn't, don't invent one. Follow the spreadsheet's group labels and row order; do not reorganize. The only exception is the LUCI OS endpoint combining rule below.

**Combine endpoint pricing into one line item.** LUCI OS endpoint licenses must appear as a **single line item** referencing the **total number of endpoints** — never split out by video, audio, or other sub-categories. If Mike's spreadsheet has them combined, mirror that. If a previous AI run split them into separate video/audio/etc. rows, combine them back into one row with the total endpoint count. The label should match Mike's spreadsheet (e.g. "LUCI OS & Endpoint Licenses" or "LUCI OS — Annual Partnership") — do not invent a different label.

### 6. Logo + pattern (do not re-break these)

- **If no client logo is provided, find one online** — prefer the property/brand’s official site or CDN (SVG first, then transparent PNG). Do **not** leave a placeholder or invent a white box. Confirm the mark matches the client/property named in the doc.
- **Transparent on any surface.** Strip colored or white backgrounds so the logo sits cleanly on light sheets **and** dark/navy bands. Prefer true SVG/PNG with alpha; never opaque JPEG or a PNG with a baked-in white/colored rectangle.
- **Match the page design.** Size and placement per the cover’s `logo-pos--*` rules (see `skills/cover-page-customization.md`). On navy/band spots, prefer a white/reversed logo (or set `data-logo-light="1"` when the asset is already light); on light-sheet spots, use the natural/color logo.
- Circuit / header textures must live under this project’s `assets/textures/` at the paths the CSS already uses. Missing file or wrong server root = “pattern didn’t load.”

### 7. Footer matches title

When the document title / cover kicker changes (e.g. Budgetary → Proposal, or a client project title), update **every** `.doc-foot` / running footer to match. Footers are not optional leftovers.

### 8. Date on every document (mandatory)

Every sales document cover **must** show a proposal/estimate date. The master templates already include a date field — populate it on every customization:

- **Templates with `.doc-cover__summary`** (Proposal - LUCI Retrofit, Budgetary Estimate, Capabilities Document): the date lives in `.doc-cover__date` below the client summary text. Format: "Month DD, YYYY" (e.g. "July 29, 2026").
- **Templates with `sow-meta` rows** (Proposal - LED, Scope of Work): the date lives in a `sow-meta__row` with label "Date" and `data-studio="proposal-date"` (or `data-studio="sow-date"`).
- **Proposal - Upgrade**: the date is inline in the summary text via `data-studio="proposal-date"`.

Never ship a document with a placeholder date ("[Month DD, YYYY]" or "Today"). Set the real date before generating the PDF.

---

## Typography (non-negotiable)

| Tier | Font | Use for |
|------|------|---------|
| Display | Syncopate 700 | Cover/close display lines only — ≤3 words, single line |
| Structure | Space Grotesk 600–700 | Headlines, section titles, labels, metric numerals |
| Body | Inter 400 | **All** running copy — paragraphs, lists, descriptions, notes |

- Never set body copy in Space Grotesk.
- Never use Syncopate for multi-line section headers or sentences.

## Spacing

- Base unit **8px**. Padding, margins, gaps: 8, 16, 24, 32, 40, 48, 64.
- **4px** only for tight label-to-value pairs.
- Do not invent off-scale values (no 13px, 22px, 37px).

## Color & accent

- **Bright mint `#68E3BE`** — dark backgrounds only.
- **Light accent `#2b9e80`** — links, kickers, small labels on white/off-white. Never use retired `#176B54`.
- **Never** bright mint on light backgrounds.
- Body text on light: `#354F5C` on off-white `#F5F8FA`.

## Layout discipline

- **Do not** add bordered boxes around content blocks; use whitespace and hairline separators.
- **Sharp corners** — `border-radius: 0` on document furniture (brand trait).
- **Do not** add drop shadows to flat content.
- Keep existing `.doc-page` structure — one section = one printed sheet.
- **Page sizing is locked** — `.doc-page` uses `height: var(--page-h)` (US Letter, 1056px) with `overflow: hidden` on screen **and** in print. Pages cannot stretch or shrink beyond the printable area. If content overflows, it clips visibly on screen — trim copy or split to a new `.doc-page`; never change the page height.

## Voice & tone

Canonical source: **LUCI Messaging Guide** (`ui_kits/review/messaging/messaging-guide.html` → Voice & tone). The rules below are baked in here so every document customization inherits them. For cover-page goal rewrites, also follow `ui_kits/internal-portal/skills/cover-page-customization.md` (audience, framing, length, no invented facts).

### Voice rules (apply to every line you write or rewrite)

- **Engine and verbs — not layers.** Never use *layer* as a noun for LUCI ("orchestration layer," "application layer," "one layer for…"). Describing accumulation in the *client's* stack is fine; naming LUCI a layer is not. Lead with **orchestration engine** (positioning/tagline) and **LUCI orchestrates…** (headlines, capability copy). Approved alternatives when they fit: *runs, operates, integrates, consolidates, refines, platform, infrastructure*.
- **Always write A/V** — never "AV" or "A-V" — in body copy, headlines, labels, captions, alt text, and diagrams.
- **Watch repetition.** If *engine* or *orchestrates* appears more than once in a short passage (a page, a deck section, an email), rotate to a precise alternative. Same word three times reads like a crutch.
- **Institutions, not adjectives.** Describe what the platform does for the enterprise, never how the software feels to use. "Operate every endpoint from one interface" passes; "absurdly simple" does not.
- **Subtraction over addition.** Lead with what LUCI removes — variables, vendors, interfaces, refresh cycles — not with the capabilities it adds.
- **Declarative over promotional.** State facts. Avoid emotional verbs ("revolutionize," "transform," "empower"). If a claim needs an adverb to land, it isn't landing — cut the modifier, then cut the sentence it was propping up.
- **Discretion over display.** No client names in public materials. No percentage claims. Describe scale and complexity in general terms.
- **Standardization is the advantage.** Never apologize for a standard approach. Customization is what broke every A/V environment they've had before.
- **Lean, not padded.** Cut modifiers a claim leans on ("if a claim needs a modifier to land, it isn't landing — cut it"). Favor lean copy, but vary sentence length and structure for flow — don't force every sentence short. Narrative is welcome where it carries more weight than a punchy line.

### Approved vs retired language

**Use:** orchestration engine, platform, infrastructure · LUCI orchestrates / runs / operates / integrates / consolidates / refines · institutional, operational, embedded, accountable, continuous · LUCI FDE, the embedded team, the standard · "removes variables," "shorter list," "fewer moving parts."

**Retire:** absurdly simple / easy to use / intuitive (consumer register) · revolutionize / transform / empower (empty emotional verbs) · best-in-class / game-changing (pitch-deck language) · owner's rep (use LUCI FDE or embedded team) · *layer* when naming LUCI · any percentage claim in brand-level copy · named clients in public materials.

### Tone & voice (from the live website — the way we talk about LUCI)

The website (lucisystems.com) is the reference for *how LUCI sounds* — the tone and stance, not a sentence-template to copy. Match the voice below; do not copy its layout or structural tics.

**How we talk about LUCI:**
- **Lead with the customer's problem; stage LUCI as the solution.** Don't open with LUCI — establish the problem and stakes first so the reader knows *why LUCI matters* before LUCI appears. LUCI is the means, not the subject. This is the primary register for marketing and sales copy; in an SOW or proposal, use it where it aids persuasion, not in raw technical scope.
- **Frame the problem as accumulation, silos, and complexity.** The prospect's pain is what they've accumulated and fragmented — too many vendors, interfaces, and workarounds living in separate silos — not a missing capability.
- **Stakes are operational, not aspirational.** "not optional," "non-negotiable," "cannot afford failure," "24/7 enterprise environments." Write to a high-stakes operational world, not to aspiration.
- **The team is permanent and accountable.** "with a team that stays," "built in, not bolted on," "the engineer who walks the property on day one is the engineer who supports it in year five."

**Key phrases (signature LUCI lines — reference for the voice; the tagline/sub-tagline/boilerplate are verbatim):**
- "The Orchestration Engine for Enterprise Multimedia" (tagline — verbatim)
- "One interface to control, automate, and execute the entire guest experience." (sub-tagline — verbatim)
- "Complexity isn't solved by a better interface. It's solved by a shorter list of things to manage."
- "built in, not bolted on"
- "with a team that stays"
- Value-prop boilerplate (Messaging Guide → Value proposition) — **verbatim**, do not paraphrase.

**Don't canonize sentence structure.** The homepage leans short and declarative, but that is a homepage choice, not a LUCI rule. Vary sentence and paragraph structure for flow; narrative is often more impactful than a string of punchy lines, and marketing-speak is wrong in a SOW, MSA, or proposal. Match the register to the document:
- **Marketing, sales decks, web copy** — may use 2nd person ("your property," "your team") and the homepage's punch.
- **Scope of work, MSA, proposal, technical scope** — 3rd person, factual, narrative where it aids clarity. No marketing register.

### What you must never change (voice)

- LUCI product claims, capability names, or technical-architecture descriptions — unless the template skill explicitly allows it.
- The tagline, sub-tagline, and boilerplate value prop (use verbatim).

## What you must never change

- **Locked pages/regions (per template `SKILL.md`)** — no changes of any kind, including color, styling, spacing, or CSS (HTML, inline styles, scoped `<style>` blocks, or shared stylesheets). If asked to change a locked region, do NOT edit first — flag the lock and ask whether to override (local-only vs canonical) before making any change.
- Linked stylesheets (`sales-document.css`, template-specific CSS).
- LUCI logo images and embedded base64 logos.
- Canonical diagram SVGs (`luci-what-luci-is`, `luci-system-architecture`, etc.) — content or layout.
- Page footers, draft badges, and document spine order.
- Contact close block (names, email, address) unless Jane explicitly requests an update.

## File hygiene

- Edit **only** elements marked editable in the template skill (`.doc-edit`, `[data-studio]`, or `contenteditable="true"` regions) — this covers styling/CSS/color too, not just text. A color tweak to a locked region is still an edit to a locked region; run the pre-edit gate in `.cursor/rules/luci-doc-customization.mdc` first.
- Do not remove HTML comments that label pages (`<!-- PAGE N · … -->`).
- Preserve `&mdash;` and existing entity encoding in static copy.
- When swapping a client logo: use **PNG or SVG with a transparent background** (never an opaque JPEG or a PNG with a white background — it renders as a white box on dark covers and bands). Update `src` and `alt` on `.doc-cover__client` only. For dark covers (`.doc-page--dark.doc-page--cover`), prefer a **white** logo file; the cover CSS normalizes a dark logo to white via filter, but an opaque background still boxes.
- **Do not add "Addressed to" (or similar) labels** to the cover header box, the prepared-for area, or anywhere else on the first page. The cover's existing labels (`Budgetary estimate` / `Proposal` / `Scope of work` kicker, `Prepared for` eyebrow, `Client summary`) are the only labels that belong there. If the client org needs to appear, it goes in the `Prepared for` value or the `Client summary` text — not as a new labeled row. Adding "Addressed to" was an erroneous AI insertion; do not reproduce it.

### Saving (typed edits)

- **Save** in the edit bar is the primary path. When the LUCI dev server is running (the agent starts it automatically), Save POSTs the live DOM to `POST /__save` and overwrites the **same** working `.html` file on disk — Mike clicks once, no file picker, no Downloads artifact. If the dev server is not running, the button falls back to the File System Access API (Mike picks the file once) and finally to a download as a last resort (with an alert telling Mike to ask Cursor to reopen the project).
- Before any further agent pass after Mike types in preview: the working file is already updated (via the dev server save), so Cursor reads the latest version. If Mike used the download fallback instead, write the live DOM back into the working file before editing.
- **Download PDF** = `POST /__pdf` on the LUCI dev server → `scripts/render-pdf.sh` (headless Chrome). Never `window.print()` — that crashes Cursor's in-editor browser. The button shows "Rendering…" then downloads the PDF. If the local preview server is not running, the button asks you to restart it.

### PDF export — gradient + mask flattening (mandatory)

CSS gradients and mask-images cause macOS Preview to "blink in and out" on open/scroll — Chrome turns them into PDF Shading / Pattern / SoftMask XObjects that Preview renders lazily. The fix is automatic: `scripts/patch-sales-pdf-html.py` injects a `@media print` style block before `</head>` during PDF export that:

1. **Flattens all CSS gradient backgrounds** to flat fills (`#E6F5EF` for mint-tinted cards/tiles, `#F5F8FA` for light callouts/scope blocks).
2. **Replaces SVG mask icons** (checkmarks) with direct SVG `background-image` — draws the shape directly instead of using a mask cutout, eliminating the SoftMask Xobject.
3. **Removes all gradient mask-images** on circuit texture fades (`::before` pseudo-elements).

**When you add a NEW CSS gradient or mask-image** to a sales document stylesheet (or to a client file's inline `<style>`), you MUST also add it to the flattening rules in `scripts/patch-sales-pdf-html.py`. Otherwise the PDF will blink in macOS Preview. The existing rules cover: `.doc-softicon`, `.be-delivers__grid li`, `.be-summary__total`, `.be-tier-chip--selected`, `.be-why-features`, `.led-check-panel`, `.led-feature-card`, `.led-warranty-duration`, `.led-callout`, `.sow-scope-block`, `.upg-scope`, `.doc-feature::before`, `.doc-uc__benefits li::before`, `.sow-scope-list--checks li::before`, and the circuit texture `::before` pseudo-elements.

**Verify after PDF export:** the PDF should have zero `/ShadingType` and zero `/Pattern` Xobjects. The only `/SMask` entries should be on raster image alpha channels (logos), not on vector content. File size should be under 1.2 MB.
