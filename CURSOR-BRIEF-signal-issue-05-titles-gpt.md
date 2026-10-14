CURSOR BRIEF
Repo: design (`luci-design` only)
Model: GPT (`luci-cursor --role gpt`)
Mode: execute
Job: Recommend titles for Signal Issue 05. RECOMMENDATION FILE ONLY. Do NOT edit any HTML. The operator applies the choices.

## Output
Write `ui_kits/newsletter/issue-05/picks-pack/issue-05-title-recommendations.md` containing exactly these sections:

1. **Masthead "This Issue" line**: ONE pick + one-line rationale + 2 runner-ups.
2. **Welcome heading**: ONE pick, with the single accent word/phrase marked in `*asterisks*` (it renders in the gold `<em>` accent, like Issue 04's "The Right Place for a *Standard*") + one-line rationale + 2 runner-ups (also with the accent marked).
3. **Advice section name** (used in 3 places: welcome body sentence, TOC entry, Advice kicker): ONE pick + one-line rationale + 2 runner-ups.

Keep it short. No other sections.

## Inputs (read)
- Issue 05 copy: `LUCI Systems Design System/ui_kits/newsletter/the-signal-issue-05-copy.md` (welcome dek/body, Field, Design with LUCI, Advice blurbs, Mike column)
- Picks pack options: `ui_kits/newsletter/issue-05/picks-pack/issue-05-titles-advice-mwm-DRAFT.html`
  - Theme A–H: Keep A/V on Course · Hold the Project Steady · Carry the Standard Through Every Handoff · Stay Aligned from Design to Operation · Plan It. Build It. Run It. · Keep Complex A/V Moving Together · Turn Continuity into Control · Bring Every Phase into Line
  - Advice names: Operating Notes · How to Run It · The Operating Playbook
- Conventions: Issue 04 (`the-signal-issue-04-september-2026.html`): masthead "Navigating Standardization vs. Adaptation", welcome heading "The Right Place for a *Standard*". Issue 03 (`the-signal-issue-03-august-2026.html`): masthead "Always moving, always forward". Match their length, tone, and capitalization style. The masthead line and welcome heading may differ (as in Issue 04).

## Locked theme (don't change the idea)
Continuity: the A/V "stabilizer" that holds a complex project steady from plan to floor and into daily operation. The welcome dek already says: "The steadier the line from planning through daily operation, the better a complex A/V project holds together."

## Rules
- You may pick from the options or write better ones.
- Active voice. Spell it "A/V". Never "layer". Never "property-by-property". Never imply LUCI replaces other tech. No vendor names.
- REJECTED: "One Thread from Plan to Floor" (don't use it or a near-clone).
- Advice name: it must work as a kicker label, a TOC entry, and inline in the sentence "The Quick Tip and ___ offer practical ways to keep schedules, venues, endpoints, and access aligned." It should suit a recurring section of practical operating advice from Mike.
- Don't deploy, push, or edit other files.
