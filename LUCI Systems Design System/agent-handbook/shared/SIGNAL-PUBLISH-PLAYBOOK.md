# Signal → Webflow publish playbook

**Added:** 15 September 2026
**Applies to:** Ermintrude (Editorial, owns the Signal), Weatherby (Website), Vikram (Video), Consuelo (Case Studies), Longinus (Librarian), Cornelius (CoS).
**Purpose:** the concrete steps to get a Signal issue live on Webflow — and the one rule the team broke last time.

Operational companion to `shared/GROK-TO-CURSOR-DELEGATION.md` and `canon/channel-playbooks.md` → The Signal. Read both first; this doc covers only the publish workflow.

---

## 1. The one rule that broke last time

**Webflow publishing is a Cursor task — not a Grok task.** Cursor has direct Webflow API access through the Webflow MCP tools (`plugin-webflow-webflow`). Bots do **not** paste HTML into the Webflow Designer themselves and do **not** call the Webflow API themselves.

What went wrong on Issue 04:
- Bots pasted the newsletter HTML into the **wrong page** (the Aliante case-study page got the Issue 04 masthead).
- Bots pasted huge HTML blocks into the Designer by hand, then published — which **clobbered** API-pushed custom code because the Designer held a stale version of the field.
- Bots did not know Cursor could upload videos, host images, wire URLs, push custom code, and verify the live page end-to-end.

**The fix:** the owning bot hands the publish to Cursor with a complete brief (issue number, source HTML path, media list). Cursor executes every Webflow step via the API and tells the bot + Jane what to publish by hand. Bots traffic and gate; Cursor builds and ships.

---

## 2. Who does what in the publish flow

| Beat | Owner | What they actually do |
|---|---|---|
| Lock copy + packet | Ermintrude | Jane approves the packet; Ermintrude confirms the source HTML in `ui_kits/newsletter/the-signal-issue-NN-<month>-<year>.html` is final. |
| Videos | Vikram | Delivers web-ready encodes (see §4) and tells Cursor the local paths. |
| Featured case study | Consuelo | Confirms the locked case study; if its own page also ships this cycle, flags it to Cursor (see §8). |
| Asset inventory | Longinus | Confirms where every photo/SVG/CSS lives locally so Cursor can host them. |
| Webflow publish | Weatherby → **Cursor** | Weatherby owns the *intent*; **Cursor executes** the Webflow API work (host, wire, push, verify). |
| Sequence + gates | Cornelius | Logs the job on `CURRENT-WORK-BOARD.md`; gates Jane at packet-approve and at publish. |

Bots never touch the Webflow Designer custom-code fields. If a bot believes a field needs editing, it briefs Cursor. The only Webflow action a human takes is the final **Publish** click (see §6 — there is no Publish API for non-Enterprise sites).

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
6. **Tell Jane + the bot to Publish** (§6) and **hard-refresh** the live URL.
7. **Verify** the live page (§7).

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

## 7. Verification (Cursor, after Jane publishes)

Cursor curls the live URL with a cache-buster and confirms:
- **Issue page:** title is "The Signal — Issue NN · LUCI Systems"; the masthead renders (`masthead`, `Issue NN`); no stale content from a previous issue; the mesh background loads (no 404 on the SVG); fonts load (Syncopate/Space Grotesk/Inter); body copy is Inter at standard size (not the Webflow-shared `p { 1.25em }` override — the CSS `p` reset is present).
- **Hub page:** the new issue is the featured card (num `NN`, correct title + date); the new issue is the first archive card with the "Latest" badge; the previous issue no longer carries "Latest"; the placeholder advanced to the next number; the archive note reads "Issues 01–NN".
- **Links:** every `/the-signal/issue-NN` link resolves HTTP 200 (not 404). The featured case study's "Read the full … case study" link points to the live case-study URL (no `/resources/` segment — that 404s).

If anything is stale, it is almost always caching or a clobbered publish — re-push or re-paste and have Jane hard-refresh **before** debugging the code.

---

## 8. When a case-study page ships the same cycle

If the issue's featured field story has its own case-study page going live the same cycle (e.g., Aliante with Issue 04), Consuelo flags it to Cursor in the same brief. The case-study page uses the **same two-field pattern**:
- **Head** = Google Fonts `<link>` (case-study fonts).
- **Before `</body>`" field** = the self-contained case-study body (its own `<style>` + `.luci-cs` markup, all media already on hosted URLs). Source: `ui_kits/case-studies/<name>-webflow-body-FILLED.html`.

The case-study body is large (~49 KB) — it ships by **hand-paste** (§6), not API reproduction. Cursor confirms the page slug is the case-study slug (e.g. `aliante` → `/case-studies/aliante`), never an issue slug.

---

## 9. Handoff brief — what a bot sends to Cursor

When the owning bot hands the publish to Cursor, the brief contains (no brand lecture — Cursor has the rules):

```
SIGNAL PUBLISH — Issue NN (<Month> <Year>)
Source HTML: ui_kits/newsletter/the-signal-issue-NN-<month>-<year>.html  (confirmed final by Ermintrude)
Videos (web-ready, local paths):
  - <name>: <local path>  (Vikram)
Images: confirm with Longinus where each photo/SVG lives locally
Featured case study: <name>  (Consuelo) — case-study page also shipping this cycle? yes/no
Hub: update this cycle (promote NN to featured + archive)
Live URLs to verify after publish:
  - https://lucisystems.com/the-signal/issue-NN
  - https://lucisystems.com/the-signal/home
Jane gates: packet approved (yes) · publish (pending Cursor push)
```

Cursor does the rest: host, wire, push, stage any hand-paste files on Desktop, tell Jane what to publish, verify, and update the work-board row when live.
