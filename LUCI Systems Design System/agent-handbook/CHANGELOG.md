# Handbook changelog

## 2026-09-10 — v2

- Added direct local Grok Bot → Cursor delegation through the authenticated Cursor CLI; GitHub and visible Cursor chat windows are not required.
- Added `shared/GROK-TO-CURSOR-DELEGATION.md`: context-transfer layers, role boundaries, brief contract, safety gates, and evidence requirements.
- Added the `luci-cursor` runner with read-only-by-default behavior and role-based model routing.
- Updated all five role briefs and saved-skill prompts to delegate strategy, design, making, and review to the correct Cursor model.
- Current defaults: GLM 5.2 Max for implementation/mechanical QA; GPT-5.6 Sol High for unlocked copy/strategy; Claude Opus 5 Thinking Medium for open design/Jane-level review.
- **Design Direction starts on GLM** (Jane, 10 Sep). Role `design-direction` now defaults to GLM 5.2 Max; new role `design-direction-open` carries Claude Opus 5 Thinking Medium and is used only for open visual planning or when a GLM pass already ran and fell short.

## 2026-08-28 — v1

- Initial LUCI Agent Handbook for five Grok Bots.
- Organizational context, work board, source map, Cursor chat index.
- Shared operating protocol + Cursor/model protocol (Grok directs; Cursor executes; 85–90% GLM; ChatGPT copy/strategy gated; Claude design/review gated).
- Canon snapshots: visual, voice, production, channels.
- Role briefs + training playbooks + onboarding/calibration.
