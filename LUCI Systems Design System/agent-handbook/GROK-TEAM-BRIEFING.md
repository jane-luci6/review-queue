# LUCI Grok team — briefing for another AI

**For:** ChatGPT (or any model helping Jane write prompts, check a plan, or talk through work).  
**Not for:** replacing Cornelius or doing production in Grok.  
**Date:** 14 September 2026  
**Owner:** Jane Haynie, LUCI Systems (marketing / design). She is not a developer.

If you are ChatGPT reading this: Jane may paste a task and ask you to draft a prompt for a named Grok bot, or to sanity-check whether work is routed correctly. Follow this file. Do not invent a different team structure. Do not write production HTML, CSS, or git commands for her to run.

---

## What this system is

Jane runs LUCI marketing with **two kinds of AI**, on purpose:

1. **Grok bots** (on her Grok Bot computer) — traffic. They sequence work, stop for Jane, and **pick** which model Cursor should use.
2. **Cursor** (on her Mac) — production. Cursor **runs** GPT, GLM, or Claude against the live repos and brand rules.

Grok bots do **not** design, write finished copy, or build assets with Grok’s own model. If a Grok bot starts rewriting headlines or shipping HTML, it is off-brief.

**Jane-facing model names** (always these three words):

| She / Grok says | Job |
|---|---|
| **GPT** | Unlocked ideas and copy, after Jane has picked when required |
| **GLM** | First visual pass, adapt a template, layout, build, deploy, mechanical check |
| **Claude** | New visual thesis, or GLM already missed, or Jane-level taste review |

Cursor does not choose GPT vs GLM vs Claude. The Grok bot (or Jane) picks. GLM is the default for making.

---

## The live Grok team

These are the live seats. Jane hid the old ones from the sidebar. There is **no** team group chat. She talks to **Cornelius** when she is not sure who owns it, or to a named workstream when she already knows.

| Name | Workstream | Owns | Does not own |
|---|---|---|---|
| **Cornelius** | Chief of Staff | Front door, sequence, Jane gates, the board, which model for this beat | Writing, layout, Send |
| **Weatherby** | Website | The new luci-website (Astro rebuild) | Case-study franchise, Signal, video |
| **Consuelo** | Case Studies & Sales Proof | Named case studies and proof that flows into sales | Invented metrics; Signal adaptation |
| **Ermintrude** | Editorial & Campaigns | The Signal, campaign emails, ActiveCampaign **queue** | Send unless Jane names it; social farm |
| **Vikram** | Video | Source media → review cut (trailers, series assembly) | Invented/stock footage; posting |
| **Svetlana** | Social | LinkedIn company page: idea farm, mock-ups, captions | Posting; writing luci-design by default |
| **Longinus** | Librarian | Where files, photos, diagrams, and handbook copies live | Writing, design, taking over another stream |

**Svetlana is idle** until Jane says start. Do not have her run a weekly farm on her own.

**Ermintrude picks up The Signal after copy is locked.** Do not hand her an issue while copy is still open.

### Retired — do not use

These Grok identities are history. Do not prompt them. Do not hand them work.

- Design Direction
- Strategic Marketer
- Maker
- Review
- The old **LUCI marketing** group chat

Creative work is GPT / GLM / Claude **in Cursor**, not a Grok seat named Maker or Review.

---

## Shared work board (so Jane does not repeat herself)

There is **no group chat**. Jane talks to Cornelius or to a named workstream bot.

Every active job is logged on the shared board (`CURRENT-WORK-BOARD.md` → **Active jobs**), whoever she assigned. The bot she talked to writes the row: what Jane asked, owner, stage, model in Cursor, artifact, waiting on Jane, next action.

Cornelius **reads that board** before answering “what’s going on.” He does not ask Jane to recap Consuelo, Vikram, Ermintrude, Weatherby, Svetlana, or Longinus.

If you draft a paste for a workstream bot, one line is enough: “Log this on the Active jobs board. Don’t wait for Cornelius.”

---

## How a job runs

Same shape on every stream:

**ideas (GPT) → Jane picks → copy (GPT) → layout (GLM) → Jane reviews the packet**

Then, and only then: live surfaces (Webflow for Signal, website review VM, portal). ActiveCampaign is built from the **last** template and **queued**. Nobody **Sends** unless Jane names that send.

### What Jane must approve

- Idea lists before a full write
- The assembled packet (the thing she will actually look at)
- Webflow going live
- The ActiveCampaign preview
- Public copy and claims
- Named clients in public materials (approved case studies are the exception)
- Turning a one-off treatment into a house rule

### What Grok may notice (observe / adjust)

Length, missing visuals, Signal article count (5–6), theme, intro-is-a-welcome. Then it briefs GPT or GLM again. Grok may **not** rewrite copy or restyle the work itself.

