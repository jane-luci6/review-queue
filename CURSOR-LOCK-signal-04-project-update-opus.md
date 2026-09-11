# LOCK — Signal Issue 04 · LUCI Project Update (section 01)

**Role:** `design-direction-open` (Claude Opus 5) · **Status:** DIRECTION LOCKED, Maker-ready
**Date:** 11 September 2026
**For:** GLM Maker — apply this to `ui_kits/newsletter/the-signal-issue-04-september-2026.html` **and** the Webflow pair (`the-signal-issue-04-webflow-head.html` / `-webflow-body.html`)
**Copy source (locked, do not rewrite):** `ui_kits/newsletter/the-signal-issue-04-copy-r3.md` §01
**Too-big reference (do not reproduce):** `CURSOR-NOTE-signal-04-project-update-too-big.png`
**Current build being replaced:** `.proj-snapshot` block — CSS ~L2626–2738, markup ~L2886–2928

---

## 1. Diagnosis — why the two prior passes missed

**The tall version (the too-big PNG)** turns a three-line status note into the issue's biggest visual event: a US map with dotted flight paths, then three portrait photos roughly 800px tall. It outweighs the Aliante field story that immediately follows it, and it makes a rack shot and a building exterior compete as hero images when neither is one.

**The current compact version** overcorrects into thinness. Three cards across an 820px column give each card about 250px, so a 56px thumbnail plus four stacked micro-levels (city 11px, date 11px, property name 14px, sentence 13px) wrap into ragged four- and five-line blocks with unequal bottoms. Four type levels inside a 250px card is more hierarchy than the content can carry. The route line above it (`Lewiston — Tulsa — Las Vegas`) then repeats the same three cities the cards already name, so the section says the geography twice and still reads unresolved.

The content is a **three-item log**, not a gallery and not a grid. It should be built like one.

---

## 2. Spatial thesis — the itinerary ledger

**One column, three hairline-separated rows, read top to bottom in about five seconds.**

The section is a short travel log between the Welcome and the Aliante field story. Its job is to establish *breadth* — three properties, three kinds of work, one month — and then hand off. It earns roughly 380–420px of page height, not 1,400.

Three moves make it work:

1. **Rows, not columns.** A full-column row gives the one-sentence description a real measure, so the type can stay at readable size instead of shrinking to survive a 250px column. Rows also collapse height, because no row reserves the tallest sibling's height. This is the de-boxed hairline-list pattern the house already uses for tabular content (`luci-visual-design.mdc`) rather than a card grid.
2. **The photo is a stamp, not a picture.** A 48px square thumbnail flush at the left of each row acts as a passport stamp — enough to say "we were physically there," too small to invite reading. Photos never gain height; the row height is set by the text.
3. **Geography is carried by the copy, not by chrome.** The opening dek already says "From Lewiston to Tulsa to Las Vegas." That is the route. Delete the dot-and-segment route line and the map — both were redundant, and the map was the origin of the too-big read.

The section reads as its own compact section (centered kicker, like every other Signal section), not as a numbered article and not as a sidebar callout.

---

## 3. Axes considered — recommendation

| Axis | Description | Height | Verdict |
|---|---|---|---|
| **A — Itinerary ledger** | Three hairline rows, 48px square stamp left, name + city on one line, one sentence under it. | ~380px | **RECOMMENDED — build this** |
| **B — Caption strip** | Three landscape photos (3:2, ~180×120) on one line, two-line caption under each. | ~470px | Rejected. More photographic, but three equal photos in a row is still a photo wall in miniature, and it re-opens the "which image is the hero" problem. Keep in reserve only if Jane wants the photos larger. |
| **C — Text-only log** | Same three rows, no thumbnails, date as a micro-label. | ~300px | Rejected. Cleanest and smallest, but Jane said tiny photos are welcome, and the stamps are what make the section feel like field work rather than a bulleted list. |

Build **A**. Do not build B or C unless Jane asks to see them.

---

## 4. Hierarchy — top to bottom

