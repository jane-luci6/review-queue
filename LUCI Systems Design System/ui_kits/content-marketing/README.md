# Content Lab — LUCI ideas & strategy vault

A Design Hub space for the **input side** of content marketing: raw transcripts,
written strategies, images, and notes that accumulate until there is enough to
mine into concrete content ideas for the website, social, blog, and *The Signal*.

This is **not** a deliverables library. Finished assets still live where they
belong — `Marketing Content` (newsletter, brochure, case studies), `Messaging &
brand` (canonical copy), and the `luci-website` repo. This space feeds those.

## Where it lives

```
LUCI Systems Design System/ui_kits/content-marketing/
  index.html     ← the space page (loaded in the Design Hub). Single source of
                   truth for: how-it-works, strategic themes, source log,
                   ideas backlog, voice flags, open questions.
  README.md      ← this file (operating instructions).
  sources/       ← raw materials Jane drops in (images, transcripts, docs).
```

It is wired into the Design Hub as the **“Content strategy & ideas”** nav space
(in `LUCI Systems Design System/index.html` → `NAV_CONFIG` → `contentLab`).

## The loop

1. **Jane drops a source** into `sources/` (image, transcript, doc, or pastes a
   link) and says “review this.”
2. **Agent logs it** in the Source Log on `index.html` (id, date, type, summary,
   terminology flags) and copies any image into `sources/` with a clean
   `kebab-case` name.
3. **Agent mines it** — adds strategic themes and channel-tagged ideas to the
   Ideas Backlog, each traced back to its source id (`SRC-NN`).
4. **Agent flags voice drift** in the Voice & Terminology Flags table before
   anything is drafted (see “Canonical voice” below).
5. **An idea graduates** to the right deliverable space (website, newsletter,
   sales) and its status here moves to *Live*.

## Naming conventions

- Source files in `sources/`: `YY-MM-DD-<short-kebab-description>.<ext>`
  (e.g. `07-13-cabana-room-event-gtm-strategy.png`).
- Source log ids: `SRC-01`, `SRC-02`, … newest gets the next number; keep the
  log **newest first**.
- Idea ids: `<channel><n>` — `W` website, `S` social, `B` blog, `N` newsletter,
  `SE` sales enablement, `R` risk/guardrail. Reuse the channel letter, increment
  within the channel.
- Idea statuses: `Idea` → `Ready to draft` → `Drafting` → `Live`, plus
  `Needs source` when waiting on raw material.

## Canonical voice (apply before drafting anything from a source)

The source notes drift from LUCI’s voice. Always correct:

| Source says | LUCI says | Why |
|---|---|---|
| “Lucy” | “LUCI” | Brand is LUCI. Confirm with Jane whether “Lucy” is an alias/codename/artifact. |
| “orchestration layer” | “orchestration engine” / “LUCI orchestrates…” | Voice rule: never *layer* as a noun for LUCI. |
| “AV” | “A/V” | Always A/V — body, heads, captions, alt text, diagrams. |
| implied ownership of zone logic | Credit Q-SYS for backend routing | Q-SYS is a named third-party product (QSC). Honesty Protocol is a hard guardrail. |
| “capability loss” as a fear | “No capability loss” as reassurance | Buyer-facing only as reassurance, always paired with crediting Q-SYS. |

## On-brand notes for the page

`index.html` reuses the shared doc stylesheet
(`ui_kits/review/messaging/messaging-docs.css`) and follows the LUCI design
rules: light Track-C document canvas, Space Grotesk for heads/labels, Inter for
all copy, `#2b9e80` (`--mint-dark`) as the only light-surface accent, sharp
corners, hairline separators, no bright mint on light. Keep it that way when
editing.

## Maintenance

- The Source Log and Ideas Backlog live **only** on `index.html` — there is no
  separate data file. Edit the HTML directly.
- When adding a source image, also add it as a nav item under
  `NAV_CONFIG.contentLab` → `Source materials` so it is openable directly from
  the Hub (see how the two PNGs are wired).
- Bump the “N source documents filed · N ideas surfaced” line in the masthead
  after each review pass.
