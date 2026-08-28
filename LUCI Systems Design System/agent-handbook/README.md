# LUCI Agent Handbook

**Snapshot date:** 28 August 2026  
**Audience:** Jane’s five Grok Bots — Chief of Staff, Design Direction, Strategic Marketer, Review, Maker  
**Maintainable source:** this folder in `luci-design`  
**Grok durable copy:** `/workspace/LUCI-Agent-Handbook` on the shared Grok Bot computer

This pack is the shared briefing for the Grok team. It is **not** a license for Grok Bots to build LUCI assets on Grok’s cloud computer. Production happens in **Cursor**, on Jane’s machine, in `luci-design` and `luci-website`.

## What this pack is for

- Bring every Bot up to date on LUCI, what shipped, what is in flight, and what is parked.
- Teach how Jane works: plain English, no dumped commands, review on LAN VMs, GLM-first.
- Give each role authority boundaries, reading lists, Cursor briefs, and a training playbook.

## Reading order (every Bot)

1. This README
2. [`00-LUCI-ORGANIZATIONAL-CONTEXT.md`](00-LUCI-ORGANIZATIONAL-CONTEXT.md)
3. [`shared/CURRENT-WORK-BOARD.md`](shared/CURRENT-WORK-BOARD.md)
4. [`shared/CURSOR-AND-MODEL-PROTOCOL.md`](shared/CURSOR-AND-MODEL-PROTOCOL.md)
5. [`shared/SHARED-OPERATING-PROTOCOL.md`](shared/SHARED-OPERATING-PROTOCOL.md)
6. [`shared/SOURCE-OF-TRUTH-MAP.md`](shared/SOURCE-OF-TRUTH-MAP.md)
7. Your role file in [`roles/`](roles/)
8. Your skill file in [`skills/`](skills/)
9. Canon files named in your role brief
10. [`ONBOARDING-AND-CALIBRATION.md`](ONBOARDING-AND-CALIBRATION.md) — run the calibration for your role

## Non-negotiable operating picture

| Rule | Meaning |
|---|---|
| Grok directs. Cursor executes. | Do not ship HTML, CSS, diagrams, PDFs, or deploys from Grok. |
| GLM is the default Cursor model | **85–90%** of Cursor work. |
| ChatGPT / Claude are scarce | **10–15% combined.** ChatGPT = unlocked copy/strategy. Claude = open design direction or Jane-level review. |
| Jane is not a developer | Interpret plain English. Never ask her to run a command. |
| Local repos beat GitHub | GitHub remotes are far behind. Do not clone GitHub and assume it is current. |
| Review URLs, not localhost | Website: `http://10.10.1.37`. Portal: `http://10.10.1.17:8081`. Hard-refresh (Cmd+Shift+R). |
| Always **A/V** | Never “AV” or “A-V”. Never call LUCI a “layer”. |

## Confidentiality

- Named clients appear in **case studies** and internal sales docs. Public marketing stays discreet unless the client has approved the named asset.
- Do not put credentials, `.env`, SSH keys, or VPN passwords in this handbook or in `/workspace`.
- Do not treat Grok `/workspace` as the system of record. Copy durable updates back into this repo folder.

## Onboarding prompt (paste to Chief of Staff first)

```
Read /workspace/LUCI-Agent-Handbook/README.md and follow its reading order.
You orchestrate. You do not build LUCI assets on this computer.
Production is in Cursor on Jane’s Mac: luci-design and luci-website.
Default Cursor model is GLM (85–90%). ChatGPT and Claude together are 10–15%, gated.
Copy this handbook to /workspace/LUCI-Agent-Handbook if it is not already there.
Then give me a one-page status: in flight, waiting on Jane/Mike, parked, next action.
```

## Folder map

```
agent-handbook/
  README.md
  00-LUCI-ORGANIZATIONAL-CONTEXT.md
  ONBOARDING-AND-CALIBRATION.md
  CHANGELOG.md
  shared/     protocols, source map, chat index, work board
  canon/      visual, voice, production, channel playbooks
  roles/      one brief per Bot
  skills/     training playbooks + native Grok skill-save prompts
```
