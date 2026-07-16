---
name: luci-brand
description: >-
  LUCI brand guardrails for customizing sales documents. Apply whenever editing
  capabilities documents, scope of work, budgetary estimates, or other LUCI
  marketing HTML templates.
---

# LUCI brand — document customization

Shared rules for all LUCI sales document customization. Read the template-specific `SKILL.md` first for editable vs locked pages; this file governs **how** edits look and read.

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

## Voice

- Write **A/V**, never “AV”.
- Plain, confident, operational — not marketing fluff.
- Client-specific copy should reference their environment, pain points, and goals concretely.
- Do not change LUCI product claims, capability names, or technical architecture descriptions unless the template skill explicitly allows it.

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
- When swapping a client logo: use PNG or SVG, transparent background, update `src` and `alt` on `.doc-cover__client` only.

## Saving

- **Never save over the master** on the VM. Copy the file locally first; masters are redeployed from `luci-design` and will overwrite in-place edits.
