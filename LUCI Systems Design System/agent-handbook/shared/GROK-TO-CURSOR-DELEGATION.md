# Grok Bot → Cursor delegation

**Added:** 10 September 2026  
**Applies to:** Cornelius (CoS), Weatherby (Website), Consuelo (Case Studies & Sales Proof), Ermintrude (Editorial & Campaigns), Vikram (Video), Svetlana (Social), Longinus (Librarian)  
**Purpose:** Grok picks the LLM and sends Jane’s job to Cursor on her Mac. Cursor does not choose GPT vs GLM vs Claude.

## The operating model

**Grok picks the model. Cursor runs it.** GPT, GLM, and Claude do the creative. Grok workstream bots traffic: sequence, Jane gates, observe/adjust, assign Jane’s edits.

Do **not** recap brand or voice in the brief. Cursor already has `.cursor/rules`.

The bridge is `luci-cursor` (`run-cursor-delegation.sh`). Jane-facing names: **GPT**, **GLM**, **Claude**. The script’s `--role` flag is only an internal preset for default model + boundary — not a Cursor UI role and not a Grok bot name.

## How context transfers

1. Handbook  
2. Work board (`CURRENT-WORK-BOARD.md` Active jobs — whoever Jane assigned)  
3. Decision log  
4. Live repos + `.cursor/rules`  
5. This task’s brief (outcome, locks for *this* job, files — no brand lecture)

## Who traffics vs which model

| Work | Grok bot | Model to pick |
|---|---|---|
| Front door, sequence, board | Cornelius (CoS) | GLM for status; otherwise pick as below |
| New site pages | Weatherby (Website) | GPT copy · GLM layout/build · Claude only if thesis is new / GLM missed |
| Case studies / sales proof | Consuelo (Case Studies & Sales Proof) | GPT spine · GLM template/build |
| Signal, email, AC | Ermintrude (Editorial & Campaigns) | GPT ideas/copy · GLM adapt/layout · queue AC after Jane |
| LinkedIn farm / mock-ups / captions | Svetlana (Social) | GPT ideas/captions · GLM art · Jane posts · idle until she says start |
| Trailers / series cuts | Vikram (Video) | GPT outline · GLM assembly · Jane for generation she owns |
| Where files/photos/diagrams live; handbook copy stale | Longinus (Librarian) | GLM search/audit · hand the owning stream |

All seven live chats exist. Do not hand work to Design Direction, Strategic Marketer, Maker, or Review.

| Beat | Pick |
|---|---|
| Unlocked ideas / copy | GPT |
| Adapt template, layout, build, deploy, mechanical check | GLM |
| New visual thesis, or GLM already missed, or Jane-level taste review | Claude |

## How a project runs

Example — Signal (Ermintrude; copy first, then she picks up):

1. Queue the issue.  
2. GLM adapts a locked case study into the template.  
3. GPT proposes the rest + features. **Jane picks.**  
4. GPT writes.  
5. GLM lays out. Grok may flag length, visuals, 5–6 count, theme, intro — then send GPT or GLM again.  
6. Jane reviews the packet.  
7. Webflow live, AC from last template, **queue** the list. Do not Send unless Jane says so.

Same shape everywhere: **ideas (GPT) → Jane → copy (GPT) → layout (GLM) → Jane.**

The owning Grok bot logs the job on `CURRENT-WORK-BOARD.md` (Active jobs) as soon as Jane assigns it. Cursor briefs include updating that row when stage/artifact changes. See `shared/WORK-BOARD-PROTOCOL.md`.

## Observe and adjust

Grok may notice structure and brief Cursor. Grok may not rewrite copy or restyle.

Length, visuals present, Signal 5–6, theme, intro length. Jane’s edit notes → the right model.

### Learned preferences in briefs (earn the right to anticipate)

All Grok bots are expected to learn from Jane’s edits, corrections, preferences, repeated requests, and the way she directs GPT / GLM / Claude over time. The goal is for bots to gradually take on more production-direction responsibility as they build a reliable history of what Jane repeatedly asks for — **without replacing her judgment with bot guesses**.

A bot may proactively add a preference to a Cursor brief **only** when it has enough prior Jane behavior to reasonably believe Jane is at least **~80% likely to ask for this change herself** in this situation. That judgment must be based on a real history of Jane making the same or closely related request in comparable work.

- **Do not** infer a preference from one correction, one conversation, or general creative assumptions.
- **Do not** generalize a repeated preference into unrelated contexts just because it worked elsewhere.
- **Context still matters.** A repeated preference is not automatically universal.

When a bot proactively applies a learned preference, it must tell Jane with a short note such as:

> “I added X to the Cursor brief because you’ve asked for that repeatedly in similar work.”

Jane then has the chance to confirm the preference or correct the bot if it was applied in the wrong context.

**When uncertain, ask Jane or leave the decision to her rather than guessing.**

### Preferences are not house rules

A one-off preference is **not** a house rule. A repeated preference is **not** automatically universal. Learned preferences may guide briefs without becoming formal house rules. **Only Jane can promote a preference into a universal rule** (see “make a rule / remember this” in `SHARED-OPERATING-PROTOCOL.md`).

## Jane still owns

Idea lists, assembled packet, Webflow/AC preview, **Send**, public claims, house rules.

## After Jane approves

Build from the last template. Show Jane. Queue. Don’t send.

## If there is no playbook

Propose the beat list once. Wait for Jane. Then it is the playbook.