1. **Kicker (unchanged):** existing centered `.kicker` — 28px mint-dark rule · `LUCI Project Update` · 28px rule. Keeps the section visually peer to every other Signal section.
2. **Opening line:** `It's been a busy month for LUCI!` — Space Grotesk 700, left-aligned, deliberately **one step below** an article `.art-title`. This is the section's only piece of scale.
3. **Dek:** `From Lewiston to Tulsa to Las Vegas, our teams have been clearing racks, installing LED displays, bringing systems online, and training the people who will run them.` — Inter, muted, capped measure.
4. **Ledger:** three rows, hairline between, top hairline above the first row.
   - Row content order: **stamp · property name · city, state · (date, only where copy gives one) · one-sentence description.**
   - Property name is the loudest thing in the row; the sentence is the quietest.
5. **Aliante bridge:** the closing line, set apart above by whitespace only (no rule, no box), with a mint-dark `→` leading it. `Aliante` bold in navy. This line is the section's exit ramp into the dark "In the field" section directly below, so it sits close to the section's bottom edge.

---

## 5. Build spec

All values are existing Issue 03/04 tokens. Nothing new is introduced.

### Section

```
.proj-snapshot   background var(--white); padding clamp(36px,5vw,52px) var(--pad)
```

### Opening line

```
font-family var(--body)   /* Space Grotesk */
font-weight 700
font-size   clamp(21px, 2.6vw, 26px)
line-height 1.15
letter-spacing -0.02em
color       var(--navy)
margin      0 0 12px
max-width   24ch
```

No `<em>` gold highlight on this line — the section is too small to carry a half-highlight, and gold is secondary here.

### Dek

```
font-family 'Inter'
font-size   clamp(15px, 1.7vw, 16px)
line-height 1.6
color       #354F5C
max-width   62ch
margin      0 0 clamp(22px, 3vw, 28px)
```

### Ledger rows

```
ul.proj-log            list-style none; margin 0; padding 0;
                       border-top 1px solid var(--rule-light)

li.proj-log__row       display grid;
                       grid-template-columns 48px 1fr;
                       column-gap 16px;
                       align-items start;
                       padding 16px 0;
                       border-bottom 1px solid var(--rule-light)

img.proj-log__stamp    width 48px; height 48px; object-fit cover;
                       border-radius 0; display block
                       /* per-image object-position tuned by hand — see §6 */

.proj-log__head        display flex; flex-wrap wrap;
                       align-items baseline; gap 4px 10px;
                       margin-bottom 5px

.proj-log__name        var(--body) 700 / 15px / -0.01em / var(--navy)
.proj-log__place       'Inter' 500 / 12.5px / var(--navy-muted)
.proj-log__date        'Inter' 600 / 11px / 0.06em / uppercase /
                       var(--mint-dark); margin-left auto
.proj-log__text        'Inter' 400 / 14px / 1.55 / var(--navy-muted);
                       margin 0; max-width 62ch
```

Row height lands at roughly 82–90px, so three rows plus header and bridge total ~380–400px.

### Aliante bridge

```
p.proj-log__bridge     'Inter' 400 / clamp(15px,1.7vw,16px) / 1.6 / #354F5C
                       margin clamp(22px,3vw,26px) 0 0; max-width 62ch
p.proj-log__bridge::before
                       content '→'; color var(--mint-dark);
                       font-weight 700; margin-right 10px
strong                 700, var(--navy)
```

### Mobile (≤640px)

Rows already stack correctly. Only change: `column-gap 12px`, stamp stays 48px, and `.proj-log__date` drops `margin-left:auto` so it sits inline after the city instead of pushing to the right edge.

---

## 6. Photography direction

Three existing files, reused as-is — no new shoot, no re-crop of the masters:

| Row | File | Square crop note |
|---|---|---|
| Clearwater River Casino & Lodge | `assets/since-last-signal/clearwater-river.jpeg` | Rack shot. Center on the equipment faces, not the ceiling or the floor cabling — at 48px the cable tangle reads as noise. |
| Swigs at Osage Casino Hotel | `assets/since-last-signal/osage-swigs.jpeg` | Crop to the LED plane itself. Do **not** frame the LUCI wordmark on the wall — a logo that small is illegible and reads as a smudge. |
| California Casino | `assets/since-last-signal/california-casino.jpg` | Crop to the illuminated facade band, not the full tower. A whole building at 48px is a gray rectangle. |

