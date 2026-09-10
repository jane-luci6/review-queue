# New LUCI email communications and nurture plan

The email system for customers, warm prospects, and net-new prospects: sequence, timing, purpose, response handling, and long-term nurture.

The campaign theme, audiences, and shared marketing channels live in the [New LUCI Campaign Strategy](http://10.10.1.17:8081/internal-portal/index.html#coming-soon/new-luci-campaign-strategy). This document covers email only.

## Email decisions

- Existing customers receive direct pre-launch email because they have a reason to anticipate the release.
- Only high-intent warm prospects receive a pre-launch preview invitation: people who completed a demo or seriously pursued one. Broader warm and net-new outreach begins at launch.
- A reply, booked meeting, or active opportunity stops marketing automation.
- Anyone in an active Mark or Mike conversation is suppressed from automated nurture.
- Opens and ordinary clicks inform reporting; they do not trigger a sales handoff.
- A person receives only the cycle that matches their current lifecycle stage.
- The pre-launch seminar is positioned as a private preview, not a sales demo. Every invitation states when New LUCI becomes available.
- Marketing recovery begins only after Mark or Mike explicitly hands the prospect back. The handback timing remains to be defined with Sales.

## How The Signal fits

The Signal carries the broad customer preview and can include the seminar save-the-date. It is planning context for this program, not an email in the cycles below.

Each direct customer email has one specific job:

1. Drive seminar registration or attendance.
2. Announce that New LUCI is available.
3. Give customers the replay and upgrade path.
4. Resolve remaining upgrade questions.

## Email plan by audience and phase

![Email plan by audience and phase](./LUCI%20Systems%20Design%20System/ui_kits/internal-portal/luci-prospect-nurture-lifecycle.svg)

## Existing customers

### Pre-launch seminar cycle

1. **Seminar invitation**
   - **Timing:** About two to three weeks before the seminar.
   - **Purpose and message:** Give customers an early look at New LUCI. Include the What's New asset so they can see the features and customer benefits before deciding to attend.
   - **CTA:** Review what is coming and register for the live preview.

2. **What to expect**
   - **Timing:** Seven to ten days before the seminar.
   - **Purpose and message:** Give the invitation a second chance with three concrete takeaways. Registrants receive agenda content; nonregistrants receive another registration opportunity.
   - **CTA:** Review the agenda or register.

3. **Event reminder**
   - **Timing:** Two days before the seminar.
   - **Purpose and message:** Convert registrations into attendance with the date, time, and joining details.
   - **CTA:** Add to calendar or join the session.

4. **Recording for non-attendees**
   - **Timing:** Two to three business days after the seminar; customers who did not attend.
   - **Purpose and message:** Give customers who could not attend the same product view while the pre-launch announcement is still current.
   - **CTA:** Watch the seminar recording.

### Launch and upgrade cycle

1. **Customer launch announcement**
   - **Timing:** Launch day.
   - **Purpose and message:** Announce that New LUCI is available and package the What's New asset, upgrade process, preparation steps, and FAQ in one actionable message.
   - **CTA:** Review the release and start the upgrade process.

2. **Upgrade follow-up**
   - **Timing:** Seven to ten days after launch; suppress once an upgrade is scheduled.
   - **Purpose and message:** Resolve remaining timing or process questions without repeating the feature overview.
   - **CTA:** Choose the next step for the property.

## Warm prospects

Warm prospects include anyone with prior LUCI exposure—a demo, request, website visit, referral, or colleague’s introduction. One broad launch message can cover those differences, but the pre-launch invitation goes only to the people who previously invested meaningful time in a demo or serious request.

### Selected pre-launch preview

1. **Private preview invitation**
   - **Timing:** About two to three weeks before launch; past-demo and serious past-request prospects only.
   - **Purpose and message:** Offer an early look at what has changed and state the launch date clearly.
   - **CTA:** Register for the private preview.

2. **What to expect**
   - **Timing:** Seven to ten days before the seminar.
   - **Purpose and message:** Show three concrete changes they will see. Registrants receive agenda content; nonregistrants receive another registration opportunity.
   - **CTA:** Review the agenda or register.

3. **Registered-attendee reminder**
   - **Timing:** Two days before the seminar; registrants only.
   - **Purpose and message:** Convert registrations into attendance without sending another product pitch.
   - **CTA:** Add to calendar or join the session.

4. **Personal preview follow-up**
   - **Timing:** Next business day after the seminar; sent by Mark.
   - **Purpose and message:** Ask what stood out and offer a direct conversation before broader launch follow-up begins.
   - **CTA:** Reply to Mark or choose a time to reconnect.

5. **Recording for no-shows**
   - **Timing:** Two to three business days after the seminar; registrants who did not attend.
   - **Purpose and message:** Preserve the value of the invitation without asking for another live commitment.
   - **CTA:** Watch the private-preview recording.

### Launch re-engagement cycle

1. **What changed**
   - **Timing:** Launch day.
   - **Purpose and message:** “LUCI has changed a lot since you last saw it.” Reopen the broader warm list with the operational-precision story. Private-preview recipients receive a shorter availability follow-up instead.
   - **CTA:** See what is different.

2. **Recorded preview**
   - **Timing:** Four to five days after email 1.
   - **Purpose and message:** Let prospects see New LUCI without asking them to commit to a live sales demo.
   - **CTA:** Watch the edited seminar recording.

3. **Operational proof**
   - **Timing:** Four to five days after email 2.
   - **Purpose and message:** Make the platform credible with consolidation numbers from running properties.
   - **CTA:** See the proof or reply with a question.

4. **Direct invitation**
   - **Timing:** Five to seven days after email 3.
   - **Purpose and message:** Close the launch cycle with a low-friction invitation to reconnect.
   - **CTA:** Book a short conversation or walkthrough.

## Net-new prospects

### Acquisition cycle

1. **The operational problem**
   - **Timing:** Start of the outbound cycle.
   - **Purpose and message:** Lead with the cost of separate A/V systems and workflows—not with New LUCI features.
   - **CTA:** Recognize the problem.

2. **Consolidation proof**
   - **Timing:** Five days after email 1.
   - **Purpose and message:** Show what a shorter list of systems, vendors, and workflows looks like.
   - **CTA:** See how LUCI consolidates the operation.

3. **Recorded walkthrough**
   - **Timing:** Five days after email 2.
   - **Purpose and message:** Introduce New LUCI visually after the prospect understands the problem and proof—without asking for a live meeting.
   - **CTA:** Watch the edited seminar recording.

4. **Platform, team, and invitation**
   - **Timing:** Five days after email 3.
   - **Purpose and message:** Connect the orchestration engine and embedded team, then invite qualified interest into a conversation.
   - **CTA:** Book a demo.

## Response handling

The response flow starts after a warm prospect responds or a net-new prospect requests a demo. It does not send either person back to an acquisition cycle already in progress.

![Response handling after a prospect raises a hand](./LUCI%20Systems%20Design%20System/ui_kits/internal-portal/luci-prospect-routing.svg)

### After a warm response

1. **Immediate response** — immediately acknowledge the reply, booking, or request and answer the immediate question.
2. **Personal outreach** — same or next business day from Mark, continuing from the prospect's prior LUCI context.

### After a net-new demo request

1. **Immediate confirmation** — immediately; confirm the request and provide a calendar.
2. **Personal follow-up** — same or next business day from Mike or Mark.

Mark or Mike owns the prospect until an explicit handback to Marketing. The ownership window and handback status still need to be defined with Sales.

### Unbooked request recovery — after Sales handback

1. **Scheduling recovery** — provisionally, about seven days after the final personal attempt and explicit handback.
2. **Leave the invitation open** — provisionally, seven to ten days later.

### Post-demo recovery — after Sales handback

1. **Relevant reason to reconsider** — provisionally, ten to fourteen days after the final personal attempt and explicit handback.
2. **Close the loop** — provisionally, seven to ten days later.

After two recovery emails at most, a quiet prospect moves to the Prospect Pulse.

## Prospect Pulse

The Prospect Pulse is shared by warm and net-new prospects who complete their relevant cycle without entering sales. Send one concise email every four to six weeks for approximately six months.

Each email starts with a recognizable property problem, connects it to a LUCI benefit, and proves the connection with a workflow, capability, or operating result.

1. **Month 1 — When the property has too many systems:** separate interfaces, vendors, and workflows create operational drag; LUCI provides property-wide orchestration and control. Mention the recent New LUCI release as supporting proof.
2. **Month 2 — When a critical change cannot interrupt what is live:** an event, source change, or floor update must happen at the right moment; staging and presets enable safer execution.
3. **Month 3 — When every team needs the same picture:** operations, IT, marketing, and leadership need one operating view and a clearer record of what happened.
4. **Month 4 — When the property adds another venue:** expansion and renovation should extend the existing standard instead of adding another isolated interface and workflow.
5. **Month 5 — When something fails and ownership is fragmented:** in-product context, audit history, and the embedded team carry an incident from detection through resolution.
6. **Month 6 — When the next refresh decision arrives:** compare another replacement cycle with a standardized platform that consolidates the environment and becomes more capable over time.

Each Pulse has one idea, one proof point, and one ask. After Month 6, move unresponsive prospects to a low-frequency quarterly pulse or park them.

## Copy build order

1. Customer seminar email cycle.
2. Customer launch and upgrade cycle.
3. Warm prospect private-preview and launch cycles.
4. Net-new acquisition cycle.
5. Demo-request and post-demo response emails.
6. Six Prospect Pulse emails.

As each copy set is completed, link it from the corresponding email card in the IMP.

## Decisions to finalize

- Seminar/demo date, registration platform, and launch timing.
- Exact sender and send time for each cycle.
- Where completed copy will live in the IMP.
- CRM fields, suppression automation, and the explicit Sales-to-Marketing handback status.
- Mark and Mike's ownership window and final-attempt process before recovery begins.
- Whether unresponsive prospects move to quarterly nurture or are parked after Month 6.
