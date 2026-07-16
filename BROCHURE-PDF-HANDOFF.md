# LUCI Sales Brochure — PDF / Portal Session Handoff

**Last updated:** 2026-07-08 (evening)  
**Status:** Page 1 approved. Acrobat opens without blinking. Portal + PDF aligned on screenshot layout and gradient feather.

---

## Start here tomorrow

Jane confirmed page 1 looks correct (“There we go!!”). Before changing anything, **hard-refresh** the portal (`Cmd+Shift+R`) and spot-check the Desktop PDF in Acrobat.

**Likely next work:** pixel-level verification of pages 2–4 (orbit sharpness, diagram text, team icons) using the same rigor as page 1 — not eyeballing image descriptions.

---

## What was fixed (this session)

### Page 1 — platform screenshot + gradient feather

| Symptom | Root cause | Fix |
|--------|------------|-----|
| Screenshot floated mid-band, gap above mint line | Two competing CSS layouts in `brochure.css` (obsolete grid + navy-band override); print flex shrank the band | Removed obsolete grid block (~lines 533–640); single navy-band layout only |
| Hard left edge, no gradient in PDF | Print rule replaced CSS feather with solid navy strip (Acrobat blink workaround); later, baked feather on *uncropped* source was cropped away by `object-fit: cover` + `object-position: right` | Pre-crop source to printed shot aspect **then** bake feather; hide CSS `.cap-shot__feather` in print only |
| Portal and PDF diverged | Screen uses PNG + live CSS gradient; PDF uses patched `interface-floor-view-brochure.jpg` | Separate assets per channel; layout shared via screen CSS |

**Measured print box for `.cap-shot` (page 1):** ~4.59in × 4.70in (width = page minus 46% left offset; height = fixed 4.7in band; ±24px bleed clipped by `overflow: hidden`).

**Feather bake aspect:** `BROCHURE_SHOT_ASPECT = 4.59 / 4.70` in `prepare-sales-pdf-assets.py` — crop right-anchored from `interface-floor-view.orig.png`, then apply gradient stops matching `.cap-shot__feather` in CSS.

### Other fixes (earlier in session, not re-verified at pixel level)

- **Acrobat blink:** baseline JPEGs (`progressive=False`), flat print backgrounds (no CSS gradient Pattern/Shading), Ghostscript passthrough (no downsampling/font re-subset), qpdf linearize last
- **Orbit fuzzy:** PDF uses `embedded-operation-orbit-brochure.png` at 1800×1000 (lossless), not low-res JPG
- **Icons missing in PDF:** removed print rules that hid `.cap-softicon` / `.cap-team-icon` SVGs
- **Text rendering:** `-dCompressFonts=false -dSubsetFonts=false` in GS pass
- **Logos pages 1 & 5:** fixed broken base64 `src` → `assets/logos/luci-wordmark-white-320.png?v=7`

### Branding decision (do not revert)

- **Hero (page 1) and closing (page 5) headlines stay Syncopate** — intentional brand exception, not a bug.

---

## Key files

| File | Role |
|------|------|
| `LUCI Systems Design System/ui_kits/sales/brochure.html` | Source HTML |
| `LUCI Systems Design System/ui_kits/sales/brochure.css` | Layout; navy-band block ~line 1725+; print rules at end |
| `LUCI Systems Design System/scripts/prepare-sales-pdf-assets.py` | Rasters + `interface-floor-view-brochure.jpg` feather bake |
| `LUCI Systems Design System/scripts/patch-sales-pdf-html.py` | PDF export HTML: JPG/PNG swaps, brochure-specific floor + orbit assets |
| `LUCI Systems Design System/scripts/render-pdf.sh` | Chrome → GS → qpdf |
| `LUCI Systems Design System/assets/sales/LUCI-Brochure.pdf` | Canonical PDF output |
| `~/Desktop/LUCI-Brochure.pdf` | Jane’s working copy for Acrobat review |

**Brochure-only PDF assets:**

- `ui_kits/sales/assets/interface-floor-view-brochure.jpg` — pre-cropped + feather baked (PDF only)
- `ui_kits/sales/assets/diagrams/embedded-operation-orbit-brochure.png` — high-res orbit (PDF only)

**Portal (screen) still uses:** `interface-floor-view.png` + live `.cap-shot__feather` CSS gradient.

---

## Commands

```bash
cd "LUCI Systems Design System"

npm run pdf:brochure          # prepare rasters + render PDF
npm run build:review          # sync to ui_kits/review/
npm run deploy:portal         # ship to http://10.10.1.17:8081
```

Copy to Desktop after rebuild:

```bash
cp "LUCI Systems Design System/assets/sales/LUCI-Brochure.pdf" ~/Desktop/LUCI-Brochure.pdf
```

**Review URLs:**

- Portal: `http://10.10.1.17:8081` (hard-refresh)
- Brochure HTML: `ui_kits/review/sales/brochure.html` on portal

**Do not use `localhost:4321` as the deliverable** — Jane reviews on `10.10.1.17`.

---

## Architecture notes (for future edits)

1. **One layout per page** — do not reintroduce duplicate grid + override blocks in `brochure.css`.
2. **PDF-only visuals → baked assets** in `prepare-sales-pdf-assets.py`; minimal print CSS overrides.
3. **Feather / gradients in PDF:** either bake into the raster at the **post-crop** pixels the browser will show, or accept CSS gradient Pattern objects (blink risk).
4. **Canonical assets rule:** master diagrams live in `assets/diagrams/`; brochure copies are asset-local; propagate on request only.

---

## Suggested tomorrow checklist

- [ ] Open `~/Desktop/LUCI-Brochure.pdf` in Acrobat — confirm still no blink, page 1 still good
- [ ] Portal page 1 — screenshot + feather matches PDF
- [ ] Page 2: `luci-what-luci-is` diagram text sharp; Key Features icons + labels
- [ ] Page 3: orbit sharp (`embedded-operation-orbit-brochure.png` in PDF)
- [ ] Page 4: team stroke icons visible; header text clean
- [ ] If any page regresses: measure printed geometry (debug outline technique) before guessing CSS
- [ ] Optional: CSS consolidation pass — merge stacked `@media print` blocks in `brochure.css`
- [ ] Git commit only if Jane asks

---

## Agent transcript (full conversation)

`/Users/janehaynie/.cursor/projects/Users-janehaynie-Documents-Cursor-Projects-luci-design/agent-transcripts/8245f6c9-6f06-46c4-9cd1-da64514a3858/8245f6c9-6f06-46c4-9cd1-da64514a3858.jsonl`

---

## Quick prompt for a new Cursor tab

> Read `BROCHURE-PDF-HANDOFF.md` in the luci-design repo root. Continue LUCI sales brochure PDF work: verify pages 2–4 in Acrobat and on `http://10.10.1.17:8081`, using the same pixel-measurement approach used for page 1 feather fix. Do not change Syncopate hero/closing headlines. Deploy with `npm run deploy:portal` after meaningful changes.
