# LUCI Launch Plan Deck — build guide

Everything needed to add slides to the New LUCI Launch Marketing Plan deck without re-deriving the design.

**Files**

| File | Role |
|---|---|
| `../sales/sales-deck.css` | Base slide shell, tokens, fonts, footer furniture. Link **first**. |
| `launch-plan-deck.css` | The patterns in this guide (`.lp-*`). Link **second**. |
| `launch-plan-patterns.html` | Every pattern rendered as a real slide. Copy from here. |
| `new-luci-launch-marketing-plan-brief.md` | The narrative — what each slide has to say. |

**Every slide file starts with exactly this head:**

```html
<link rel="stylesheet" href="../../assets/fonts/luci-brand-fonts.css">
<link rel="stylesheet" href="../sales/sales-deck.css">
<link rel="stylesheet" href="launch-plan-deck.css">
```

Slides are fixed **1280 × 720**. Preview by serving `ui_kits/` and opening the file; do not open with `file://` or the font and asset paths break.

---

## The three rules that are not negotiable

**1. Mint is structure. Gold is a flourish.**
Mint carries every structural mark — kickers, column labels, rules, timeline nodes, spines, counters. Gold appears only as a highlighted phrase inside a headline (`<span class="accent-gold">`) or the single cover rule. Gold is never a section label, never a divider bar, never a category colour.
Use `--mint` on dark canvases and `--mint-dark` (`#2b9e80`) on light. Bright mint on a light background fails contrast at 1.23:1 and is forbidden.

**2. Body copy is Inter. Always.**
Space Grotesk (`--font`) is for headlines, labels, item names, and large numerals. Inter (`--font-body`) is for every sentence — descriptions, notes, captions, list copy. A paragraph in Space Grotesk is a bug.

**3. Syncopate is the display moment, and there is one per slide at most.**
It appears in this deck only as small tracked counters (`.lp-who__num`, `.lp-ask__num`, `.lp-divider__num`) and the `LUCI` wordmark in the footer. Maximum three words, 25 characters, one line. Never a headline, never a sentence.

---

## Standard slide skeleton

Titled slides all share this frame. The head and footer are fixed; only the body changes.

```html
<section class="slide slide--dark">
  <div class="s-head">
    <p class="kicker">Section label</p>
    <h2 class="s-title">Plain statement. <span class="accent-gold">Emphasis here.</span></h2>
  </div>

  <div class="s-body">
    <!-- one pattern from below -->
  </div>

  <div class="s-foot"><span class="s-foot__num">05</span><span class="s-wordmark">LUCI</span></div>
</section>
```

Swap `slide--dark` for `slide--light` to change canvas. Alternate them across the deck so the eye gets a break — roughly dark, dark, light, dark, light. Every pattern below styles itself correctly on both.

---

## Picking a pattern

Choose by **what kind of information it is**, not by how it looks.

| The content is… | Use | Section in CSS |
|---|---|---|
| The deck title | Cover | 1 |
| A breather between sections | Divider | 2 |
| Subjects compared across several kinds of attribute | **Matrix** | 3 |
| Steps in time order | **Timeline rail** | 4 |
| Things that each need a sentence of justification | Definition list | 5 |
| A standing claim plus supporting detail | Split + anchor | 6 |
| Signs of progress | Indicators | 7 |
| Decisions someone must make | Numbered asks | 8 |
| One line that has to land | Statement | 9 |
| A caveat or open question | Note | 10 |

**Matrix vs. timeline is the decision people get wrong.** A matrix compares subjects that all exist at once — its columns are different *kinds* of thing, so each column gets its own visual treatment. A timeline shows one thing moving through stages — every stop gets *identical* treatment, because a timeline ranks by position, not by emphasis. If you want to make a later stage look quieter, it is not a timeline; it is a taxonomy, and it belongs in a matrix.

---

## The patterns

### 1 · Cover

```html
<section class="slide slide--dark lp-cover">
  <div class="lp-cover__frame">
    <img class="lp-cover__logo" src="../../assets/diagrams/luci-full-mint.png?v=1" alt="LUCI Systems">
    <p  class="lp-cover__eyebrow">New LUCI</p>
    <h1 class="lp-cover__title">Launch Marketing Plan</h1>
    <hr class="lp-cover__rule">
    <p  class="lp-cover__deck">One sentence of context.</p>
  </div>
  <footer class="lp-cover__footer">
    <p class="lp-cover__session">Working session &middot; Mike + Mark + Jane</p>
    <p class="lp-cover__stamp">Internal</p>
  </footer>
</section>
```

Title caps at ~15 characters per line before it wraps badly. No footer furniture on the cover.

### 2 · Section divider

```html
<section class="slide slide--dark lp-divider">
  <p  class="lp-divider__num">02</p>
  <h2 class="lp-divider__title">Where the next leads come from</h2>
  <p  class="lp-divider__deck">Optional single line.</p>
  <div class="s-foot">…</div>
</section>
```

Dividers are meant to be sparse. Do not add content to fill them.

### 3 · Matrix

Columns are message types; rows are subjects. Set widths with `--lp-cols`.

