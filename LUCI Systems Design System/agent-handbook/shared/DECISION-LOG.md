# Decision log

**Purpose:** Short summaries of locks Jane (or a gated specialist pass she accepted) actually made. Chief of Staff reads this to know what happened without reading Cursor chats.

**Not a work board.** The board is current status. This file is the trail of *decisions*.

**Newest first.** One or two sentences. Name the lock, not the debate.

---

## 2026-09-25

- **Upgrade Guide deep content = FAG-style standalone asset (not under site chrome).** Jane lock: deep guide is a standalone asset page like the FAG customer guide — **one in-asset sticky nav only** (back-to-landing + chapter/feature jump; scroll-spy + shareable `#` hashes; mobile wrap). **No competing website header/nav.** Pair with a **landing page** that gives context and links into the guide. Features render as **always-open sections** (not accordion); accordion **only** for Technical + FAQ. Per-feature pages deferred. Will likely ship on **old Webflow first** before new Astro — IA/nav pattern must port; Astro/.37 mocks are for review only. Live `/luci-upgrade-guide/` accordion stays until Jane approves cutover. Preview mocks: landing `http://10.10.1.37/luci-upgrade-guide-asset-mock/` · guide `http://10.10.1.37/luci-upgrade-guide-asset-mock/guide/`. Jane, 25 Sep (Weatherby).

## 2026-09-24

- **Upgrade Guide section headers = mint wash (not brochure blackbar).** Jane corrected a misclick: lock soft mint wash + ink/accent-light duo + split mint|gold rule for all section lockups; wash full-bleed, lockup type aligned to page text margins. Hero scrim behind words slightly stronger. Reference `559bd69`. Jane, 24 Sep.

- **Tall hero headers need a right-column floorplan layer.** Short heroes can use the with-plan mesh alone at `center / cover`. Taller headers (e.g. Upgrade Guide) need more: keep that mesh framing and add a separate right-pinned floorplan layer (`.ug-hero__plan` + `luci-plan-right-panel.png` or equivalent) so the plan covers the right side after the text, with a soft fade into the copy. Do not solve tall headers by re-running the old zoom/Y crop dials. Reference commit `f8daf43`. Jane, 24 Sep.

## 2026-09-24

- **Upgrade Guide In-product support row carries a Plus chip.** Small gold-wash pill (`Plus`) sits inline next to the support title on `.ug-support-spotlight` (brand tokens only: `rgba(var(--gold-rgb), 0.22)` + `var(--ink-strong)`); liner/body copy unchanged; hero, deep-dive (`9c5f0e1`), and intro untouched. Live on `http://10.10.1.37/luci-upgrade-guide/#ug-pillars` (commit `dd1888d`). Jane/CoS, 24 Sep (Weatherby; GLM empty-log flake → applied directly).
- **Upgrade Guide pillars use the two-pager gradient fills, and in-product support returns to its own full-width row.** The three `.ug-pillar` boxes now carry the Mike Review Queue v2 two-pager `p1-pill`/`p2-card` gradients per nth-child (room `#E8EEF2→#F3F6F8`, view `#EBF9F4→#F4FCF9`, security `#D4EFE4→#E8F6EF`) with card radius/padding; nested feature pills switched to a translucent white fill so they read on all three gradients (mint left accent kept, no new pill copy). The support fold-in (commit `8ca170c`) is undone for the overview: the 4th security `featurePills` entry is pulled out and support lives in a compact spotlight row under the 3-col grid, full content width, darker gray fill `#D8DEE3→#E8EDF0` (two-pager `.p2-spotlight__box`), linking to `#ug-feature-in-product-support` (deep-dive entry left intact). Hero, thesis, path, FAQ, CTA, and technical sections untouched. Live on `http://10.10.1.37/luci-upgrade-guide/#ug-pillars` (commit `f392897`). Jane/CoS, 24 Sep (Weatherby/GLM brief).
- **New LUCI Upgrade Landing hero uses the mesh + floorplan family (Flow C), not lines-only mesh.** `.ug-hero__mesh` on `src/pages/luci-upgrade-guide.astro` now points at `luci-bg-hero-with-plan-transparent-1920x1080.svg` (copied into `public/images/mesh/`), the same with-plan asset as the Flow C What's New one-pager hero. Dropped `mix-blend-mode: screen` (the asset is self-transparent over navy; screen would blow out the floorplan raster), raised opacity 0.4 → 0.82 so both mesh and floorplan read, and strengthened the radial scrim center stop 0.72 → 0.82 for headline/CTA legibility while keeping the cloud shape so mesh + plan still read through on the right. No copy changes; no circuit textures; lines-only mesh removed from the hero. Live on `http://10.10.1.37/luci-upgrade-guide/` (commit `55662b1`). Jane, 24 Sep (Weatherby/GLM brief).

