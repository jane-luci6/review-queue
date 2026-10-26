# Brief: revise customer journey Email 1 "Welcome to the LUCI family" (COPY ONLY)

You are the senior B2B email copywriter for LUCI Systems (A/V orchestration for casinos, resorts, venues). Write ONLY these two new files in `LUCI Systems Design System/ui_kits/email/`:
- `email-1a-welcome-revision-copy.md` (human-readable)
- `email-1a-welcome-revision.json` (structured, shape below)
Do not edit `email-1a-welcome.html` or any other file. Read for context: `ui_kits/email/email-2-pre-kickoff.html`, `email-3-install-confirmed.html`, `email-5-go-live.html` (journey neighbours; skim the visible text only, the files contain large base64 blobs), `ui_kits/email/customer-journey-data.js` (top `emailRules` only), and `agent-handbook/canon/messaging-voice.md`.

## Situation
Email 1 of the customer onboarding journey (sent by Michael Epstein, CEO, from mepstein@lucisystems.com) was written to go out right before the kick-off call, so it carries a lot: benefits checklist, "what happens next" kick-off section, a "before your kick-off call" support-portal sign-up box, and an "installation journey" graphic. LUCI could not sync it with the kick-off, so it is now a plain WELCOME TO THE LUCI FAMILY email that can go out any time after the contract and before travel is scheduled.

Current copy (for reference; do not reuse its structure blindly):
- Header: "Welcome to the LUCI family." / "Where you can control, automate, and execute the entire guest experience from a single interface."
- "Hi %FIRSTNAME%," (renders blank in previews)
- "Welcome to the LUCI family, where we will support every system, every team, and every guest experience %PROPERTY% delivers. We're excited to have you with us!"
- "The engineers you'll meet in the coming weeks are integral to our partnership. These are the same people you'll work with throughout your entire LUCI engagement as an extension of your team."
- "They're ready to get LUCI installed so you can:" + 4 benefit checkmarks (shared view of every A/V system and zone; remove vendor management, processor conflicts, workarounds; turn screens into a tool for shaping the guest experience; a foundation that gets more capable over time)
- "What happens next": kick-off call (confirm technical requirements and network; walk through the implementation timeline; discuss onsite install date)
- Dark box: "Before your kick-off call, please complete the sign-up form to request access to the LUCI Customer Support Portal... forward the sign-up link to anyone on your team who needs access." Button "Request portal access". "...explore the platform documentation before we meet."
- "From there, we'll begin the installation process, which will look like this:" + graphic: Kickoff (review implementation, technical reqs, confirm install date) > Design review (confirm network architecture, order hardware, set timeline) > Onsite prep (ship equipment, finalize travel logistics) > Onsite (one week install, connect every endpoint to LUCI) > Go live (LUCI is live, no downtime during the transition)
- "If you have any questions, please feel free to reach out, and I'll be happy to help." "Welcome aboard." Signature Michael Epstein – CEO.
- Old subject: "This is your official welcome to the LUCI family!" Old preheader: "Here's what happens next, and what we need from you before your kick-off call."

## Jane's direction (Marketing Director)
1. Warmer, less corporate; it should read naturally, like Mike wrote it to a new partner.
2. Do NOT mention the kick-off (KO) call at all, anywhere (copy, subject, preheader, process step names).
3. Keep the process walk-through (it is helpful), but do NOT imply where the client is in that process. No "we'll begin", "next", "before your call", "first", "from there", "you're here", "in the coming weeks". Present it as "here's how a LUCI project generally goes". No timeline commitments (no "one week install", no dates, no durations).
4. Tone down hammering LUCI's benefits; the checklist is too much. At most one light, natural line about what LUCI will do for them.
5. Keep it short and personal from Mike.

