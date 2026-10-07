# CURSOR BRIEF — Belterra Park STB-6500 setup guide: professional redesign

**Asked by:** Jane · **Date:** 2026-10-07
**File to rebuild:** `LUCI Systems Design System/ui_kits/guides/belterra-park-lg-stb-setup-guide.html`
**Source content (locked — do not rewrite):** `/Users/janehaynie/Downloads/LUCI - Belterra Park LG Setup Guide.pdf`
**Current-state screenshots:** `.tmp-grok-briefs/belterra-stb-guide/current-p1.png` … `current-p4.png`
**Review surface:** `http://10.10.1.37:8080/guides/belterra-park-lg-stb-setup-guide.html`

---

## 1. What this document is

A **bench-setup field guide** for a LUCI tech configuring 20+ new LG STB-6500 set-top boxes at Belterra Park. The tech is standing at a bench, box in one hand, remote in the other, glancing at this sheet between button presses. It is printed and written on (the Install Log).

That use case drives every design decision:

- **Scannable at arm's length.** Values the tech has to type (IPs, ports, codes) must be the most visible thing on the page.
- **Never lose your place.** Step numbers must be big, steady, and continuous (1–25).
- **Prints clean.** It's a working document, so it has to look good in grayscale and on an office laser printer.
- **Professional, not decorated.** It should read like a precision instrument manual from a premium hardware company, not a marketing brochure. The bar: Apple's or Sonos's installer guides, set in LUCI's brand.

The content is final. **Do not reword, cut, or reorder procedure steps or values.** You can restructure *presentation* freely: grouping, which page things sit on, labels and headers.

---

## 2. What went wrong in v1 (fix every item)

Look at the four `current-p*.png` screenshots alongside this list.

### Critical: content is hidden (ship-blocker)

1. **Mid-page navy bands overlap the content above them.** `.doc-page-band` uses `margin: calc(-1 * var(--page-pad)) …` to pull itself flush to the *top edge* of a sheet. That only works when the band is the **first** element on the page. Placed mid-page, the negative top margin slides the band up over the previous block. Result:
   - Page 1: the **Pro:Centric mode → Manual → HTML** settings row is hidden behind the Step 1 band.
   - Page 2: **step 13 (Connect / No DNS error is normal)** is hidden behind the Step 3 band.
   - Page 3: **steps 24 (Repack) and 25 (Complete the log)** are hidden behind the Troubleshooting band.
   - `fit-check.py` reported "All pages fit" because overlapping content doesn't add height. **Fit-check can't catch this — you must look at the screenshots.**

### Design failures

2. **Too many heavy navy bands.** Six full-bleed dark bands in four pages. They chop the document into slabs, compete with the content, and break the house rule (no full-bleed dark band mid-document; see `luci-sales-document-system.mdc`). They also waste print toner.
3. **The 4-column table is mostly empty.** In Steps 2 and 3, 14 of 18 rows have blank "Enter" and "You should see" cells, so the page reads as a sparse spreadsheet with a wall of whitespace on the right.
4. **Typography is off-brand.** The page loads Google Fonts but body copy inherits `var(--font)` (Space Grotesk) from `sales-document.css`. **All non-head copy must be Inter.** Sales/print docs must use `../../assets/fonts/luci-brand-fonts.css`, not a Google Fonts `<link>` (see the PDF export standard in `luci-sales-document-system.mdc`).
5. **Weak masthead.** The LUCI mark alone, at 26px, plus a plain 26px title doesn't look like a finished, branded document. There's no Belterra presence and no clear document identity.
6. **Gold "Setup" title accent on light** uses `--gold-deep` as text. That violates the dual-accent rule (`--gold-deep` is non-text only; gold text only on dark).
7. **Installer codes card breaks.** "Menu ×10 → 9 8 7 6" wraps across two lines in a cramped two-column grid, and the label "Installer menu" wraps too.
8. **Factory-reset step numbers are misaligned.** The `::before` counter sits in the grid's first column, but the text column starts later. Numbers float at the left margin, unrelated to the text.
9. **Uneven page fill.** Pages 1–3 have large dead zones at the bottom while content is crammed (and hidden) above.
10. **Install Log has no write-in affordance.** The MAC Address and Initials columns are blank space with no line to write on, and the checkboxes are tiny (13px).
11. **Code chips everywhere.** Every IP gets a tinted pill, even inside sentences, so nothing stands out because everything does.

---

## 3. Design direction

### Overall concept: "instrument manual"

A calm, precise, light document. Structure comes from **typography, a strong left rail of step numbers, and hairlines**, not dark slabs. Dark navy appears **once**: a compact header band at the top of page 1 that carries the brand. Everything else is off-white canvas.

