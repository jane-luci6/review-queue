# Brief (GPT, --execute): The Signal Issue 06 (November 2026) — SLATE options for Jane

You are proposing OPTIONS for Jane to pick from. NOT full copy. Draft only: no ActiveCampaign, no send, no Webflow, never push. Commit locally when done.

## Deliverables (write both files)
1. `ui_kits/newsletter/issue-06/signal-06-slate.md` — the slate in plain markdown.
2. `ui_kits/content-marketing/signal-06-slate-review.html` — a single self-contained browser review page presenting the same slate for Jane. Copy the look (inline <style>, nav bar, fonts, colors, .kicker, cards, yellow `.ph` placeholder highlight) from `ui_kits/content-marketing/new-luci-prospect-emails-review.html`. Title/H1: "Signal Issue 06 (Nov) slate". Plain, skimmable, cards. No external assets. Include a small pick checkbox per option (visual only, no JS needed).

## What to propose
- **2–3 theme title options** (short headline + one-line rationale each).
- **5–6 piece options**, each mapped to an EXISTING Signal section (see section pattern from Issue 05 `ui_kits/newsletter/the-signal-issue-05-october-2026.html`: Welcome, LUCI Project Update / In the field, Beyond the platform, Inside LUCI, LUCI Quick Tip, What's coming, A Minute with Mike). Per piece: section, working title, 2–3 line angle, what it needs from whom, status (Ready to draft / Needs Mike's bullets / Needs Jane decision). Mark more than 6 only as clearly optional extras.

## Locked inputs
- **Theme (locked):** long-term clients / never losing a client. Meaning: all our valued clients have been part of our family since the inception of LUCI, and it only makes us better; their support is helping us grow the company and build a better product, leading into the new version.
- **New version:** divulge a bit more on New LUCI since it is closer; beta framing only. Launch theme phrase: "Putting the power of programming in your hands."
- **30-day project highlights piece (must include):**
  - Boyd: now 25 of 26 properties on LUCI — angle "your enterprise can be that way too".
  - Caesars: still expanding, with LUCI giving remote support to their integrator.
  - Treasure Chest: ONLY as a positive new-client highlight: stood up LUCI, sportsbook redone to swap in Boyd Gaming, added switches and TVs, audio finished, in two days. NOT a full case study. Do not mention any control-system brand.
  - Mike will bullet more highlights later: mark this piece (and any other highlight piece) with a yellow placeholder "[MIKE'S BULLETS NEEDED]".
- **Candidate topics still open (offer as options):** client forums (intros, how clients use LUCI, tips and tricks), scripting, long-term relationships.
- Issue 05 email shell rule: the email teaser will reuse the Issue 05 email shell later; not needed now, just note it.
- **Notes box on the page (as a note only, not a piece):** December issue plan = holiday thank-you to long-term clients plus office-closed / holiday coverage notice (Mike has a template); send around Dec 15.

## Wording locks (hard)
- No release date anywhere; never "launched"/"now available"; New LUCI is in beta.
- LUCI is never itself a "layer" (LUCI coordinating layers of tech is fine).
- "replace" only literally (e.g. LED walls replacing TVs), never "LUCI replaces your technology".
- Always "A/V" with the slash. Single "LUCI appliance" if hardware is named.
- No partner/vendor/integrator names (Boyd, Caesars, Treasure Chest are clients and are allowed; do not name Caesars' integrator; no control-system brands).
- Never "property-by-property". No support box mention.
- "we've never lost a client" is an approved claim and may be used.
- Customer-facing promise: more control in the client's hands, with LUCI's partnership still behind them.
- No invented numbers beyond those above.

## Self-check before finishing
grep both files for: launched, release date, layer, replaces, "AV " without slash, property-by-property, Crestron. Fix any hit. Then commit locally (do not push) and print the two file paths.
