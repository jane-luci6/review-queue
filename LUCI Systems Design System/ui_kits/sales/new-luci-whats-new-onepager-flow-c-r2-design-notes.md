# New LUCI What’s New one-pager — Flow C R2 · design-elevation notes

**Built:** 17 September 2026 · GLM · design-elevation pass over `new-luci-whats-new-onepager-flow-c.html`.
**Copy source:** `new-luci-whats-new-onepager-flow-c-r2-copy.md` (locked). **No copy was rewritten.** No line was flexed for letter fit.

## What this pass did

Applied the LUCI sales-print mesh treatment and elevated craft so the sheet reads as finished LUCI sales print, matching the most recent sales pieces GLM has built (capabilities document, brochure, field-activation guide).

### 1. Mesh integrated into the masthead (the primary dark field)

The masthead was a flat navy gradient with soft radial glows. It now carries the **mint-gold circuit mesh** used across the latest sales hero bands:

- Smoke base (`assets/textures/texture-3.png`) + navy gradient, same layer order as the capabilities/brochure cover band.
- `texture-circuit-header-mintgold.png` as a `::before`, masked to **fade in from the right** (`linear-gradient(90deg, transparent 38% → #000 100%)`) so the left-aligned announcement + headline read clean. Opacity 0.72, `background-size: 460px auto` — reads as a real background, not a faint center blob.
- A soft mint radial glow upper-left for depth (atmosphere, not a spotlight).
- Mint 4px bottom rule retained (structure).

### 2. Mesh bookends the footer (second dark field)

The thin navy footer now carries the **mint-only circuit** (`texture-circuit-navy-mint.png`) fading in from the right — the capabilities cover pattern where a second visible mint texture bookends the hero. Subtle (opacity 0.55, 60% width) so it doesn't compete with the wordmark/audience label.

### 3. Print-stable mesh (Chrome print-to-pdf skips CSS backgrounds)

Chrome's `--print-to-pdf` does not reliably render `url()` CSS backgrounds, so the masthead also includes a print-only `<img class="band-circuit-print" src="assets/textures/band-circuit-baked.jpg">` (fade + navy baked into the JPG), hidden on screen. In `@media print` the masked `::before` and glow are disabled and the masthead/footer fall back to solid navy + the baked image — the same approach the field-activation guide uses for its bands.

### 4. Craft elevation (hierarchy, spacing, type roles)

- **Theme headline** is now the dominant read: bumped from `clamp(26px, 3.1vw, 32px)` (which resolved to ~26px on the 816px sheet) to a fixed **30px**. Space Grotesk 700, mint `<em>` on *programming* retained.
- **Announcement** sits as a mint Syncopate eyebrow above the headline; **date** stays a distinct mint line below a hairline at the masthead foot (visible at a glance, per the locked layout instruction).
- **Middle title** “The 3 Promises of New LUCI” gets a proper head + 40×3 mint rule lockup (was a loose title + rule).
- **Ledger rows** keep the 30/70 split proof ledger; refined rhythm — promise numerals (Syncopate, mint-dark) get a touch more breathing room above the header, feature rows stack on hairlines (no cards, no equal columns), row height follows content (promise 03 is slightly taller for its four features; all three headers keep equal visual weight).
- **Close** stays a compact information close (mint rule + info line + contact placeholders) — **not** a download CTA, **not** a dark band.
- Three-tier type discipline held: Syncopate for kicker + announcement + promise numerals (display moments); Space Grotesk bold for theme headline, promise headers, feature names, section title; **Inter for the subhead, promise leads, feature teasers, close copy** (all non-head text).

## What did not change

- **Copy:** every locked string verbatim (HTML entities for apostrophes/dashes/middots render identically; no wording flexed).
- **Structure:** masthead → “The 3 Promises of New LUCI” → split proof ledger (promise left / features+teasers right) → thin close → footer. No upgrade-path steps, no download CTA, no promise index band.
- **Feature mapping / promise titles:** untouched.
- **Placeholders:** `[UPGRADE GUIDE URL]`, `[NAME]`, `[TITLE]`, `[EMAIL]`, `[PHONE]` retained.
- **Feature-list JSON:** not touched (none referenced by this file).
- **No invented metrics, no client names.**
- Self-contained (no shared `sales-document.css` dependency); brand fonts via `../../assets/fonts/luci-brand-fonts.css` (static Inter / Space Grotesk / Syncopate, no Google Fonts `<link>`).

## Print verification (this pass)

- Headless Chrome `--print-to-pdf`: **1 page**, US Letter, **353 KB** (up from 153 KB — the baked circuit JPG embedded for print; well under the 1.2 MB target).
- Natural content-height probe: **1046px** vs 1056px target → **−10px** (underfill, no overflow, no clipping). Block heights: mast 342 · middle 546 · close 118 · foot 40.
- `@page { size: letter; margin: 0 }`; `.sheet` locked to `8.5in × 11in` with `overflow: hidden`.

## How to open / print

Open in a browser (or Cursor's in-editor preview). Print → Save as PDF: US Letter, margins none, scale 100%, background graphics ON.

If a future edit overflows, do **not** trim copy — the sheet is locked at 8.5×11 with `overflow: hidden`, so overflow is silently clipped. Inspect in the browser and tighten spacing (not copy) in the embedded `<style>`.
