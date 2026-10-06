# Signal Issue 05 picks pack — source and fact-check notes

**Status:** DRAFT review pack only
**Issue:** The Signal Issue 05 · October 2026
**Deliverable:** `issue-05-titles-advice-mwm-DRAFT.html`

## Source register

| Use in pack | Source | Timestamp | Fact carried forward |
|---|---|---:|---|
| Quick Tip: calendar collision | Mike consult, 06-26 | Not supplied in delegated lock | When two scheduled presets share the same TVs, the next preset wins. Today’s behavior only. |
| Advice: build venues first | Mike consult, 06-26 | 00:40:02 | Create venues, save views, and name property sections before dropping endpoints so control can be delegated by need. |
| Advice: access models | Mike consult, 06-26 | 00:40:31 | One client keeps a single admin everyone calls; most create many users and filter access by locations and sources. |
| MwM basement/config-forward pull | `09_28 New LUCI Mark_Mike-transcript` · Mike | 00:10:02 | Clients can load maps; configuration that lived in Level 2/the database is brought forward for clients and integrators. |
| MwM “power of programming” pull | `09_28 New LUCI Mark_Mike-transcript` · Mike | 00:10:40 | “The power of programming” means letting clients do more directly instead of routing every action through LUCI or a third party. |
| What’s Coming: Reporting & Analytics | `/Users/janehaynie/Documents/Cursor Projects/luci-website/src/data/upgradeGuide.ts` · `reporting-analytics` | Current source | Review incident volume/duration, command success/failure, latency, and preset activity across 24-hour, 7-day, and 30-day views; use the overview to spot patterns, then move into the relevant record. |

The two Mark/Mike quotations in the HTML are reproduced verbatim from the delegated CoS source excerpts. The 06-26 items and Reporting & Analytics source are paraphrased; no additional product claims were added.

## Verbatim Mark/Mike pulls

### Mike · 09_28 · 00:10:40

> “I always say, the power of programming. Let them do it. Let our clients do it, versus having to rely on us or a third party.”

### Mike · 09_28 · 00:10:02

> “They’re able to load their own maps now. Think of it this way: we’re trying to build this, where it’s completely customizable, like completely independent of needing us. The reason why everybody needed us is because everything was done like level two, like in a basement. Right in our database. Everything had to be configured in the database. These guys brought all of that forward, so they’re able to allow our client or our client’s integrator to do whatever they want.”

## CoS fact-check notes

- **Filename correction:** The earlier cue “09-08” was a typo. The verified source file is `09_28 New LUCI Mark_Mike-transcript`.
- **Speaker accuracy:** The basement metaphor is Mike on the 09_28 Mark/Mike call at 00:10:02. Adam/Boyd on 09-10 is the modern login, branding, and configuration UI demo. Do not merge the speakers or attribute the basement line to Adam/Boyd.
- **External framing:** Mike’s “independent of needing us” wording is retained only in the internal source pull. Final customer copy must frame the shift as more client control with LUCI partnership and accountability still behind the operation.
- **What’s New tie-in:** The Minute with Mike outlines and What’s Coming callout may point to the What’s New two-pager shipping in the issue. The callout identifies it as the first published piece on the new LUCI without restating its feature copy.
- **Design services bridge:** Optional and limited to one sentence. No D3 mention.

## Quick Tip lock

- **Locked topic:** Calendar collision from Mike consult 06-26—when two scheduled presets share the same TVs, the next preset wins. This describes today’s behavior only.
- Approved seed wording: “Don’t stack a drawing on a daypart without a plan.”
- Do not tease New LUCI lockout or Staging-Apply in this tip.
- **PIN demoted:** Admin PIN was previously gated as the Quick Tip candidate; it is no longer the Quick Tip and does not appear in the HTML status strip.

## What’s Coming lock

- **Locked feature:** Reporting & Analytics, framed as part of the new version / beta—never as already launched.
- Claims align to `luci-website/src/data/upgradeGuide.ts`: patterns across time, using incident volume/duration, command success/failure, latency, and preset activity across the last 24 hours, 7 days, or 30 days.
- Distinction retained: Live monitoring = now; Audit trails = who/what/when; Reporting & Analytics = patterns across time.
- Fan asset: `signal-05-reporting-analytics-fan.png`, referenced relatively from the HTML.
- Fan tabs: Overview, Commands, Automation, Reliability. “Realtime degraded” and “Establishing connection” were scrubbed. Systems and Device Incidents are intentionally omitted from the Signal visual and its claims.
- Preferred source screenshots: `richard-oct5-upgrade-followups/ui-screenshots/06-analytics-overview.png`, `05-analytics-commands.png`, `04-analytics-automation.png`, `03-analytics-reliability.png`.

## Brand and scope check

- `A/V` is spelled with the slash.
- Theme options stay inside the locked continuity/stabilizer idea; no second theme was introduced.
- Rejected title “One Thread from Plan to Floor” was not reused or closely paraphrased.
- Prohibited brand constructions were checked: no use of `layer`, `replaces`, or `property-by-property` in proposed customer-facing copy.
- `LUCI` is spelled correctly throughout.
- No Webflow, ActiveCampaign, Send, final Minute with Mike column, or newsletter production was completed.
