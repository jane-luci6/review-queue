# Task: "Whole Property" — zone names knocked out of real Syncopate letter strokes

## Project context

You are working in **LUCI Systems** (a B2B tech brand). The website is an Astro static site in the git repo at:

  /Users/janehaynie/Documents/Cursor Projects/luci-website

A sibling repo holds the brand design system:

  /Users/janehaynie/Documents/Cursor Projects/luci-design

The LUCI brand has a strict, canonized visual system. The relevant rules live in `.cursor/rules/` inside the luci-design repo (read `luci-visual-design.mdc`, `luci-modern-design-guidelines.mdc`, and `luci-website-review-deploy.mdc` before starting). Quick summary of what matters here:

- **Three-tier fonts:** Syncopate (display, ≤3 words, single line, uppercase), Space Grotesk (structure — headlines, labels, metric numerals), Inter (all running body/copy, always).
- **Palette:** navy-deep `#0A161C`, navy `#0B141A`, mint `#68E3BE`, off-white `#F5F8FA`. Bright mint is used on dark backgrounds only.
- **De-boxed aesthetic:** whitespace + hairlines carry structure, not stacked containers. Sharp corners (radius 0). The 4px mint accent bar is reserved for true callouts only.

## The design task

On a hero/landing treatment, render the phrase:

  Control your
  WHOLE PROPERTY

where **WHOLE PROPERTY** is set in **Syncopate 700**, giant, mint `#68E3BE` on the navy-deep `#0A161C` background. "Control your" sits above it in small white Space Grotesk uppercase.

Inside the strokes of those mint Syncopate letters, **knock out** the names of the property zones a LUCI controls — i.e. render each zone name in navy `#0A161C` (same as the background) sitting *inside* the mint letter, reading as clean negative space cut out of the letterform. The letter keeps its natural Syncopate outline and shape — no added outline, no skeleton letters, no distortion of the letterform.

Each zone name must:

1. **Run inline with the direction of the stroke it occupies** — vertical words on vertical stems, horizontal words on horizontal bars, diagonal words on the W's diagonals, curved words following the O's arc.
2. **Fill the full space of its stroke** — top to bottom AND width-wise. The word should span the stroke's full length and fill the stroke's thickness. Use `textLength` + `lengthAdjust="spacingAndGlyphs"` so the word stretches to exactly the stroke length, and set font-size from the stroke's measured thickness so the word height fills the stroke thickness.
3. **Appear exactly once.** 13 zones, 13 letters (W-H-O-L-E P-R-O-P-E-R-T-Y), one zone per letter, in left-to-right reading order.
4. Be clipped to the real letter outline so nothing spills outside the letter.

This is the user's original sketch concept: e.g. one location word in the far-left diagonal stroke of the W, one in the right diagonal, etc. — straight strokes, one word each, clean knockout.

## The 13 zones (in order)

  Lobby, Pool, Theater, Ballroom, Sportsbook, Marquee, Restaurant,
  Bar & lounge, Casino floor, Event Venue, Conference Room, Parking structure,
  Wayfinding sign