## 2026-09-22

- **Upgrade Guide timing area: remove the internal proposed timeline ladder; keep only Release (January 19) + an approximate pace line.** The Dec 10 / Jan 6 / Jan 14 / Jan 19 draft checklist and "Proposed timeline — draft for Jane review" block are gone from the customer-facing page; the timing strip shows Release — January 19 and Pace — about 10 customers a week (approximate; Jane to dial in), with the rollout folded into a single short line. Laptop fulfillment, the ~hour-or-two cutover, and the four how-it-works steps stay; the mid-page duplicate "Talk to your account team" contact card is replaced by a compact end-of-path CTA link to `#ug-cta`, which remains the primary contact destination. Jane, 22 Sep (Weatherby/GLM brief).

## 2026-09-17

- **New LUCI What’s New one-pager advances Flow C with a split proof ledger.** Announce a new version for January 19, use one more-control/better-support subhead, present the three retitled promises with 5–8-word feature teasers, and close with an information URL plus contact details—no duplicate promise index or fulfillment path. Jane.
- **New LUCI release communications follow a fulfilled, not self-serve, path.** Keep one benefit-led release story, route customers through direct upgrade fulfillment and prospects through simple orientation, add PR and optional demonstration, and do not create a public Upgrade Guide/download archive; end-of-support belongs in intentional direct customer communication. Jane.
- **Main `/resources` page caps each section at 3 items and ships tighter cards.** Case Studies shows 3 (Yaamava, Aliante, Ameristar) with a "See all case studies" CTA into `/resources/case-studies`; full inventory (incl. Aliante) stays on the typed landing. Cards tightened via CSS only — media `16/9`→`2/1`, smaller body padding/type scale/gaps, narrower video stack; LUCI tokens preserved. Jane, 17 Sep (Weatherby follow-up brief).
- **Homepage proof band features Yaamava; casinos-gaming features Boyd Aliante; hotels-resorts stays Ameristar.** `HomeProof.astro` is now prop-driven (`study` prop, default Ameristar); the Resources case-study grid adds the Aliante card after Yaamava. Proof-band fields on Yaamava and Aliante are derived only from locked title/dek figures (no new claims). Jane, 17 Sep (Weatherby brief).

## 2026-09-16

- **New LUCI What’s New one-pager uses Option 1 — Three promises.** The release page opens with “Putting the power of programming in your hands” and organizes proof under Operate, Make it yours, and See and secure; later layout should feel like an announcement, not an equal-column datasheet. Jane.

## 2026-09-15

- **Signal publish playbook reflects Webflow API reality.** On this (non-Enterprise) Webflow site, Cursor cannot add HTML via the API and there is no Publish API. Webflow work is now split by lane: Cursor hosts assets + wires URLs + preps the final HTML + briefs the bots with exact page IDs/field names; Grok bots paste the HTML into the Designer; Jane does the final Publish click. ActiveCampaign stays a bot task; Cursor still hands the canonical link list. Jane, 15 Sep.
- **Signal Issue 04 ActiveCampaign teaser uses the Issue 03 intro register and exact wall dimensions.** The intro is one short preview paragraph; wall references use either `106' x 20'` or `2,000 square feet`, never “106-foot.” The secondary grid restores the “From the team” separator above From LUCI and A Minute with Mike. Jane, 15 Sep.
- **Signal Issue 04 morning copy locks applied.** Welcome opening replaced with three-paragraph consistency/flexibility framing (kept "You'll see that principle…" onward + sign-off); Project Update Aliante dimension now `106' x 20'`; Clearwater "rack" → "headend"; Swigs city corrected to Ponca City, Oklahoma with two-phase copy (copy-r5); What's Coming close dropped "property-by-property" ("…as New LUCI moves through beta and toward release."). Synced review mirror + webflow body split. Jane, 15 Sep.

## 2026-09-14

