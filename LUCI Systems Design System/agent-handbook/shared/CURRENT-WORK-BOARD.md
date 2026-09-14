# Current work board

**Board date:** 10 September 2026  
**Sources:** CoS live calendar (10 Sep morning), `DECISION-LOG.md`, `the-signal-issue-04-choices.md`, `COS-task-calendar.json`.  
**If a line is wrong, Jane corrects it.** The 28 Aug board is history.

Treat older briefs (`_project-context.md`, `CURSOR-MORNING-BRIEF.md`, `WIP-notes.md`, website README “next phases”) as **history**, not this board.

**Grok seats (live):** Cornelius (CoS) · Weatherby (Website) · Consuelo (Case Studies & Sales Proof) · Ermintrude (Editorial & Campaigns) · Vikram (Video) · Svetlana (Social) · Longinus (Librarian). Svetlana is idle until Jane says start.

**Board rule:** every active job is logged below, whoever Jane talked to. Protocol: `shared/WORK-BOARD-PROTOCOL.md`. Cornelius reads this file before status answers. Jane does not brief him on work already assigned to another bot.

---

## Active jobs

Workstream bots update this table when Jane assigns them work. Cornelius does not wait to be told.

| ID | Jane asked | Owner | Stage | Model | Artifact | Waiting on Jane | Next |
|---|---|---|---|---|---|---|---|
| signal-04-ac-draft | Design/create Issue 04 email in ActiveCampaign from last template with placeholders (Webflow not ready). No Send. Jane finalizing copy today; send Tue Sep 15. | Ermintrude | GLM teaser HTML built from Issue 03 template; Mike card placeholder | GLM | `ui_kits/email/email-signal-issue-04-teaser.html` + `-notes.md` | Jane review AC draft | Ermintrude paste/create AC campaign draft; no Send |
| aliante-rc2-finish | Finish Aliante video today — Jane watch/approve RC2; polish vs Mike-ready. | Vikram | Jane review / finish | none | assembly/aliante-led-rough-cut-2.mp4 | Jane finish call | Vikram ready for polish notes; no invent; no post |
| aliante-edit-blueprint | Diagnose RC2 story gaps; write scene-by-scene editorial blueprint before RC3. GPT only. No RC3, no Vikram yet. | Consuelo | Parked — Jane said come back later | GPT | `video-production/projects/aliante-led/editorial/aliante-edit-blueprint-v1.md` | Jane returns to lock structure | Hold; no RC3 / no Vikram until Jane reopens |
| aliante-imovie-handoff-rc2 | iMovie handoff folder reproducing RC2 as editable pieces (timeline 40 clips + titles.md verbatim + alternates + RC2 reference). No RC3, no shot swaps, no timing changes. | Vikram | Jane ready — package complete | GLM | `video-production/projects/aliante-led/assembly/imovie-handoff-rc2/` | Jane | Jane opens in iMovie; decides next (edit / RC3 / park) |
| signal-04-layout | GLM applying copy-r3 + Opus Project Update ledger into HTML. | Ermintrude | GLM layout r3 | GLM | lock 6c6f5f7 + copy f73725f | Jane review on 127.0.0.1:8765 | GLM running in Terminal |

---

## Waiting on people

| ID | Item | Waiting |
|---|---|---|
| signal-04-open | Signal Issue 04: Theme; Welcome names | Jane, then Mike letter review |
| aliante-cs | Aliante **written** case study, second pass | Jane |
| aliante-rc2 | Aliante trailer RC2 (~2:29) — CoS marked review PASS; Jane still to watch / property-name if needed | Jane |
| wave-1 | Website Wave 1 drafts in `REVIEW.html` | Jane read |
| launch-remaining | New LUCI: sign-in/session placement, proof pull, email bodies, sales deck/Capabilities, AC Deals, Nick Cloudflare/GA; demo webinar date | Jane / Mike / Nick |
| tactics | Four 2026 tactics — Jane’s picks | Jane |
| four-winds | Deposit confirm before Customer Journey write | Jane |
| clearwater-306090 | Add Clearwater 30/60/90 in ActiveCampaign | Jane’s **yes** on that write |
| yaamava-p8 | Capabilities p8 variant B — last noted 28 Aug; **confirm if still open** | Jane |

---

## Projects (in flight / held)

