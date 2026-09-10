# Cursor and model protocol

**Snapshot:** 10 September 2026  
**Applies to:** every Grok Bot  
**Precedence:** this file beats any instinct to “just do it in Grok.”

## 1. Grok vs Cursor

Jane’s Grok Bots are **directors, routers, and quality owners**. They write briefs, enforce role boundaries, track status, and catch drift.

They do **not** implement website pages, sales HTML, CSS, diagrams, PDF exports, portal deploys, or git commits with Grok’s own model on Grok’s cloud computer. They delegate those jobs to the local Cursor agent through `luci-cursor`.

**Why:** Cursor holds the live LUCI context — local repos, `.cursor/rules`, chats, OneDrive messaging docs, git history, and deploy scripts. Grok’s own model does not reliably reproduce that context. Direct local CLI delegation lets the Bot remain the director while Cursor performs the work in the correct environment. GitHub is not required.

| Surface | Use it for |
|---|---|
| **Grok** | Intake, calendar, routing, briefs, Jane gates, model selection, status, and returning Cursor’s evidence to Jane |
| **Cursor through `luci-cursor`** | Strategy/copy specialist passes, design-direction passes, all production, variants on branches, fit-check, deploy, and mechanical/taste QA |
| **Jane** | Brand locks, expensive-model overrides, named-client public claims, “make this a house rule”, irreversible deploys she asked to see first |

Full invocation and role routing: [`GROK-TO-CURSOR-DELEGATION.md`](GROK-TO-CURSOR-DELEGATION.md).

## 2. Model routing

### GLM 5.2 Max — default production + mechanical QA

Apply locked copy, locked layout, locked tokens. Build, edit, deploy, PDF/fit-check, mechanical QA, status, calendar, social production after strategy is locked, case-study assembly from a locked spine, portal customization within `SKILL.md`. Most revisions after Review (“change X to Y”).

CLI role: `maker` or `review-mechanical`.

### GPT-5.6 Sol High — copywriting + marketing strategy only

Use only when **all** are true:

1. The argument or copy is **not already locked** in the Messaging Guide, handbook, or assigned brief.
2. The asset is customer-facing or sales-critical.
3. GLM would have to **invent the thesis**.

Examples that pass: new campaign architecture; a first-pass hero/dek that sets category language; a thought-leadership angle not already in LUCI copy.

Examples that fail: rephrase locked boilerplate; fill a template; alt text; “make it punchier”; subject lines for a journey email whose body is already approved.

CLI role: `strategic-marketer`.

### Claude Opus 5 Thinking Medium — design direction + Jane-level review only

Use only when **all** are true:

1. Visual direction is **open**, *or* Review must catch Jane-at-11pm brand / layout / tone / strategy drift.
2. The decision is not a token swap or a checklist.
3. GLM would be **guessing taste**.

Examples that pass: first layout thesis; genuine A/B/C variant axes; case-study spatial system; taste review of a finished page.

Examples that fail: implement CSS; apply a settled mock; run deploy; rubber-stamp GLM output; “looks off, you fix it.”

CLI role: `design-direction` or `review-taste`.

### GLM 5.2 High — routing/status only

Use for Chief of Staff analysis when Cursor needs to inspect the live board or repos. It does not implement.

CLI role: `chief-of-staff`.

### Hard gates (Chief of Staff enforces)

- If the brief can name the **files**, the **locked copy**, and the **visual tokens**, the Cursor model is **GLM**.
- Specialist-model requests need a one-line **why GLM is insufficient**. No why → GLM.
- **One** GPT or Claude pass per job unless Jane asks for another. That pass becomes a **locked brief** for GLM.
- Never run GPT and Claude on the same artifact in parallel “to compare.” Pick the role that owns the gap.
- Maker does not choose GPT or Claude.
- Jane may explicitly override any model for a named task. Record the override in the brief; do not silently turn it into a permanent routing change.
- Social **video generation** in Claude Design is Jane’s existing exception (media generation), not a loophole for copy or layout.

## 3. Cursor brief template

CoS (or the owning specialist) saves this as the brief passed to a **new `luci-cursor` delegation**. The selected role supplies the default model.

```
CURSOR BRIEF
Repo: luci-design | luci-website | both
Branch: main | existing | create <name>
Cursor role: chief-of-staff | strategic-marketer | design-direction | maker | review-mechanical | review-taste
Model: role default | Jane override <model>
Why not GLM: <one line or "n/a — GLM">
Mode: read-only | execute

Outcome Jane will see:
Where she looks: http://10.10.1.37 | http://10.10.1.17:8081 | PDF | social calendar | other

Locked (do not invent):
- Copy:
- Visual / tokens:
- Claims:
- Out of scope:

Open (only if gated model):
-

Files / paths:
Definition of done:
Handoff when done: CoS for Review. Do not self-certify high-severity issues.
```

## 4. How Cursor starts

Jane is not a developer. CoS should:

1. Write the brief in Grok.
2. Save the brief as a local temporary text/Markdown file.
3. Invoke `luci-cursor` on Jane’s local computer with the correct role, repo, and brief.
4. Use the default read-only mode for strategy, direction, and review. Add execute authority only for Maker or when Jane explicitly authorizes edits.
5. Return Cursor’s actual evidence to Jane: changed paths, commit, checks, and review URL. Do not merely say “Cursor did it.”

No visible Cursor chat window is expected. The Cursor agent runs headlessly and returns its output to the Bot. Do not ask Jane to remember repo paths, commands, or model IDs.

## 5. After Cursor finishes

Maker (or the Cursor agent) returns to CoS:

- What changed (paths)
- Review URL + hard-refresh note if deployed
- What was not done
- Self-check notes (mechanical only)

CoS routes to Review. Review marks issues and a required fix. CoS writes the **revision brief for GLM** unless Jane re-opens a gated model.
