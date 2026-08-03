---
name: luci-sales-deck
description: >-
  Customize the LUCI sales deck for a prospect meeting. Use when Mike or sales
  needs a demo primer with editable cover copy, client logo, tailored environment
  slide (text + photos), while keeping the LUCI story locked.
---

# Sales deck — customization

Pre-demo / in-meeting primer. **12 slides (16:9).** Source master: `sales-deck.html` in this folder (build copy from `ui_kits/sales/`).

**Workflow:** see `../_brand/SKILL.md` — two-folder architecture, create workspace, dev server, fit check, page packing, voice, PDF export. This file covers only the template-specific page map and editable regions.

Voice: see `../_brand/SKILL.md` → Voice & tone.

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
- **Do not** replace slide 3's LUCI interface screenshot with a property photo.

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
| "Prepared for" kicker | `[data-studio="cover-kicker"]` | Click to edit (usually stays "Prepared for") |
| Client logo | `[data-studio="client-logo"]` | Replace `src` and `alt`. SVG or high-res PNG. Dark logos render white via CSS filter; white logos need `style="filter: none; opacity: 1;"` |

**Locked on cover:** LUCI logo (`.cover__logo`), gold rule (`.cover__rule`).

---

## Editable regions (slide 2 — environment)

| Element | Selector | What to change |
|---------|----------|----------------|
| Kicker | `[data-studio="env-kicker"]` | Click to edit (default: "Your environment") |
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
