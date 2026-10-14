CURSOR BRIEF
Repo: design (`luci-design` only)
Model: GPT (`luci-cursor --role gpt`)
Mode: execute
Job: Signal Issue 05 (October 2026): FULL first-draft COPY, every section. Copy only. GLM lays it into the shell in a separate step.

## Outcome
Write ONE markdown copy deck:
`LUCI Systems Design System/ui_kits/newsletter/the-signal-issue-05-copy.md`

Jane sends the first draft to Mike on Fri Oct 9. Write every section now from the confirmed picks below. Do NOT block on open decisions. Use visible bracketed placeholders, in the exact form `[ALL CAPS LABEL — TBD]`, wherever a decision or number is still open. At the end of the deck, list every placeholder you used.

Do NOT edit the HTML shell, luci-website, Webflow, or ActiveCampaign. No send. Do NOT put pricing or dollar figures anywhere, because the repo is public.

## Read first (canon, format, and prior drafts)
- Canon: `LUCI Systems Design System/agent-handbook/canon/messaging-voice.md`, `channel-playbooks.md`, `agent-handbook/shared/DECISION-LOG.md` (Signal 05 + Osage entries are binding)
- Prior issue copy format + length: `LUCI Systems Design System/ui_kits/newsletter/the-signal-issue-04-copy-r3.md` and the Issue 04 HTML `the-signal-issue-04-september-2026.html` (match section lengths, voice, and kicker/headline/dek pattern)
- Current Issue 05 shell (section order + slot notes): `LUCI Systems Design System/ui_kits/newsletter/the-signal-issue-05-october-2026.html`
- Picks pack (theme ideas, Advice blurbs, MwM outlines + verbatim quotes, QT draft, What's Coming draft): `ui_kits/newsletter/issue-05/picks-pack/issue-05-titles-advice-mwm-DRAFT.html` + `NOTES.md`
- Field r2 (polish from this): `ui_kits/newsletter/issue-05/in-the-field-osage-swigs/osage-swigs-in-the-field-r2-DRAFT.html` + `NOTES-r2.md`
- Osage fact sheet (Consuelo, Oct 7 partnership spine): `case-studies/osage-ponca-swigs/osage-swigs-fact-sheet.md`
- Swigs facts: `case-studies/osage-ponca-swigs/sources/swigs-osage-ponca-city-spotlight.txt`
- Design services source: `content-library/sources/jesse-design-services-2026-09-30/transcript.txt` + `CATALOGUE.md`
- Reporting & Analytics claims: `../luci-website/src/data/upgradeGuide.ts` (`reporting-analytics` feature). READ ONLY.

## Brand locks (every section)
- Active voice. Give cold readers context: say who, where, and what before any insider shorthand.
- Spell it **A/V** (with the slash). Spell it **LUCI** (never "Lucy").
- NEVER write "property-by-property".
- NEVER say LUCI replaces other tech. LUCI works with and absorbs other A/V tech so it's all managed through one interface.
- NEVER call LUCI a "layer".
- Never imply reduced LUCI support or partnership.
- Marketing doesn't name partner/vendor brands (no Design LED, NovaStar, LG, QSC, JBL, Crestron, etc.).
- New LUCI = new version / beta framing only. NEVER "we launched" / "now available" / "is live".
- Don't invent quotes, numbers, customer names, outcomes, or UI menu paths.
- Warm, human, a little lightness. Never stiff.

## Section order (match the shell) + what to write

### 1. Welcome / theme (letter from Mike, signed Mike Epstein, CEO)
- Theme LOCKED (Jane Oct 6): continuity, the A/V "stabilizer bar" that runs through a whole project, from plan to floor and into daily operation. Hugely important on complex properties.
- Title: use the placeholder `[THEME TITLE — TBD]`. Do NOT pick from the picks-pack options A–H. Do NOT use "One Thread from Plan to Floor".
- Write a 2–3 paragraph welcome that sets up the theme and previews the issue: Osage Ponca City partnership (Field), Design with LUCI, Quick Tip, Advice, What's Coming (Reporting & Analytics + What's New two-pager), and Minute with Mike.
- Also write the one-line "Here's what this issue holds" summary and the TOC labels (use `[ADVICE SECTION NAME — TBD]` for Advice in the TOC).

### 2. LUCI Project Update
Not part of Jane's confirmed picks, and there's no roster source. Write a one-line opener and leave the cards as `[PROJECT UPDATE — TBD]` placeholders (property / city / date / one line). Don't invent jobs.

### 3. In the Field: Osage Casino Hotel – Ponca City (multi-year partnership)
- Polish from Field r2. Follow the DECISION-LOG Osage locks: multi-year partnership, NOT an LED spotlight. Arc: original LUCI install → ballroom onto LUCI → Swizzle → Swigs (latest).
- Venue name: use **Swizzle** (not Swallow).
- Lead with relationship length / project count. The stats row stays clearly marked placeholders, e.g. `[YEARS WITH LUCI — TBD]`, `[PROJECTS AT PONCA CITY — TBD]`. A third stat may be "Ponca City · this year's focus" (sourced), plus one Swigs proof stat only if it reads well.
- Web CS headline lock is "One foundation for every property expansion." Echo that thesis. The Signal headline may be a shorter variant, but don't contradict it.
- Swigs specs (three planes, nearly 20 ft, 60 cabinets / 480 panels, 3840 × 1296, two audio zones, four presets, 25.5 total working hours by a four-person onsite team) are secondary body proof only, and must match the spotlight exactly. No vendor names.
- Tie lightly to the theme: continuity / embedded partner.
- Include a pull-out "What Ponca City runs on LUCI now" list, sourced only (Swigs A/V endpoints + audio zones + display presets under LUCI alongside existing property tech; ballroom on LUCI). No invented ROI.
- Photo captions: `Photo TBD: Osage Project Media`. Soft link: "Read the full case study → `[CASE STUDY URL — TBD]`".
- Never mention Sand Springs.

