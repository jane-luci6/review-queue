# Brief: New LUCI upgrade campaign, Chunk 1 (existing-customer pre-launch webinar, emails 1–4)

You are the senior B2B email copywriter for LUCI Systems (A/V orchestration for casinos, resorts, venues). Work ONLY in:
`LUCI Systems Design System/ui_kits/internal-portal/email-copy/CUST/`
Read first: the four scaffolds `CUST-WEBINAR-01..04-*.md` in that folder, `../_INDEX.md`, and `LUCI Systems Design System/agent-handbook/canon/messaging-voice.md` + `channel-playbooks.md` if present. Do not edit any other file.

## Campaign context (keep the whole campaign in mind)
Existing customers (Operations and IT at current LUCI properties) get a cycle: pre-launch webinar (THIS CHUNK) -> upgrade readiness -> launch & upgrade -> post-upgrade. The Signal newsletter carries the broad preview and save-the-date; each direct email has ONE job. Beta ends Nov 20; the private preview webinar is around Nov 24, so email 1 goes out early November.

Chunk 1 plan:
1. CUST-WEBINAR-01 Seminar invitation — ~2–3 weeks before. Early look at New LUCI; include the overview asset so they see features/benefits before deciding to attend. CTA: review what is coming and register for the private preview.
2. CUST-WEBINAR-02 What to expect — 7–10 days before. Second chance with three concrete takeaways. Registrants get agenda content; non-registrants another registration chance (write ONE email that works for both, or note a one-line variant swap). CTA: review the agenda or register.
3. CUST-WEBINAR-03 Event reminder — 2 days before, registrants. Date, time, joining details. CTA: add to calendar or join.
4. CUST-WEBINAR-04 Recording for non-attendees — 2–3 business days after. Same product view while the pre-launch news is current. CTA: watch the recording.

## Product facts (from the published LUCI Upgrade Overview — use only these)
Theme: "Putting the power of programming in your hands." A new version of LUCI is on its way, putting more day-to-day programming control in your hands across the room, the interface, and the operation, on a faster, more responsive foundation.
01 Greater control of the room/guest experience: venue panels (tablets show only approved controls for that space), staging (prepare screens, sources, audio behind the scenes, apply on cue), audio group control.
02 Flexible control of your view: customizable interface (brand colors, light/dark, backsplashes), live map flexibility (upload your own floor plans), live screen view (see what's on any TV or LED wall from an iPad or browser).
03 Informed control of operations: audit trails, monitoring & analytics, sign-in & session control (email, PIN, Microsoft).
Plus in-product support: raise a request with context and logs; when something goes down, the LUCI team gets an alert.
Asset link — always call it "LUCI Upgrade Overview": https://www.lucisystems.com/product-briefs/luci-upgrade-overview

## LOCKED guardrails (violating any = fail)
- More control for the client, with LUCI's partnership/support still fully behind them. Never imply reduced support or that they're on their own.
- NO release/launch/availability date anywhere. Webinar timing is fine. New LUCI is "on its way"/in beta — never "launched", "now available", "is here".
- Hardware = a single "LUCI appliance" (only if needed); never mention a support box.
- LUCI works with and absorbs other tech. Never say it replaces anything. Never use the word "layer". No partner/vendor names.
- Never "property-by-property". Don't lead with "operational precision".
- The webinar is a PRIVATE PREVIEW for customers, not a sales demo. No selling, no pricing.
- Active voice; write for a cold reader (skimming, may not remember last email); spell "A/V"; human and light but professional. No hype, no exclamation stacks, no em-dash chains.
- Mike wants "we've never lost a client" more prominent — use it ONLY if it fits naturally (likely nowhere forced; say where/why you did or didn't).
- Body copy (greeting through CTA, excluding signature) max 150 words. Count precisely and report.
- Keep the scaffold format: greeting "Dear #Name#,", signature block placeholders. Use placeholders for unknowns: [WEBINAR DATE], [WEBINAR TIME], [WEBINAR PLATFORM], [REGISTRATION LINK], [JOIN LINK], [CALENDAR LINK], [RECORDING LINK], [AGENDA LINK].
- Do not state the exact webinar date anywhere except as the placeholders.

## Process — do it genuinely, per email
A) Campaign strategy (once): arc across the 4 emails, how each one's job differs, how to avoid repetition, tone ladder.
B) For EACH email:
 1. Strategy: what we're writing and why; for whom (ops vs IT angle); best way to reach them (sender, length, structure, timing); how to make impact while staying professional; the PRIMARY MESSAGE in one sentence.
 2. Three DISTINCT draft directions (different angle/structure, not word swaps), each a short full draft or tight sketch (~60–120 words) with a name.
 3. Pick the final and explain why it won (and what you borrowed from the losers).
 4. Final copy (≤150 words, report exact count), one preheader (≤90 chars), three subject lines with clearly different moods (label each mood).
C) Self-audit each final against every guardrail above; list any tension honestly.

## Outputs (write all three)
1. Overwrite each `CUST-WEBINAR-0N-*.md`: keep header metadata, set Status to "draft v1 — for Jane review", and fill in strategy, three directions, winner rationale, final copy, word count, preheader, subject lines, audit.
2. `CUST-WEBINAR-chunk1-strategy.md`: the campaign strategy (A) + open questions for Jane.
3. `CUST-WEBINAR-chunk1.json` with exactly this shape (strings plain text; body as array of paragraphs including greeting and CTA line; no signature):
{"campaign_strategy":"...","open_questions":["..."],"emails":[{"id":"CUST-WEBINAR-01","title":"...","timing":"...","audience":"...","primary_message":"...","strategy":{"what_why":"...","for_whom":"...","reach":"...","impact":"..."},"directions":[{"name":"...","summary":"...","draft":"..."}],"winner":"name","why_won":"...","subject_lines":[{"mood":"...","text":"..."}],"preheader":"...","body":["Dear #Name#,","..."],"cta_label":"...","word_count":0,"guardrail_notes":"..."}]}
Count word_count over the body array by whitespace split. Ensure valid JSON.
