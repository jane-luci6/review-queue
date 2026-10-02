# Work board protocol (Grok)

**Locked:** 10 September 2026 · Jane  
**Board file:** `shared/CURRENT-WORK-BOARD.md`  
**Why this exists:** Jane talks to workstream bots directly. Cornelius still needs to know what is in flight without her repeating herself.

Cursor already logs **locks** in `DECISION-LOG.md`. This protocol is the **Grok** gap: live job status on the shared board, whoever Jane assigned.

## Rule

Every active job must be logged on the shared work board, **regardless of which bot Jane talks to.**

If Jane assigns work directly to Consuelo, Vikram, Ermintrude, Weatherby, Svetlana, or Longinus, **that bot** updates the board. Do not wait for Cornelius. Do not ask Jane to brief him.

Cornelius must **read the current board** before answering questions about team status, priorities, dependencies, or “what’s going on.” He does not ask Jane what she already gave another Grok bot.

## Where to write

Grok bots share one computer. Log immediately on the handbook copy they can edit:

`/workspace/LUCI-Agent-Handbook/shared/CURRENT-WORK-BOARD.md`

→ section **Active jobs**.

The Mac master is `luci-design/…/agent-handbook/shared/CURRENT-WORK-BOARD.md`. If Cursor is already running the job, the Cursor brief includes updating that master row so the next handbook copy is not stale.

Jane should not have to paste the same status into two chats.

## When to log

- **Start:** Jane assigns work (even a short “take this and send it to GLM”).
- **Change:** owner, stage, model, artifact, or gate changes.
- **Stop:** job is waiting on Jane, handed off, parked, or done — update the row, then move it to Waiting / Projects / Closed as needed. Do not leave a finished job in Active jobs.

A status-only change is **not** a decision-log entry. Locks still go to `DECISION-LOG.md`.

## Required fields (every Active jobs row)

| Field | Meaning |
|---|---|
| **Jane asked** | What she said, in one line. Not a transcript. |
| **Owner** | The Grok bot trafficking it (not “Cursor”). |
| **Stage** | Where it is now (e.g. GPT ideas, waiting Jane pick, GLM layout, Jane review, queue). |
| **Model** | GPT / GLM / Claude in Cursor for **this** beat. `none` if not in Cursor yet. |
| **Artifact** | File, URL, or packet she will look at. |
| **Waiting on Jane** | The gate, or `none`. |
| **Next** | The next action, and who takes it. |

Use a stable **ID** (`signal-04-layout`, `aliante-cs-pass2`). Reuse it; don’t spawn duplicate rows for the same job.

## Do not

- Ask Jane to recap another bot’s work for Cornelius.
- Keep the job only in your own chat memory.
- Log every mechanical GLM tweak. Log the job and stage, not every pixel.
- Treat the weekly Projects table as a substitute for an Active jobs row while you are in the work.
