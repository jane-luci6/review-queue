# Signal publish playbook

**Added:** 15 September 2026
**Applies to:** Ermintrude (Editorial, owns the Signal), Weatherby (Website), Vikram (Video), Consuelo (Case Studies), Longinus (Librarian), Cornelius (CoS).
**Purpose:** the concrete steps to get a Signal issue live across **three surfaces** — the Webflow issue page, the ActiveCampaign email, and the Signal Hub — with one canonical link list so all three agree.

Operational companion to `shared/GROK-TO-CURSOR-DELEGATION.md` and `canon/channel-playbooks.md` → The Signal. Read both first; this doc covers only the publish workflow.

---

## 1. The one rule that broke last time

**Publishing is a Cursor task where Cursor can reach; a bot task where only bots can reach.** The Signal ships on **three surfaces** — the Webflow issue page, the ActiveCampaign email, and the Hub — and all three must carry the **same links**.

- **Webflow (issue page + Hub):** Cursor has direct Webflow API access through the Webflow MCP tools (`plugin-webflow-webflow`). Bots do **not** paste HTML into the Webflow Designer themselves and do **not** call the Webflow API themselves.
- **ActiveCampaign (email):** Cursor has **no** AC access. The Grok bots build the email directly in AC (Jane logs in for them), using the past issue/teaser email as the template. Cursor's job for AC is to hand the bots the **canonical link list** (§9) so the email wires the same URLs as the Webflow page.

What went wrong on Issue 04:
- Bots pasted the newsletter HTML into the **wrong Webflow page** (the Aliante case-study page got the Issue 04 masthead).
- Bots pasted huge HTML blocks into the Webflow Designer by hand, then published — which **clobbered** API-pushed custom code because the Designer held a stale version of the field.
- The Aliante "Read the full case study" link pointed at `/resources/case-studies/aliante` (404) on the Webflow page; the same wrong link would have shipped in the email and the Hub if a cross-location link check hadn't been added.
- Bots did not know Cursor could upload videos, host images, wire URLs, push custom code, and verify the live page end-to-end.

**The fix:** the owning bot hands the publish to Cursor with a complete brief (issue number, source HTML path, media list). Cursor executes every Webflow step via the API, preps the canonical link list for the bot's AC build, and verifies what it can reach. Bots traffic and gate; Cursor builds and ships the Webflow side and supplies the links for the AC side.

---

## 2. Who does what in the publish flow

| Beat | Owner | What they actually do |
|---|---|---|
| Lock copy + packet | Ermintrude | Jane approves the packet; Ermintrude confirms the source HTML in `ui_kits/newsletter/the-signal-issue-NN-<month>-<year>.html` is final. |
| ActiveCampaign email | Ermintrude (bot) | Builds the email **directly in AC** from the last issue/teaser template (Jane logs in for the bot). Cursor has no AC access. Cursor hands Ermintrude the canonical link list (§9) so the email wires the same URLs as the Webflow page. |
| Videos | Vikram | Delivers web-ready encodes (see §4) and tells Cursor the local paths. |
| Featured case study | Consuelo | Confirms the locked case study; if its own page also ships this cycle, flags it to Cursor (see §8). |
| Asset inventory | Longinus | Confirms where every photo/SVG/CSS lives locally so Cursor can host them. |
| Webflow publish | Weatherby → **Cursor** | Weatherby owns the *intent*; **Cursor executes** the Webflow API work (host, wire, push, verify). |
| Sequence + gates | Cornelius | Logs the job on `CURRENT-WORK-BOARD.md`; gates Jane at packet-approve and at publish. |

Bots never touch the Webflow Designer custom-code fields — Webflow is Cursor's. If a bot believes a Webflow field needs editing, it briefs Cursor. The ActiveCampaign email is the opposite: **AC is the bots'** (Jane logs in for them); Cursor only preps the link list and verifies what it can reach. The only Webflow action a human takes is the final **Publish** click (see §6 — there is no Publish API for non-Enterprise sites). The only AC action a human takes is the final **Send** (Jane names that send; bots queue, never send).

