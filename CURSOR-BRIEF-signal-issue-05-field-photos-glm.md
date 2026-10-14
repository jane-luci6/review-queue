CURSOR BRIEF
Repo: design (`luci-design` only)
Model: GLM (`luci-cursor --role glm`)
Mode: execute
Job: Fill the two photo slots in Signal Issue 05 "In the Field" with the processed Osage photos, in the Issue 04 style. Layout only. Do NOT change any copy outside the captions/alt text given here.

## File to edit IN PLACE
`LUCI Systems Design System/ui_kits/newsletter/the-signal-issue-05-october-2026.html`
Style reference: `LUCI Systems Design System/ui_kits/newsletter/the-signal-issue-04-september-2026.html` (its `field-scale` band and its `figure.field-slider-figure` before/after slider).

## Photos (already in the repo; reference them relatively, exactly like other `assets/...` paths in the Issue 05 file)
All are 1600x900 JPEGs in `LUCI Systems Design System/ui_kits/newsletter/assets/in-the-field/`:
- `assets/in-the-field/osage-led1-wall-finished.jpg` — finished flat LED wall (LED install 1, Swizzle)
- `assets/in-the-field/osage-swigs-live-wall.jpg` — Swigs three-plane LED wall live with sports sources
- `assets/in-the-field/osage-swigs-install.jpg` — Swigs wall during cabinet installation (BEFORE)
- `assets/in-the-field/osage-swigs-multiview.jpg` — the same Swigs wall commissioned, multi-source layout (AFTER; same framing as the install shot)

## Slot 1: the `field-scale` band in `section#field-story` (currently `<div class="field-photo-ph">` + caption "Photo TBD: Osage Project Media")
Replace the placeholder with a small 2-up photo gallery inside the existing `.field-scale__band` (this is where Issue 04 had its video):
- Markup: `<div class="field-gallery">` with two `<figure class="field-gallery__item">`, each holding `<img class="field-gallery__img" ... width="1600" height="900" loading="lazy">` and a small label `<span class="field-gallery__tag">Swizzle</span>` / `<span class="field-gallery__tag">Swigs</span>` styled like Issue 04's `.field-slider__tag` (small uppercase pill over the bottom-left corner of the image).
  - Left: osage-led1-wall-finished.jpg, alt "Swizzle at Osage Casino Hotel — Ponca City: the finished LED wall displaying the LUCI logo"
  - Right: osage-swigs-live-wall.jpg, alt "Swigs at Osage Casino Hotel — Ponca City: the three-plane LED wall live with multiple sports sources above the stage and bar"
- Caption (replace "Photo TBD: Osage Project Media", keep `field-scale__caption`): "Swizzle and Swigs, the two venue phases of the latest expansion, on the same LUCI foundation."
- CSS: add a few rules in the existing `<style>` block near the other `.field-scale` rules: `.field-gallery{display:grid;grid-template-columns:1fr 1fr;gap:12px}` `.field-gallery__item{position:relative;margin:0}` `.field-gallery__img{display:block;width:100%;height:auto;aspect-ratio:16/9;object-fit:cover;border-radius:` same radius the Issue 04 video/slider uses `}`; tag styles copied from `.field-slider__tag`; and a mobile rule (`@media (max-width: 600px)`) that stacks to one column. Reuse existing tokens/variables; don't restyle anything else.

## Slot 2: `figure.field-slider-figure` in the light body section (currently a `field-photo-ph` + "Photo TBD: Osage Project Media")
Replace with Issue 04's before/after slider markup, copied exactly (same classes, same `data-field-slider`, range input, divider, Before/After tags). The page already has the slider script and CSS; don't duplicate them.
- Base (after) image: osage-swigs-multiview.jpg, alt "The commissioned three-plane Swigs LED wall running a multi-source video layout", width="1600" height="900"
- `.field-slider__before` image: osage-swigs-install.jpg, alt "The three-plane Swigs LED wall during cabinet installation", width="1600" height="900"
- Range `aria-label`: "Drag to see the Swigs wall move from installation to live programming"
- Caption (`field-ba__caption`): "Drag to see the three-plane wall move from installation to live programming."

## Rules
- Touch only these two slots and the new CSS rules. Do not edit any other copy, section, or image.
- No other images. No external URLs.
- Don't deploy, push, or edit other files.
- After editing, confirm both slots render images (no remaining `field-photo-ph` inside `section#field-story` or the following Field body section; the Design with LUCI placeholder further down must stay).
