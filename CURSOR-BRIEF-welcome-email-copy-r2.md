# Brief r2: editor pass on the Email 1 welcome revision

Re-read `CURSOR-BRIEF-welcome-email-copy.md` (repo root); all guardrails still apply. Revise only `LUCI Systems Design System/ui_kits/email/email-1a-welcome-revision.json` and `email-1a-welcome-revision-copy.md` (keep them in parity, keep the JSON shape, keep the three directions).

Editor notes on the FINAL ("The team that stays"):
1. Step 5 is named "Handoff", which collides with the body line "aren't a handoff team" and makes the end of the project sound like LUCI hands off. Rename it (for example "Go live") with a descriptor that keeps the same engineers present ("Your team takes the controls, and the same engineers stay with you." or better). Check all five step descriptors read as plain, neutral, parallel, and imply no stage or timeline. Keep "LUCI appliance" singular.
2. Jane asked for "lighthearted but sharp". Add ONE light, human touch somewhere in the body or close (dry and warm, not cute, no exclamation mark). Keep it short.
3. The header subline "A note from Mike about the team behind your LUCI project." is flat. Offer a warmer, shorter subline (under 70 characters) that does not repeat the body.
4. Tighten wherever a sentence works harder than it needs to. Keep the body at 150 words or less (it is about 105 now; shorter is fine) and recount `word_count` exactly.
5. Subject lines: keep three clearly different moods; make sure at least one is a little playful or curious, not three variations of "welcome". 55 characters max. Preheader complements, 90 characters max.
6. Re-run the scripted banned-term check from the first brief, and note "r2 changes" in `guardrail_audit` and the md.