### 4. Design with LUCI (Design services). LOCKED, write it in full
- Frame: a current LUCI offering. Plan and design support is part of the LUCI subscription / service relationship. NEVER mention D3 or any former company.
- From Jesse's transcript: the same team designs the infrastructure LUCI needs, coordinates it, turns the system on, and trains the owner, so no "who built this?" chain. Design intent minimizes rack hardware. Scope runs from tenant improvements and LED-only design up to fuller low-voltage + LED design. LUCI does not install the hardware (say it gracefully, only if it helps).
- Tie to the continuity theme without reusing the rejected title phrase.
- Don't name client properties (spellings are unverified). Diagram slot: `[DESIGN DIAGRAM — TBD: AI redraw of cleaned plan; never the customer floor plan]`.
- Headline, dek, ~150–250 words body, plus a CTA (talk to your LUCI team).

### 5. Advice (two locked blurbs)
- Section name placeholder: `[ADVICE SECTION NAME — TBD]`.
- Blurb 1, "Build venues first, then drop endpoints" (Mike, 06-26 consult 00:40:02): create every venue, save views, and name each section first, so control can be delegated cleanly when endpoints land.
- Blurb 2, "Users like candy, or one admin everyone calls" (Mike, 06-26 00:40:31): there's no harm in keeping control with one admin; most clients hand out users freely and filter by location and source. Both models work. Choose deliberately.
- Polish the picks-pack versions. 2–4 sentences each, with short headlines.

### 6. Quick Tip: calendar collision (LOCKED)
- TODAY'S behavior only: when two scheduled presets share the same TVs, the next preset wins.
- Seed line (CoS-approved): "Don't stack a drawing on a daypart without a plan."
- NO tease of New LUCI lockout / Staging-Apply / any future fix.
- Headline + 2–3 sentence intro + 3 short practical steps. Steps must be behavioral (check which TVs each preset touches, check timing overlap, plan the hand-back). Do NOT invent menu names or click paths. If a UI step is needed, use `[UI PATH — TBD: confirm in current LUCI]`.

### 7. What's Coming: Reporting & Analytics (beta) + What's New two-pager promo
- New version / beta framing only. Never "launched".
- Claims must stay within the Upgrade Guide `reporting-analytics` entry: incidents (volume/duration), command success/failure, latency, preset activity, 24-hour / 7-day / 30-day views, an overview to spot patterns, then drill into the device/command/automation record. Live monitoring = now. Audit trails = who/what/when. Reporting & Analytics = patterns across time.
- Visual: the fan image of four Analytics tabs (Overview, Commands, Automation, Reliability). Write a caption. Don't claim anything beyond those tabs.
- Promo callout: the What's New two-pager in this issue is the first published piece on the new LUCI. Write a soft invite to open/read it. CTA = contact your LUCI team. Do NOT link or mention a public Upgrade Guide URL (decision log: the two-pager points to LUCI contact).
- Optional single nod to the New LUCI theme: "putting the power of programming in your hands" (light; the Mike column owns it).
- This section absorbs the shell's separate "What's New · slot locked" note. One promo, not two.

### 8. A Minute with Mike: "Putting the power of programming in your hands"
- Headline locked: Putting the power of programming in your hands.
- Use picks-pack MwM spine 1 (recommended): principle → the old constraint (configuration lived deep in the database, so changes routed through LUCI or a third party) → proof (clients and their integrators can load their own maps and make configuration changes) → partnership guardrail (more day-to-day control, with the LUCI team and partnership still right behind them) → tie-in to the What's New two-pager.
- Verbatim Mike quote you may use (Mark/Mike 09_28, 00:10:40): "I always say, the power of programming. Let them do it. Let our clients do it, versus having to rely on us or a third party." Rewrite the "rely on us" idea in external voice so it never reads as reduced support. Do NOT publish "independent of needing us".
- Optional supporting beat, Mike Oct 8 review (00:04:22–00:05:09, paraphrase only, beta framing): clients have asked for finer roles and permissions. Today it's admin vs. user. The new version adds roles and access profiles that break down what each user can do. Keep it as "in the new version", not shipped. One or two sentences max.
- First person, Mike's voice. ~200–300 words. Sign as Mike Epstein, CEO, LUCI Systems.
- Must not stack the same idea as Advice blurb 2. Reference it lightly at most.

### 9. Happenings
Not in Jane's picks. Leave `[HAPPENINGS — TBD]` with a one-line note.

### 10. Closing + support block
Keep the existing support-portal block wording. Refresh the closing paragraph so it lands the continuity theme in 2–3 sentences, signed "The LUCI Team".

## Deck format
For each section, use labeled fields matching the shell slots: Kicker / Headline / Dek / Body / Stats / Captions / CTA. Add a top "Draft status" note (first draft for Mike review Oct 9). End with:
1. a "Placeholders left" list (every `[… — TBD]`)
2. a short "Sources used" list with file + timestamp
3. a self-check confirming: no banned words, A/V spelling, no vendor names, no "launched", no Sand Springs, no D3, no pricing

## Execute
Write the deck now. Commit is fine (luci-cursor auto-commits). Do not push.
