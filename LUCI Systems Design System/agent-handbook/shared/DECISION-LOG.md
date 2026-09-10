# Decision log

**Purpose:** Short summaries of locks Jane (or a gated specialist pass she accepted) actually made. Chief of Staff reads this to know what happened without reading Cursor chats.

**Not a work board.** The board is current status. This file is the trail of *decisions*.

**Newest first.** One or two sentences. Name the lock, not the debate.

---

## 2026-09-10

- **Grok workstreams replace creative seats** (Jane, 10 Sep). Live bots: CoS, Website, Case Studies & Sales Proof, Editorial & Campaigns, Video. Grok picks GPT/GLM/Claude; Cursor runs it. Old Design Direction / Marketer / Maker / Review Grok seats are retired.
- **Decision log starts.** Cursor appends here at real lock points so CoS can see what Jane decided without the chat archive.
- **Grok facilitates; Cursor decides.** GLM / Claude / ChatGPT lead strategy, design, copy, and implementation. Grok writes the assignment packet, asks Jane when a fact is missing, and follows Cursor unless the result is clearly way off plan.
- **Design Direction starts on GLM.** Role `design-direction` = GLM 5.2 Max first. Escalate to `design-direction-open` (Claude Opus 5) only for open visual planning or after a GLM pass fell short.
- **Grok reaches Cursor via local CLI, not GitHub.** Bridge is `luci-cursor` on Jane’s Mac. No Cloud Agent, no required GitHub, no Cursor chat window. Commits stay local.
