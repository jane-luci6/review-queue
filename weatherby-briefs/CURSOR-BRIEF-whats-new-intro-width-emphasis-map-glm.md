# CURSOR BRIEF — What's New two-pager: intro width + emphasis + map/cols breathing room (GLM)

Model: GLM  
Repo: design (`--repo design`)  
Mode: execute  
Owner: Weatherby  
Branch: current (`p1-scaleup` — do not invent a branch switch)

## Outcome
Jane reviewed the live What's New two-pager (IMP + canonical). Fix three layout/copy-emphasis issues on page 1 only. Do **not** change locked intro wording except adding `<strong>` / `<b>` for highlights using the page's existing mint/ink emphasis pattern.

## Canonical (edit this)
`/Users/janehaynie/Documents/Cursor Projects/luci-design/LUCI Systems Design System/ui_kits/sales/new-luci-whats-new-onepager.html`

Live review: http://10.10.1.17:8081/sales/new-luci-whats-new-onepager.html

## Locked intro (exact wording — only add emphasis tags)
We rebuilt LUCI from the ground up around the capabilities, functionality, and performance you asked for—making monitoring, support, and future upgrades easier. You gain more control, with the LUCI team still right there when you need us.

## Do exactly

### 1) Intro width = callout + three-column width
- `.p1-intro` currently has `max-width:62ch`, which makes it narrower than `.p1-callout` and `.p1-cols` above/below.
- Remove the `max-width:62ch` constraint (or otherwise make `.p1-intro` span the **same content width** as the callout and the three columns). Intro should align left/right with callout + cols.

### 2) Highlight a few words for emphasis (don't over-bold)
- Use the page's existing emphasis pattern: callout/pagehead use `<b>` with mint accent via `.p1-callout b` / `.p1-pagehead b` → `color:var(--accent-light);font-weight:700`.
- Add matching rule for `.p1-intro b` and/or `.p1-intro strong` (same accent-light + weight 700). Prefer `<b>` for consistency with callout, or `<strong>` if you style both identically.
- Sensible salients (pick a light set — do **not** bold every suggestion):
  - capabilities / functionality / performance (or the triad as a group)
  - monitoring / support (and maybe future upgrades if it still reads clean)
  - more control
  - LUCI team
- Do **not** change any other words, punctuation, or em dash. Exact locked sentence text must remain identical aside from the inserted tags.

Suggested (adjust if over-bold; keep sparse):
```html
<p class="p1-intro">We rebuilt LUCI from the ground up around the <b>capabilities</b>, <b>functionality</b>, and <b>performance</b> you asked for—making <b>monitoring</b>, <b>support</b>, and future upgrades easier. You gain <b>more control</b>, with the <b>LUCI team</b> still right there when you need us.</p>
```
If that feels too heavy, drop "future upgrades" (already not bolded above) and/or collapse the triad to fewer bolds — Jane said don't over-bold.

### 3) Reduce three-box overlap with the floorplan/map
- Page 1: left map (`img.p1-map`), right content (`.p1-inner` with callout + intro + `.p1-cols`).
- Jane: the three boxes overlap the map a bit too much — give columns more breathing room vs map.
- Preserve overall design. Prefer a **small** layout nudge, e.g.:
  - Increase `.p1-inner` left padding (today `padding:24px 115px 0 var(--pad)` → left is only `--pad`/62px while right is 115px — content encroaches left into the L-map). Nudge content right by raising left padding modestly (e.g. toward ~88–110px range) and optionally trim right padding slightly to keep total content width usable; **or**
  - Slight map crop/position tweak if padding alone isn't enough.
- Do not restyle pillar cards, pills, masthead, page 2, or footers beyond what this breathing-room tweak needs.
- Verify print/letter sheet (816×1056) still fits without overflow or clipped columns.

### 4) Twin + deploy
- After edits: `npm run build:review` then `npm run deploy:portal` from `LUCI Systems Design System/` (cwd that owns package.json).
- Review twin under `ui_kits/review/sales/new-luci-whats-new-onepager.html` must match (build:review copies it).
- Do **not** rewrite `new-luci-whats-new-onepager-flow-c.html` unless you confirm it is still an intentional live twin that must stay byte-synced — last intro commit only touched canonical + review; prefer canonical + review path only (same as fed7621).

### 5) Out of scope
- Upgrade Guide: **do not touch** (Jane's note is two-pager map/boxes; UG fine).
- No copy rewrite beyond emphasis tags.
- Do not commit unrelated dirty tree files (many unrelated mods/untracked). Commit **only**:
  - `LUCI Systems Design System/ui_kits/sales/new-luci-whats-new-onepager.html`
  - review twin if it differs after build (or let build:review regenerate it and include if committed historically)
  - this brief under `weatherby-briefs/`
- Optionally update CURRENT-WORK-BOARD Active job if lightweight; skip if it would drag in unrelated board noise.

## Verify before return
1. Intro has no narrower max-width than callout/cols; visual width matches.
2. Intro has sparse mint `<b>`/`<strong>` highlights; wording otherwise exact.
3. Three columns sit with clearer gap from left map (less overlap).
4. `curl -s -o /dev/null -w "%{http_code}" http://10.10.1.17:8081/sales/new-luci-whats-new-onepager.html` → 200
5. Commit SHA + live URL reported.

## Return
Commit SHA, live URL, HTTP status, what changed for width / overlap / emphasis (specific CSS + which words bolded).