### Page architecture (4 sheets, US Letter)

| Sheet | Contents |
|---|---|
| **1 · Overview** | Branded header band (only dark element in the doc) → intro + "Before you start" → **Settings at a Glance** as the hero reference panel → **Step 1** (steps 1–4) |
| **2 · Configure** | **Step 2 · Network** (steps 5–13) → **Step 3 · LUCI server** (steps 14–22) |
| **3 · Finish + fix** | **Step 4 · Finish** (steps 23–25) → **Troubleshooting** → **Factory reset (InStop)** |
| **4 · Install Log** | Fill-in worksheet, rows 155–174 + blank overflow rows if they fit |

If any sheet doesn't fit, **add a page** (page-count invariant). Never shrink type below the minimums in §4, and never cut content.

### 3.1 Page-1 header band (the one dark moment)

- Full-bleed navy band **at the very top of sheet 1** (the only position where the `.doc-page-band` negative-margin trick is valid). Keep the circuit texture and the 4px mint bottom rule.
- **Left:** LUCI full logo `assets/logos/luci-full-mintmark-white.png` (copy into `ui_kits/guides/assets/` per canonical-assets rule), ~26px tall.
- **Right:** Belterra Park logo. Use `ui_kits/sales/assets/clients-mono/belterra-park.png` (RGBA, transparent). On navy, render it white via `filter: brightness(0) invert(1)` scoped to this band only, ~30px tall, ~0.9 opacity. Copy it into `ui_kits/guides/assets/` too.
- Between/below: mint kicker `FIELD SETUP GUIDE`, then title **"LG STB-6500 Pro:Centric Setup"** in Space Grotesk 700, ~30px, off-white, with **"Pro:Centric Setup"** in bright `--gold` (allowed: gold text on dark).
- Optional thin meta row inside the band (Inter 11px, 60% off-white): `Belterra Park · Cincinnati, OH · Rev 1 · Oct 2026`.

### 3.2 Settings at a Glance — the hero reference panel

This is the most-used part of the document. Make it unmistakable.

- Contained panel: `--tint` fill, **4px mint (`--accent-light`) top rule** (not gold-deep; this is structure), sharp corners, ~20px/24px padding.
- Label: `SETTINGS AT A GLANCE` (Space Grotesk 700, 11px, tracked 0.18em, `--accent-light`).
- **Two-column definition grid, 7 rows, every row visible** (verify!):
  - IP Address → `10.14.153.155` + small Inter note "first box, then count up (156, 157, 158…)"
  - Subnet Mask → `255.255.252.0`
  - Gateway → `10.14.152.1`
  - DNS → "Leave blank"
  - Pro:Centric Server IP → `10.14.152.30`
  - Server Port → `2126`
  - Pro:Centric Mode → "Manual → HTML"
- Values: **monospace, 17–18px, 600, `--ink-strong`**, left-aligned in the value column (right-aligned numbers in a two-col grid look ragged). Labels: Space Grotesk 600, 11px, uppercase, `--navy-muted`.
- Hairlines between rows, none around the outside.

### 3.3 Section headers (replaces mid-page navy bands)

A light, typographic lockup per step. This is the house section-lockup pattern adapted for print:

```
STEP 2                                   ← Space Grotesk 700, 11px, tracked 0.18em, --accent-light
Network configuration                    ← Space Grotesk 700, 22px, --ink-strong, -0.02em
━━━━ (40×3px --accent-light rule)
Set a static IP on the box.              ← Inter 14px, --ink (optional one-line deck)
```

- Optional: a large ghosted step numeral ("2") behind the lockup, `rgba(43,158,128,0.08)`, ~96px, like the `.doc-secnum` device. Only if it doesn't crowd.
- Space above a section header: 32px; below the rule: 16px. **No negative margins.**

### 3.4 Procedure steps: a two-tier row, not a 4-column table

Replace the sparse 4-column grid with a **step row** that only shows what exists:

```
┌────┬─────────────────────────────────────────────────────────────┐
│ 10 │ IP Address                        10.14.153.[label number] │
│    │ e.g. 10.14.153.155                                          │
└────┴─────────────────────────────────────────────────────────────┘
```

