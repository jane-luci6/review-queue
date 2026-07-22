---
name: luci-scope-of-work
description: >-
  Customize the LUCI Scope of Work for a specific client project. Use when
  scoping post-demo work — cover meta, project intent, technical scope, IDF
  scope, deliverables, and open items are editable; LUCI branding on the cover
  stays fixed.
---

# Scope of work — customization

Post-demo scoping document for prospects moving forward. **9 pages (US Letter).** Source master: `scope-of-work.html` in this folder.

Also read: `../_brand/SKILL.md`

## Voice

Match LUCI's voice on every line you write or rewrite. Full contract: `../_brand/SKILL.md` → **Voice & tone**. Canonical source: LUCI Messaging Guide (`ui_kits/review/messaging/messaging-guide.html`). Cover-page goal rewrites: `ui_kits/internal-portal/skills/cover-page-customization.md` (audience, framing, length, no invented facts) — applies to the cover project-title / prepared-for / basis lines.

- **Engine and verbs — not layers.** Never use *layer* as a noun for LUCI. Lead with **orchestration engine** / **LUCI orchestrates…**; rotate to *runs, operates, integrates, consolidates, refines*.
- **Always write A/V** — never "AV" or "A-V" (body, headlines, labels, captions, alt text, diagrams).
- **Declarative, not promotional.** State facts; no "revolutionize / transform / empower / absurdly simple." Short sentences, one idea each, em-dash payoff. Stay factual and scoping-focused — no marketing language in technical scope.
- **Subtraction over addition.** Lead with what LUCI removes (variables, vendors, interfaces, refresh cycles), not what it adds.
- **Institutions, not adjectives.** Describe what the platform does for the enterprise, not how it feels.
- **Discretion over display.** No client names or percentage claims in public materials.
- **Retired terms:** absurdly simple / easy to use / intuitive · revolutionize / transform / empower · best-in-class / game-changing · owner's rep (use LUCI FDE / embedded team) · *layer* for LUCI.
- **Verbatim lines:** tagline, sub-tagline, and value-prop boilerplate — use as written, do not paraphrase.
- **Tone & voice (lucisystems.com):** lead with the customer problem, then stage LUCI as the solution (don't open with LUCI — establish why it matters first); frame the problem as accumulation, silos, and complexity; stakes are operational. Vary sentence structure for flow (no mandatory short-declarative or contrast-pair tics). 2nd person OK in marketing/sales copy; 3rd person in SOW/MSA/proposal. Key phrases + verbatim tagline/boilerplate: `../_brand/SKILL.md` → Tone & voice.

## Portal URL workflow (primary)

**Preview URL:** `http://10.10.1.17:8081/internal-portal/customization/scope-of-work/scope-of-work.html`

When Mike pastes this URL into Cursor chat:

1. Read this `SKILL.md` and `../_brand/SKILL.md` before any edits.
2. Copy master from `LUCI Systems Design System/ui_kits/sales/scope-of-work.html` to `ui_kits/sales/<client>-scope-of-work.html`.
3. Customize cover and scope sections per this skill — preserve CSS classes.
4. Do **not** edit the HTML file on the VM deploy folder (overwritten on deploy).

See also: `../CURSOR.md`, `AGENTS.md` in this folder.

### Open the rendered preview in the editor (automatic)

After customizing, **automatically open the rendered client HTML in Cursor's in-editor (Glass) browser — not the HTML source** — without being asked:

1. From `LUCI Systems Design System/ui_kits/sales/`, start a local server in the background: `python3 -m http.server 8771 --bind 127.0.0.1` (increment the port if busy).
2. Verify: `curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:8771/<client>-scope-of-work.html` → `200`.
3. Open `http://127.0.0.1:8771/<client>-scope-of-work.html` in Cursor's in-editor browser via the `cursor-app-control` MCP `open_resource` tool (URI = that URL). Do **not** use a `file://` URI — that opens the HTML source, not the rendered doc.

Click highlighted editable text and type; save the file when done. User fallback if the pane doesn't appear: `Cmd+Shift+P` → "Simple Browser: Show" → paste the localhost URL.

## When to use

After discovery meetings, site surveys, or when the client needs a written scope for LUCI multimedia re-unification or similar engagement.

## Workflow

1. Open the **portal preview** (URL above) or copy that URL into Cursor chat.
2. Provide: project title, client org, basis (survey/meeting notes), and scope context. Optionally attach site notes or meeting minutes.
3. Save the **client version** in luci-design under `ui_kits/sales/<client>-scope-of-work.html` — not over the master.
4. Preview → Print/Save as PDF (US Letter).

---

## Page map — editable vs locked

| Page | Sections | Status |
|------|----------|--------|
| **1** | Cover & document meta | **EDITABLE** (see exceptions below) |
| **2** | §1 Project intent · §2 Guiding principles | **EDITABLE** |
| **3** | §3 Project phasing · §4 System scope (4.1 start) | **EDITABLE** |
| **4** | §4 System scope (4.2–4.4 continued) | **EDITABLE** |
| **5** | §4 System scope (4.5–4.6 continued) | **EDITABLE** |
| **6** | §5 IDF / rack scope (5.1–5.4) | **EDITABLE** |
| **7** | §5 IDF / rack scope (5.5–5.6 continued) | **EDITABLE** |
| **8** | §6 Deliverables · §7 Assumptions, constraints & exclusions | **EDITABLE** |
| **9** | §8 Open items to confirm | **EDITABLE** |

There is **no separate close page** in this template — the document ends at open items (page 9).

### Cover exceptions (page 1 — do not change)

| Element | Why locked |
|---------|------------|
| `.doc-cover__logo` (LUCI logo image) | Brand |
| “Prepared by” value should remain **LUCI Systems, LLC** unless Jane directs otherwise | Standard attribution |

Everything else on the cover with `doc-edit` / `contenteditable="true"` is editable.

---

## Editable regions by section

### Cover (page 1) — `.doc-page--cover`

| Element | Selector | What to change |
|---------|----------|----------------|
| Display headline | `.doc-cover__display` | “Scope of Work” + client short name in `<em>` |
| Project title | `[data-studio="project-title"]` | Full project name line |
| Prepared for | `[data-studio="prepared-for"]` | Client organization |
| Basis | `[data-studio="basis"]` | Survey notes, meetings, source documents |
| Client logo | `.doc-cover__client` | Replace `src` and `alt` |

### Overview (page 2) — `.doc-page--overview`

- §1 Project intent: narrative + key outcomes list
- §2 Guiding principles: all bullet items

### Phasing + system scope start (page 3) — `.doc-page--phasing`

- §3 Project phasing: intro + Phase 1/2/3 blocks
- §4 System scope header + §4.1 LUCI platform bullets

### System scope continued (pages 4–5) — `.doc-page--system-scope`

- §4.2 IPTV through §4.6 (all subsections and lists)

### IDF / rack scope (pages 6–7) — `.doc-page--idf-scope`

- §5.1 through §5.6 — per-location rack and venue blocks

### Deliverables & terms (page 8) — `.doc-page--terms`

- §6 Deliverables list
- §7 Assumptions, constraints & exclusions

### Open items (page 9) — `.doc-page--open-items`

- §8 Open items to confirm list

All editable content uses `class="doc-edit" contenteditable="true"`. When editing HTML directly, preserve those classes.

---

## Typography & font styling (required)

Fonts are applied by **CSS classes**, not inline styles. When customizing copy, **change text only** — preserve every wrapper element and its classes so headers stay Space Grotesk and body copy stays Inter.

| Role | Element / class | Font | Do |
|------|-----------------|------|-----|
| Cover display | `.doc-cover__display` | Syncopate | Edit words only; keep `<em>` for client short name |
| Cover meta labels | `.doc-eyebrow` | Space Grotesk | Edit label text only |
| Cover meta values | `.sow-meta__value` | Inter | Edit value text only |
| Section headers | `.doc-page-band__title` | Space Grotesk 700 | Edit title text; keep one line where possible |
| Subsection headers (4.1, 5.2, …) | `.sow-subsection-title` | Space Grotesk 700 | Edit title text only |
| List / block labels | `.sow-list-label` | Space Grotesk 600 | Edit label text only |
| Phase labels | `.doc-fn__label` | Space Grotesk 700 | Edit phase name only |
| Phase descriptions | `.doc-fn__text` | Inter | Edit body copy only |
| Body paragraphs | `.doc-section-head__text` | Inter | Edit paragraph text only |
| List items | `.sow-scope-list li` | Inter | Edit item text; use `<strong>` for lead terms (e.g. **Reuse-first:**) |

### Rules when adding or rewriting content

1. **Never** add inline `font-family`, `font-size`, or `font-weight` — the linked stylesheets (`sales-document.css`, `scope-of-work.css`) own typography.
2. **Never** replace a styled element with a plain `<p>` or `<div>` — duplicate the markup pattern from a neighboring item (same classes).
3. **New list items** must use `<li class="doc-edit" contenteditable="true">…</li>` inside the existing `<ul class="sow-scope-list …">`.
4. **New subsections** must use `.sow-subsection-title` for the heading and `.doc-section-head__text` or list markup for supporting copy — same structure as adjacent §4.x / §5.x blocks.
5. **Do not** strip `doc-edit` or `contenteditable="true"` from elements you modify.
6. Linked stylesheets and `<head>` font links must not be removed or swapped.

If preview shows wrong fonts after an edit, the HTML structure was likely broken — restore the original classes from the master copy.

---

## Copy guidance

- Use **specific counts, systems, and locations** from site notes (endpoints, IDFs, phases, vendor names).
- Keep subsection numbering (4.1, 4.2, … 5.6, 6, 7, 8) — do not renumber unless restructuring entire section.
- Phasing language should flag deferrals and dependencies clearly.
- Open items should be actionable confirmation questions, not vague placeholders.
- Match tone of sample (Ameristar): operational, reuse-first, phased execution.

---

## Do not

- Protected elements (LUCI cover logo, document CSS/structure, page footers, band big numbers) are **locked — no changes of any kind, including color, styling, or CSS.** If asked to change one, do NOT edit first — flag it and ask whether to override (local-only vs canonical) before making any change.
- Change LUCI cover logo or document CSS/structure.
- Remove page footers (`.doc-foot`) or band big numbers (`.sow-band-bignum`).
- Add inline font styles or unclassed elements that bypass the typography table above.
- Add marketing language to technical scope — stay factual and scoping-focused.
- Invent hardware specs or pricing not supported by client notes.

---

## Common tasks

**New property from site notes**
1. Cover: project title, prepared-for, basis, logo, display `<em>` name.
2. Page 2: rewrite intent and outcomes for their environment.
3. Pages 3–5: align phasing and §4 system scope to their stack (IPTV, audio, network, etc.).
4. Pages 6–7: IDF/rack specifics per their floor plan notes.
5. Pages 8–9: deliverables, assumptions, open confirmation items.

**Update `<title>`** in `<head>` to reflect client/project name.
