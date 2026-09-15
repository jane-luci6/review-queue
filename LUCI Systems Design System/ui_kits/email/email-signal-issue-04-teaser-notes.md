# Signal Issue 04 teaser — notes

**File:** `email-signal-issue-04-teaser.html`
**Adapted from:** `email-signal-issue-03-teaser.html` (last Signal teaser template)
**Issue:** 04 · September 2026
**Structure (r2):** field-led + hero photo. Mirrors Issue 03 exactly — dark lead card + 600px hero photo, then a 2x2 grid (row 1 light, row 2 dark), no Project Update card.
**Theme (masthead, locked):** Navigating Standardization vs. Adaptation
**Web destination (when live):** `https://www.lucisystems.com/the-signal/issue-04`
**Status:** Ready for ActiveCampaign paste. All copy applied verbatim from `email-signal-issue-04-teaser-r2-copy.md`. No placeholders remain. **No Send.** Jane reviews; Ermintrude pastes/uploads into ActiveCampaign.

Enter the subject line and preheader text manually when creating the campaign in ActiveCampaign. Personalization tag: `%FIRSTNAME%`.

---

## Subject line candidates (from r2 copy file)

1. `A 106-foot field story is inside`
2. `Inside Issue 04: Standardize the operation, not the hardware`
3. `The Signal: A sportsbook built to run as one`

**Recommended:** #1 — matches the email headline verbatim and carries the field-story lead.

## Preheader candidates (from r2 copy file)

1. `Aliante's curved LED wall leads a new issue about standardization, adaptation, and the work in between.`
2. `A field story from Aliante, a map that follows your view, a Quick Tip, and a Minute with Mike.`
3. `See how one operating standard leaves room for different hardware, spaces, and teams.`

**Recommended:** #1 — names the lead (Aliante's curved LED wall) and previews the theme in plain register.

---

## Section / card inventory (r2 structure — mirrors Issue 03)

| # | Card | Anchor | Kicker | Headline |
|---|---|---|---|---|
| Lead | In the field (dark card + 600px hero photo) | `#field-story` | `In the field` | A 106-foot wall on the platform Aliante already runs |
| Grid row 1, light | What's coming | `#whats-coming` | `What's coming` | A map that faces the way you do |
| Grid row 1, light | LUCI Quick Tip | `#quick-tip` | `LUCI Quick Tip` | Make every endpoint easier to find — and easier to service |
| Grid row 2, dark | From LUCI | `#from-luci` | `From LUCI` | Put LUCI to work across every team |
| Grid row 2, dark | A Minute with Mike | `#mike-column` | `A Minute with Mike` | Standardize the operation, not the hardware |

All five cards link to `https://www.lucisystems.com/the-signal/issue-04#<anchor>`. Plain kickers — no `01·06` numbering (per r2 brief).

---

## Hero photo (lead)

- **Source:** `https://cdn.prod.website-files.com/62d7d68d14611c2a31d863cd/6aa965ad594087632ec8988b_after-web.jpg` (Aliante after shot — Issue 03 pattern: large 600px-wide hero photo underneath the dark lead card)
- **Alt:** `Aliante sportsbook after the remodel — 106' x 20' curved LED wall live`
- **Width:** `600` (matches Issue 03 Sam's Town hero photo placement)

---

## What changed from prior Issue 04 draft → r2 rebuild

- **Lead swapped:** LUCI Project Update opener (no photo) → In the field dark card + 600px Aliante hero photo (Issue 03 pattern).
- **Project Update card dropped** entirely (per r2 brief — no `#project-update` card in the teaser).
- **Grid reorganized** to Issue 03's 2x2 pattern: row 1 light (What's coming + Quick Tip), row 2 dark (From LUCI + Mike). Mike moved from a separate full-width end card into the grid's dark row 2 right column — same position Mike holds in Issue 03.
- **Kickers de-numbered:** `01 ·` … `06 ·` numbering removed; plain kickers throughout (per r2 brief).
- **Intro rewritten** to the r2 narrative intro (two paragraphs + theme line), headline "A 106-foot field story is inside".
- **All card copy** pulled verbatim from `email-signal-issue-04-teaser-r2-copy.md`.
- **Hidden preheader** updated to field-led framing (Aliante's 106-foot curved LED wall first).
- **Separate full-width Mike end card removed** (Mike now in grid).

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

## Self-check (mechanical)

- File exists and opens locally (valid XHTML transitional doctype).
- Tag balance: 16 `<tr>` / 16 `</tr>`, 6 `<table>` / 6 `</table>`. (Issue 03 has 17 `<tr>` — the extra row is its "From the team" separator band, which Issue 04 has no equivalent for.)
- No remaining `project-update`, `01 &middot;`–`06 &middot;`, "It's been a busy month", "2,000 square feet of game-day impact", or "Lewiston to Ponca City" references.
- All five Issue 04 section anchors present and link to `issue-04#<anchor>`.
- Hero photo URL, alt text, and `width="600"` match the r2 brief.
- All card copy matches `email-signal-issue-04-teaser-r2-copy.md` verbatim.
- No remaining `PLACEHOLDER` strings.

## Not done / handoff

- **No ActiveCampaign API calls.** Ermintrude pastes/uploads the HTML into AC and creates the campaign draft.
- **No Send.** Jane reviews the AC draft; send is Tue Sep 15 per work board (Jane names that send).
- **Mike column body:** teaser carries title + deck only (Issue 03 pattern); the full Mike letter lives in the newsletter `#mike-column`.
- **Webflow:** `https://www.lucisystems.com/the-signal/issue-04` is not live yet (Webflow pending). URL pattern used per brief; Jane knows Webflow is pending.
- **Full newsletter HTML untouched** per brief — only the teaser was rebuilt.