- **Left rail (0.5in):** step number, Space Grotesk 700, 20px, `--accent-light`, tabular numerals, `01`–`25` zero-padded, continuous across the document.
- **Action** (the thing to select/do): Space Grotesk 600, 14.5px, `--ink-strong`. Menu items to press can be bold.
- **Enter value** (only when present): right-aligned on the same line, **monospace 15px 600 `--ink-strong`** inside a subtle chip (`--tint` bg, 4px radius, 2px 8px padding). This is the only place chips appear.
- **"You should see"** (only when present): second line under the action, Inter 12.5px, `--ink`. For warnings/expected results, prefix with a small label: `EXPECT` (mint) for normal outcomes, `CAUTION` (Inter 600, `--ink-strong`, with a 3px `--gold-deep` left tick) for "Do not unplug the box during the download."
- Rows separated by 1px `--rule-light` hairlines; ~10px vertical padding. Rows with only an action stay single-line and compact.
- **Menu-path compression (allowed, presentation only):** Steps 5–8 are pure navigation. Keep each as its own numbered row (numbering must match the source), but they can be tighter (8px padding). Do **not** merge them into one row, because techs cross-check numbers.
- Column header row ("Select / Do · Enter · You should see") is **not needed** with this structure. Drop it.

### 3.5 Inline values in sentences

Inside running sentences (intro, troubleshooting, prereq), set IPs/codes in monospace 600 `--ink-strong` **without** the tinted chip. Chips are reserved for "Enter" values in procedure rows.

### 3.6 Troubleshooting

- Section lockup (§3.3) with kicker `TROUBLESHOOTING`, title "When a box won't set up".
- Two-column rows: **Problem** (Space Grotesk 700, 14px, `--ink-strong`, ~1.9in column) | **What to do** (Inter 13px bullets, short 8×2px `--accent-light` dash markers).
- Hairlines between problems.

### 3.7 Factory reset (InStop)

- A **contained caution panel**: `--tint` bg, **4px `--gold-deep` left bar** (gold-deep is fine as a non-text structural mark), 20px padding.
- Header inside: `FACTORY RESET · INSTOP` (11px tracked, `--accent-light`) + "Only if setup failed. This erases the box's configuration." (Inter 13px, `--ink-strong`).
- Four numbered sub-steps using the same left-rail step-row as §3.4 (numbers `R1`–`R4` or `1`–`4` in a smaller 16px numeral, **aligned to the text baseline**).
- **Drop the separate installer-codes card.** The codes are already in the steps as chips (`9 8 7 6`, `117`, `413`, `0413`). Duplicating them was the v1 card that broke. If space remains, a single-line strip is OK: `Codes · Menu ×10 → 9876 → Exit · 117 → Menu · 413 → OK · 0413`, with `white-space: nowrap` per item.

### 3.8 Install Log (sheet 4): a real worksheet

- Section lockup: kicker `INSTALL LOG`, title "One line per STB", one-line Inter instruction.
- Columns: **Label · IP Address · STB MAC Address · Server Found · Box Marked · Initials**. Give MAC the widest column (~2.1in); it's 17 characters handwritten.
- Pre-printed Label (mono 600, `--accent-light`) and IP (mono 500, `--ink-strong`).
- **Write-in cells get a visible baseline:** a 1px `--navy-muted` at ~40% opacity bottom border inset inside the cell, so the tech knows where to write. Hairline row separators stay `--rule-light`.
- Checkboxes: **16px**, 1.5px `--navy-mid` border, sharp corners, centered in their columns.
- Row height ≥ 0.34in (handwriting needs room). Light zebra (`rgba(16,35,45,0.025)` on even rows) is allowed to help the eye track across.
- If space remains below row 174, add **2–4 blank rows** (Label/IP cells empty with write-in lines) for "Add lines past .174 as needed."
- Footer note under the table: Inter 12px.

### 3.9 Running footer (every sheet)

- Left: `LUCI · Belterra Park · LG STB-6500 Pro:Centric Setup`
- Right: `Page 1 of 4`
- Hairline above; 10px Inter; `--navy-muted`. Keep the existing `.doc-foot` pinning.

---

## 4. Type and color spec (non-negotiable)

**Fonts:** link `../../assets/fonts/luci-brand-fonts.css`. **Remove the Google Fonts `<link>`.**

| Role | Font | Size / weight | Color |
|---|---|---|---|
| Doc title (band) | Space Grotesk | 30px / 700 | off-white + `--gold` accent span |
| Section title | Space Grotesk | 22px / 700 | `--ink-strong` |
| Kicker / labels | Space Grotesk | 10.5–11px / 700, tracked 0.16–0.18em, uppercase | `--accent-light` (light), `--mint` (dark band) |
| Step numerals | Space Grotesk | 20px / 700, tabular | `--accent-light` |
| Step action | Space Grotesk | 14.5px / 600 | `--ink-strong` |
| Body / notes / "you should see" / bullets | **Inter** | 12.5–14px / 400–500 | `--ink` |
| Values (IP, port, codes) | mono stack (`--mono`) | 15px in rows, 17–18px in settings panel / 600 | `--ink-strong` |

