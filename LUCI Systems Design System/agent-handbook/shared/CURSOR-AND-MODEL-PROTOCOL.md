# Cursor and model protocol

**Snapshot:** 28 August 2026  
**Applies to:** every Grok Bot  
**Precedence:** this file beats any instinct to “just do it in Grok.”

## 1. Grok vs Cursor

Jane’s Grok Bots are **directors, routers, and quality owners**. They write briefs, enforce role boundaries, track status, and catch drift.

They do **not** implement website pages, sales HTML, CSS, diagrams, PDF exports, portal deploys, or git commits on Grok’s cloud computer.

**Why:** Cursor holds the live LUCI context — local repos, `.cursor/rules`, chats, OneDrive messaging docs, and deploy scripts. Grok’s computer is a separate VM. GitHub remotes are hundreds of commits behind Jane’s machine. Building on Grok would fork a stale, rule-blind copy of the work.

| Surface | Use it for |
|---|---|
| **Grok** | Intake, calendar, routing, briefs, Jane gates, “which model?”, status, Review *diagnosis* (issues + required fix, not a rebuild) |
| **Cursor** | All production: edit files, variants on branches, fit-check, deploy, mechanical QA |
| **Jane** | Brand locks, expensive-model overrides, named-client public claims, “make this a house rule”, irreversible deploys she asked to see first |

## 2. Model budget (non-negotiable)

Target mix across Cursor work: **85–90% GLM**, **10–15% ChatGPT + Claude combined**.

### GLM — default. Use unless a gate below is met.

Apply locked copy, locked layout, locked tokens. Build, edit, deploy, PDF/fit-check, mechanical QA, status, calendar, social production after strategy is locked, case-study assembly from a locked spine, portal customization within `SKILL.md`. Most revisions after Review (“change X to Y”).

### ChatGPT in Cursor — copywriting + marketing strategy only

Use only when **all** are true:

1. The argument or copy is **not already locked** in the Messaging Guide, handbook, or assigned brief.
2. The asset is customer-facing or sales-critical.
3. GLM would have to **invent the thesis**.

Examples that pass: new campaign architecture; a first-pass hero/dek that sets category language; a thought-leadership angle not already in LUCI copy.

Examples that fail: rephrase locked boilerplate; fill a template; alt text; “make it punchier”; subject lines for a journey email whose body is already approved.

### Claude in Cursor — design direction + Jane-level review only

Use only when **all** are true:

1. Visual direction is **open**, *or* Review must catch Jane-at-11pm brand / layout / tone / strategy drift.
2. The decision is not a token swap or a checklist.
3. GLM would be **guessing taste**.

Examples that pass: first layout thesis; genuine A/B/C variant axes; case-study spatial system; taste review of a finished page.

Examples that fail: implement CSS; apply a settled mock; run deploy; rubber-stamp GLM output; “looks off, you fix it.”

### Hard gates (Chief of Staff enforces)

- If the brief can name the **files**, the **locked copy**, and the **visual tokens**, the Cursor model is **GLM**.
- Expensive-model requests need a one-line **why GLM is insufficient**. No why → GLM.
- **One** ChatGPT or Claude pass per job unless Jane asks for another. That pass becomes a **locked brief** for GLM.
- Never run ChatGPT and Claude on the same artifact in parallel “to compare.” Pick the role that owns the gap.
- Maker does not choose ChatGPT or Claude.
- Social **video generation** in Claude Design is Jane’s existing exception (media generation), not a loophole for copy or layout.

## 3. Cursor brief template

CoS (or the owning specialist) pastes this into a **new Cursor chat**. Set the model in Cursor first.

```
CURSOR BRIEF
Repo: luci-design | luci-website | both
Branch: main | existing | create <name>
Model: GLM (default) | ChatGPT (gated) | Claude (gated)
Why not GLM: <one line or "n/a — GLM">

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

## 4. Who opens Cursor

Jane is not a developer. CoS should:

1. Write the brief in Grok.
2. Tell Jane, in plain English, which Cursor chat to open (or open it via Cursor if the Bot has approved local-computer access).
3. Name the model: “Use GLM.” / “Use ChatGPT for this one pass because [gate].” / “Use Claude for direction only, then GLM builds.”

Do not ask Jane to remember repo paths or script names. Put those in the brief for Cursor.

## 5. After Cursor finishes

Maker (or the Cursor agent) returns to CoS:

- What changed (paths)
- Review URL + hard-refresh note if deployed
- What was not done
- Self-check notes (mechanical only)

CoS routes to Review. Review marks issues and a required fix. CoS writes the **revision brief for GLM** unless Jane re-opens a gated model.
