CURSOR BRIEF
Repo: design (`luci-design` only)
Model: GLM (`luci-cursor --role glm`)
Mode: execute
Job: Rebuild Signal Issue 05 on Issue 04's exact template. Layout/markup only. DO NOT CHANGE ANY COPY.

## Files
- EDIT (overwrite in place, keep the filename): `LUCI Systems Design System/ui_kits/newsletter/the-signal-issue-05-october-2026.html`
- TEMPLATE (copy its head, CSS, scripts, masthead, TOC, section/component markup exactly): `LUCI Systems Design System/ui_kits/newsletter/the-signal-issue-04-september-2026.html`
- Secondary reference for consistency: `the-signal-issue-03-august-2026.html` (same family as 04)
- COPY SOURCE (every word stays exactly as in the current Issue 05 HTML; the deck is a backup reference): current Issue 05 HTML + `LUCI Systems Design System/ui_kits/newsletter/the-signal-issue-05-copy.md`

## Why
Jane: Issue 05 doesn't look like the other newsletters. The CSS block is already identical to Issue 04 (the only addition is `.tbd`). The problem is the MARKUP. Issue 05 was built on an old CoS placeholder shell that uses different section bands and simplified components, instead of Issue 04's components.

## Mismatches to fix (Issue 05 now → match Issue 04/03)
1. In the Field opener band: `sec--sand` → `sec--deep` with `style="border-bottom: 4px solid var(--mint);"`, exactly like 04 `#field-story`.
2. Field body: currently a plain `sec--white` with `art-body` paragraphs. Use 04's body section: `<section class="sec sec--light" aria-labelledby="field-story-title" style="padding-top: clamp(40px, 6vw, 64px); padding-bottom: 0; border-bottom: none;">` with `field-num` blocks (`field-num__head` / `field-num__rule` / `field-num__body`), `field-pair` + `field-runs field-runs--inline field-runs--pair` with icon list items (`field-runs__item--icon` + `field-runs__ic` svg + `field-runs__txt`, reusing 04's icon SVGs), and 04's `field-readmore` block for the case-study link line (keep the `[CASE STUDY URL — TBD]` mark visible in the link/line). No field-num titles exist in the copy: do NOT invent titles. Use field-num blocks without a head, or the closest 04 pattern that needs no new words. Put the second "Photo TBD: Osage Project Media" placeholder where 04's `field-slider-figure` sits, as a static 16:9 placeholder figure using the `field-ba__caption` caption class. Omit 04's `field-scope` ticker (there's no sourced data for it).
3. Field photo placeholder: currently an inline-styled grey div. Make it the same box size/position as 04's `field-scale__band` video (16:9), styled as a dashed placeholder, with the `field-scale__caption` caption.
4. Kicker numbers: remove every `<span class="kicker__num">` (04 and 03 don't use them). Kicker markup = rule / label / rule, exactly as in 04.
5. Quick Tip: `sec--mid` → `sec--dark`. Put the steps in 04's `quick-tip__media` wrapper with `ol.steps.steps--dark` and `<li><p>…</p></li>` items. There's no video/screenshot, so omit `quick-tip__shot` but keep the 04 wrapper/spacing.
6. What's Coming: `sec--white` → `sec--light`. Fan image goes in 04's `figure.ui-shot.ui-shot--lg` with `<img>` (src `assets/whats-coming/signal-05-reporting-analytics-fan.png`, keep the alt) and `figcaption.ui-shot__cap`. Replace the inline-styled `callout` blocks (10 inline styles) with 04's components: the What's New two-pager promo goes in 04's `beta-note` block (heading/lines from the copy). The 24-hour / 7-day / 30-day views stay as copy in an existing 04 pattern; no inline styles.
7. Minute with Mike: `sec--light` → `sec--white`. Use 04's `article-head article-head--mike` with `article-head__text` (kicker, art-title, art-deck) + `article-head__art` with the same Mike portrait `<img class="mike-portrait" src="https://s3.amazonaws.com/webflow-prod-assets/62d7d68d14611c2a31d863cd/6aa987c809a45884e4a15a8c_mike-epstein.jpg" …>`. End with 04's `author-card author-card--mike` (Mike Epstein / CEO, LUCI Systems) instead of `art-signoff`. No pullquote: there's no pullquote copy, so don't invent one.
8. Project Update: use 04's `proj-snapshot` / `proj-log__row` markup INCLUDING the `proj-log__stamp` image slot. Since there are no photos, render the stamp slot as a same-size dashed placeholder (an element with class `proj-log__stamp` plus a placeholder modifier, no inline styles). Placeholder text stays `<mark class="tbd">`.
9. Design with LUCI / Advice / Happenings (no direct 04 equivalent): build them like 04's `#from-luci` section (`sec`, kicker rule/label/rule, `art-title` with `<em>`, `art-deck` if the copy has a dek, `art-body`). The design diagram placeholder goes in a `figure.ui-shot` box (dashed, same width as 04 ui-shot), not an inline-styled `<p>`. Advice blurb subheads: use an existing 04/03 subhead class that suits art-body (not `field-num__title` out of context). If none exists, add one minimal rule next to `.tbd`.
10. Band rhythm (white/light alternation like 04; deep/dark only where 04 uses them): Welcome `sec--white` · Project Update `sec--white proj-snapshot` · Field opener `sec--deep` + body `sec--light` · Design with LUCI `sec--white` · Advice `sec--light` · Happenings `sec--white` · Quick Tip `sec--dark` · What's Coming `sec--light` · Mike `sec--white` · Need a hand `sec--sand need-hand` · closing/footer exactly as 04.
11. DRAFT strip: currently a full `aside.sec.sec--sand` band with inline padding. Replace it with ONE slim line (about 28–32px tall), placed above the masthead: small caps text "DRAFT · Signal Issue 05 · first draft for Mike review · placeholders highlighted", ~11–12px, a yellow (#FFE58A) or navy bar, full width. One small CSS rule (`.draft-strip`) next to `.tbd`. No other chrome changes.
12. Masthead, TOC, closing, footer, `<head>`, fonts, and scripts: byte-for-byte Issue 04 structure, swapping only issue number/date/numeral/title text and TOC labels from Issue 05. Keep `[Theme — TBD]` highlighted (`tbd--dark`) in the masthead. Keep 04's field-slider script only if a slider is present (it won't be, so it can stay harmlessly or be dropped).
13. No inline `style=""` attributes beyond the ones Issue 04 itself uses (e.g. the field band border, the field body padding, proj-log stamp object-position).

## Hard rules
- COPY IS FROZEN. Every visible word, punctuation mark, and placeholder in Issue 05 stays exactly as it is now. Same set of 21 `<mark class="tbd">` placeholders (count may differ only if a placeholder moves into a stamp/placeholder box; list any change). Don't add titles, captions, pullquotes, or stats that aren't in the copy.
- Keep `.tbd` / `.tbd--dark` yellow highlight.
- No "Sand Springs", no lorem, no new vendor names.
- Don't edit Issue 04/03 or any other file except the Issue 05 HTML (and, if needed, the single CSS additions inside that file's style block).
- Don't deploy, push, or touch luci-website / Webflow / ActiveCampaign. No pricing.

## Validate before finishing
- `diff` of visible text (tags stripped, whitespace collapsed) between the old and new Issue 05: report any wording difference (should be none, apart from removed kicker numbers "02/03…" and DRAFT strip wording if shortened).
- Classes used in 05 ⊆ classes defined in the CSS (plus draft-strip/tbd/placeholder modifier).
- Section band classes match the list in item 10.
- HTML parses; fan image path resolves.

## Report
Changes per section, final band list, placeholder count, any copy diffs (should be none).