- **Aliante case-study video placed on luci-website Resources → Videos.** The Aliante Sportsbook reel (encoded from the OneDrive master to a web-ready 720p H.264/AAC ~15 MB file at `public/videos/aliante-reel.mp4`) added as a second player in the Resources Videos section alongside the existing LUCI Platform Run video; the Aliante case-study page reel points at the same hosted file with the approved wall-finished poster. Live on review VM `http://10.10.1.37`. Jane, 14 Sep.
- **Signal Issue 04 Mike goal line locked.** First sentence of the last body paragraph in "A Minute with Mike" changed to "The goal isn't a single manufacturer ecosystem." (was "The goal isn't identical hardware everywhere."); second sentence unchanged. Jane, 14 Sep.
- **Hortensia not stood up.** Cursor already does mechanical and taste QA. No Headmistress Grok seat. Jane.
- **Hortensia (Headmistress) stood up.** Final inspection of finished packets before Jane. Not the retired Review seat. Not project management. Jane.

## 2026-09-11

- **Aliante iMovie card 02 — `40 acres` highlighted in mint display scale (revises prior card 02 lock).** Jane revised the one-off "Across more than 40 acres" card (no period) to highlight `40 acres` the same way as card 01's `100,000+`: SpaceGrotesk-SemiBold 128px, mint `#68E3BE`. Lead-in `Across more than` stays off-white Medium 52 @ 95%. No mint rule. Shared baseline at 128px exceeded the 864 measure, so the card breaks cleanly to two lines (lead-in above, mint numeral on the anchor y=920). S-class plate (top y=680) matches card 01. Per-card override of BODY-TREATMENT-LOCK §2/§3.1/§6 for this card only — not a house rule; lock still governs c02–c19. Per Vikram/GLM brief, 11 Sep.

- **Signal Issue 04 TOC + From LUCI mechanical locks.** TOC now leads with LUCI Project Update as 01 and renumbers the rest (02 In the field → 06 A Minute with Mike) to match live section order. From LUCI drops "below" ("Choose your team, or read…") and gains breathing room (scoped margin-top) between the FAG role tiles and the following paragraph. Welcome r4 copy still pending (file not present). Jane, 11 Sep.

- **Aliante iMovie card 02 — no mint rule, all off-white Medium (per-card override).** One-off "Across more than 40 acres" card (no period) extends the card 01 no-rule override: N-class plate + bed, single-line narrative, all words off-white Medium 52 (no mint type — no display numeral). Same per-card override pattern as card 01; still not a house rule, and the lock still governs the c02–c19 titles.md sequence. Per Vikram/GLM brief, 11 Sep.

- **Signal Issue 04 §01 kicker shows a visible `01`.** Jane resolved Opus's open call #10 in favor of a number — the Project Update kicker now reads `01 · LUCI Project Update`. The `01` is a section marker only; per Opus §8 it is **not** added to the TOC (TOC keeps its 5 entries 01–05). Jane, 11 Sep.

- **Aliante iMovie card 01 — mint on the numeral, no rule (per-card override).** Jane removed the 56×3 mint rule from the one-off "With 100,000+ square feet of gaming," card and set `100,000+` in LUCI mint `#68E3BE` (bright mint on the dark plate); `With` and `square feet of gaming,` stay off-white Medium. Overrides BODY-TREATMENT-LOCK §2/§6 (mint only as rule / no mint type) **for this card only** — not a house rule; the lock still governs c02–c19. Jane, 11 Sep.

- **Aliante RC2 body onscreen text locked to rev 2 — corner plate + bed.** Jane approved the left-anchored editorial direction with a hard-edged bottom-left corner plate (navy-deep @ 0.62) over a full-bleed gradient bed, replacing the rev 1 gradient-only pass that lost to busy footage; measure tightened to 864. Rendered as the c02 preview. Jane, 11 Sep.

- **Learned preferences rule locked.** Grok bots may proactively add a preference to a Cursor brief only when prior Jane behavior shows she is at least ~80% likely to ask for that change herself in this situation; the bot tells Jane when it applies one. One-off ≠ house rule; repeated ≠ universal; only Jane promotes a preference to a universal rule. Jane, 11 Sep.

- **Aliante case study approved into Downloads; New LUCI launch timeline pushed to Review Queue.** Jane approved the Aliante case study (moved to IMP Downloads → Current Content → Case studies; live on review site `.37`); the New LUCI launch timeline entered the IMP Review Queue for internal planning review (beta, property by property — not a public splash). Jane, 11 Sep.

