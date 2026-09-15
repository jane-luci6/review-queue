# Signal Issue 04 teaser — notes

**File:** `email-signal-issue-04-teaser.html`
**Adapted from:** `email-signal-issue-03-teaser.html` (last Signal teaser template)
**Issue:** 04 · September 2026
**Structure (r3):** field-led + hero photo. Mirrors Issue 03 exactly — dark lead card + 600px hero photo, then a 2x2 grid with a full-width **From the team** separator band between the light row (What's coming + Quick Tip) and the dark row (From LUCI + Mike). No Project Update card.
**Theme (masthead, locked):** Navigating Standardization vs. Adaptation
**Web destination (when live):** `https://www.lucisystems.com/the-signal/issue-04`
**Status:** Ready for ActiveCampaign paste. All copy applied verbatim from `email-signal-issue-04-teaser-r3-copy.md`. No placeholders remain. **No Send.** Jane reviews; Ermintrude pastes/uploads into ActiveCampaign.

Enter the subject line and preheader text manually when creating the campaign in ActiveCampaign. Personalization tag: `%FIRSTNAME%`.

---

## Subject line candidates (from r3 copy file)

1. `Aliante's 106' x 20' wall leads Issue 04`
2. `Inside Issue 04: Standardize the operation, not the hardware`
3. `The Signal: One operating standard, room to adapt`

**Recommended:** #1 — matches the email headline verbatim and names the lead.

## Preheader candidates (from r3 copy file)

1. `A field story from Aliante, a map that follows your view, a Quick Tip, and a Minute with Mike.`
2. `See 2,000 square feet of sportsbook wall run with the rest of the property.`
3. `Issue 04 explores what should stay standard—and what should adapt.`

**Recommended:** #1 — summarizes the contents cleanly and avoids dimension repetition in the preview strip. (Applied as the hidden preheader in the HTML.)

---

## Section / card inventory (r3 structure — mirrors Issue 03 with From the team separator)

| # | Card | Anchor | Kicker | Headline |
|---|---|---|---|---|
| Lead | In the field (dark card + 600px hero photo) | `#field-story` | `In the field` | A 106' x 20' wall on the platform Aliante already runs |
| Grid row 1, light | What's coming | `#whats-coming` | `What's coming` | A map that faces the way you do |
| Grid row 1, light | LUCI Quick Tip | `#quick-tip` | `LUCI Quick Tip` | Make every endpoint easier to find — and easier to service |
| Separator | **From the team** (full-width band, mint chat icon + Syncopate label) | — | — | — |
| Grid row 2, dark | From LUCI | `#from-luci` | `From LUCI` | Put LUCI to work across every team |
| Grid row 2, dark | A Minute with Mike | `#mike-column` | `A Minute with Mike` | Standardize the operation, not the hardware |

All five cards link to `https://www.lucisystems.com/the-signal/issue-04#<anchor>`. Plain kickers — no `01·06` numbering (per r2 brief, carried into r3).

---

## Hero photo (lead)

- **Source:** `https://cdn.prod.website-files.com/62d7d68d14611c2a31d863cd/6aa965ad594087632ec8988b_after-web.jpg` (Aliante after shot — Issue 03 pattern: large 600px-wide hero photo underneath the dark lead card)
- **Alt:** `Aliante sportsbook after the remodel — 106' x 20' curved LED wall live`
- **Width:** `600` (matches Issue 03 Sam's Town hero photo placement)

---

## Dimension lock (r3)

Zero occurrences of "106-foot" / "106 foot" anywhere in the file (title, subject notes, body, alt text). Wall references use **`106' x 20'`** and/or **`2,000 square feet`** only, per the r3 copy file and Jane's 15 Sep decision log.

---

## What changed from r2 → r3

- **Intro collapsed to one paragraph:** the two r2 intro paragraphs replaced with the single r3 intro paragraph (Aliante wall now runs with the rest of the property; issue contents preview; Mike on standardizing the operation—not the hardware).
- **Headline updated:** `A 106-foot field story is inside` → `Aliante's 106' x 20' wall leads Issue 04` (matches r3 copy file email headline).
- **In the field headline:** `A 106-foot wall...` → `A 106' x 20' wall...` (dimension lock).
- **In the field blurb:** `LUCI built...more than 2,000 square feet` → `LUCI brought...2,000 square feet` (r3 copy verbatim).
- **Mike deck:** `Get consistency at the operating layer and flexibility at the hardware layer.` → `Keep the operation consistent while the hardware adapts to each space.` (r3 copy verbatim).
- **Hidden preheader:** rewritten to r3 preheader candidate #1 (no "106-foot").
- **From the team separator restored:** full-width mint chat icon + "From the team" Syncopate label band inserted between the light grid row (What's coming + Quick Tip) and the dark grid row (From LUCI + Mike) — same visual treatment as Issue 03. Redundant `border-top` removed from the dark row cells (the separator band provides the transition).

## What was NOT changed (preserved from Issue 03 template / r2)

- Table layout, widths (600px container), cell padding.
- Embedded base64 fonts (Space Grotesk 400/500/600/700, Syncopate 700).
- Header LUCI logo base64.
- Font stack, color tokens, inline-style approach (ActiveCampaign-safe).
- Mobile `@media` breakpoints and `.stack` / `.stack-pad` reflow.
- Primary CTA de-boxed treatment (mint text link + accent underline, no filled button).
- Closing + signature block (Michael Epstein – CEO, contact lines, eco line, privacy link).
- Footer note: ActiveCampaign appends the newsletter footer (logo, unsubscribe, sender address) automatically.
- All card copy for What's coming, Quick Tip, and From LUCI (unchanged from r2 — r3 copy file matches).
- Sentence-case headline rendering (matches Issue 03 convention; r3 copy file's Title Case is doc formatting, not a rendering directive).

---

## Self-check (mechanical)

- File exists and opens locally (valid XHTML transitional doctype).
- Tag balance: 17 `<tr>` / 17 `</tr>`, 6 `<table>` / 6 `</table>` (matches Issue 03 — the From the team separator band restores the row count to 17).
- **Dimension lock:** grep confirms zero "106-foot" / "106 foot" occurrences. All wall references use `106' x 20'` or `2,000 square feet`.
- No remaining `project-update`, `01 &middot;`–`06 &middot;`, or r2-only strings (`A 106-foot field story`, `Get consistency at the operating`, `more than 2,000 square feet`, `LUCI built the curved`).
- All five Issue 04 section anchors present and link to `issue-04#<anchor>`.
- Hero photo URL, alt text, and `width="600"` match the r3 brief.
- All card copy matches `email-signal-issue-04-teaser-r3-copy.md` verbatim.
- From the team separator band present (mint chat icon + Syncopate label, colspan=2, same styling as Issue 03).
- No remaining `PLACEHOLDER` strings.

## Not done / handoff

- **No ActiveCampaign API calls.** Ermintrude pastes/uploads the HTML into AC and creates the campaign draft.
- **No Send.** Jane reviews the AC draft; send is Tue Sep 15 per work board (Jane names that send).
- **Mike column body:** teaser carries title + deck only (Issue 03 pattern); the full Mike letter lives in the newsletter `#mike-column`.
- **Webflow:** `https://www.lucisystems.com/the-signal/issue-04` is not live yet (Webflow pending). URL pattern used per brief; Jane knows Webflow is pending.
- **Full newsletter HTML untouched** per brief — only the teaser was updated.
