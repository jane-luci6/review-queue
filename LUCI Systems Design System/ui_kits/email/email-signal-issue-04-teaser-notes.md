# Signal Issue 04 teaser — notes

**File:** `email-signal-issue-04-teaser.html`
**Adapted from:** `email-signal-issue-03-teaser.html` (last Signal teaser template)
**Issue:** 04 · September 2026
**Theme (masthead, locked):** Navigating Standardization vs. Adaptation
**Web destination (when live):** `https://www.lucisystems.com/the-signal/issue-04`
**Status:** Ready for ActiveCampaign paste. Mike card filled with locked copy and restyled to match Issue 03's dark/mint treatment. No placeholders remain. **No Send.** Jane reviews; Ermintrude pastes/uploads into ActiveCampaign.

Enter the subject line and preheader text manually when creating the campaign in ActiveCampaign. Personalization tag: `%FIRSTNAME%`.

---

## Subject line candidates

1. `The Signal · Issue 04 is live — navigating standardization vs. adaptation`
2. `Issue 04 of The Signal is live`
3. `The Signal is live — September 2026`
4. `A 106-foot LED wall, a map that faces you, and more — Issue 04 of The Signal`
5. `The Signal · Issue 04 — standardization vs. adaptation`

**Recommended:** #1 — names the issue, signals it's live, and previews the theme in lowercase (matches the Issue 03 teaser's plain-spoken register).

## Preheader candidates

1. `Aliante's 2,000-square-foot LED wall, a Quick Tip on endpoint names, a map that faces the way you do, the Field Activation Guide, and a Minute with Mike.`
2. `A busy month in the field, Aliante's sportsbook remodel, a Quick Tip, what's coming to New LUCI, and the Field Activation Guide.`
3. `Issue 04 — navigating standardization vs. adaptation. Read the September issue.`
4. `Standardize the operation, not the hardware. Issue 04 of The Signal is live.`

**Recommended:** #1 — mirrors the Issue 03 preheader shape (field notes first, then the rest of the issue beats) and reads in the preview pane without trailing off.

---

## Section / card inventory (matches Issue 04 TOC order)

| # | Card | Anchor | Kicker | Headline |
|---|---|---|---|---|
| 01 | Lead (full-width dark) | `#project-update` | `01 · LUCI Project Update` | It's been a busy month for LUCI! |
| 02 | Grid row 1, light | `#field-story` | `02 · In the field` | 2,000 square feet of game-day impact |
| 03 | Grid row 1, light | `#quick-tip` | `03 · LUCI Quick Tip` | Make every endpoint easier to find — and easier to service |
| 04 | Grid row 2, dark | `#whats-coming` | `04 · What's coming` | A map that faces the way you do |
| 05 | Grid row 2, dark | `#from-luci` | `05 · From LUCI` | Put LUCI to work across every team |
| 06 | Full-width closing card | `#mike-column` | `06 · A Minute with Mike` | **[PLACEHOLDER]** |

All six cards link to `https://www.lucisystems.com/the-signal/issue-04#<anchor>`.

---

## Placeholder inventory

| Location | Placeholder text | Status |
|---|---|---|
| Mike card headline | `[PLACEHOLDER: Minute with Mike — Jane finalizing]` | **Filled** — "Standardize the Operation, Not the Hardware" (locked from newsletter `art-title`). |
| Mike card blurb | `[PLACEHOLDER: Jane is finalizing Mike's column for Issue 04. Copy may change before send.]` | **Filled** — "Get consistency at the operating layer and flexibility at the hardware layer." (newsletter `art-deck`). |

**No remaining placeholders.** All other card copy is pulled from the live Issue 04 newsletter HTML (`the-signal-issue-04-september-2026.html`).

---

## What changed from Issue 03 → 04

- Title / header / date: Issue 03 · August 2026 → Issue 04 · September 2026.
- Lead story: Sam's Town field-story (with hosted image) → LUCI Project Update opener (no image — project update is a ledger; no hosted Aliante image available, so omitted per brief).
- Grid row 1 (light): `whats-coming` + `web-next` → `field-story` (Aliante) + `quick-tip` (endpoint names).
- Grid row 2 (dark): `quick-tip` + `mike-column` → `whats-coming` (map rotation) + `from-luci` (Field Activation Guide).
- Dropped Issue 03's "From the team" dark separator band (no equivalent in Issue 04's structure).
- Dropped `web-next` card (not in Issue 04 TOC).
- Added full-width closing card for `mike-column` (placeholder) after the grid.
- Dropped the Sam's Town lead-story `<img>` (Issue-03-specific hosted photo; no Issue 04 equivalent hosted).
- Kept the generic LUCI hero texture background URL on dark cells (brand chrome, reused from Issue 03).
- Primary CTA: `Read Issue 03` → `Read Issue 04`, URL → `issue-04`.
- Closing line: "next issue arrives September 15" → "October 15".
- Preheader text rewritten for Issue 04 beats.
- All section anchors updated to `issue-04#<anchor>`.

