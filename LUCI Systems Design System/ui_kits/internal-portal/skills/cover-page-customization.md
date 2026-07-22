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

### Logo placement (4 sanctioned spots)

The cover carries a client-logo slot with **four sanctioned placements** — no free
positioning. Set the spot by adding a `logo-pos--X` class to `.doc-page--cover`
(`bottom-left` is the default and needs no class). The in-preview edit bar exposes
these as a "Logo spot" chip group Mike can tap; the agent sets the initial spot
when building the client file.

| Class | Spot | Treatment |
|-------|------|-----------|
| `logo-pos--bottom-left` | bottom-left of the light sheet (default) | natural colors, ≤44px tall |
| `logo-pos--band` | centered under the headline, in the navy band | inverted to white |
| `logo-pos--band-right` | vertically centered on the right of the navy band, over the pattern | inverted to white, larger (≤72px) |
| `logo-pos--bottom-right` | bottom-right of the light sheet | natural colors, ≤44px tall |

The band spots (`band`, `band-right`) move `.doc-cover__prepared` into `.doc-cover__hero`
via JS and apply `filter: brightness(0) invert(1)` so a dark/colored logo reads white
on navy. The light-sheet spots keep natural colors.

**Default-picking guidance (agent):** pick a spot that fits the logo.
- Wide/wordmark logos (most hotel & casino marks) → `bottom-left` (default) or `bottom-right`.
- A compact, dark mark that benefits from the band moment → `band` or `band-right`.
- When in doubt, leave `bottom-left`.
Mike can change it in one tap from the edit bar, so the default is reversible.

**White-logo handling:** if the provided logo is already light/white on transparent,
the invert filter would turn it black. On drop, the edit script samples luminance and
marks `data-logo-light="1"` on the img; the CSS skips the invert for light logos on
band spots. If the agent places a known-white logo by hand, set
`data-logo-light="1"` on `.doc-cover__client` and prefer a light-sheet spot
(`bottom-left`/`bottom-right`) — or, if the band is still desired, the attribute keeps
it from inverting to black.

**Logo cleanup for dark backgrounds (band spots):** the band spots invert a
dark/colored logo to white via a CSS filter. On a low-res or anti-aliased raster
logo that filter softens the edges, and any upscale reads pixelated — exactly
what makes a logo look fuzzy on the navy band. Before placing a logo on a band
spot (`logo-pos--band` / `logo-pos--band-right`), prepare it so it's crisp on dark:

1. **Prefer the brand's white / reversed (knockout) logo.** Most brands publish
   one (look for a `-white` / `-reversed` / `-knockout` asset). Drop it in and set
   `data-logo-light="1"` on `.doc-cover__client` — the CSS skips the invert
   filter, so a native white logo renders clean with no halo. This is the best
   outcome; look for it first.
2. **Else prefer a vector (SVG) over a raster (PNG/JPG).** A vector inverts and
   scales crisply at any band size; a raster inverts with softened edges and
   pixelates when upscaled. If only a raster exists, source one at **≥2× the
   display size** (band-right caps at ~320px wide → source ≥640px; band caps at
   ~280px → ≥560px). Ensure the SVG has its text converted to outlines / fonts
   embedded, so the secondary type doesn't fall back in browser or PDF export.
3. **Else fall back to a light-sheet spot.** If the only asset is a small, dark,
   raster logo, place it `bottom-left` / `bottom-right` (≤44px, natural colors,
   no invert, no upscale) rather than forcing a pixelated band placement. Tell
   Mike it's on the light sheet because the source logo wasn't crisp enough for
   the band, and offer to swap in a white / vector version if he has one.

Transparent background is required either way (no white box). If you have image
tools, you may re-export the provided logo knocked out to white on transparent
at higher resolution — but sourcing the brand's official white/reversed or
vector asset is preferred over re-processing.

**If the provided logo still won't be crisp on the band** (small raster, no
white/vector variant available, and a band spot is still desired): **go online
and source a clearer one.** Look for the brand's official press/brand kit, an
SVG from a logo library (e.g. Wikipedia/WMF, official site assets), or a
high-resolution PNG (≥2× the display size). Prefer a vector or a white/
reversed version per the steps above. Confirm the sourced logo is the correct
brand (file name, visual match) before placing — same mismatch-confirm rule as
an uploaded logo. If you can't find a clearer one, fall back to a light-sheet
spot and tell Mike. Don't ship a pixelated band placement.

**Tell Mike:** after placing the logo, the agent should say which spot it's in and
that it's changeable in one tap via the edit-bar "Logo spot" chips — don't ask him
to pick upfront, just place a sensible default and point him at the chips.

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
