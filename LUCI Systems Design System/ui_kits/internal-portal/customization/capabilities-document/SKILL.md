---
name: luci-capabilities-document
description: >-
  Customize the LUCI Capabilities document for a specific client. Use when Mike
  or sales needs a post-demo leave-behind with client name, summary, and logo
  on the cover while keeping the technical body locked.
---

# Capabilities document — customization

Post-demo personalized leave-behind. **9 pages (US Letter).** Source master: `capabilities-document.html` in this folder (build copy from `ui_kits/sales/`).

**Workflow:** see `../_brand/SKILL.md` — two-folder architecture, create workspace, dev server, fit check, page packing, voice, PDF export. This file covers only the template-specific page map and editable regions.

Voice: see `../_brand/SKILL.md` → Voice & tone.

## When to use

After a demo, when the prospect needs a capabilities overview scoped to their property — cover personalized, LUCI story unchanged.

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
| **8** | Proof of impact (Yaamava&rsquo; case study) | **LOCKED** |
| **9** | Close (contact + next step) | **EDITABLE** (headers + contact rep only) |

**Page 1 (cover)** and **page 9 (close)** may be customized. Pages 2–8 are protected brand and technical content.

---

## Editable regions (page 1 only)

All on `.doc-page--cover`:

| Element | Selector / marker | What to change |
|---------|-------------------|----------------|
| Cover kicker | `[data-studio="cover-kicker"]` | e.g. "Capabilities overview" |
| Cover display headline | `.doc-cover__display` | "Prepared for" + property name in `<em>` |
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
| Close kicker | `[data-studio="close-kicker"]` | e.g. "Next step" |
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

This includes all diagrams under `assets/diagrams/`, feature SVGs, journey connector, and the Yaamava&rsquo; proof copy.

**Page 8 is the Yaamava&rsquo; Resort &amp; Casino case study.** Every number on it comes from the approved case study (`ui_kits/case-studies/yaamava.html`, mirrored in `luci-website/src/data/caseStudyYaamava.ts`) &mdash; 1,000+ endpoints, 34 LED walls across seven venues, 290,000 sq ft under management, and a named quote from Toni Pepper, CITO of the San Manuel Band of Mission Indians. Don't swap in a different property's numbers, and don't re-cut the quote: it's a verbatim fragment, elided with an ellipsis, not a paraphrase. The sheet fits US Letter with about 2px to spare, so any added copy has to displace copy of the same length.

The Paragon and Aliante client copies were delivered on the earlier Ameristar case study and were deliberately left there &mdash; they are not out of sync by accident.

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
- Edit pages 2–8 copy, even "small" wording tweaks.
- Change the LUCI company block or close logo on page 9.
- Change CSS links or add inline styles that break print layout.
- Remove `doc-draft-badge` unless sending final (confirm with Jane).
