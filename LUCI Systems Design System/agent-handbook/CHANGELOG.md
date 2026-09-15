# Handbook changelog

## 2026-09-15 — v5

- **Signal publish playbook corrected for Webflow API reality** (Jane, 15 Sep). On this (non-Enterprise) Webflow site, Cursor cannot add HTML via the API and there is no Publish API. The playbook now splits Webflow work by lane: Cursor hosts assets + wires URLs + preps the final HTML + briefs the bots with exact page IDs/field names; Grok bots (Ermintrude/Weatherby) paste the HTML into the Webflow Designer; Jane does the final Publish click. ActiveCampaign stays a bot task (Cursor has no AC access; Cursor still hands the canonical link list). Three-surface rule and Issue 04 failure lessons (wrong-page paste, Designer clobber, bad Aliante case-study URL) preserved. Updated `shared/SIGNAL-PUBLISH-PLAYBOOK.md` (§1, §2 ownership table, §5 sequence, §6 clobber rule, §10 handoff), and matching lines in `roles/chief-of-staff.md` and `canon/channel-playbooks.md`.

## 2026-09-14 — v4

- **Hortensia not stood up** (Jane, 14 Sep). Cursor already runs mechanical QA (GLM) and Jane-level taste review (Claude). A Headmistress Grok seat would duplicate that. Draft `roles/headmistress.md` and `skills/headmistress-skill.md` removed.

## 2026-09-11 — v3

- **Learned preferences rule added** (Jane, 11 Sep). Grok bots may proactively add a preference to a Cursor brief only when prior Jane behavior shows she is at least ~80% likely to ask for that change herself in this situation. The bot tells Jane when it applies one (“I added X to the Cursor brief because you’ve asked for that repeatedly in similar work”). A one-off preference is not a house rule; a repeated preference is not automatically universal; only Jane promotes a preference to a universal rule. Added to `shared/GROK-TO-CURSOR-DELEGATION.md` (new “Learned preferences in briefs” + “Preferences are not house rules” subsections under Observe and adjust), `GROK-TEAM-BRIEFING.md` (observe/adjust + How Jane talks), `shared/SHARED-OPERATING-PROTOCOL.md` (How Jane talks), `00-LUCI-ORGANIZATIONAL-CONTEXT.md` (How Jane works with agents), and one row in the README non-negotiable table.

## 2026-09-10 — v2

- **Librarian renamed Longinus** (Jane, 10 Sep). Was Archimedes.
- **Archimedes (Librarian) stood up** (Jane, 10 Sep). Where-things-live utility. Does not write or design.
- **Active jobs on the shared board** (Jane, 10 Sep). Workstream bots log every assignment on `CURRENT-WORK-BOARD.md`. Cornelius reads the board before status. Protocol: `shared/WORK-BOARD-PROTOCOL.md`.
- **Website renamed Weatherby** (Jane, 10 Sep). Was Winston.
- **Live Grok names locked** (Jane, 10 Sep). Cornelius, Winston, Consuelo, Ermintrude, Vikram, Svetlana.
- **Social bot set up, idle** (Jane, 10 Sep). OneDrive Social Media workflow. Not the archived Next.js app.
- **Video bot named Vikram** (Jane, 10 Sep). Source media → review cut. Does not post.
- Added direct local Grok Bot → Cursor delegation through the authenticated Cursor CLI; GitHub and visible Cursor chat windows are not required.
- Added `shared/GROK-TO-CURSOR-DELEGATION.md`: context-transfer layers, role boundaries, brief contract, safety gates, and evidence requirements.
- Added the `luci-cursor` runner with read-only-by-default behavior and role-based model routing.
- Updated all five role briefs and saved-skill prompts to delegate strategy, design, making, and review to the correct Cursor model.
- Current defaults: GLM 5.2 Max for implementation/mechanical QA; GPT-5.6 Sol High for unlocked copy/strategy; Claude Opus 5 Thinking Medium for open design/Jane-level review.
- **Design Direction starts on GLM** (Jane, 10 Sep). Role `design-direction` now defaults to GLM 5.2 Max; new role `design-direction-open` carries Claude Opus 5 Thinking Medium and is used only for open visual planning or when a GLM pass already ran and fell short.
- **Grok workstreams** (Jane, 10 Sep). CoS + Website + Case Studies & Sales Proof + Editorial & Campaigns + Video. Grok picks the LLM; Cursor runs it. Creative Grok seats retired.
- **Grok facilitates; Cursor decides** (Jane, 10 Sep). Bots write briefs, ask Jane questions, and follow GLM / Claude / ChatGPT unless the result is clearly way off plan. They do not second-guess specialist or Maker passes as a matter of taste.
- **Decision log** (Jane, 10 Sep). Cursor appends a short lock summary to `shared/DECISION-LOG.md` at real decision points so CoS can see what happened without reading chats. Not a dump of every tweak.
- **Brand lines stay in Cursor, not in Grok briefs** (Jane, 10 Sep). Do not recap mint/type/A/V/voice for Cursor. Cursor already has the rules. Grok does not “fix” visual or voice.

## 2026-08-28 — v1

- Initial LUCI Agent Handbook for five Grok Bots.
- Organizational context, work board, source map, Cursor chat index.
- Shared operating protocol + Cursor/model protocol (Grok directs; Cursor executes; 85–90% GLM; ChatGPT copy/strategy gated; Claude design/review gated).
- Canon snapshots: visual, voice, production, channels.
- Role briefs + training playbooks + onboarding/calibration.