```html
<div class="lp-matrix" style="--lp-cols: 210px 320px 1fr;">
  <div class="lp-matrix__head">
    <p class="lp-matrix__label">Audience</p>
    <p class="lp-matrix__label">The path they follow</p>
    <p class="lp-matrix__label">What we build for them</p>
  </div>

  <div class="lp-row">
    <div class="lp-who">
      <span class="lp-who__num">01</span>
      <span class="lp-who__name">Existing<br>customers</span>
    </div>
    <div class="lp-seq">
      <span class="lp-seq__stage">Preview</span>
      <span class="lp-seq__arrow">&rarr;</span>
      <span class="lp-seq__stage">Understand</span>
      <span class="lp-seq__arrow">&rarr;</span>
      <span class="lp-seq__stage">Upgrade</span>
    </div>
    <div class="lp-list">
      <span class="lp-item">Seminar &amp; recording</span>
      <span class="lp-item">What&rsquo;s New one-pager</span>
    </div>
  </div>

  <p class="lp-note">Optional caveat.</p>
</div>
```

Three cell treatments, and they are not interchangeable:

- `.lp-who` — identity. Syncopate counter plus a large Space Grotesk name.
- `.lp-seq` — a progression. Tracked uppercase joined by mint arrows, so it reads as movement rather than a list.
- `.lp-list` — an inventory. Dot-marked Inter that wraps inline.

Rows flex to fill the slide. Two to four rows works; five is cramped. Keep it to three columns — four breaks the reading measure.

### 4 · Timeline rail

Every stop is styled identically. Nesting a definition list inside each stop is the normal use.

```html
<div class="lp-rail">
  <div class="lp-stop">
    <div class="lp-stop__head">
      <span class="lp-stop__label">At launch</span>
      <span class="lp-stop__rule"></span>
    </div>
    <div class="lp-defs" style="--lp-defw: 148px;">
      <div class="lp-def">
        <span class="lp-def__n">LinkedIn</span>
        <span class="lp-def__d">Why it earns its place.</span>
      </div>
    </div>
  </div>
  <!-- more .lp-stop -->
</div>
```

The connector line and node are drawn by CSS pseudo-elements; the last stop drops its connector automatically. Three or four stops fit comfortably.

### 5 · Definition list

Name plus reason. Works inside a timeline stop or on its own. Widen the name column with `--lp-defw` when names are long.

```html
<div class="lp-defs" style="--lp-defw: 148px;">
  <div class="lp-def">
    <span class="lp-def__n">Blog</span>
    <span class="lp-def__d">Answers the problems properties already search for.</span>
  </div>
</div>
```

Keep each reason to one line at the width you have — roughly 90 characters in a full-width column, 70 in a split.

### 6 · Split + anchor

A standing claim on the left, detail on the right.

```html
<div class="lp-split" style="--lp-split: 288px 1fr;">
  <div class="lp-anchor">
    <p class="lp-anchor__name">Website</p>
    <p class="lp-anchor__copy">One or two sentences.</p>
    <p class="lp-anchor__tag">Every channel returns here</p>
  </div>
  <div><!-- rail, defs, or list --></div>
</div>
```

The anchor's mint spine sizes to its own content. `.lp-anchor__tag` is optional and holds the takeaway.

### 7 · Indicators

Built for named signs of progress, not conversion percentages. `.lp-ind__n` can hold a cadence, a count, or a direction — whatever is honest.

```html
<div class="lp-inds" style="--lp-ind-cols: 4;">
  <div class="lp-ind">
    <p class="lp-ind__n">Weekly</p>
    <p class="lp-ind__l">Publishing cadence</p>
    <p class="lp-ind__d">Live and indexed, not sitting in draft.</p>
  </div>
</div>
```

Three or four columns. Do not invent percentages or forecasts.

### 8 · Numbered asks

The slide people are meant to act on, so it is deliberately large.

```html
<div class="lp-asks">
  <div class="lp-ask">
    <span class="lp-ask__num">01</span>
    <div>
      <p class="lp-ask__h">ActiveCampaign Pipelines</p>
      <p class="lp-ask__d">What it unblocks, and by when it has to happen.</p>
    </div>
  </div>
</div>
```

Two or three asks. More than four and it stops reading as a request.

### 9 · Statement

```html
<div class="lp-statement">
  <p class="lp-statement__t">The plan is ready. <em>Two decisions start it.</em></p>
  <p class="lp-statement__d">Optional supporting line.</p>
</div>
```

`<em>` takes mint emphasis and is not italic. Use this with no `.s-head` — the statement is the whole slide.

### 10 · Note

```html
<p class="lp-note">Feature content stays preliminary until Mike confirms the promoted list.</p>
```

Sits last in a slide body. For caveats and open decisions, not for content that matters.

---

## Copy rules for this deck

Full detail is in `.cursor/rules/luci-messaging-voice.mdc`. The parts that bite most often:

- Write **A/V**, never "AV".
- Never call LUCI a "layer". It is an orchestration engine, a platform, infrastructure.
- Lead with what the launch **removes** — steps, systems, handoffs — before what it adds.
- State facts. No "revolutionise", "transform", "empower", "seamless", "best-in-class".
- No percentage claims and no invented metrics. This deck is internal, but the habit carries.
- Titles work best as a plain clause plus a gold emphasis clause: *"Two decisions"* + *"unblock the rest."*

## Before calling a slide done

1. Does the pattern match the kind of information, per the table above?
2. Mint on every structural mark; gold only inside a headline or the cover rule.
3. Every sentence in Inter; every label and name in Space Grotesk.
4. At most one Syncopate element, three words or fewer.
5. Slide numbers and `LUCI` wordmark present, in sequence, on all non-cover slides.
6. Screenshot at 1280 × 720 and confirm the last line clears the footer. `.slide` is `overflow: hidden`, so content that runs past the bottom is silently cut — it will not warn you.
7. Spacing on the 8px scale — 8, 16, 24, 32, 40, 48, 64.