## Guardrails (locked)
- Active voice; cold-reader context (a busy GM or IT director who signed recently and may not remember every detail); spell "A/V".
- Hardware: if mentioned, a single "LUCI appliance". Never mention a support box.
- Never describe LUCI itself as a "layer" (LUCI coordinating or orchestrating layers of technology is fine). Do not broadly say LUCI replaces existing technology.
- Never imply reduced support; the team stays with them.
- No release date; no New LUCI launch talk (this is the onboarding journey, not the upgrade campaign; do not mention New LUCI or beta at all).
- Don't name partners or customers. No "property-by-property". No pricing.
- "We've never lost a client": Mike likes it prominent; use it only if it fits naturally, warm, not salesy (it can fit a family/partnership welcome).
- The "engineers you'll meet" idea is good if kept human (real people, same team throughout), without timing ("in the coming weeks" implies a stage).
- Lighthearted but sharp, warm, never cute or salesy. No exclamation stacks.
- Greeting: use `Dear #Name#,` (the standard used in the other campaign emails). Note in open_questions that the real ActiveCampaign field in this template today is `%FIRSTNAME%`, so the merge tag is TBD for Jane.
- `%PROPERTY%`: prefer a natural phrase ("your property", "your team") unless the merge field genuinely adds warmth; state your decision and flag the merge-field question.
- Support portal sign-up: Jane has not decided whether it stays. Write the final so it works WITHOUT it, and also supply a short optional "portal block" (2 sentences + button label) that can be dropped in if Jane keeps it, worded with no reference to any call or stage ("Whenever it's convenient..."). The live sign-up link is https://app.smartsheet.com/b/form/3c05a169bfa14ae4ab834018381bc3a1 and the portal is https://lucisystems.atlassian.net/servicedesk/customer/portals. Note that Email 5 (go-live) and Email 8 (30-day) already offer portal access, and Email 2 (pre-kickoff) refers to "the LUCI support site".

## Process (do it genuinely)
1. Short strategy: what this email is and why; for whom; how to reach them (sender, length, structure); how to make an impact while staying professional; the PRIMARY MESSAGE in one sentence (a warm human welcome).
2. THREE distinct copy directions (different angle/structure, not word swaps), each a full draft including header headline and optional header subline, body, the process walk-through lead-in line and the 5 neutral step names with one short descriptor each, closing, sign-off.
3. Recommend a final and explain why it won (and what it borrowed).
4. Final: header headline + subline (may keep "Welcome to the LUCI family." if it still earns it), body copy, process lead-in, 5 neutral steps (name + 1 short descriptor each; rename "Kickoff" to something neutral like "Planning"; no durations; equal weight), closing, sign-off, optional portal block. Report the body word count (greeting through sign-off, excluding the step labels/descriptors and the optional portal block) and keep it at 150 words or less.
5. Three subject lines with clearly different moods (label them; 55 characters max; no "kick-off") and one preheader (90 characters max, complements the subject, no stage implication).
6. Self-audit against every guardrail and Jane's five directions; list tensions and Jane-only decisions.

## JSON shape (valid JSON, plain text strings)
{"strategy":{"what_why":"","for_whom":"","reach":"","impact":"","primary_message":""},
 "directions":[{"name":"","summary":"","header":{"headline":"","subline":""},"body":["Dear #Name#,","..."],"process_lead_in":"","steps":[{"name":"","descriptor":""}],"closing":["..."],"signoff":""}],
 "winner":"","why_won":"",
 "final":{"header":{"headline":"","subline":""},"body":["Dear #Name#,","..."],"process_lead_in":"","steps":[{"name":"","descriptor":""}],"closing":["..."],"signoff":"","portal_block_optional":{"text":["",""],"button":"","note":""}},
 "word_count":0,"subject_lines":[{"mood":"","text":""}],"preheader":"",
 "property_merge_decision":"","guardrail_audit":"","open_questions":["..."]}
`word_count` = whitespace-split words of final.body + final.process_lead_in + final.closing + final.signoff. Exactly 3 directions, 5 steps each, 3 subject lines. Run a scripted check before finishing: valid JSON, counts, lengths, and that none of these appear in any final/subject/preheader text: kick-off, kickoff, kick off, next, layer, replace, launch, New LUCI, beta, support box, property-by-property, "in the coming weeks", "we'll begin".
