# Current work board

**Board date:** 28 August 2026  
**Primary source:** `luci-design/COS-task-calendar.json` (updated 27 Aug 2026)  
**Git snapshot:** luci-design `main` @ `6c18687` (27 Aug); luci-website branch `persona-hero-subhead-gold` @ `324fdfe` (20 Aug). Uncommitted website: Tachi bingo-hall image + Sam’s Town section-variants preview.

Treat older briefs (`_project-context.md` 16 Jun, `CURSOR-MORNING-BRIEF.md` 8 Jul, `WIP-notes.md` June, website README “next phases”) as **history**, not this board.

---

## Waiting on people

| ID | Item | Waiting |
|---|---|---|
| launch-buckets | Launch campaign: confirm bucket view (what / for whom / when) | Jane |
| mike-features | Primary / secondary / IT feature list | Mike |
| yaamava-layout | Capabilities / retrofit: pick Yaamava layout variant | Jane |
| ac-nurture | ActiveCampaign prospect tracks (no-response + post-demo) | Jane to approve plan |
| aliante-trailer | Aliante project trailer review + property sign-off | Jane |
| linkedin | LinkedIn strategy copy pass | Mike |
| screen-rec | Screen recording recreation — contact pop on logo slide | Jane |

---

## Projects (in flight / waiting)

| Project | Status | Next |
|---|---|---|
| New LUCI launch campaign | in_flight | Confirm bucket view. Mike still on the feature list. What’s New one-pager next. **Not** an August public launch. Beta, property by property. No launch case study. Do not replace Q-SYS. |
| Website rebuild (`luci-website`) | in_flight | Astro + Netlify. **Fall launch.** Messaging/feature audit still needed. Working branch is `persona-hero-subhead-gold` (~472 commits ahead of GitHub `origin/main`). Review at `http://10.10.1.37`. |
| Sales docs + Customization Studio | in_flight | Pick Yaamava layout on capabilities / retrofit proposal. Portal: `http://10.10.1.17:8081`. |
| Case studies | in_flight | Yaamava is the new featured install. Ameristar and Tachi already live. Sam’s Town is the standing **visual template**; in stakeholder due-for-review (v2). |
| Customer journey emails | in_flight | **Clearwater “LUCI is Live” due 28 Aug** (Mitchell Wilson) — calendar still `done: false` as of 27 Aug snapshot. Tachi 60-day already sent (~22 Aug). |
| The Signal | in_flight | Start September **1 Sep**. Send **15 Sep**. |
| Prospect nurture (ActiveCampaign) | in_flight | Two short tracks planned. **Not built.** Stay off Mark/Mike live deals. |
| Aliante project trailer | in_flight | Jane review + property name sign-off. |
| LinkedIn strategy | waiting | Copy pass sitting with Mike. Jane may post without per-post Mike approval (production mode). |
| Screen recording recreation | waiting | Contact pop on the logo slide. |

---

## Calendar (upcoming)

| Date | Type | Item |
|---|---|---|
| 28 Aug 2026 | email | Clearwater River — Go live / LUCI is Live (stage 5) |
| 1 Sep | newsletter | Start September Signal |
| 4 Sep | email | Clearwater — Survey (stage 6) |
| 11 Sep | email | Clearwater — Signal welcome (stage 7) |
| 15 Sep | newsletter | Send September Signal |
| 25 Sep | email | Tachi Palace — 90-day check-in |
| 27 Sep | email | Clearwater — 30-day check-in |
| 1 Oct | newsletter | Start October Signal |
| 15 Oct | newsletter | Send October Signal |
| 27 Oct | email | Clearwater — 60-day check-in |
| 16 Nov | milestone | Boyd Treasure Chest expansion (already on LUCI since March — not a new install) |
| 26 Nov | email | Clearwater — 90-day check-in |

### September Signal candidate topics

Clearwater go-live; Yaamava case study; New LUCI as **beta framing only** (not a ship announcement); website coming this fall (already teased in Issue 03); Field Activation Guide; Minute with Mike.

---

## Parked — do not restart without Jane

| Item | Note |
|---|---|
| Old portal on `10.10.1.37:8080` | Superseded by `.17:8081`. Cleanup blocked on VPN + sudo. Script: `~/cleanup-luci-hub-37.sh`. |
| HomeIntro ticker NFL team names | Three approaches rejected (overlay, card-over, blur). Photo restored. **Do not retry blur or card-over.** Commit `a843a16` on website branch. |
| Vendor-reduction line vs Q-SYS | Parked 5 Aug. Do not imply we drop endpoint partners. Honesty Protocol: credit backends. |
| Budgetary estimate template trim | COS still says hold new client work until Jane confirms. Library notes a Jul 9 trim — **confirm with Jane** before treating as open. |
| E-mesh on the website | SVG done. CTA/footer apply still pending. |
| Client document library | Deferred. Mike still saves locally. |
| Portal long-term rebuild (FastAPI / TipTap) | Documented Jul 2026. **Not built.** Static portal remains production. |

---

## Launch / demand-gen guardrails (locked)

From `ui_kits/content-marketing/campaigns/luci-campaign-plan.md` (canonical plan; root `luci-campaign-plan.md` is a shorter duplicate):

- Offer: **platform + partnership**. Control / Automate / Execute (Oversee sits under Control).
- New LUCI is **beta, property by property** — not a public splash. Do not date it as an August launch.
- Sit **above** endpoints. Do **not** replace Q-SYS. Never name Hub, CoreX, the tunnel vendor, or correlation IDs.
- Feature list is not final until **Mike signs it**.
- Stay off live **Mark** (outbound) and **Mike** (demos, feature list, customization) conversations.
- No case study for this launch. No dedicated website release page — audit pages we have.
- Journey and Signal stay out of live sales conversations.

---

## Git / deploy reality (agents must know)

- **Do not clone GitHub and assume current work.** luci-design local `main` was **271 commits ahead** of `origin/main` as of this snapshot. luci-website GitHub `origin/main` still ~16 Jun; working branch is ~472 commits ahead.
- Website review: `http://10.10.1.37` via `./deploy.sh` in `luci-website`.
- Portal: `http://10.10.1.17:8081` via `npm run deploy:portal` from Design System folder.
- Public lucisystems.com cutover to the Astro site is **fall**; Webflow still used for Signal, FAG, some case-study embeds, landing-page handoff.
