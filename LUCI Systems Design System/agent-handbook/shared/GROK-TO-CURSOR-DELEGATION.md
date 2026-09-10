# Grok Bot → Cursor delegation

**Added:** 10 September 2026  
**Applies to:** Chief of Staff, Website, Case Studies & Sales Proof, Editorial & Campaigns, Video  
**Purpose:** Grok picks the LLM and sends Jane’s job to Cursor on her Mac. Cursor does not choose GPT vs GLM vs Claude.

## The operating model

**Grok picks the model. Cursor runs it.** GPT, GLM, and Claude do the creative. Grok workstream bots traffic: sequence, Jane gates, observe/adjust, assign Jane’s edits.

Do **not** recap brand or voice in the brief. Cursor already has `.cursor/rules`.

The bridge is `luci-cursor` (`run-cursor-delegation.sh`). Jane-facing names: **GPT**, **GLM**, **Claude**. The script’s `--role` flag is only an internal preset for default model + boundary — not a Cursor UI role and not a Grok bot name.

## How context transfers

1. Handbook  
2. Work board  
3. Decision log  
4. Live repos + `.cursor/rules`  
5. This task’s brief (outcome, locks for *this* job, files — no brand lecture)

## Who traffics vs which model

| Work | Grok bot | Model to pick |
|---|---|---|
| Front door, sequence, board | Chief of Staff | GLM for status; otherwise pick as below |
| New site pages | Website | GPT copy · GLM layout/build · Claude only if thesis is new / GLM missed |
| Case studies / sales proof | Case Studies & Sales Proof | GPT spine · GLM template/build |
| Signal, email, social, AC | Editorial & Campaigns | GPT ideas/copy · GLM adapt/layout · queue AC after Jane |
| Trailers / series cuts | Video | GPT outline · GLM assembly · Jane for generation she owns |

Until the four workstream bots exist, **CoS traffics all of it**.

| Beat | Pick |
|---|---|
| Unlocked ideas / copy | GPT |
| Adapt template, layout, build, deploy, mechanical check | GLM |
| New visual thesis, or GLM already missed, or Jane-level taste review | Claude |

## How a project runs

Example — Signal (Editorial, or CoS until that bot exists):

1. Queue the issue.  
2. GLM adapts a locked case study into the template.  
3. GPT proposes the rest + features. **Jane picks.**  
4. GPT writes.  
5. GLM lays out. Grok may flag length, visuals, 5–6 count, theme, intro — then send GPT or GLM again.  
6. Jane reviews the packet.  
7. Webflow live, AC from last template, **queue** the list. Do not Send unless Jane says so.

Same shape everywhere: **ideas (GPT) → Jane → copy (GPT) → layout (GLM) → Jane.**

## Observe and adjust

Grok may notice structure and brief Cursor. Grok may not rewrite copy or restyle.

Length, visuals present, Signal 5–6, theme, intro length. Jane’s edit notes → the right model.

## Jane still owns

Idea lists, assembled packet, Webflow/AC preview, **Send**, public claims, house rules.

## After Jane approves

Build from the last template. Show Jane. Queue. Don’t send.

## If there is no playbook

Propose the beat list once. Wait for Jane. Then it is the playbook.
