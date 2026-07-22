# Design rules redesign — working notes (scratch, not a shipped rule)

Goal: ONE design rules file every agent references for every design effort. Unify on the NEW system (rounded, soft cards); retire the old sharp/de-boxed system. No redesigning already-shipped / already-redesigned assets. Room for per-asset variation (Website ≠ Guide ≠ Sales doc ≠ Case study). Single source of truth for hard rules (fold redundant restatements).

## Framing decisions (from kickoff)
- Unify on new system (rounded, soft cards, soft shadows, gradients OK). Retire old sharp/de-boxed system.
- Do NOT redesign shipped/already-redesigned assets (newsletter already sent; others already redesigned).
- ONE design rules file; every agent references it for every design effort.
- Per-asset variation layer needed (Website / Sales docs / Case studies / Guide / Legacy-frozen).
- Single source of truth for hard rules (Inter-for-body, Syncopate-≤3-words, #2b9e80-on-light, 3-tier fonts) — state once, pointers elsewhere.

## Batch 1 — Framing + Spacing (decided)
- R1 KEEP+MODIFY — Track by copy density. ADD a dark/light switch by section: default darker themes for web-hosted content, lighter themes for PDFs (printability; web isn't meant to be printed).
- R2 MODIFY — Newsletter (web) = Track A. Newsletter EMAIL = Track C. (Correct track assignments.)
- R3 KEEP — Apply in order: Foundation → Track → Channel.
- R4 KEEP — Validate against §8 checklist before shipping.
- R5 KEEP — 8px base unit (8,16,24,32,40,48,64,96,128).
- R6 KEEP — 4px only legal half-step (tight type: label-to-number, icon-to-text).
- R7 KEEP — Never off-scale; round to nearest 8 (or 4 exception).
- R8 KEEP — Fluid clamp(min, vw, max), on-scale min/max.

## Batch 2 — Layout + Typography §3.1 (decided)
- R9+R10 MERGED+REFRAMED — Body copy measure: cap at ~60–70ch ONLY for sustained multi-paragraph reading, AND ONLY when the remaining column space has a purpose (image/pattern/sidebar/pull-quote/sticky TOC/offset). NEVER leave an empty gap beside shortened text — if no purpose for the space, let text run to the content-column width. Short blocks (sentence/card/1–2 line intro) don't cap. Honest guardrail: 140+ char lines on a wide canvas hurt sustained reading — for long-form, give the space a purpose (don't orphan, don't run ultra-long lines). Decoration to justify a cap only when it earns its place.
- R11 KEEP — Fluid side padding clamp(28px, 6vw, 60px).
- R12 KEEP+MODIFY (three-tier fonts):
  - Tier 1 Syncopate: REMOVE the ≤3-word/≤25-char hard limit. OK for 1–5 words. For >5 words: lead-in (first few words) in Space Grotesk smaller, then the most impactful words in Syncopate (generalized split-title = house pattern). Syncopate ONLY in all caps.
  - Tier 2 Space Grotesk: headlines/subheads/labels/metric numerals; not body. (keep)
  - Tier 3 Inter: ALL running body/copy/recede, non-negotiable. (keep)
  - All three embedded in luci-brand-fonts.css + each canonical diagram SVG. (keep)
- R12 KICKER FLAG → (a): keep kickers as a RARE listed Syncopate use (true eyebrow over display masthead, "Section 01" tag, load-bearing wayfinding). Use sparingly — Jane finds them irritating in most situations. Reconciles §3.1 with subhead-over-kicker.
- VALIDATED from files: FAG hub caps body at 64ch/62ch; website caps widely at 48–70ch (PersonaCapabilities, WhoWeServeReframe, HomeHero, IndustryChallenges). Where no companion fill → orphaned-text-in-empty-gap look she reported.

## Batch 3 — Typography §3.2–3.5 (in progress)
- R13 KEEP+MODIFY — One display moment per asset (one giant Syncopate). **Exception:** closing bookend page that is essentially a cover (strong headline, no other major elements) may use Syncopate all-caps again — e.g. sales doc close, deck close.
- R14 KEEP+MODIFY — Hierarchy through scale/weight, not decoration. Colored subhead default; kicker rare. **CANONIZE headline accent rhythm** (was split across luci-dual-accent-system + sales CSS, not in main design rules):
  - **Opening header (bookend):** white/off-white headline text + **mint** accent on the most captivating word(s) (`<em>` or accent span).
  - **Middle headers:** white headline text + **gold** accent on captivating word(s).
  - **Final header (bookend):** reverts to **white + mint** (same as opener).
  - Applies to dark-canvas documents (sales docs, FAG, deck dark slides). Light-canvas section headers use ink + `#2b9e80` accent per dual-accent light rules.
  - Source refs: `luci-dual-accent-system.mdc` (cover/close mint, middle gold); `sales-document.css` `.doc-page-band__accent` / `--gold`; FAG hub `fag-hero` mint / `fag-pick__heading em` gold / `fag-close` gold (close may need mint accent alignment — verify on consolidate).
- R15 KEEP+MODIFY — Type scale table KEEP + **Presentation deck (Track B) scale** as separate row set:
  - Slide title 40–52px (Space Grotesk bold)
  - Slide kicker 13–14px (tracked uppercase; rare)
  - Body/lead 18–21px (Inter; read-from-back size)
  - Labels/footer default floor 12–14px
  - **Exception:** detailed/diagram-level labels (lowest-level headers on LUCI + Systems graphic, etc.) may go to **10pt** — only at that granularity, not general slide copy
  - Deck headers: kicker → s-title → rule (NOT website lockup, NOT FAG colored subhead)
- R16 DECIDED — **Website main nav pages only** use SectionBlock lockup (big name → mint rule → tracked role). Applies to every top-level clickable nav page (Platform, Who We Serve hub, Resources, Contact, etc.). **Subpages TBD** — persona pages (Marketing, etc.) and industry pages (Casino, etc.) not locked yet; Jane will decide later. **Does NOT apply to other assets** (FAG, sales docs, deck, case studies) unless Jane explicitly requests. Default elsewhere = colored subhead (subhead-over-kicker).

## Batch 4 — Color (§4) (pending)
(pending)

## Batch 4 — Color (decided)
- R17 KEEP — Accent for small elements only (headline accent words in R14 rhythm = explicit exception).
- R18 KEEP — Two accent values: bright mint `#68E3BE` dark-only; light accent `#2b9e80` on light (confirmed by Jane). `#176B54` retired.
- R19 KEEP — Contrast table non-negotiable.
- R20 KEEP — Never color-only state.
- R21 MODIFY — Mint structural, gold expressive. **Gold allowed from asset open** (not middle-only) but **mint/green always takes precedence**; no large gold blocks — work gold into icons/outlines/gradients/accent words, not backgrounds.
- R22 MODIFY — **Bright gold `#EDD086` is the primary gold** for text on dark. **Eliminate gold-deep `#CEB06E` as a named primary** — looks terrible per Jane. Deeper golds OK only inside gradients/icon strokes/outlines (not as a separate "gold-deep for light text" system). Rules/CSS that mandate gold-deep for light-surface icons need revisiting on consolidate.
- R23 MODIFY — Light vs dark page model KEEP with nuance: **PDF/printable assets prioritize light canvases**; **website uses D/L/D/L alternating section model** (dark/light/dark/light).
- R24 MODIFY — No full-bleed dark band mid-document **PDF-only** (not website).

## Batch 6 — Tracks A/B/C (§A/B/C) (pending)
(pending)

## Batch 7 — Anti-patterns, Flagship, Checklist, Conflict resolution (§6–9) (pending)
(pending)

## Per-asset variation (to draft after core rules settled)
- **Website — main nav pages:** SectionBlock lockup for section headers (R16).
- **Website — subpages (persona/industry):** TBD — not locked; Jane decides later.
- **Website — default elsewhere / non-lockup sections:** colored Inter subhead (subhead-over-kicker).
- **Presentation deck (Track B):** own type scale (R15); kicker → title → rule headers.
- **Sales docs (PDF, Track C):** light canvas, doc- spine; colored subhead default.
- **Case studies:** split-title hero + colored subhead for sections.
- **Guide (FAG):** colored subhead default.
- **Legacy/frozen (newsletter, hub, messaging docs):** no redesign unless asked.
