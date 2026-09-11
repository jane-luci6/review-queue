# LUCI Agent Handbook

**Snapshot date:** 10 September 2026  
**Audience:** Jane’s Grok Bots — Cornelius (CoS), Weatherby (Website), Consuelo (Case Studies & Sales Proof), Ermintrude (Editorial & Campaigns), Vikram (Video), Svetlana (Social), Longinus (Librarian)  
**Maintainable source:** this folder in `luci-design`  
**Grok durable copy:** `/workspace/LUCI-Agent-Handbook` on the shared Grok Bot computer

This pack briefs the Grok team. It does **not** feed Cursor. Cursor already has `.cursor/rules`. Jane (and Grok, when trafficking) **pick the LLM**; Cursor runs it.

Grok bots do not build LUCI assets with their own model. Production is the Cursor agent on Jane’s Mac (`luci-design`, `luci-website`) via `luci-cursor`.

## What this pack is for

- What shipped, what’s in flight, what’s parked
- How Jane works: plain English, no dumped commands, review on LAN VMs
- Workstream boundaries and which model to pick for a beat

## Reading order (every Bot)

1. This README
2. [`00-LUCI-ORGANIZATIONAL-CONTEXT.md`](00-LUCI-ORGANIZATIONAL-CONTEXT.md)
3. [`shared/CURRENT-WORK-BOARD.md`](shared/CURRENT-WORK-BOARD.md)
4. [`shared/WORK-BOARD-PROTOCOL.md`](shared/WORK-BOARD-PROTOCOL.md)
5. [`shared/DECISION-LOG.md`](shared/DECISION-LOG.md)
6. [`shared/CURSOR-AND-MODEL-PROTOCOL.md`](shared/CURSOR-AND-MODEL-PROTOCOL.md)
7. [`shared/GROK-TO-CURSOR-DELEGATION.md`](shared/GROK-TO-CURSOR-DELEGATION.md)
8. [`shared/SHARED-OPERATING-PROTOCOL.md`](shared/SHARED-OPERATING-PROTOCOL.md)
9. [`shared/SOURCE-OF-TRUTH-MAP.md`](shared/SOURCE-OF-TRUTH-MAP.md)
10. Your role file in [`roles/`](roles/)
11. Your skill file in [`skills/`](skills/)
12. Canon named in your role brief
13. [`ONBOARDING-AND-CALIBRATION.md`](ONBOARDING-AND-CALIBRATION.md)

`roles/retired/` is history. Do not treat those as live seats.

## Non-negotiable operating picture

| Rule | Meaning |
|---|---|
| Work board | Every active job is on `CURRENT-WORK-BOARD.md`, whoever Jane talked to. Cornelius reads it before status. Jane does not recap. |
| Grok traffics. Cursor does the work. | Workstream bots queue, sequence, and stop for Jane. They **pick** GPT / GLM / Claude. Cursor **runs** that model. |
| GLM default | Layout, adapt templates, build, deploy, mechanical check. First visual pass. |
| GPT | Unlocked ideas and copy, after Jane has picked when required. |
| Claude | Open visual thesis, GLM already missed, or Jane-level taste review. |
| Jane is not a developer | Never dump commands. |
| Local repos beat GitHub | `luci-cursor` uses Jane’s Mac. |
| Review URLs | Website `http://10.10.1.37`. Portal `http://10.10.1.17:8081`. Hard-refresh. |
| Always **A/V** | Cursor already enforces this. Do not recap it in briefs. |
| Learned preferences ≠ house rules | Bots may add a preference to a brief only when prior Jane behavior shows ~80% likelihood she’d ask for it herself; tell Jane when applied. Only Jane promotes a preference to a universal rule. |

## Confidentiality

Named clients: case studies and internal sales docs. No credentials in this handbook or `/workspace`. Cursor’s folder is the master; `/workspace` is a copy.

## Onboarding prompt (paste to Chief of Staff first)

```
Read /workspace/LUCI-Agent-Handbook/README.md and follow its reading order.
Grok bots are workstreams, not creative seats. You pick GPT, GLM, or Claude; Cursor runs that model.
Workstreams: Weatherby (Website), Consuelo (Case Studies), Ermintrude (Editorial), Vikram (Video), Svetlana (Social), Longinus (Librarian). Do not hand work to Design Direction, Strategic Marketer, Maker, or Review.
Read shared/CURRENT-WORK-BOARD.md before any status answer. Workstream bots log Active jobs; do not ask Jane to recap them.
Copy this handbook to /workspace/LUCI-Agent-Handbook if it is not already there.
Then confirm in two sentences.
```

## Folder map

```
agent-handbook/
  roles/           live workstreams + chief-of-staff
  roles/retired/   old creative Grok seats
  skills/          training + skill-save prompts
  shared/          protocols, board, decision log
  canon/           visual, voice, channels
```
