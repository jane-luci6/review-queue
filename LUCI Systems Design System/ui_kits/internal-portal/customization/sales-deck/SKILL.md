---
name: luci-sales-deck
description: >-
  Customize the LUCI sales deck for a prospect meeting. Use when Mike or sales
  needs a demo primer with editable cover copy, client logo, tailored environment
  slide (text + photos), while keeping the LUCI story locked.
---

# Sales deck — customization

Pre-demo / in-meeting primer. **12 slides (16:9).** Source master: `sales-deck.html` in this folder (build copy from `ui_kits/sales/`).

Also read: `../_brand/SKILL.md`

## Portal URL workflow (primary)

**Preview URL:** `http://10.10.1.17:8081/internal-portal/customization/sales-deck/sales-deck.html`

When Mike pastes this URL into Cursor chat:

1. Read this `SKILL.md` and `../_brand/SKILL.md` before any edits.
2. Copy master from `LUCI Systems Design System/ui_kits/sales/sales-deck.html` to `ui_kits/sales/<client>-sales-deck.html`.
3. Customize **slides 1–2** only — copy, logo, and photos (see editable regions below).
4. Do **not** edit the HTML file on the VM deploy folder (overwritten on deploy).

See also: `../CURSOR.md`, `AGENTS.md` in this folder.

## Open the rendered preview in the editor (automatic)

After customizing, **automatically open the rendered client HTML in Cursor's in-editor (Glass) browser — not the HTML source** — without being asked:

1. From `LUCI Systems Design System/ui_kits/sales/`, start a local server in the background: `python3 -m http.server 8771 --bind 127.0.0.1` (increment the port if busy).
2. Verify: `curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:8771/<client>-sales-deck.html` → `200`.
3. Open `http://127.0.0.1:8771/<client>-sales-deck.html` in Cursor's in-editor browser via the `cursor-app-control` MCP `open_resource` tool (URI = that URL). Do **not** use a `file://` URI — that opens the HTML source, not the rendered deck.

Editable regions use `class="deck-edit"`, `contenteditable="true"`, and `[data-studio]` markers — **click highlighted text to type**. Use **Download HTML** in the edit bar to save. Preserve all `deck-edit`, `contenteditable`, and `data-studio` attributes when editing in Cursor. User fallback if the pane doesn't appear: `Cmd+Shift+P` → "Simple Browser: Show" → paste the localhost URL.

---

## Photo strategy (read before customizing)

**Do not** paste photos onto product slides or stretch images outside the frames. Slide 2 has three fixed slots:

| Slot | Selector | Use |
|------|----------|-----|
| Hero (large left) | `[data-studio="env-photo-primary"]` | Best wide shot — sportsbook, gaming floor, venue |
| Supporting 1 (top right) | `[data-studio="env-photo-secondary-1"]` | Second angle — bar, event space, exterior |
| Supporting 2 (bottom right) | `[data-studio="env-photo-secondary-2"]` | Third angle — optional |

**Rules:**
- **Swap `src` only** — never change slot size, grid, or CSS. Frames use `object-fit: cover` and 16px radius with mint hairline.
- **1 photo is enough** — fill the hero; leave secondary slots on `deck-photo-placeholder.svg`.
- **2 photos** — hero + one secondary; leave the third placeholder.
- **No photos yet** — leave all three placeholders; slide still reads on-brand.
- **Update `alt`** on each swapped image with a short scene description.
- **Do not** replace slide 3’s LUCI interface screenshot with a property photo.

---

## Slide map — editable vs locked

| Slide | Section | Status |
|-------|---------|--------|
| **1** | Cover — headline, kicker, client logo | **EDITABLE** |
| **2** | Your environment — kicker, headline, 3 photo slots | **EDITABLE** |
| **3–12** | LUCI story, proof, journey, close | **LOCKED** |

---

## Editable regions (slide 1 — cover)

| Element | Selector | What to change |
|---------|----------|----------------|
| Cover headline | `[data-studio="cover-title"]` | Click to edit wording |
| “Prepared for” kicker | `[data-studio="cover-kicker"]` | Click to edit (usually stays “Prepared for”) |
| Client logo | `[data-studio="client-logo"]` | Replace `src` and `alt`. SVG or high-res PNG. Dark logos render white via CSS filter; white logos need `style="filter: none; opacity: 1;"` |

**Locked on cover:** LUCI logo (`.cover__logo`), gold rule (`.cover__rule`).

---

## Editable regions (slide 2 — environment)

| Element | Selector | What to change |
|---------|----------|----------------|
| Kicker | `[data-studio="env-kicker"]` | Click to edit (default: “Your environment”) |
| Headline | `[data-studio="env-title"]` | Click to edit — may include `<span class="accent-gold">` for gold emphasis |
| Hero photo | `[data-studio="env-photo-primary"]` | Property `src` + `alt` |
| Supporting 1 | `[data-studio="env-photo-secondary-1"]` | Optional |
| Supporting 2 | `[data-studio="env-photo-secondary-2"]` | Optional |

**Locked on slide 2:** slide chrome (`.s-foot`), mosaic grid layout.

---

## Locked regions (slides 3–12)

Do **not** modify slides **3–12**, including journey stage labels and descriptions on slide 10.

---

## Do not

- Edit slides 3–12 — **no changes of any kind**, including color, styling, spacing, or CSS, not just copy/diagrams/journey text. If asked to change a locked slide, do NOT edit first — flag the lock and ask whether to override (local-only vs canonical) before making any change.
- Add or remove slides.
- Paste photos outside the slide 2 mosaic frames.
- Edit slides 3–12 copy, diagrams, or journey text.
- Change the LUCI logo on cover or close.
