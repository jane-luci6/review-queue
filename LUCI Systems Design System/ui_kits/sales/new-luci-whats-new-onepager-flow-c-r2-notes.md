# New LUCI What’s New one-pager — Flow C R2 notes

**Built:** 17 September 2026 · GLM · rebuilt from `new-luci-whats-new-onepager-flow-c-r2-copy.md` (locked copy + Split Proof Ledger layout direction).

`new-luci-whats-new-onepager-flow-c.html` is the R2 rebuild of Flow C. It replaces the prior Flow C (Promise, proof, path) per the locked R2 copy and layout decision.

## Changelog vs prior Flow C

- **Top field regrouped.** Kicker (`WHAT’S NEW`) + announcement (`A NEW VERSION OF LUCI IS COMING`) + theme headline (`Putting the power of programming in your hands`, mint `<em>` on *programming*) + **one** subhead (`The new version of LUCI puts more control in your hands—with better support behind it.`) + date line (`RELEASE DATE · JANUARY 19`) all live together in the masthead. The date is now a distinct mint-accented line below a hairline at the bottom of the masthead (visible at a glance), replacing the prior top-right `[RELEASE DATE]` placeholder. Jane fills nothing here — January 19 is locked copy.
- **Promise index band removed.** The prior `The promise — three controls` three-column index band (Control the room / Control your view / Control your security) is gone. The pillars now appear **once**, inside the ledger.
- **Middle retitled.** The middle section is titled `The 3 Promises of New LUCI` (used once), with a 40×3 mint accent rule beneath.
- **Split Proof Ledger.** Each promise is one full-width ledger row: **~30% left** holds the promise number (`01` / `02` / `03` in Syncopate, mint-dark), the retitled promise header, and the short lead sentence; **~70% right** holds that promise’s features as compact horizontal lines — **feature name at left, 5–8-word teaser at right** — stacked with hairline separators (no cards, no equal columns). Row height follows content; the third promise is slightly taller because it carries four features. All three headers keep equal visual weight.
- **Promises retitled** (per locked R2 copy):
  - 01 · Greater control of the room
  - 02 · More flexible control of your view
  - 03 · Deeper control over security
- **Feature teasers are the locked 5–8-word lines** (word-count checked in the R2 copy file): e.g. `Put room controls where work happens.` (6), `Build the next look before applying it.` (7), `Adjust linked zones without losing their balance.` (7), etc. Teasers are set in Inter (body/recede tier); feature names in Space Grotesk bold.
- **Upgrade-path / fulfillment block removed.** The prior `Your path to New LUCI` dark band — `Confirm plan → shipped laptop → coordinated activation` steps with arrows, the `[NAME]` path headline, and the path contact line — is gone. No arrows, no path label, no fulfillment sequence.
- **Close is now a compact information close, not a download CTA.** A light block at the bottom: a 40×3 mint accent rule, the line `For more information, visit [UPGRADE GUIDE URL].`, then contact placeholders (`[NAME] · [TITLE]` / `[EMAIL] · [PHONE]`). It is **not** a dark CTA band and **not** a download button. The dark footer bar (wordmark + audience label) stays as the sheet bookend.
- **No invented metrics, no client names, no download CTA** — per brief and launch guardrails.
- **Off-page (still off):** Add any endpoint · Display model catalog · Upgrade Guide body · download CTAs.

## What did not change

- Sheet mechanics: `.sheet` locked to `8.5in × 11in`, `overflow: hidden`, `@page { size: letter; margin: 0 }`.
- Brand tokens, fonts (`../../assets/fonts/luci-brand-fonts.css` — static Inter / Space Grotesk / Syncopate, no Google Fonts), the LUCI white wordmark, the navy masthead with mint 4px bottom rule, the dark footer bar.
- Self-contained — no shared `sales-document.css` dependency; can be moved or handed off independently.
- Three-tier type discipline: Syncopate for kicker + promise numerals (display moments); Space Grotesk bold for the theme headline, promise headers, feature names, section title; Inter for the subhead, promise leads, feature teasers, close copy.

## How to open / print

Open in a browser (or Cursor's in-editor preview). The screen view shows the sheet centered on a grey desk surround.

**Print → Save as PDF** with:
- **Paper size:** US Letter
- **Margins:** None (the `@page { size: letter; margin: 0 }` rule handles it)
- **Scale:** 100% (do not “fit to page” — the sheet is already exactly 8.5×11)
- **Background graphics:** ON (so the navy masthead, mint bars, and mint-dark accents render)

## Print verification (this build)

Headless Chrome print-to-PDF: **1 page**, US Letter, 153 KB.
Natural content height probe: **967px** vs 1056px target → **−89px** (underfill, no overflow, no clipping). Block heights: mast 288 · middle 527 · close 113 · foot 38.

If a future edit overflows, do **not** trim copy — the sheet is locked at 8.5×11 with `overflow: hidden`, so overflow is silently clipped. Open in the browser and inspect; tighten spacing (not copy) in the file's embedded `<style>`.
