# Agent Readiness Testing

Validate that an API is usable by an LLM agent — and discover the agent's
tool and skill catalog empirically — by having a capable model role-play
the not-yet-built agent against the real API.

## Purpose

Two outcomes from one activity:

1. **Test the API** — prove an LLM can actually accomplish real tasks with
   the endpoints you built (discoverability, error quality, response
   usability, missing capabilities).
2. **Discover the agent design** — let real tasks reveal which tools and
   skills the eventual purpose-built agent needs, instead of guessing them
   up front.

## When to use

- Right after coding an API surface, before building the production agent.
- Whenever you add or change endpoints an agent will consume.
- As an exploratory pass to shape the agent's tool/skill catalog.

Not a replacement for deterministic unit/integration tests — a complement.

## The method: grounded execution, not pure role-play

| Flavor | What happens | Value |
|--------|--------------|-------|
| Pure role-play | The model *imagines* being the agent and narrates | Low — untethered from reality; risks plausible-looking fiction |
| Grounded execution | The model *actually calls* the API with a real request | High — a live integration test with an LLM driving it |

Always use grounded execution: the model makes the same real API calls the
production agent would make, and the real outputs are the test result.

## Setup for realism

The driver model has advantages the production agent won't have (broader
context, a different/stronger model). Constrain it to the agent's real
conditions so findings are trustworthy:

1. **Real tool surface only** — give the driver exactly the tools the agent
   will have ("you have only `search`, `get_item`"), nothing more.
2. **Real scoped credential** — use the same scoped key the agent will use,
   so access/permission behavior is exercised.
3. **Only the context the agent would have** — the task input and the API,
   not prior conversation history. Force discovery through the API.

A gap hit under these constraints is a gap the production agent would hit.
A gap hit outside them is noise.

## The feedback loop

```
Role-play a real task (grounded)
        │
        ▼
Hit a gap  ─────────────────────────────┐
        │                                │
        ▼                                │
Classify the gap (see taxonomy)          │
        │                                │
        ▼                                │
Shape the tool / skill / API to close it │
        │                                │
        ▼                                │
Re-run the task ─────────────────────────┘  (new gaps surface → repeat)
```

You let the work define the toolset, rather than defining the toolset and
hoping it fits the work.

## Gap taxonomy

Each gap maps to a specific design artifact:

| Gap you hit | What it means | Where it goes |
|-------------|---------------|---------------|
| "There's no way to do X" | Missing **tool** | A new tool definition |
| "Tool works but output is unusable / I had to guess" | Tool has the **wrong shape** | Refine the tool contract |
| "I knew *what* to do but not *how*" | Missing **skill** (procedure) | A skill / workflow doc |
| "I could do it but shouldn't be allowed" | **Scope / guardrail** finding | Credential scope or policy rule |

## What it tests well vs. what it doesn't

**Tests well**
- API contract and end-to-end flow
- Whether a task is *achievable* with the real toolset
- Discoverability, error-message quality, response usability
- Missing capabilities (gaps in the API)
- Edge cases (deliberately probe malformed input, missing fields)

**Does not test (caveats)**
- **Model fidelity** — the driver isn't the production agent. Strong smoke
  test, not a conformance guarantee.
- **Determinism** — the driver may approach a task differently each run.
  Good for exploration, poor for regression. Keep deterministic tests too.
- **Context leakage** — without the realism constraints, the driver may use
  knowledge the real agent lacks.

## Capturing findings

Each session's gaps are your API-hardening and agent-design backlog:

- Log every gap as a ticket or a note the moment it surfaces.
- Tag it with its taxonomy class (tool / tool-shape / skill / scope).
- The accumulating list *is* the agent's capability catalog, arriving in
  the order reality hands it to you.
- Shared patterns that recur across domains → shared tools/skills.
  Domain-specific ones → domain-specific tools/skills.

## Session template

```
Driver framing:
  "You are the <role> agent. Your only tools are <tool list>.
   You authenticate with <scoped key>. You have this input: <document/request>.
   Accomplish: <task>. Execute against the real API and report:
     - which calls you made and what came back
     - whether the task succeeded
     - where you got stuck or had to guess
     - what was missing"

Reviewer (you):
  - Read the transcript as a test result.
  - Classify each gap (tool / tool-shape / skill / scope).
  - Decide the fix; capture it.
  - Re-run to confirm the gap closed and surface the next one.
```

## Principle

If a capable model — given only the agent's real tools, scope, and context
— struggles to accomplish a task against your API, the production agent
will struggle more. Fix the friction now, while it is cheap, and let each
session write the spec for the agent's tools and skills.