- **Signal 04 Project Update stays its own compact section** between Welcome and Aliante (not the tall photo wall, not a numbered article). Green cabinet/panel/hour/display metric chips eliminated; property name + short human line + a quiet date (e.g. "Live · August 24") is enough. Jane, 11 Sep, revising the prior "callout / not a formal section" brief.

## 2026-09-10

- **Librarian renamed Longinus** (was Archimedes). Same find-things seat. Jane.
- **Archimedes (Librarian) stood up** (Jane, 10 Sep). Finds where files, photos, diagrams, and handbook copies live. Does not write or design.
- **Active jobs on the shared board.** Every live job is logged on `CURRENT-WORK-BOARD.md` whoever Jane talked to. Workstream bots write the row. Cornelius reads the board before status; Jane does not recap. Jane.
- **Website renamed Weatherby** (was Winston). Same Website seat. Jane.
- **Live names:** Cornelius (CoS), Winston (Website), Consuelo (Case Studies), Ermintrude (Editorial), Vikram (Video), Svetlana (Social). Jane.
- **Vikram (Video) stood up** (Jane, 10 Sep). Source media → review cuts is Vikram’s. CoS no longer holds Video. Aliante RC2 Jane watch / optional polish stays on that stream.
- **Svetlana (Social) stood up** (Jane, 10 Sep). LinkedIn company page only. Posting still held until New LUCI launch unless Jane opens it.
- **CoS renamed Cornelius** (Jane, 10 Sep). Same Chief of Staff seat.
- **Social bot set up, idle.** Process is OneDrive `Marketing - Documents/Social Media` (`WORKFLOW.md`, `CONTENT-DIRECTION.md`). Not the archived Next.js app. Not the shut-down Claude bench. Jane names the bot later. Does not post until she says start.
- **Video bot is Vikram.** Source media → review cut. Does not post. Jane.
- **Edith picks up Signal after copy is finalized.** Do not hand Issue 04 to her while copy is still open. Jane.
- **Signal Issue 04 remainder locked.** Quick Tip is current LUCI endpoint names/notes (overrides the earlier kiosk pick). What’s coming is unused New LUCI with a visual — copy uses venue panels plus a searchable activity record (look/map/staging already ran in Issue 03). Minute with Mike is “Standardize the operation, not the hardware.” “Since the last Signal” is a short photo wall: Clearwater, Sam’s Town, Osage, California. Extra visual/infographic parked. Theme and Welcome names still open. Jane, September newsletter chat.
- **Edith (Editorial & Campaigns) stood up** (Jane, 10 Sep). Signal, email, social, AC assembly traffic to Edith. CoS no longer holds that stream. Video still pending.
- **Work board refreshed 10 Sep.** Signal 04, Aliante written CS, Wave 1, launch remainders. Yaamava is featured-on-site, not the open case-study write.
- **Decision log starts.** Cursor appends here at real lock points so CoS can see what Jane decided without the chat archive.
- **Grok facilitates; Cursor decides.** GLM / Claude / ChatGPT lead strategy, design, copy, and implementation. Grok writes the assignment packet, asks Jane when a fact is missing, and follows Cursor unless the result is clearly way off plan.
- **Design Direction starts on GLM.** Role `design-direction` = GLM 5.2 Max first. Escalate to `design-direction-open` (Claude Opus 5) only for open visual planning or after a GLM pass fell short.
- **Grok reaches Cursor via local CLI, not GitHub.** Bridge is `luci-cursor` on Jane’s Mac. No Cloud Agent, no required GitHub, no Cursor chat window. Commits stay local.

## 2026-09-09

- **Issue 04 Field is a shortened Aliante study** with a link to the full page. Use the before/after slider. Drop “one of the largest LED walls in Las Vegas.” Icons on “What Aliante runs now.” Six-layout header is a plain descriptive line. Jane.
- **Aliante long case study photo/copy locks.** Next chapter uses a before photo; consolidation uses Jane’s rack shot and includes projector count; Building photos are Image (16), keep 2–3, IMG_4804; before/after uses Jane’s matched before. Sportsbook list: drop item 2; 03 ends after “focus”; 04 is the coordinated-interface line. Jane.