Verify each stamp at 1× on a white background before shipping. If a crop reads as gray mush, adjust `object-position` — do not enlarge the stamp.

---

## 7. Copy mapping (verbatim from copy-r3 §01)

| Slot | Text |
|---|---|
| Opening line | It's been a busy month for LUCI! |
| Dek | From Lewiston to Tulsa to Las Vegas, our teams have been clearing racks, installing LED displays, bringing systems online, and training the people who will run them. |
| Row 1 | **Clearwater River Casino & Lodge** · Lewiston, Idaho · Live August 24 — The team cleared out equipment and cabling that no longer needed to stay before the property went live. |
| Row 2 | **Swigs at Osage Casino Hotel** · Tulsa, Oklahoma — The crew completed the LED installation across three angled planes and brought the new bar and stage systems onto LUCI. |
| Row 3 | **California Casino** · Las Vegas, Nevada — The crew rebuilt the sportsbook rack, brought the displays online, and trained the property team before heading out. |
| Bridge | Those were the quick stops. At **Aliante**, the work opened onto a much larger canvas. That's the next story. |

Rows 2 and 3 have no date. Leave the date slot empty — do not invent one, and do not substitute a status word to fill the gap.

---

## 8. Explicit do-nots for GLM

- **No map.** No US outline, no city pins, no dotted or dashed connecting paths. This was the single biggest cause of the too-big read.
- **No route line.** Delete `.proj-snapshot__route` (dots + segments) entirely. The dek already names the three cities; naming them twice is what made the old block feel padded.
- **No photo taller than 48px** anywhere in this section. No portrait crops, no 3:2 strip, no full-bleed band, no hover growth.
- **No metric chips or metric lines** — cabinets, panels, hours, displays, square footage. Jane eliminated these on 11 Sep and the copy lock repeats it.
- **No boxes.** No card background fills, no borders around rows, no radii (sharp corners are a brand trait), no drop shadows, no tinted panels. Separation is hairline + whitespace only.
- **No Syncopate.** The masthead owns the issue's one display moment. The opening line is Space Grotesk.
- **No gold in this section at all** — no `<em>` half-highlight on the opening line, no gold dot, no gold rule. Mint-dark carries the date and the bridge arrow; mint is the primary accent here.
- **No bright mint (`--mint`)** on this white canvas. Light-surface accent is `--mint-dark` (`#2b9e80`) only.
- **No CTA button, no "read more," no outbound link.** The Aliante bridge is prose; the field story is the next section on the page.
- **Do not add this section to the table of contents** and do not render a numbered `01` badge. It stays an unnumbered compact section between Welcome and In the field, per the 11 Sep decision. (`§01` in the copy packet is the packet's ordering marker, not a rendered number.) If Jane later wants a number, it goes as a small mint-dark `01` inside the existing kicker — not as a TOC article entry.
- **Do not touch** the Welcome section above, the TOC, or any Aliante field-story chrome below.
- **Do not restyle other sections** to match. This treatment is local to Project Update in Issue 04; it is not a house pattern until Jane says so.
- **Do not ship the desktop build only.** The Webflow head/body pair must carry the same CSS and markup, or the sent issue and the review page disagree.

---

## 9. Definition of done for the Maker pass

1. `.proj-snapshot` CSS block and markup replaced in `the-signal-issue-04-september-2026.html`; `.proj-snapshot__route`, `.proj-snapshot__stops`, `.proj-stop*` rules removed rather than left orphaned.
2. Same treatment mirrored into `the-signal-issue-04-webflow-head.html` and `-webflow-body.html`.
3. Rendered section height between roughly 360px and 430px at 820px column width. If it exceeds 430px, the spec has been over-built — check for restored photo height or an added rule.
4. Each 48px stamp legible at 1×.
5. Copy matches §7 verbatim, including the missing dates on rows 2 and 3.
6. No new CSS custom properties, no new fonts, no new colors.

---

## 10. Open call for Jane

One item is a taste call I made rather than one she stated: **the section stays unnumbered** (centered kicker only), because the 11 Sep decision says it is not a numbered article, while the copy packet labels it §01. If she wants a visible `01`, it belongs in the kicker, and the fix is two lines of CSS — not a re-layout.
