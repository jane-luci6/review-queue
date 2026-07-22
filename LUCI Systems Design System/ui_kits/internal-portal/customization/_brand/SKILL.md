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
- When swapping a client logo: use PNG or SVG, transparent background, update `src` and `alt` on `.doc-cover__client` only.

## Saving

- **Never save over the master** on the VM. Copy the file locally first; masters are redeployed from `luci-design` and will overwrite in-place edits.
