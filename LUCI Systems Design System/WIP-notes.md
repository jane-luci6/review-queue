# WIP / Handoff Notes

Running log of in-progress items and handoffs. Newest at top.

---

## Jamul jackpot celebration workflow — review with Mike

**Status:** Not urgent. **Look at:** week of Jun 23, 2026.

**Found:** Teams chat with Mike (Jun 17) — two files on OneDrive Marketing/Content:
- `jamul-jackpot-celebration-workflow.html`
- `jamul-jackpot-celebration-workflow (1).pptx`

**What it appears to be:** "Jamul Casino — Jackpot Celebration on LUCI" — a four-phase walkthrough for setting up jackpot-triggered celebration automation (slot/jackpot trigger → LUCI Scripting Engine → tiered win thresholds → TelemetryTV playlist override). Prepared for a Jamul scope & responsibilities discussion.

**Unclear:** Whether this was a seminar, customer workshop, sales deliverable, or internal planning doc — and whether Marketing needs to publish, adapt, or archive it.

**Action:** Open HTML, skim deck, ask Mike for context and next steps.

**OneDrive path:** `Marketing - Documents/Content/` (synced locally under OneDrive-LUCISystems).

---

## Send 30-day check-in email to Ameristar Council Bluffs

**Status:** Not started. **Action:** send Email 8 (30-day check-in) to Ameristar CB.
**File:** `ui_kits/email/email-8-30day-checkin.html`

**Decision needed:** Send the current version now, or wait for the FAQ → Resources & training rework (see item below, which is blocked on portal access)?

---

## Clearwater Casino — onboard into customer journey

**Status:** Not started. **Target:** this week (week of Jun 16, 2026).

**Goal:** Get Clearwater Casino into the customer onboarding journey, starting with their "Install Date Confirmed" email.
**Likely file:** `ui_kits/email/email-3-install-confirmed.html` (Email 3 · Install Confirmed).

**Open questions / needs before build:**
- Confirmed install date + property details (merge fields: %PROPERTY%, %FIRSTNAME%, recipient).
- Confirm whether this is just the one send now, or kicking off the full journey sequence for Clearwater.

---

## 30-day check-in email — replace FAQ with Resources & training

**Status:** Blocked on portal access (Jane). Email not yet touched.
**File:** `ui_kits/email/email-8-30day-checkin.html`

**Goal:** Swap the low-utility FAQ section for a curated Resources & training module (docs / videos / trainings) pulled from the LUCI Support Portal.

**Why the current FAQ block is weak:**
- The "View the FAQ" button links to `#faq`, but there is no `#faq` anchor or FAQ content in the email — it goes nowhere useful.
- Copy is vague ("user access, automation scheduling, how to report recurring issues") with nothing the customer can actually open.

**Jane's next steps (blocker):**
1. Get added to the LUCI Support Portal.
2. Pull 1–2 short how-to videos, a user/admin guide or quick-reference doc, any role-based training, and optionally release notes / "what's new."
   - Aim for "getting more out of LUCI" (30-day mindset), not first-week basics.
   - Avoid duplicating go-live materials already covered in emails 4–5.

**Build plan (once content is in hand):**
- Replace the "Common questions at the one-month mark" section + its dead `#faq` button with a de-boxed resource list: each row = thumbnail/icon + title + one-line "what you'll learn" + link.
- Update FAQ-referencing copy to match: header subtitle (line ~87), preheader (line ~47), and `<title>`/header text as needed.