## What was NOT changed (preserved from Issue 03 template)

- Table layout, widths (600px container), cell padding.
- Embedded base64 fonts (Space Grotesk 400/500/600/700, Syncopate 700).
- Header LUCI logo base64.
- Font stack, color tokens, inline-style approach (ActiveCampaign-safe).
- Mobile `@media` breakpoints and `.stack` / `.stack-pad` reflow.
- Primary CTA de-boxed treatment (mint text link + accent underline, no filled button).
- Closing + signature block (Michael Epstein – CEO, contact lines, eco line, privacy link).
- Footer note: ActiveCampaign appends the newsletter footer (logo, unsubscribe, sender address) automatically.

---

## Send-day updates (15 Sep)

- **Mike card filled + restyled.** Headline "Standardize the Operation, Not the Hardware" and blurb "Get consistency at the operating layer and flexibility at the hardware layer." pulled from the locked newsletter `#mike-column` `art-title` / `art-deck`. Card restyled from a light panel (`#F5F8FA` bg, `#2b9e80` accents, `#10232D` title) to the Issue 03 Mike treatment: dark panel (`#10232D` + hero-texture gradient), mint `#68E3BE` kicker + "Read more", `#F5F8FA` title, `#C9D4DA` body. Title set as plain single-color text (no `<em>` split) to match Issue 03's teaser Mike card.
- **Project Update lead: Tulsa → Ponca City.** The geographic sweep "From Lewiston to Tulsa to Las Vegas" was wrong — no Issue 04 property is in Tulsa; the Oklahoma property (Swigs Stage) is in Ponca City. Changed to "From Lewiston to Ponca City to Las Vegas" in the teaser **and** synced the newsletter `proj-snapshot__dek` + webflow body split so the teaser matches the newsletter.
- **Aliante wall dimension: 106-foot → 106' x 20'.** Applied wherever the wall dimension is named: the Aliante field card and the Project Update lead clause ("…including a 106' x 20' curved LED wall at Aliante").
- **TOC numbering (01–06) kept** as the Issue 04 structure; colors, spacing, card hierarchy, and CTA style already match Issue 03 — no other drift found in a full scan (header, welcome, section header, lead, both grid rows, primary CTA, footer all consistent with Issue 03).



- File exists and opens locally (valid XHTML transitional doctype).
- Tag balance: 17 `<tr>` / 17 `</tr>`, 6 `<table>` / 6 `</table>`.
- No remaining `issue-03` / `Issue 03` / `August 2026` / `Sam's Town` / `web-next` references.
- All six Issue 04 section anchors present and link to `issue-04#<anchor>`.
- **No remaining `PLACEHOLDER` strings.** Mike card headline + blurb filled with locked copy.
- **No remaining `Tulsa` references.** Project Update lead now reads "Lewiston to Ponca City to Las Vegas" (matches newsletter dek).
- **No bare `106-foot`** — wall dimension now "106' x 20'" wherever named.
- Mike card is a dark panel with mint `#68E3BE` kicker + "Read more" and `#F5F8FA` / `#C9D4DA` text (matches Issue 03 Mike card).

## Not done / handoff

- **No ActiveCampaign API calls.** Ermintrude pastes/uploads the HTML into AC and creates the campaign draft.
- **No Send.** Jane reviews the AC draft; send is Tue Sep 15 per work board (Jane names that send).
- **Mike column body:** teaser carries title + deck only (Issue 03 pattern); the full Mike letter lives in the newsletter `#mike-column`.
- **Webflow:** `https://www.lucisystems.com/the-signal/issue-04` is not live yet (Webflow pending). URL pattern used per brief; Jane knows Webflow is pending.
- **Lead-story image:** omitted (no hosted Aliante image). If Jane wants a hero image on the lead card, a hosted AC-content URL will be needed.
