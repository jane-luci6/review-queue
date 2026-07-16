# Cover-page customization simulation

Simulate the Customization Studio's cover-page feature for the budgetary
estimate (and, with the same shape, the capabilities document): take a company
name, plain-language goals, and a logo, and produce the customized cover — with
the goals **rewritten** as a business-audience overview in LUCI's voice.

Use the **agent-readiness-testing** method (`agent-readiness-testing.md`): the
agent performs the real task the not-yet-built feature would do, against the real
document, and reports the gaps. Don't build the feature yet — simulate it first.

## The feature (intended behavior)

Inputs (from the Customization Studio cover form):
- **Company name** — the property/company (e.g., "Tachi Palace").
- **Goals, plain-language** — notes: goals, pain points, current system, meeting
  context. The form field is "What should the introduction speak to?"
- **Client logo** — PNG or SVG, transparent background.

Outputs (placed in the cover):
- Company name → the designated areas (see table).
- Goals → **rewritten** for a business audience as an overview of what the
  prospect is looking to accomplish and how LUCI helps, in LUCI voice/tone.
- Logo → the client-logo slot.

## Designated placement areas (budgetary estimate)

| Input | Selector | What to set |
|-------|----------|-------------|
| Company name | `.doc-cover__display` (replace "your property") | Cover headline |
| Company name | `.doc-cover__summary-text strong` (replace `[Property Name]`) | Bold lead-in in Client summary |
| Company name | `.be-intro__text strong` on page 2 (replace `[Property Name]`) | Page-2 intro |
| Goals rewrite | `.doc-cover__summary-text` (full paragraph) | Client summary |
| Logo | `.doc-cover__client` (`src` + `alt`) | Client logo image |

Locked: `.doc-cover__logo` (the LUCI wordmark — never the client's).

Logo handling — confirm on mismatch: if the uploaded logo filename doesn't
match the company name (or otherwise looks wrong), **confirm with the user
before placing or skipping** — do not autonomously decide. The user may be
testing, or may want the uploaded image placed regardless of a name mismatch.
Place it on the user's say-so; only skip on the user's say-so. Surface the
mismatch (e.g., "uploaded `Aliante.jpeg` for `Paragon Casino` — place anyway?").

## The rewrite contract (the core agent task)

Turn the plain-language goals into the cover's Client summary:
- **Audience:** the prospect's business/leadership reader — not internal LUCI notes.
- **Frame:** what the prospect is looking to accomplish, then how LUCI helps them
  get there. Lead with the prospect's goal; LUCI is the means, not the subject.
- **LUCI voice** (see `.cursor/rules/luci-messaging-voice.mdc` + the Messaging
  guide → Voice & tone):
  - Engine and verbs, not layers — "LUCI orchestrates / runs / consolidates /
    integrates." Never use **layer** as a noun for LUCI.
  - Always write **A/V**, never "AV" or "A-V".
  - Watch repetition — don't repeat engine/orchestrates within the passage;
    rotate to a precise alternative (runs, operates, consolidates, refines).
- **Length:** 2–3 sentences, fits the summary block (~60ch measure). Keep the
  Phase 1 / scoped-estimate framing only where it's actually true for the client.
- **No invented facts:** reframe only what the input gives. If the goals are too
  thin to write a credible overview, that's a gap — surface it, don't fabricate.

## Simulation procedure (grounded execution)

1. Read the budgetary master (`ui_kits/sales/budgetary-estimate.html`), its
   `customization/budgetary-estimate/SKILL.md`, and the LUCI voice rule.
2. Take the inputs: company name, plain-language goals, logo path.
3. Draft the rewrite per the contract above.
4. Copy the master to `ui_kits/sales/<client>-budgetary-estimate.html` and apply:
   name in the three areas, rewrite in `.doc-cover__summary-text`, logo in
   `.doc-cover__client` (transparent PNG/SVG; if it must sit on a dark band,
   filter to white: `filter: brightness(0) invert(1)`).
5. Report: the before/after rewrite, where each input landed, and every gap.

## Known gaps (from inspecting the current form)

The budgetary cover form in `internal-portal/index.html` (budgetary cover
section) as built today:
- **The goals field (`context`) has no `inject` target** — the plain-language
  notes are captured but never placed. *(Tool-shape gap.)*
- **No rewrite step** — the form only injects raw text. The business-audience /
  LUCI-voice rewrite is the agent's job today; production needs an LLM step or an
  agent call wired into the form. *(Skill/tool gap.)*
- **Company name injects only into `.doc-cover__summary-text strong`** — not the
  `.doc-cover__display` headline or the page-2 `.be-intro__text` placeholder.
  *(Tool-shape gap — add `inject` targets or `[data-studio]` hooks there.)*

Compare the capabilities-document cover form, which does inject its
`clientSummary` into `[data-studio="client-summary"]` — but still raw text, no
rewrite. The rewrite gap is shared.

## Session template

```
Driver framing:
  "You are the cover-customization agent for the LUCI budgetary estimate.
   Inputs: company name = <name>; goals (plain language) = <notes>; logo = <path>.
   Rewrite the goals into the Client summary per the rewrite contract, then place
   the name, summary, and logo into the designated areas of a client copy of
   ui_kits/sales/budgetary-estimate.html. Execute against the real file and
   report: the before/after rewrite, where each input landed, and any gaps
   (missing injects, goals too thin to rewrite, logo not transparent, name
   overflow in the headline)."
```