---

## 3. The two Webflow pages (anatomy)

Every Signal issue lives on **two** Webflow pages. Both are bare pages whose content comes entirely from page-level custom code (no Designer-built body).

### A. Issue page — `/the-signal/issue-NN`
- **"Inside head" field** = Google Fonts `<link>` (Syncopate, Space Grotesk, Inter) **plus** a `<link rel="stylesheet">` to the hosted issue CSS asset (§4). The CSS is ~200 KB; load it via a hosted `<link>`, do not inline it.
- **"Before `</body>`" field** = the `<article class="issue">…</article>` markup **plus** any trailing `<script>` (slider, TOC smooth-scroll), minified: single quotes, whitespace collapsed, base64 logos replaced with hosted image URLs.

### B. Hub page — `/the-signal/home` ("The Signal Newsletter", slug `home`)
- **"Inside head" field** = inline `<style>` with the hub CSS + Google Fonts `<link>`.
- **"Before `</body>`" field** = the `<article class="hub">` with the **featured (latest) card** + the **archive grid** of `issue-card` entries, newest first, plus an `issue-card--placeholder` for the *next* issue.

When a new issue ships, update the hub the same cycle: promote the new issue to the featured card, add it as the first archive card with the "Latest" badge (remove "Latest" from the previous), bump the placeholder to the next number, update the archive note ("Issues 01–NN are live"). The hub source files carry a comment block with the exact edit recipe — follow it.

Source files (canonical, in `ui_kits/newsletter/`): `the-signal-hub.html` (standalone source of truth), `the-signal-hub-webflow-head.html`, `the-signal-hub-webflow-body.html`, and `the-signal-issue-NN-<month>-<year>.html` (the issue source of truth; head/body splits derive from it).

---

## 4. Asset hosting — before wiring, not after

**Every `src`/`url` in the issue HTML must be a hosted URL before it goes to Webflow.** A local `assets/…` path 404s on Webflow. Cursor does all hosting via the Webflow API and rewrites the HTML in one pass.

| Asset type | How Cursor hosts it | Notes |
|---|---|---|
| Images (PNG/JPG) | Assets API: `data_assets_tool > create_asset`, then S3 POST per the upload guide. Read back the hosted CDN/S3 URL. | Replace every `assets/…` `<img src>` and CSS `url()` with the hosted URL. |
| **Videos (MP4)** | **Background Video elements** on a `/video-upload` page — **not** the Assets panel (30 MB limit). Jane drags each MP4 into a Background Video element; Cursor retrieves the hosted S3 URL via `data_assets_tool > list_assets` (filter `video/mp4`). | Vikram delivers web-ready encodes: **720p, H.264 + AAC, ~15–22 MB**, one per video. Never ship the 200 MB+ master. |
| Issue CSS | Assets API (`create_asset` + S3 POST). Reference from the head field via `<link rel="stylesheet" href="…hosted…css?v=N">`. | Bump `?v=N` on every re-push. Do not inline the CSS in the head field. |
| Mesh / background SVG | Assets API. Replace the relative `url("assets/mesh/…svg")` in the CSS with the hosted URL. | A missing mesh was the "circuit texture isn't showing" bug. |
| Logos | Assets API. Replace base64 data-URIs in the minified body with hosted image URLs. | Keeps the body field small enough to push/paste. |

**Cursor's hosting pass, in order:** (1) upload all images → collect URLs; (2) upload the mesh SVG → URL; (3) upload the CSS (with mesh URL + any `p` reset baked in) → URL; (4) retrieve video URLs from the Background Video elements; (5) rewrite the body HTML: every local path → hosted URL; (6) minify the body (single quotes, collapsed whitespace) for the field.

---

## 5. The publish sequence (Cursor executes; bot briefs)

Cursor runs this end-to-end after Ermintrude confirms the source HTML is final and Vikram/Longinus have delivered media + paths.