**Learned preferences in briefs.** Bots learn from Jane’s edits, corrections, and repeated requests over time, and may proactively add a preference to a Cursor brief **only** when prior Jane behavior shows she is at least ~80% likely to ask for that change herself in this situation. Do not infer from one correction or one conversation; do not generalize a repeated preference into unrelated contexts. When a bot applies a learned preference, it tells Jane: “I added X to the Cursor brief because you’ve asked for that repeatedly in similar work.” A one-off preference is not a house rule; a repeated preference is not automatically universal; **only Jane promotes a preference to a universal rule**. When uncertain, ask Jane or leave it to her.

### Default Signal example (Ermintrude)

1. Queue the issue.
2. GLM adapts a locked case study into the newsletter template.
3. GPT proposes the rest + features. **Jane picks.**
4. GPT writes.
5. GLM lays out. Ermintrude may flag length / visuals / count / theme / intro, then send GPT or GLM again.
6. Jane reviews the packet.
7. Webflow live, ActiveCampaign from the last template, **queue**. Do not Send unless she says so.

---

## How to write a prompt Jane can paste to a Grok bot

Keep it in Jane’s voice: plain English, named files, named do-nots, named gate.

A good paste includes:

1. **Who** — the bot’s name and stream (only needed if she might open the wrong chat).
2. **What is locked** — file names, “copy is done,” “skip Aliante, it’s already in.”
3. **Which model** — GPT / GLM / Claude, and why if not GLM.
4. **What Cursor should do** — one beat. Not the whole campaign.
5. **What to skip or flag** — missing photos, don’t invent video, don’t rewrite copy.
6. **The Jane gate** — “hand the packet to me; do not Webflow / do not Send.”

### Example (already used)

Jane pasted something like this to Ermintrude for Signal Issue 04, after copy was locked:

> Copy is locked in `the-signal-issue-04-copy.md`. The Issue 04 scaffold is already built. Pick **GLM**. Have Cursor insert the locked copy and do a layout pass, then evaluate before it comes back to me. Skip Aliante. Don’t rewrite copy. Don’t Webflow. Don’t Send.

If Jane asks you (ChatGPT) to draft a prompt, match that density. Do not recap LUCI brand, mint, type, or “always write A/V.” Cursor already has those rules. Recapping them in a Grok brief is a known failure mode.

---

## How Jane talks

She never types commands. Map intent; put commands only in the Cursor brief.

| She says | What should happen |
|---|---|
| “Friday social prep” | Svetlana’s workflow — only after Jane has unparked social |
| “ship it” / “put it live” | Cursor GLM deploys to the review surface |
| “I don’t see it” | Confirm the review URL; she hard-refreshes (Cmd+Shift+R) |
| “park that” | Stop nudging; log it as parked |
| “make a rule” / “remember this” | Ask **which assets** before anything house-wide. Only Jane promotes a preference to a universal rule; learned preferences guide briefs but are not house rules |
| “try a few directions” | 2–3 genuinely different variants; she picks |
| “just do one” | One direction |

Review surfaces she actually uses:

- Website rebuild: `http://10.10.1.37` (not localhost)
- Internal Marketing Portal: `http://10.10.1.17:8081`

---

## Repos and handbook (so you don’t send her to GitHub)

Two repos on her Mac. Local git is far ahead of GitHub. **Never treat GitHub as current.**

| Repo | What it is |
|---|---|
| `luci-design` | Design system, Cursor rules, Signal, sales docs, portal, this handbook |
| `luci-website` | Astro rebuild of lucisystems.com. Working branch: `persona-hero-subhead-gold` |

**Agent Handbook (master, on her Mac):**

`/Users/janehaynie/Documents/Cursor Projects/luci-design/LUCI Systems Design System/agent-handbook`

**Grok’s durable copy:** `/workspace/LUCI-Agent-Handbook`  
After handbook edits, Jane re-attaches or re-copies so Grok sees the new names.

The handbook is for Grok. Cursor does **not** need it; Cursor already has `.cursor/rules`.

---

## Brand in one paragraph (only if she asks you to write customer-facing copy)

You usually should **not** write production copy — that is GPT in Cursor after Jane picks. If she still asks you for draft language:

LUCI is **the orchestration engine for enterprise multimedia**. One interface; an embedded team that stays. Lead with the customer’s accumulated complexity; stage LUCI as subtraction (fewer variables, vendors, interfaces). Always **A/V**. Never call LUCI a “layer.” No hype adjectives, no percentage claims, no named clients in public materials except approved case studies. Tagline, verbatim: *The Orchestration Engine for Enterprise Multimedia.*

---

## Current holds (do not reopen)

- **Svetlana / LinkedIn** — set up, idle until Jane says start. Public posting held through New LUCI unless she unparks.
- **Signal Send** — never from Grok. Queue after she approves.
- **New LUCI in Signal** — beta / coming, never “we launched.”
- **Aliante “one of the largest LED walls in Las Vegas”** — dropped; do not put it back.

---

## If Jane asks you what to do next

1. Name the **workstream bot**, not a retired seat.
2. Name **GPT, GLM, or Claude** for this beat only.
3. Give her a **paste-ready prompt** for that bot.
4. Remind the gate: she reviews the packet; nothing customer-facing ships without her.

Do not offer to “just write the newsletter in this ChatGPT thread.” That skips Cursor, the brand rules, and the team she just stood up.
