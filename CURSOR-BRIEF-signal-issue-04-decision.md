# Cursor brief: Signal Issue 04 decision sheet (Jane)

Jane wants a shortlist of articles plus theme options, lightly designed, easy to scan, so she can pick what Issue 04 (send Sep 15) is. Not the newsletter itself. Not live. Lorem Issue 04 shell already exists; this is the content-choice page.

Jane-facing. No agent notes on the page.

## Model
Strategic Marketer: lock themes + shortlist (ChatGPT OK for this lock — Jane-facing Signal Issue 04 choices; one-line why). Then Design Direction, then Maker GLM. Review before Jane.

## What already shipped (do not recap as news)

- **01 June — Clearing the Deck:** Ameristar field. Jane hire. Unnamed “coming in August / full rollout / built to think.”
- **02 July — The Version of Tomorrow:** Tachi field. Command Trail named as August lead (preview, no beta, no UI). Minute with Mike debut (lighting; “doesn’t replace”).
- **03 August — Always moving, always forward:** Sam’s Town field (current platform, not a beta site). First screenshots: look/themes, geo map, staging. “First beta property in the next thirty days.” Fall website announced. Lightning anecdote already in Mike’s column.

Issue 04 must **advance** that arc.

## Tension Jane must pick (do not resolve in copy)

Issue 03 + Aug 12 demo: beta within ~30 days, tidbit + screenshot, not a feature dump. Aug 27 GTM: public launch, full Signal article after launch, no more teasers. Aug 28 campaign plan: property-by-property beta, Signal = beta framing only. Jane’s Coming Soon rewrite recast a public launch. Named beta site and GA date are **not** in the files. Suncoast was internal play, not a customer name.

## Strong unused fodder (from Call Recordings + Cursor)

1. **Aliante Race & Sports wall** — best unused field story. EJ (Jul 31), Jason (Jul 15), Mike on site, videos Aug 27–28, photos. Curved ~106×20, 93→106 ft, ¼" plywood, 15 racks→2. Do not say biggest wall in Vegas. LUCI already on property.
2. **Venue panels / cabana / bar** — Jul 14 Will, Aug 12 pairing demo, Aug 25 “big one.” Hardware SKU not confirmed. Panel presets not shipped as of Aug 25.
3. **Staging then Apply** — Aug 12 + 25. Mike lockout example. Issue 03 already showed staging as a first look — only if there is a new angle (live event / drawing), not a re-debut.
4. **Audit + in-product support** — who/when/how long, human chooses to escalate. Do not name Hub, CoreX, correlation IDs, Cloudflare.
5. **Themed login / light-dark** — easiest screenshot. Issue 03 already showed the look as first peek — only if we add a new still or a property-themed example.
6. **Clearwater go-live** — photos Aug 31. No transcript. Need Jane/Mike names before copy.
7. **Yaamava case study** — live on the site. Pointer, don’t rebuild.
8. **FAG** — evergreen closer, not news.
9. **New LUCI status** — only if Jane picks the frame (beta live / still coming / public launch). No GA date. No named beta site unless she clears it.
10. **Minute with Mike** — new quotes from Aug 12, don’t recycle 03.

Skip: Sam’s Town, Tachi, Ameristar, Command Trail debut, “weeks from beta” as if new, EverPass/Sunday Ticket (held), Morgan pitch, internals.

## Deliverable

One HTML decision page in luci-design `ui_kits/newsletter/` e.g. `the-signal-issue-04-choices.html`. Jane opens with Show Preview.

Page shape:
- 3 theme options (title + one sentence + what field story it implies + how New LUCI shows up)
- Shortlist of articles (name, one-line why, source, already-ran / ready / needs Jane)
- A recommended mix for Sep 15, marked as a recommendation she can ignore

House: A/V. Never LUCI a layer. Never “LUCI replaces.” No partner names. Light design, not a new thesis. Kickers `#2b9e80`. Mint dark only.

Do not deploy. Do not overwrite Issue 01–04.