- **No Syncopate.** This is a working document. Space Grotesk carries the title.
- **Accents:** mint/`--accent-light` is primary (kickers, numerals, rules, structure). Gold appears only as **bright `--gold` text in the dark header band** and as **`--gold-deep` non-text marks** (caution bars/ticks). Never `--gold-deep` as text.
- **Minimum sizes:** nothing below 10px; body copy ≥ 12.5px; values ≥ 15px.
- Spacing on the 8px scale (4px only for tight type). Sharp corners except the 4px chip radius.
- Body ≥ 4.5:1 contrast. Check grayscale: step numerals and values must still read when printed black-and-white.

---

## 5. Build constraints

- Keep linking `../sales/sales-document.css` for tokens, `.doc`, `.doc-page`, `.doc-foot`, and print rules. Add page-scoped classes in the guide's `<style>` (prefix `guide-`). **Do not edit `sales-document.css`.**
- **Use `.doc-page-band` only as the first child of sheet 1.** Nowhere else. Any other band-like element must have zero negative margins.
- Copy logos into `ui_kits/guides/assets/` and reference them relatively with `?v=1`.
- Add any new filled surfaces (tint panels, zebra rows, header band) to an `@media print { … print-color-adjust: exact }` block.
- Strip scaffolding: no `.doc-hub-link` in print (already hidden), no draft badges, no comments describing the change.

---

## 6. Verification (do all of these, in order)

1. **Content audit against the source PDF.** Count that all of these render visibly in the screenshot: 7 settings rows, steps 01–25, 3 troubleshooting problems (with all 4 bullets under "Server not found"), 4 reset steps, Install Log rows 155–174. Every IP/port/code matches the PDF character for character.
2. **Overlap check (fit-check can't catch this).** Run a probe in headless Chrome: for every pair of adjacent block children in each `.doc-page`, assert `next.top >= prev.bottom`. Any negative gap is a failure.
3. `python3 scripts/fit-check.py ui_kits/guides/belterra-park-lg-stb-setup-guide.html`: every sheet must report OK, and the last block must clear the footer by ≥ 24px.
4. **Screenshot all four sheets** (headless Chrome, 900px wide, scale 1) and look at them. Check for wrapping values, orphaned single rows, and dead zones larger than ~1.5in at the bottom of sheets 1–3. Rebalance by moving whole sections between sheets, not by shrinking type.
5. **Grayscale check:** screenshot with `filter: grayscale(1)` on `body` and confirm the hierarchy still reads.
6. **Print to PDF** with `bash scripts/render-pdf.sh ui_kits/guides/belterra-park-lg-stb-setup-guide.html /tmp/belterra-guide.pdf` and confirm 4 pages, no blank trailing page, fonts embedded (`pdffonts`, no Type 3).

## 7. Deploy and hand-off

- Deploy to the hub copy on `.37` (it's not covered by the website's `rsync --delete`):
  ```
  SSH="ssh -i ~/.ssh/id_ed25519_luci_vm -o StrictHostKeyChecking=no"
  rsync -avz -e "$SSH" ui_kits/guides/belterra-park-lg-stb-setup-guide.html luci@10.10.1.37:/var/www/luci-hub/guides/
  rsync -avz -e "$SSH" ui_kits/guides/assets/ luci@10.10.1.37:/var/www/luci-hub/guides/assets/
  rsync -avz -e "$SSH" assets/fonts/ luci@10.10.1.37:/var/www/luci-hub/assets/fonts/
  ```
  Then `curl` the page, the logos, and `luci-brand-fonts.css` and confirm 200s.
- Commit with a descriptive message. Don't add a decision-log entry unless Jane locks a direction.
- Report to Jane with the URL `http://10.10.1.37:8080/guides/belterra-park-lg-stb-setup-guide.html`, the four sheet screenshots embedded inline, a reminder to hard-refresh (Cmd+Shift+R), and the PDF path.

## 8. Definition of done

- Zero hidden or clipped content (verified by the overlap probe + visual check).
- One dark element (the page-1 header band). Everything else is light, typographic, and hairline-structured.
- Values are the most legible thing on every sheet.
- Inter body, Space Grotesk heads, mono values, brand fonts file, no Google Fonts.
- Install Log is something a tech can actually write on.
- Looks like a premium hardware vendor's installer guide wearing LUCI's brand.