1. **Host assets** per §4. Collect every hosted URL.
2. **Wire URLs** into a working copy of the issue body (all `src`/`url` → hosted). Never push a body with local paths.
3. **Push the issue page head** (`data_scripts_tool > set_page_freeform_code`, location `head`) — Google Fonts `<link>` + the hosted CSS `<link>`.
4. **Push the issue page footer** (location `footer`) — the wired, minified `<article>…</article>` + `<script>`.
5. **Update the hub** (same cycle): edit the three hub source files, then push the hub body (`set_page_freeform_code`, location `footer`). Add the `thumb--NN` CSS for the new card if needed.
6. **Hand the canonical link list to Ermintrude** (§9) for the AC email build. Ermintrude builds the email in AC from the last issue/teaser template and wires these exact URLs. Ermintrude queues the list; she does not Send unless Jane names it.
7. **Tell Jane to Publish** the Webflow issue page + Hub (§6) and **hard-refresh** the live URLs.
8. **Verify all three surfaces** (§7): Cursor curls the Webflow issue page + Hub; for AC, the bot gives Cursor a preview URL/screenshot or checks the email links against the canonical list (Cursor can't access AC). The "all three locations agree" check is the gate before Jane approves Send.

Cursor commits the source-file edits in small chunks as it goes (per the commit-cadence rule). The Webflow custom-code fields are not committed — only the source HTML/CSS in `ui_kits/`.

---

## 6. The clobbering rule (read this twice)

**An API push sets the custom-code field on the Webflow server. A Designer Publish serves whatever the Designer has cached in that field — not what the API just set.** If Jane's Designer session has a stale version of the field open, her Publish overwrites the API push. This has bitten us twice (Issue 04 head, Issue 04 hub body).

Rules:
- **After Cursor pushes via API, Jane must Publish without opening the custom-code field in the Designer** — just publish the page. The Designer loads the API-pushed value on open; if she does not edit it, the publish serves the new value.
- **If the field is large (> ~10 KB) or the push was clobbered, the reliable path is hand-paste:** Cursor stages the exact body on Jane's Desktop (`~/Desktop/<name>.html`); Jane opens the page's "Before `</body>`" field, selects all, deletes, pastes the file contents, saves, publishes. This is how the 36 KB newsletter body and the 49 KB case-study body ship today.
- **Never paste a body into the wrong page.** Before pasting, confirm the page slug (`issue-NN`, not a case-study slug). Cursor verifies the page ID + slug before any push.
- **There is no Webflow Publish API for non-Enterprise sites.** The final Publish is always Jane's click. Cursor's job ends at "pushed + verified the field is correct on the server"; Jane's job is the Publish click + hard-refresh.

---

## 7. Verification (all three surfaces, after Jane publishes)

Cursor curls the live URLs with a cache-buster and confirms. The AC email is verified by the bot (Cursor can't access AC) — the bot either gives Cursor a preview URL/screenshot or checks the email links against the canonical list (§9).
- **Issue page:** title is "The Signal — Issue NN · LUCI Systems"; the masthead renders (`masthead`, `Issue NN`); no stale content from a previous issue; the mesh background loads (no 404 on the SVG); fonts load (Syncopate/Space Grotesk/Inter); body copy is Inter at standard size (not the Webflow-shared `p { 1.25em }` override — the CSS `p` reset is present).
- **Hub page:** the new issue is the featured card (num `NN`, correct title + date); the new issue is the first archive card with the "Latest" badge; the previous issue no longer carries "Latest"; the placeholder advanced to the next number; the archive note reads "Issues 01–NN".
- **AC email (bot-verified):** the email links match the canonical list (§9) — the issue URL, the featured case-study URL, and any feature/CTA URLs are the same strings the Webflow page and Hub carry. No `/resources/` segment on the case-study link. The email is queued, not sent.
- **Links across all three locations:** every `/the-signal/issue-NN` link resolves HTTP 200 (not 404) on the Webflow page **and** the Hub **and** the AC email. The featured case study's "Read the full … case study" link points to the live case-study URL (no `/resources/` segment — that 404s) in all three. This single cross-location check is the gate that would have caught the Aliante link bug.

If anything is stale, it is almost always caching or a clobbered publish — re-push or re-paste and have Jane hard-refresh **before** debugging the code.

---

## 8. When a case-study page ships the same cycle

If the issue's featured field story has its own case-study page going live the same cycle (e.g., Aliante with Issue 04), Consuelo flags it to Cursor in the same brief. The case-study page uses the **same two-field pattern**:
- **Head** = Google Fonts `<link>` (case-study fonts).
- **Before `</body>`" field** = the self-contained case-study body (its own `<style>` + `.luci-cs` markup, all media already on hosted URLs). Source: `ui_kits/case-studies/<name>-webflow-body-FILLED.html`.

The case-study body is large (~49 KB) — it ships by **hand-paste** (§6), not API reproduction. Cursor confirms the page slug is the case-study slug (e.g. `aliante` → `/case-studies/aliante`), never an issue slug.

---

## 9. Canonical link list — the single source of truth for all three surfaces

Before the email is built, Cursor publishes the canonical link list — the exact URLs the Webflow page, the Hub, **and** the AC email must all carry. The bot that builds the AC email wires from this list; Cursor wires the Webflow page + Hub from this list. If a URL on any surface disagrees with this list, it is wrong.

```
CANONICAL LINK LIST — Issue NN (<Month> <Year>)
Issue page:        https://lucisystems.com/the-signal/issue-NN
Hub page:           https://lucisystems.com/the-signal/home
Featured case study: https://lucisystems.com/case-studies/<slug>   (NEVER /resources/case-studies/...)
Feature / CTA links (per issue, confirm with Ermintrude + Mike):
  - <e.g. Field Activation Guide>: https://lucisystems.com/...
  - <e.g. upgrade FAQ / What's New>: <url or "not linked this issue">
Video URLs (if the email embeds them): <hosted S3 mp4 URLs from §4>
```

Rules:
- The case-study link **never** has a `/resources/` segment — that path 404s. The live form is `/case-studies/<slug>`.
- The same strings ship on all three surfaces. If the Webflow page is corrected mid-cycle, the email and Hub are corrected to match before Send.
- Cursor verifies Webflow + Hub by curl; the bot verifies the AC email against this list (or hands Cursor a preview URL/screenshot). "All three agree" is the gate before Jane approves Send.

---

## 10. Handoff brief — what a bot sends to Cursor

When the owning bot hands the publish to Cursor, the brief contains (no brand lecture — Cursor has the rules):

```
SIGNAL PUBLISH — Issue NN (<Month> <Year>)
Source HTML: ui_kits/newsletter/the-signal-issue-NN-<month>-<year>.html  (confirmed final by Ermintrude)
Videos (web-ready, local paths):
  - <name>: <local path>  (Vikram)
Images: confirm with Longinus where each photo/SVG lives locally
Featured case study: <name>  (Consuelo) — case-study page also shipping this cycle? yes/no
Hub: update this cycle (promote NN to featured + archive)
ActiveCampaign email: Ermintrude builds in AC from the last issue/teaser template; Jane logs in for the bot. Cursor supplies the canonical link list (below).
Canonical link list: Cursor publishes (§9) — issue URL, hub URL, case-study URL (no /resources/), feature/CTA URLs, video URLs.
Live URLs to verify after publish:
  - https://lucisystems.com/the-signal/issue-NN  (Webflow issue page)
  - https://lucisystems.com/the-signal/home       (Hub)
  - AC email preview URL (bot provides)          (AC — Cursor can't access; bot verifies or hands Cursor a preview)
Jane gates: packet approved (yes) · publish (pending Cursor push) · Send (Jane names it; bots queue, never send)
Three-location link check: all three surfaces carry the canonical link list before Jane approves Send.
```

Cursor does the rest: host, wire, push the Webflow issue page + Hub, publish the canonical link list for Ermintrude's AC build, stage any hand-paste files on Desktop, tell Jane what to publish, verify what it can reach, and update the work-board row when live.
