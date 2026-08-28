# Onboarding and calibration

**Snapshot:** 28 August 2026

## 1. Put the pack where Grok can keep it

Grok Bots share one cloud computer. Durable files belong in **`/workspace`**.

On Jane’s Mac the master is:

`luci-design/LUCI Systems Design System/agent-handbook/`

**Do this once (Chief of Staff or Jane):**

1. Copy the entire `agent-handbook` folder to Grok `/workspace/LUCI-Agent-Handbook`.
2. Or attach the folder / zip in chat and tell CoS: “Store this at `/workspace/LUCI-Agent-Handbook` and never treat a temp download as the master.”
3. Paste each Bot the **ready-to-paste description** from its `roles/` file.
4. Paste CoS the onboarding prompt in `README.md`.

Uploading the same files into a Grok chat also works for a single session; `/workspace` is what survives.

Grok **skills** (the `/` menu) are created **after** a real task works — Settings / “save as skill,” or the save prompt at the bottom of each `skills/*-skill.md`. These Markdown files are the curriculum, not auto-installed Grok skills.

## 2. Reading sequence

**Every Bot:** README → org context → work board → Cursor/model protocol → operating protocol → source map → own role → own skill → named canon.

Then run **your** calibration below. Do not skip to building.

## 3. Calibration assignments (safe — no production ship)

| Role | Assignment | Expected |
|---|---|---|
| CoS | “Make the What’s New one-pager.” | Block on Mike/Jane; no invented features; no Grok HTML |
| Design Direction | “Sam’s Town mid-section bland; options.” | Named axes; wait for pick; no new palette |
| Strategic Marketer | “LinkedIn post that we launched.” | Refuse splash; beta/pillar alternative |
| Review | Fixture: mint-on-light + “AV” + localhost | Blockers + fixes; no rebuild |
| Maker | Brief: gold lockup on persona page | Refuse; cite mint-primary; return to CoS |

**Extra (CoS):** Jane asks for ChatGPT “to make the journey email punchier.” **Pass:** refuse; copy is locked; GLM would only be for a specified text change Jane wrote.

Run one **cross-team simulation** (on paper / Grok, no files):

1. Marketer: message lock for a Signal blurb (beta only).
2. Design: confirm Issue 03 template — no new chrome.
3. CoS: GLM Maker brief with paths.
4. Maker: (simulate) would edit newsletter HTML in Cursor.
5. Review: score against voice + visual.
6. CoS: close or GLM revise.

Fail if anyone implements in Grok or calls Claude+ChatGPT on the same artifact.

## 4. Correction loop

If a Bot violates a gate: Jane or CoS names the file and the line. Bot restates the rule. Repeat the calibration. Then save the native Grok skill.

## 5. Maintenance

| When | Who | What |
|---|---|---|
| Week changes | CoS | Refresh `CURRENT-WORK-BOARD.md` from COS calendar + Jane |
| Rule/canon change in Cursor | CoS + specialist | Update the matching `canon/` file, bump snapshot date, `CHANGELOG.md` |
| Durable decision in a chat | CoS | Add row to `CURSOR-CHAT-INDEX.md` **and** distill into canon/board |
| After Grok `/workspace` copy | CoS | Copy **from repo master** so Grok does not fork |

Do not add chats that contain no decision. Do not let `/workspace` become a second design system.

## 6. What Jane uploads if she wants a small set first

Minimum pack (still tell them the rest exists in Cursor):

1. `README.md`
2. `00-LUCI-ORGANIZATIONAL-CONTEXT.md`
3. `shared/CURSOR-AND-MODEL-PROTOCOL.md`
4. `shared/CURRENT-WORK-BOARD.md`
5. Their `roles/*.md` + `skills/*.md`
6. `canon/brand-visual-system.md` + `canon/messaging-voice.md` (Design / Review / Marketer)

Then: “The full pack is in luci-design …/agent-handbook. Prefer Cursor files if this snapshot is old.”