These already exist as `propertyZones` in `src/data/floorControl.ts` in the luci-website repo — read that file and use its `propertyZones` array as the source of truth (don't hardcode a different list).

## The precision requirement (this is the whole point)

Earlier attempts estimated the stroke geometry by hand and the result looked imprecise — words didn't sit cleanly in the strokes. The fix is to derive everything from **real font geometry**, not estimates. Do this:

1. **Extract the real Syncopate glyph outlines.** The Syncopate font is embedded as a base64 **woff2** `@font-face` (weight 700) inside:
   `luci-design/LUCI Systems Design System/assets/fonts/luci-brand-fonts.css`
   Decode that base64 woff2 to a ttf (Python `fontTools` + `brotli` are installed; `fontTools.ttLib.TTFont` can load the woff2 bytes directly). Use `fontTools.pens.svgPathPen.SVGPathPen` to get each glyph's outline as an SVG path string. Use these real outlines as (a) the solid mint fill and (b) the `clipPath` for the knockout.

2. **Find the real stroke centerlines via skeletonization.** Rasterize each glyph to a high-res binary mask (PIL `ImageFont.truetype`), then skeletonize (scikit-image `skimage.morphology.skeletonize`) to get the true 1px-wide centerline network of each letterform. Trace the skeleton into branches (paths between endpoints [1 neighbor] and junctions [3+ neighbors]). Each branch is a real stroke centerline — polyline of (x,y) points.

3. **Measure real stroke thickness.** `scipy.ndimage.distance_transform_edt` on the mask gives, at each skeleton pixel, the distance to the nearest edge ≈ half the stroke thickness. Thickness = 2 × that value, sampled along the branch. Set the zone name's font-size from this measured thickness so the word fills the stroke height.

4. **Place the zone name along the centerline** with SVG `<textPath>` on a `<path>` built from the branch polyline, `textLength` = polyline length (so the word fills the stroke length), `startOffset="50%" text-anchor="middle"`.

### Hard-won facts (use these, don't rediscover)

- Syncopate **UPM = 2048**, hhea ascent = 1556, descent = −426. Cap height (e.g. W glyph yMax) = **1374** font units.
- The glyph outlines from `SVGPathPen` are in **y-up** font coordinates (baseline at y=0, top at +1374). SVG is y-down, so the clip transform must flip: `transform="translate(<tx> <ty>) scale(<SCALE> -<SCALE>)"` where `ty = oymax * SCALE` and `tx = letter_x_offset - oxmin * SCALE`.
- The rasterized mask (PIL) and the outline must be **aligned by their measured bounding boxes**: outline bbox (font units, from the `glyf` table `xMin/yMin/xMax/yMax`) mapped onto the mask's ink bbox (px, via `np.where`). Work in one raster-px space: place letter i's pen-origin at x = cumulative advance, y = 0; convert mask-local points by subtracting the mask ink bbox min.
- **SCALE**: rasterize at `px = UPM * SCALE`. SCALE=2 gives ~385px stroke thickness — enough for clean skeletonization without being slow. (SCALE=3 makes 6144px masks and is very slow.)
- **One zone per letter, reading order**: for each letter pick its single longest branch (skip nubs < ~400px), assign zone index = letter index.
- **Bent strokes**: letters whose strokes connect (L, T, E, Y) have one bent skeleton branch. Split the branch at sharp bends (>~38° turn) and keep the **longest straight sub-segment** — one word per straight stroke, matching the sketch. (Helper: walk the polyline, split where the direction changes by more than the threshold, return the longest piece.)
- **Ring strokes (the O)**: the O's skeleton is one closed ring (the annular centerline). Don't wrap the word around the full ring (it goes upside-down at the bottom). Use only the **top arc** — from leftmost → topmost → rightmost — so the word reads left-to-right along the top of the O.
- Suggested font for the zone names: **Space Grotesk 700** (readable at small size). Syncopate is an option if you want consistency with the letterform, but legibility favors Space Grotesk. Your call — just state which you chose and why.
- Zone name fill: `#0A161C` (navy, matches bg → knockout). Letter fill: `#68E3BE` (mint).

## Where things go (luci-website repo)

- Generator script: `scripts/gen-hero-stroke-svg.py` (Python; emits the SVG strings).
- Generated data: `src/data/heroStrokeSvg.ts` (exports `heroStrokeWholeSvg`, `heroStrokePropSvg`, `heroStrokeZones`).
- Preview page: `src/pages/hero-stroke-options.astro` (imports the above, renders under `BaseLayout` with `darkHeader`).
- There is already a working version of all three files in place — you may start from them and improve, or throw them out and do your own. Either way, the deliverable is the same: a clean, precise knockout rendering live on the review VM.

`BaseLayout.astro` already loads Syncopate + Space Grotesk from Google Fonts, so the page itself will render the font fine. The generated SVG is self-contained (inline path data + `<textPath>`), so it works offline too.

## Deploy + review workflow (non-negotiable)

The user reviews website work on the **internal review VM at `http://10.10.1.37`**, NOT `localhost`. After every meaningful change:

1. From the luci-website repo root, run `./deploy.sh` (builds `dist/` and rsyncs to `luci@10.10.1.37:/var/www/luci`). It needs SSH to a LAN IP — run it outside any sandbox that blocks network.
2. Tell the user it's live at `http://10.10.1.37/hero-stroke-options/` and remind them to **hard-refresh** (Cmd+Shift+R) — nginx/browser caching can serve stale HTML.
3. If they say "I don't see it," re-run deploy + hard-refresh before debugging code.

## Constraints

- Do **not** modify the canonical brand-font CSS in the luci-design repo. Read the embedded woff2 from it; don't edit it.
- Do **not** touch or resize any master font files or canonical diagram masters. You're generating derived SVG from the font data; the font files themselves stay untouched.
- Keep the change scoped to the three files above (generator, generated data, preview page). Don't refactor the homepage or other components as part of this task.
- The generator is slow (~95s) because of skeletonization on large rasters. That's fine for a one-time generation. If you make it dramatically slower, downsample the mask before skeletonizing (and scale coords back up) — but only if needed.

## What "done" means

- `http://10.10.1.37/hero-stroke-options/` shows "Control your / WHOLE PROPERTY" with the real Syncopate letterforms in mint, and each of the 13 zone names knocked out in navy, sitting cleanly inside one stroke per letter, running along the stroke's true direction, filling the stroke's full length and thickness, each zone appearing once.
- The letters are the actual Syncopate outlines (not hand-drawn approximations).
- You can re-run the generator with `python3 scripts/gen-hero-stroke-svg.py` (add `--debug` to dump per-letter QA PNGs of the mask + skeleton + chosen branches to `/tmp/`).
- Deployed via `./deploy.sh`, and the user can hard-refresh to see it.

Report back: which font you chose for the zone names and why, any letters where the skeleton placement needed special handling (rings vs. bent strokes), and a screenshot or pointer to the live review URL.
