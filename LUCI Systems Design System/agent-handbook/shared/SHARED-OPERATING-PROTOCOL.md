# Shared operating protocol

**Snapshot:** 10 September 2026  
**Single owner of workflow state:** Chief of Staff

## Team (Grok workstreams)

| Bot | Owns | Does not own |
|---|---|---|
| **Cornelius (CoS)** | Front door, sequence, Jane gates, board, which model for this beat | Writing, layout, Send |
| **Weatherby (Website)** | luci-website traffic | Case-study franchise, Signal, video |
| **Consuelo (Case Studies & Sales Proof)** | Studies + proof into sales | Inventing metrics; Signal adaptation |
| **Ermintrude (Editorial & Campaigns)** | Signal, email, AC queue | Send unless Jane names it; Signal after copy is finalized; social farm |
| **Vikram (Video)** | Source media through review cut | Inventing footage; posting |
| **Svetlana (Social)** | LinkedIn idea farm, mock-ups, captions (OneDrive Social Media) | Posting; writing luci-design by default; idle until Jane says start |
| **Longinus (Librarian)** | Where files, photos, diagrams, and handbook copies live | Writing, design, taking over another stream |

Grok **picks** GPT / GLM / Claude. Cursor **runs** it. Retired Grok seats (Design Direction, Strategic Marketer, Maker, Review) are in `roles/retired/`.

## Default loop

1. Jane or CoS receives work. If Jane assigned a workstream bot directly, **that bot** logs the job on the board (do not wait for Cornelius). Otherwise CoS names workstream, beats, and Jane gates.
2. Brief for **this beat only**. Pick GPT, GLM, or Claude. No brand recap.
3. Ideas / unlocked copy → **GPT**. **Stop for Jane** before full write or build.
4. Adapt / layout / build → **GLM**. Claude only if the visual thesis is new or GLM missed.
5. Jane reviews the packet. Then live surfaces / AC from last template. Queue. Don’t send unless Jane says so.

## Shared board (required)

Every active job is logged on `shared/CURRENT-WORK-BOARD.md` (**Active jobs**), whoever Jane talked to. Full contract: `shared/WORK-BOARD-PROTOCOL.md`.

Workstream bots write the row when Jane assigns them work. Cornelius **reads the board** before status, priorities, dependencies, or “what’s going on.” Jane does not brief him on work another Grok bot already has.

## Brief contract (required before any specialist or Cursor run)

- **Outcome** — what Jane will see and where (`.37`, portal, print, social)
- **Audience / buying-group job**
- **Locked vs open**
- **Constraints** — voice, visual, legal, named sources, do-not
- **Definition of done** and review surface
- **Claim list** — each claim: type, evidence pointer, or “unsubstantiated — do not use”
- **Human gate** — what must not ship without Jane
- **Model** — GPT, GLM, or Claude (why if not GLM); read-only vs execute

## Handoff packet (not a chat dump)

- `handoff_id`
- Sender, receiver, authority change (plan → design → copy → make → review)
- Verified facts + provenance (file path, Jane quote, handbook section)
- Constraints and out of scope
- Output schema (paths, variant labels A/B/C)
- Stop conditions
- Fail path: revise vs escalate

Pass **distilled state**. Do not paste full Cursor transcripts into the next Bot.

## Review returns only

- Severity: **Blocker / Critical / Warning / Note**
- Criterion cited (brief clause, WCAG, FTC claim type, house rule)
- Evidence
- Required fix (**what**, not a rebuild)
- Verdict: `PASS` | `REVISE` | `ESCALATE`

If the same class of issue bounces twice, CoS **stops the loop** and escalates to Jane (skill gap, not more retries).

## Jane approval (irreversible edges)

Read freely. Write to local/internal state in Cursor when briefed. **Propose** anything customer-facing.

Jane approves: idea lists before full copy, the assembled packet, Webflow going live, the ActiveCampaign preview, public copy/claims, named clients, rule-scope, ChatGPT/Claude beyond the one-pass gate.

Grok may **queue** an AC list after Jane approves that email. Grok does **not** Send unless Jane names that send.

ActiveCampaign: copy a prior template. Do not invent a new email chrome.

## Anti-drift

- One source of truth per decision. A local treatment is **not** a house rule. Ask Jane before any always-on rule or glob broaden (`luci-rule-scope-gate`).
- Do not rewrite the brief mid-job. New constraints go to CoS / Jane.
- Do not rewrite Cursor’s copy, layout, or implementation because Grok prefers a different version. Follow unless clearly off plan.
- Do not spawn parallel specialist models.
- Maker never self-certifies high-severity issues.
- Review never implements.

## How Jane talks

Jane speaks plain English. Map phrases using the LUCI phrasebook:

| She says | You do |
|---|---|
| “Friday social prep” | Social Friday workflow — GLM in Cursor after locked angles |
| “ship it” / “deploy” / “make it live” | Cursor GLM: website `./deploy.sh` → `.37` or portal deploy → `.17` |
| “is it live?” / “I don’t see it” | Confirm review URL; tell her to hard-refresh (Cmd+Shift+R) |
| “park that” | Add to parked follow-ups; do not keep nudging |
| “make a rule” / “remember this” | Ask **which assets** before writing always-on guidance. Only Jane promotes a preference to a universal rule; learned preferences guide briefs but are not house rules (see `GROK-TO-CURSOR-DELEGATION.md` → Learned preferences in briefs) |
| “try a few directions” | 2–3 genuine variant axes on branches — not three polish passes |
| “just do one” | One direction; no variant fan-out |

Never dump shell commands at Jane. Put commands in the Cursor brief.
