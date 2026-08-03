---
name: luci-capabilities-document
description: >-
  Customize the LUCI Capabilities document for a specific client. Use when Mike
  or sales needs a post-demo leave-behind with client name, summary, and logo
  on the cover while keeping the technical body locked.
---

# Capabilities document — customization

Post-demo personalized leave-behind. **9 pages (US Letter).** Source master: `capabilities-document.html` in this folder (build copy from `ui_kits/sales/`).

Also read: `../_brand/SKILL.md` — especially **Efficient customization**, **Continuous page packing**, **Source fidelity**, **Totals span the full page width**, **Logo + pattern**, and **PDF export — gradient + mask flattening** (house rules for every Customization Studio doc). Mike can click-edit any text (fonts/colors stay on CSS). Populate-in-place; never rebuild.

## Voice

Match LUCI's voice on every line you write or rewrite. Full contract: `../_brand/SKILL.md` → **Voice & tone**. Canonical source: LUCI Messaging Guide (`ui_kits/review/messaging/messaging-guide.html`). Cover-page goal rewrites: `ui_kits/internal-portal/skills/cover-page-customization.md` (audience, framing, length, no invented facts) — same cover flow as the budgetary estimate.

- **Engine and verbs — not layers.** Never use *layer* as a noun for LUCI. Lead with **orchestration engine** / **LUCI orchestrates…**; rotate to *runs, operates, integrates, consolidates, refines*.
- **Always write A/V** — never "AV" or "A-V" (body, headlines, labels, captions, alt text, diagrams).
- **Declarative, not promotional.** State facts; no "revolutionize / transform / empower / absurdly simple." Short sentences, one idea each, em-dash payoff.
- **Subtraction over addition.** Lead with what LUCI removes (variables, vendors, interfaces, refresh cycles), not what it adds.
- **Institutions, not adjectives.** Describe what the platform does for the enterprise, not how it feels.
- **Discretion over display.** No client names or percentage claims in public materials.
- **Retired terms:** absurdly simple / easy to use / intuitive · revolutionize / transform / empower · best-in-class / game-changing · owner's rep (use LUCI FDE / embedded team) · *layer* for LUCI.
- **Verbatim lines:** tagline, sub-tagline, and value-prop boilerplate — use as written, do not paraphrase.
- **Tone & voice (lucisystems.com):** lead with the customer problem, then stage LUCI as the solution (don't open with LUCI — establish why it matters first); frame the problem as accumulation, silos, and complexity; stakes are operational. Vary sentence structure for flow (no mandatory short-declarative or contrast-pair tics). 2nd person OK in marketing/sales copy; 3rd person in SOW/MSA/proposal. Key phrases + verbatim tagline/boilerplate: `../_brand/SKILL.md` → Tone & voice.

## Portal URL workflow (primary)

**Preview URL:** `http://10.10.1.17:8081/internal-portal/customization/capabilities-document/capabilities-document.html`

When Mike pastes this URL into Cursor chat:

1. Read this `SKILL.md` and `../_brand/SKILL.md` before any edits.
2. Copy master to `clients/<client>-capabilities.html` using `scripts/prepare-client-doc.sh ui_kits/sales/capabilities-document.html clients/<client>-capabilities.html` (adjusts all relative paths automatically). Client files live in the top-level `clients/` folder.
3. Customize **cover (page 1)** and **close (page 9)** only — see editable regions below.
4. Do **not** edit the HTML file on the VM deploy folder (overwritten on deploy).

See also: `../CURSOR.md`, `AGENTS.md` in this folder.

### Open the rendered preview in the editor (automatic)

After customizing the doc, **automatically open the rendered client HTML in Cursor's in-editor (Glass) browser — not the HTML source** — without being asked:

1. From `LUCI Systems Design System/ui_kits/sales/`, start a local server in the background: `python3 -m http.server 8771 --bind 127.0.0.1` (increment the port if busy).
2. Verify: `curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:8771/<client>-capabilities.html` → `200`.
3. Open `http://127.0.0.1:8771/<client>-capabilities.html` in Cursor's in-editor browser via the `cursor-app-control` MCP `open_resource` tool (URI = that URL). Do **not** use a `file://` URI — that opens the HTML source, not the rendered doc.

Editable regions (`contenteditable`, `.doc-edit`, `[data-studio]`) — including the Client Summary — are click-to-edit in that rendered preview. No prompt needed for word-level tweaks. Save the file when done. User fallback if the pane doesn't appear: `Cmd+Shift+P` → "Simple Browser: Show" → paste the localhost URL.

## When to use

After a demo, when the prospect needs a capabilities overview scoped to their property — cover personalized, LUCI story unchanged.

## Workflow

1. Open the **portal preview** (URL above) or copy that URL into Cursor chat.
2. Describe what to change in plain language (property name, client summary, logo swap).
3. Save the **client version** in luci-design under `clients/<client>-capabilities.html` — not over the master.
4. Preview → Print/Save as PDF (US Letter).

---

## Page map — editable vs locked

| Page | Section | Status |
|------|---------|--------|
| **1** | Cover | **EDITABLE** |
| **2** | Orchestration opener (C/A/E + floor plan + pillar cards) | **LOCKED** |
| **3** | What LUCI is (identity diagram + key features) | **LOCKED** |
| **4** | What LUCI reduces | **LOCKED** |
| **5** | Technical architecture | **LOCKED** |
| **6** | The embedded operation (Systems delivery) | **LOCKED** |
| **7** | Deployment & support (journey + commitments) | **LOCKED** |
| **8** | Proof of impact (Ameristar case study) | **LOCKED** |
| **9** | Close (contact + next step) | **EDITABLE** (headers + contact rep only) |

**Page 1 (cover)** and **page 9 (close)** may be customized. Pages 2–8 are protected brand and technical content.

---

## Editable regions (page 1 only)

All on `.doc-page--cover`:

| Element | Selector / marker | What to change |
|---------|-------------------|----------------|
| Cover kicker | `[data-studio="cover-kicker"]` | e.g. “Capabilities overview” |
| Cover display headline | `.doc-cover__display` | “Prepared for” + property name in `<em>` |
| Cover subhead | `[data-studio="cover-subhead"]` | One-line scope framing |
| Client name | `[data-studio="client-name"]` | Property name (bold, in summary) |
| Client summary body | `[data-studio="client-summary"]` | 2–4 sentences: environment, pain points, goals |
| Client logo | `.doc-cover__client` | Replace `src` and `alt`; PNG/SVG transparent |

Elements with `contenteditable="true"` and class `doc-edit` on the cover may also be edited directly in HTML.

---

## Editable regions (page 9 — close)

On `.doc-page--close`:

| Element | Selector / marker | What to change |
|---------|-------------------|----------------|
| Close kicker | `[data-studio="close-kicker"]` | e.g. “Next step” |
| Close headline | `[data-studio="close-head"]` | Next-step headline (may include `<br>` and `<em>`) |
| Close body | `[data-studio="close-body"]` | One-line CTA under the headline |
| Contact name | `[data-studio="contact-name"]` | Rep name (default: Mark Filler) |
| Contact email | `[data-studio="contact-email"]` | Rep email — update visible text; update `href` on the `<a>` if the address changes |

The **LUCI company block** (`.doc-close__company` — address, phone, website) and the **LUCI logo** (`.doc-close__logo`) stay fixed.

Elements with `contenteditable="true"` and class `doc-edit` on the close page may also be edited directly in HTML or in the browser preview.

### Cover copy guidance

- **Client summary** should be specific: property type, fragmented systems, operational pain, what they want from LUCI.
- **Date** (`.doc-cover__date`) — set the document date (format: "Month DD, YYYY"). Never ship with the placeholder.
- Keep **Prepared for** display line short — property name in the `<em>` tag.
- Leave `.doc-note` helper lines unless Jane asks to remove them for final send.
- Do **not** change the LUCI logo (`.doc-cover__logo`).

---

## Locked regions (pages 2–8)

Do **not** modify text, images, diagrams, stats, or structure in:

- `.cap-page--what` (page 2 — brochure opener: C/A/E, floor plan, pillars)
- `.cap-page--why` (page 3 — identity diagram + key features)
- `.doc-page--reduces` (page 4)
- `.doc-page--architecture` (page 5)
- `.doc-page--systems` (page 6)
- `.doc-page--deployment` (page 7)
- `.doc-page--proof` (page 8)

On page 9, do **not** modify `.doc-close__company` or `.doc-close__logo`.

This includes all diagrams under `assets/diagrams/`, feature SVGs, journey connector, and Ameristar proof copy.

---

## Common tasks

**New client after demo**
- Update cover kicker, display `<em>` property name, subhead, client summary, swap `.doc-cover__client` logo.
- Update `<title>` in `<head>` to include property name.

**Logo swap**
```html
<img class="doc-cover__client" src="/assets/logos/client-name.svg" alt="Client Name" width="200" height="36">
```
Use a path relative to the deployed site root (`/assets/logos/…`) or a local path if working offline.

---

## Do not

- Edit pages 2–8 — **no changes of any kind**, including color, styling, spacing, or CSS (HTML, inline styles, scoped `<style>` blocks, or shared stylesheets), not just copy. If asked to change a locked page, do NOT edit first — flag the lock and ask whether to override (local-only vs canonical) before making any change.
- Add or remove pages.
- Edit pages 2–8 copy, even “small” wording tweaks.
- Change the LUCI company block or close logo on page 9.
- Change CSS links or add inline styles that break print layout.
- Remove `doc-draft-badge` unless sending final (confirm with Jane).
