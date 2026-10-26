# Brief: Net-new prospects part 2: recovery after Sales handback (NET-UNBOOKED-01..02, NET-POSTDEMO-01..02)

FIRST read `CURSOR-BRIEF-prospect-shared.md` (repo root, same folder as this brief) and obey it completely. This brief scopes one chunk.

Write ONLY these emails (scaffold paths are relative to `LUCI Systems Design System/ui_kits/internal-portal/email-copy/`). Output JSON file: `PROSPECT-net-new-2.json` in that same `email-copy/` folder.

### Cycle: Unbooked request recovery — after Sales handback
- **NET-UNBOOKED-01** (`NEW/NET-UNBOOKED-01-scheduling-recovery.md`) #1 Scheduling recovery
  - Timing: Provisional: about 7 days after Mark or Mike's final attempt and explicit handback
  - Purpose: Offer one clean path to schedule without restarting the acquisition pitch.
  - CTA: Pick a time for the walkthrough.
- **NET-UNBOOKED-02** (`NEW/NET-UNBOOKED-02-leave-the-invitation-open.md`) #2 Leave the invitation open
  - Timing: Provisional: 7–10 days after recovery email 1
  - Purpose: Close the active scheduling cycle without pressure, then move the prospect to Pulse if they remain quiet.
  - CTA: Schedule now or return when the timing is better.

### Cycle: Post-demo recovery — after Sales handback
- **NET-POSTDEMO-01** (`NEW/NET-POSTDEMO-01-relevant-reason-to-reconsider.md`) #1 Relevant reason to reconsider
  - Timing: Provisional: 10–14 days after the final personal attempt and explicit handback
  - Purpose: Reopen with one proof point or workflow tied to what the prospect cared about in the demo.
  - CTA: Reply if the priority is still active.
- **NET-POSTDEMO-02** (`NEW/NET-POSTDEMO-02-close-the-loop.md`) #2 Close the loop
  - Timing: Provisional: 7–10 days after recovery email 1
  - Purpose: End the recovery sequence respectfully, then move the prospect to Pulse if they remain quiet.
  - CTA: Restart the conversation when the timing is right.

Sender guidance and chunk notes:
- Audience: net-new prospects that Mark or Mike already tried personally and then explicitly handed back to Marketing. They requested or had a demo and went quiet. Recovery must feel respectful and human, never nagging, never guilt, never restarting the acquisition pitch. Timing in the plan is provisional; mark `timing` as provisional.
- UNBOOKED-01: one clean path to schedule ([BOOKING URL]). UNBOOKED-02: leave the invitation open without pressure, say the sequence is ending, and that LUCI will keep them on occasional updates (the plan moves quiet prospects to Pulse; do not promise frequency in a way the plan does not support, say "occasional notes").
- POSTDEMO-01: one proof point or workflow tied to what the prospect cared about in the demo: because we do not know what that was, use a clearly marked placeholder like [WORKFLOW THEY CARED ABOUT] and a short list of 3 alternative workflow hooks Mark can choose from in `guardrail_notes` or the md only (not in the email body). Never name the customer or deal, never mention deal status or pricing.
- POSTDEMO-02: close the loop respectfully ("restart whenever timing is right"). A good natural home for "we've never lost a client" is POSTDEMO-02 or POSTDEMO-01 if it reads as trust, not pressure; decide honestly.
- Keep each short (lean toward 60-110 words). Reply stops automation; reply goes to the sales owner.
