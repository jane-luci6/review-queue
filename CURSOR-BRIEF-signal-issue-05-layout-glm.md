CURSOR BRIEF
Repo: design (`luci-design` only)
Model: GLM (`luci-cursor --role glm`)
Mode: execute
Job: Lay the approved Signal Issue 05 copy deck into the Issue 05 HTML shell (IMP In Progress page). Layout only. Do NOT rewrite copy.

## Inputs
- Copy deck (source of truth for every word): `LUCI Systems Design System/ui_kits/newsletter/the-signal-issue-05-copy.md`
- Shell to edit IN PLACE (keep the filename): `LUCI Systems Design System/ui_kits/newsletter/the-signal-issue-05-october-2026.html`
- Layout/token reference (prior issue, follow its patterns): `LUCI Systems Design System/ui_kits/newsletter/the-signal-issue-04-september-2026.html` (welcome, TOC, proj-log, field opener/property/stats/scale/num blocks, quick-tip, whats-coming, mike column, closing)
- Fan image: copy `ui_kits/newsletter/signal-05-reporting-analytics-fan.png` (repo root path) to `LUCI Systems Design System/ui_kits/newsletter/assets/whats-coming/signal-05-reporting-analytics-fan.png` and reference it relatively from the shell as `assets/whats-coming/signal-05-reporting-analytics-fan.png`. Check the path matches how other `assets/...` images in the Issue 04 shell are referenced, so `npm run build:review` carries it into `ui_kits/review/newsletter/`.

## Do
1. Replace every lorem/CoS-traffic placeholder in the shell with the deck copy, section by section, in the shell's existing order: Welcome → TOC → Project Update → In the Field (+ outcomes block) → Design with LUCI → Advice → Happenings → Quick Tip → What's Coming (with fan image + What's New two-pager promo callout) → A Minute with Mike → Need a hand → Closing → Footer.
2. Remove the top "Issue 05 traffic … no deploy" CoS banner and the separate "What's New · slot locked" CoS block (its promo now lives inside What's Coming). Replace the banner with a slim DRAFT status strip: "DRAFT · Signal Issue 05 · first draft for Mike review · placeholders highlighted".
3. Remove any "Sand Springs" text left in the shell (Field is Osage Casino Hotel – Ponca City, Oklahoma). Update the field-property line accordingly.
4. TOC: renumber to match the sections actually present, use the deck's labels, and show the Advice entry as the placeholder name.
5. PLACEHOLDERS MUST BE VISIBLY HIGHLIGHTED: wrap every `[… — TBD]` (and photo/diagram placeholders) in `<mark class="tbd">…</mark>`. Add one small CSS rule in the shell's style block, e.g. `.tbd{background:#FFE58A;color:#10232D;padding:0 .25em;border-radius:3px;font-weight:600;}`, plus a dark-surface variant if a placeholder sits on navy. Photo placeholder boxes keep the dashed treatment and show their caption.
6. Keep existing tokens, fonts (embedded @font-face), classes, and responsive behavior. Reuse Issue 04 component classes rather than inventing new ones. Keep the support-portal and footer blocks.
7. Advice section: use the deck's two blurbs under the `[ADVICE SECTION NAME — TBD]` kicker/title.
8. Validate: HTML parses, no lorem ipsum left, no "Sand Springs", no "D3", no "property-by-property", no "launched", fan image path resolves on disk.

## Don't
- Don't change copy wording (except wrapping placeholders in `<mark>`).
- Don't touch luci-website, Webflow, or ActiveCampaign. Don't deploy (the operator deploys separately). No pricing.
- Don't edit other issues' files.

## Report
List: sections filled, placeholders highlighted (count + list), asset path used, any copy you couldn't place.