| Project | Status | Next |
|---|---|---|
| The Signal Issue 04 | in_flight | **Send Tue 15 Sep.** Locked: Field (short Aliante + link), Quick Tip (endpoint names/notes), What’s coming (panels + activity record), Mike (“Standardize the operation, not the hardware”), Since the last Signal (Clearwater, Sam’s Town, Osage, California), FAG. Extra visual parked. Welcome idea locked, **names open**. Still open: Theme. GPT copy → GLM into the Issue 04 template. **Ermintrude picks up after copy is finalized.** Stop before Webflow/AC until Jane approves. |
| New LUCI launch | in_flight | Mark/Mike lock-in done (CoS). Theme + Operate / Make it yours / See and prove live on IMP `.17`. Remaining: table above. Beta, property by property. **Not** a public splash. |
| Website rebuild | in_flight | Fall launch. Wave 1 drafts waiting Jane. Working branch `persona-hero-subhead-gold`. Review `http://10.10.1.37`. Aliante “largest in Las Vegas” held until the live page drops that line (calendar). |
| Case studies | in_flight | **Open: Aliante written study.** Ameristar, Tachi, Sam’s Town live. Yaamava is the **featured install on the site** — not the current “what’s next” case-study write. No New LUCI launch case study. |
| Aliante trailer | in_flight | RC2 ~2:29; CoS review PASS. Jane watch. Vikram (Video). |
| Sales docs | in_flight | Launch deck/Capabilities still in the remaining launch list. Yaamava p8: confirm with Jane. Budgetary template established. |
| Customization Studio | in_flight | Standalone with Will. **Not IMP.** |
| Customer journey | in_flight | Clearwater go-live sent 28 Aug. 30/60/90 still Jane-by-hand / Jane-yes in AC. Tachi Email 10 on **25 Sep**. Four Winds: wait on deposit. |
| Prospect nurture (AC) | in_flight | Architecture on IMP. **Not built in AC.** Stay off live Mark/Mike deals. |
| 2026 tactics | in_flight | Four tactics waiting Jane’s picks (calendar). |
| LinkedIn / social | held | Svetlana exists; **idle until Jane says start.** Process is OneDrive `Social Media/` (`WORKFLOW.md`). Hold public posting through New LUCI unless she unparks. |
| Review hub `http://10.10.1.37:8080` | live surface | Reviews/downloads. Studio is leaving that IMP page. |

---

## Calendar (upcoming)

| Date | Type | Item |
|---|---|---|
| 10 Sep | newsletter | Mike Signal 04 letter review (after Jane locks open sections) |
| 15 Sep | newsletter | **Send** Signal Issue 04 |
| 25 Sep | email | Tachi Palace — 90-day check-in |
| after Jane’s yes | email | Clearwater — 30/60/90 in AC |
| 1 Oct | newsletter | Start October Signal |
| 15 Oct | newsletter | Send October Signal |
| 16 Nov | milestone | Boyd Treasure Chest expansion (on LUCI since March — not a new install) |

---

## Closed or dropped (do not restart)

| Item | Note |
|---|---|
| PIN / zone-access screen recording post | Never shipped. Dropped 28 Aug. |
| Homepage ticker NFL names | Do not retry blur/card-over (parked follow-up in Cursor rules). |
| Budgetary estimate template trim | Template is established. |
| IMP FastAPI / TipTap rebuild | **Does not exist.** Studio is a standalone app. |
| E-mesh “still pending on website” | Wrong. E-mesh is on the website and case studies. |

---

## Standing rules (not projects)

- Never write that LUCI **replaces** other technology.
- E-mesh is the main design theme on website and case studies. Circuit only in select situations.
- Review hub stays for reviews/downloads. Studio is a separate app.
- ActiveCampaign: Jane’s **yes** before a write. After she approves a packet, Grok may build from the **last template** and **queue** the list. Do not **Send** unless she names that send.
- Always **A/V**. Never call LUCI a “layer.” GitHub is stale. Grok picks GPT/GLM/Claude; Cursor runs it.
- Work board vs CoS calendar: **this file** is what new bots should read. Workstream bots log **Active jobs** when Jane assigns them work. CoS reads the board before status; refreshes the rest when the week changes. See `shared/WORK-BOARD-PROTOCOL.md`.

---

## Launch / demand-gen guardrails (locked)

- Offer: platform + partnership. Control / Automate / Execute (Oversee sits under Control).
- New LUCI is **beta, property by property** — not a public splash.
- Sit above endpoints. **Never “LUCI replaces.”** Typically do not name partners.
- Never name Hub, CoreX, the tunnel vendor, or correlation IDs.
- Feature list is not final until **Mike signs it**.
- Stay off live **Mark** and **Mike** deal conversations.
- No case study for this launch. No dedicated website release page — audit pages we have.
- Journey and Signal stay out of live sales conversations.

---

## Git / deploy reality

- **Do not clone GitHub and assume current work.** luci-website working branch: `persona-hero-subhead-gold`.
- Website review: `http://10.10.1.37`.
- Review hub: `http://10.10.1.37:8080`.
- Current IMP: `http://10.10.1.17:8081`.
- Public lucisystems.com cutover to Astro is **fall**; Webflow still used for Signal, FAG, some case-study embeds.
