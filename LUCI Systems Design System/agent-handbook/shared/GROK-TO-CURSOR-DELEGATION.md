# Grok Bot → Cursor delegation

**Added:** 10 September 2026  
**Applies to:** Chief of Staff, Design Direction, Strategic Marketer, Review, Maker  
**Purpose:** Let Grok direct the real Cursor agent on Jane’s Mac without GitHub or a visible Cursor chat window.

## The operating model

Grok remains the persistent teammate: it remembers the job, gathers inputs, decides which specialist owns the gap, and writes the brief.

Cursor remains the production environment: it reads the live local repo, follows `.cursor/rules`, uses the selected model, edits or reviews files, verifies the result, and commits coherent work.

The bridge is Cursor’s local CLI, invoked through:

`LUCI Systems Design System/scripts/run-cursor-delegation.sh`

The script is also available to local-computer tools as `luci-cursor`.

No GitHub, Vercel, Netlify, or Cloud Agent is involved. No Cursor chat window needs to open. Cursor’s result returns to the calling Bot in the local task output, and all delegated-run logs are stored under `~/.cursor/grok-delegations/`.

## How context transfers

Do **not** transfer months of raw chat transcripts. Cursor gets four layers of context:

1. **Stable institutional context** — this handbook.
2. **Current operating state** — `shared/CURRENT-WORK-BOARD.md`.
3. **Live production law** — the repo’s `.cursor/rules`, source files, SKILL files, and git history.
4. **This task only** — a complete Cursor brief written by the owning Bot.

If a prior Cursor decision matters and is not distilled into the handbook or a rule, the brief must cite the relevant file or named chat from `shared/CURSOR-CHAT-INDEX.md`. Do not paste a whole transcript.

## Role and model routing

These are the current defaults. Jane may override a model for a specific job.

| Gap | Owning Bot | Cursor role | Default model | Cursor’s job |
|---|---|---|---|---|
| Routing, status, sequencing | Chief of Staff | `chief-of-staff` | GLM 5.2 High | Analyze and produce the handoff; usually read-only |
| New marketing argument or unlocked customer-facing copy | Strategic Marketer | `strategic-marketer` | GPT-5.6 Sol High | One strategy/copy pass; produce a lock |
| Visual direction inside the existing locked system | Design Direction | `design-direction` | GLM 5.2 Max | First pass on every visual job; produce a lock |
| Open visual planning, a new thesis, or a GLM pass that fell short | Design Direction | `design-direction-open` | Claude Opus 5 Thinking Medium | Escalation only; produce a lock |
| Faithful implementation after locks | Maker | `maker` | GLM 5.2 Max | Edit, verify, deploy if authorized, commit |
| Links, contrast, spelling, fit, deploy, file QA | Review | `review-mechanical` | GLM 5.2 Max | Diagnose only |
| Jane-level voice, hierarchy, layout, brand taste | Review | `review-taste` | Claude Opus 5 Thinking Medium | Diagnose only |

Exact CLI model IDs live in the delegation script. The Bot names the role; it does not need to memorize model IDs. Jane can explicitly override the model when she wants a different one.

## Division of labor

### Chief of Staff

- Own the complete loop and the work board.
- Decide whether the request needs Strategy, Design, Maker, Review, or Jane.
- Send **one role at a time** unless independent work genuinely benefits from parallel runs.
- Do not ask Cursor to both invent the direction and implement it in one pass.
- Give Jane a plain-language status; never expose shell syntax.

### Strategic Marketer

- Use Cursor read-only first when the argument, channel, claims, or copy thesis is open.
- Return locked message/copy to Chief of Staff.
- Do not ask Cursor to implement the page.

### Design Direction

- **Start on GLM.** Every visual job opens with a read-only `design-direction` pass. Most direction work is applying the locked LUCI visual system, which GLM does well.
- **Escalate to `design-direction-open` (Claude Opus 5) in two cases only:** the job genuinely needs open visual planning or a new thesis, or a GLM pass has already run and did not get there. Name which case in the brief.
- Do not open with Claude because a job “feels designy.” Jane's default is GLM first.
- Return named visual axes and precise constraints either way.
- If Jane requests options, the direction pass defines them; Maker builds them on branches.
- Do not ask Claude to “just finish the CSS.”

### Maker

- Accept only briefs with locked copy and locked visual direction.
- Use execute mode.
- Stop and return the gap if the brief requires taste or strategy invention.
- Deploy only when explicitly included in definition of done.

### Review

- Run after Maker.
- Mechanical and taste review are separate jobs with separate model defaults.
- Return `PASS`, `REVISE`, or `ESCALATE` with severity, evidence, and required fixes.
- Never fix the artifact directly. Chief of Staff turns findings into a Maker revision brief.

## Safety and authority

- The script defaults to **read-only plan mode**.
- File editing happens only when the Bot deliberately selects execute mode.
- Execute mode grants Cursor tool permission because the run is headless. The repo’s rules, git status, and local commit history are therefore the safety system.
- Cursor must preserve unrelated work, make the smallest coherent change, and commit in logical chunks.
- Public sends, destructive cleanup, purchases, legal acceptance, named-client claims outside approved case studies, and rule-scope changes still require Jane.
- A bot may never bypass a locked-page or canonical-asset question by phrasing it as implementation.

## Brief requirements

Every delegation includes:

- Repo: `design`, `website`, or `both`
- Outcome Jane will see
- Review surface
- Audience and channel
- Locked copy / visual direction / claims
- Open questions (read-only specialist pass only)
- Exact files or best-known paths
- Out of scope
- Definition of done
- Human approval gates
- Whether Cursor may edit or must remain read-only

Missing brief fields are a stop condition. Maker must not fill them with plausible LUCI language.

## What Jane experiences

Jane speaks normally to a Bot. The Bot should answer with:

1. who owns the next step;
2. which Cursor model it is assigning and why;
3. whether the run is planning/review or editing;
4. when Cursor is finished, what changed and where Jane reviews it.

Jane should not receive CLI commands, repo paths to type, or model IDs to remember.

## First test

Use a harmless read-only task:

> Ask Cursor to inspect the current work board and tell you the highest-priority item waiting on Jane. Do not edit anything.

Then use a narrow execute task on an already snapshotted file. Confirm the Bot returns Cursor’s actual changed paths and commit, rather than claiming it “used Cursor” without evidence.
