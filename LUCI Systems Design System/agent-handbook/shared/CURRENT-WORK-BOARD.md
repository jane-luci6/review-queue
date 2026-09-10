# Current work board

**Board date:** 28 August 2026  
**Corrected by Jane:** 28 August 2026, afternoon PT  
**Primary source:** Jane this week, then `luci-design/COS-task-calendar.json`

Treat older briefs (`_project-context.md` 16 Jun, `CURSOR-MORNING-BRIEF.md` 8 Jul, `WIP-notes.md` June, website README “next phases”) as **history**, not this board.

---

## Waiting on people

| ID | Item | Waiting |
|---|---|---|
| launch-buckets | Launch campaign: confirm bucket view (what / for whom / when) | Jane |
| mike-features | Primary / secondary / IT feature list | Mike |
| yaamava-layout | Capabilities p8: variant B with three Design fixes | Jane |
| ac-nurture | Prospect tracks (plan exists, not built) | Jane to approve |
| aliante-trailer | Aliante project trailer review + property name | Jane |

---

## Projects (in flight / held)

| Project | Status | Next |
|---|---|---|
| New LUCI launch campaign | in_flight | Confirm buckets. Mike still on the feature list. What’s New one-pager next. Beta, property by property. **Not** a public splash. LinkedIn/social held until this launch. |
| Website rebuild (`luci-website`) | in_flight | Astro + Netlify. **Fall launch.** E-mesh already applied. Messaging/feature audit still open. Working branch `persona-hero-subhead-gold`. Review at `http://10.10.1.37`. |
| Sales docs | in_flight | Yaamava p8 variant B, three Design fixes waiting Jane. Budgetary template is established. E-mesh not on sales docs yet. |
| Customization Studio (standalone app, with Will) | in_flight | **Not IMP.** Jane is not building studio in the IMP anymore. |
| Case studies | in_flight | Yaamava featured. Ameristar and Tachi live. **Sam’s Town complete** (Jane 28 Aug). E-mesh already applied. |
| Customer journey emails | in_flight | Clearwater LUCI is Live sent 28 Aug. Jane will send Signal welcome next week, then drop the eight into 30/60/90 **by hand**. No ActiveCampaign writes without her yes. Tachi Email 10 on 25 Sep. |
| The Signal | in_flight | Start **1 Sep**. Send **15 Sep**. |
| Prospect nurture (ActiveCampaign) | in_flight | Two short tracks planned. **Not built.** Stay off Mark/Mike live deals. |
| Aliante project trailer | in_flight | Jane review + property name sign-off. |
| LinkedIn / social | held | Mike reviewed the strategy. **Hold until New LUCI product launch.** |
| Review hub `http://10.10.1.37:8080` | live surface | Still used for content reviews, downloads, and other things. Not parked. Customization Studio is leaving that IMP page. |

---

## Calendar (upcoming)

| Date | Type | Item |
|---|---|---|
| 1 Sep | newsletter | Start September Signal |
| ~next week | email | Clearwater — Signal welcome (Email 7), Jane sends manually |
| 15 Sep | newsletter | Send September Signal |
| 25 Sep | email | Tachi Palace — 90-day check-in |
| after Jane drops them in by hand | email | Clearwater — 30/60/90 |
| 1 Oct | newsletter | Start October Signal |
| 15 Oct | newsletter | Send October Signal |
| 16 Nov | milestone | Boyd Treasure Chest expansion (already on LUCI since March — not a new install) |

### September Signal candidate topics

Clearwater go-live; Yaamava case study; New LUCI as **beta framing only** (not a ship announcement); website coming this fall (already teased in Issue 03); Field Activation Guide; Minute with Mike.

---

## Closed or dropped (do not restart)

| Item | Note |
|---|---|
| PIN / zone-access screen recording post | Never shipped. Dropped 28 Aug. |
| Homepage ticker NFL names | Resolved: photo regenerated without the ticker. Do not retry blur/card-over. |
| Budgetary estimate template trim | Old. Template is established. |
| IMP FastAPI / TipTap rebuild | **Does not exist.** Only Customization Studio is being rebuilt, as a standalone app. |
| Client document library in IMP | That work is the standalone Customization Studio with Will. |
| E-mesh “still pending on website” | Wrong. E-mesh is on the website and case studies. |

---

## Standing rules (not projects)

- Never write that LUCI **replaces** other technology. It works with and absorbs it so you manage everything through one interface. Marketing typically does not name partners.
- E-mesh is the main design theme on website and case studies. Circuit texture only in select situations. Not yet on other marketing materials.
- Review hub stays for reviews/downloads. Studio is a separate app.
- No ActiveCampaign writes without Jane’s explicit yes on that action.
- Always **A/V**. Never call LUCI a “layer.” GitHub is stale. Grok facilitates; Cursor’s models decide.

---

## Launch / demand-gen guardrails (locked)

- Offer: platform + partnership. Control / Automate / Execute (Oversee sits under Control).
- New LUCI is **beta, property by property** — not a public splash. Do not date it as an August launch.
- Sit above endpoints. **Never “LUCI replaces.”** Typically do not name partners.
- Never name Hub, CoreX, the tunnel vendor, or correlation IDs.
- Feature list is not final until **Mike signs it**.
- Stay off live **Mark** (outbound) and **Mike** (demos, feature list, customization) conversations.
- No case study for this launch. No dedicated website release page — audit pages we have.
- Journey and Signal stay out of live sales conversations.

---

## Git / deploy reality (agents must know)

- **Do not clone GitHub and assume current work.** luci-design local `main` was far ahead of `origin/main`. luci-website working branch is `persona-hero-subhead-gold`.
- Website review: `http://10.10.1.37`.
- Review hub (content reviews / downloads): `http://10.10.1.37:8080`.
- Current IMP: `http://10.10.1.17:8081`. Customization Studio is moving off this to a standalone app.
- Public lucisystems.com cutover to the Astro site is **fall**; Webflow still used for Signal, FAG, some case-study embeds.
