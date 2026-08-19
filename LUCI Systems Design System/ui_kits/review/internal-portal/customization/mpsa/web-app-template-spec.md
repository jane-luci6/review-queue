# MPSA — Vendor Protective · web-app template spec

Build spec for adding the **Master Purchase & Services Agreement (MPSA — Vendor Protective)** as a template in the web application / doc studio. This is a **Word (`.docx`) template**, not an HTML template — it needs a different pipeline than the sales/proposal/SOW templates. This doc specifies what the web app must implement so the MPSA behaves the same as it does in the Cursor customization studio.

The Cursor-studio reference implementation already exists (master `.docx`, fill script, dev-server preview) and is the source of truth for behavior.

---

## 1. What the MPSA is

The MPSA is the master contract LUCI signs with a customer; it governs every engagement (license, term, fees, installation, data, warranties, liability, indemnification) and pulls in Exhibits A (fee schedule), B/C (support & CARE), D (SOW), and E (software terms). It is **executed once per customer**, not per project.

Customization is **mostly filling in the blanks** from the salesperson's (Mike's) uploaded proposal: the effective date, the customer's legal name and entity type, addresses, and the two signers. The legal boilerplate is **locked** — never rewritten. The deliverable is the **native `.docx`** (the customer signs in Word / DocuSign), not a PDF.

### How it differs from the HTML templates (read this first)

| | HTML templates (Proposal, SOW, BE, Capabilities, Deck, Upgrade) | MPSA (Word) |
|---|---|---|
| Master format | `.html` | `.docx` |
| Edit model | Click-to-type in a rendered preview | Programmatic fill-from-proposal (no in-preview typing) |
| Preview | Live HTML (editable) | Read-only HTML render of the `.docx` (mammoth) |
| Export | PDF (headless Chrome) | Native `.docx` (Word download) |
| Page tools | `fit-check.py`, `pack-content.py`, footer renumbering | None — Word handles pagination + the dynamic page field |
| Locked content | Locked pages/regions (CSS, diagrams, marketing) | Locked legal boilerplate (Sections 1–13, Exhibits B/C/E) + header + footer |

**Do not** reuse the HTML pipeline's fit-check / pack-content / render-pdf / footer-numbering on the MPSA — those are HTML/PDF-only and do not operate on Word files.

---

## 2. Template assets (source of truth)

All assets live in the LUCI design-system repo and are mirrored to the shared OneDrive "Cursor Branding Files" folder. The web app should read them from the same source (or its own mirror).

| Asset | Path | Purpose |
|---|---|---|
| Master `.docx` | `ui_kits/sales/mpsa-vendor-protective.docx` | Template with a professional header + footer already built in; underscore blanks to fill |
| Template SKILL | `ui_kits/internal-portal/customization/mpsa/SKILL.md` | The blank map, fill rules, locked regions, do-nots |
| Brand SKILL | `ui_kits/internal-portal/customization/_brand/SKILL.md` | Shared voice/brand guardrails (the MPSA points here for voice) |
| Header builder | `scripts/build-mpsa-master.py` | Rebuilds the header on the master if v6 is re-copied (master-only, not per client) |
| Fill script (ref) | `scripts/fill-mpsa.py` | Reference implementation of the blank-fill (python-docx) |

### Master `.docx` — what's already built in

- **Header** (added to v6): a borderless 2-column table — LUCI logo (`assets/logos/luci-full-mintmark-blacktext.png`, ~1.3″ wide) left, "MASTER PURCHASE AND SERVICES AGREEMENT" (8pt gray, tracked uppercase) right, with a thin hairline below. One header per section (the master has one section).
- **Footer** (from v6): "LUCI Systems, LLC | Master Purchase & Services Agreement | Confidential | Page <field>" — the page number is a **dynamic PAGE field**, so Word renders the real page number per page. Do not replace it with a literal.
- **Body**: Sections 1–13 + signature block + Exhibits A–E. Only the underscore blanks (below) are fillable; all other text is locked.

---

## 3. The blank map (what the web app fills)

The master's blanks are **underscore runs** inside specific paragraphs / table cells. The reference fill script walks runs in order and replaces each `___+` sequence with the next value. The web app must fill the same fields from the uploaded proposal.

| # | Master location | Blank | Filled from (proposal) | Notes |
|---|---|---|---|---|
| 1 | Preamble (¶3) | `dated as of __________` | Effective Date | Format "Month DD, YYYY" |
| 2 | Preamble (¶3) | `and __________ ("Customer")` | Customer legal name | Exact signing entity |
| 3 | Preamble (¶3) | `a __________,` | Customer entity type | **No leading "a"** — the template already has "a " (pass "Nevada limited liability company", not "a Nevada…") |
| 4 | Preamble (¶3) | `principal place of business at __________` | Customer address | Principal place of business |
| 5 | Recital (¶4) | `facility located at __________` | Facility address | Site of install; "Same as above" if identical to #4 |
| 6 | Notices (¶47) | `If to Customer: __________` | Customer notice address | Usually "Attn: <role>, <address>" |
| 7 | Signature table, LUCI cell | `Name:` / `Title:` / `Date:` | LUCI signer | e.g. Mike Epstein / CEO |
| 8 | Signature table, Customer cell | `Name:` / `Title:` / `Date:` | Customer signer | From Mike / the deal |

**Signature lines (the long underscore lines above "Signature") are left blank** — they are for wet signatures, not fill-in. Do not replace them.

### Exhibits A & D — attachments, not text blanks

- **Exhibit A** (fee schedule) and **Exhibit D** (signed SOW) are **placeholders by design** ("This Exhibit A is a placeholder… will be provided from the LUCI Proposal…"). They are attached in Word after the blanks are filled — the fill step does **not** attach files. Leave the placeholder paragraphs in place; do not delete them.
- **Exhibits B, C, E** are standard support/CARE/software terms — locked, no per-customer content.

### Two fill strategies (pick one)

1. **Run-by-run underscore replacement** (matches the reference `fill-mpsa.py` and the current master — no master modification needed): walk the document's runs in order; for each run containing `___+`, replace the next underscore sequence with the next value. Handles multi-blank runs (the preamble's entity + address live in one run).
2. **Token placeholders** (optional, if the web app prefers): replace the master's underscore blanks with `{{tokens}}` (e.g. `{{effective_date}}`) and fill by token. This requires a tokenized master variant — keep it in sync with the underscore master if you go this route.

Either way, **preserve the document's formatting and styles** — fill the text node only, never rewrite the paragraph or re-apply styling.

---

## 4. Studio registration (the card)

Register the MPSA in the web studio's template catalog. Suggested fields (mirror the Cursor studio schema):

| Field | Value |
|---|---|
| `id` | `mpsa` |
| `title` | `MPSA - Vendor Protective` |
| `status` | `ready` |
| `description` | Master Purchase & Services Agreement (Word .docx). Fill the blanks from Mike's proposal; preview in-browser; export .docx. Legal boilerplate locked; header/footer built into the master. |
| `folder` | `mpsa` |
| `masterFile` | `mpsa-vendor-protective.docx` |
| `clientSuffix` | `mpsa` |
| `skillPath` | `ui_kits/internal-portal/customization/mpsa/SKILL.md` |
| `isDocx` | `true` (or detect from `masterFile` ending `.docx`) |

### Card UI differences from HTML templates

- **No iframe thumbnail / "Open preview" portal link.** HTML templates thumbnail their HTML preview in an iframe; a `.docx` has no HTML preview URL. Show a **DOCX badge** placeholder instead (the Cursor studio uses a "DOCX" pill on a light card with the text "Word document — preview renders via the local dev server").
- **No "Copy doc URL" action** (there is no portal HTML preview URL to copy). The primary card action is **"Copy starter prompt"** (generates the fill-workflow prompt) — see §6.
- A "Word .docx — fill blanks, preview in-browser" note tells users it's a different pipeline.

---

## 5. Customization flow (end-to-end)

1. **Create a client copy** of the master `.docx` (the web app's equivalent of `create-client-workspace.sh`): copy `mpsa-vendor-protective.docx` to a per-client working file named `<client-slug>-mpsa.docx`. Do **not** modify the master. No CSS/asset path-rewriting is needed (a `.docx` carries its assets inside the zip).
2. **Ingest the proposal** Mike uploads (the proposal doc/spreadsheet) and extract the eight values in §3. The proposal's cover, prepared-for block, and investment summary carry most of them. If a value isn't stated (e.g. the customer's legal entity type or signer), **leave the blank underscored** and flag it for Mike to fill in Word — never invent a legal entity type on a signed contract.
3. **Fill the blanks** in the client `.docx` (run-by-run underscore replacement or token fill — §3). Omit any value to leave its blank underscored.
4. **Render the preview** — convert the filled `.docx` to HTML (mammoth) and show it read-only in the studio preview pane (§7). The user reviews the filled blanks.
5. **Export** — serve the native `.docx` as a download with the house filename convention (§8). The user opens it in Word, attaches Exhibit A (signed fee schedule) + Exhibit D (signed SOW), and sends for signature.

### Locked regions (no edits of any kind)

- **All legal boilerplate** — Sections 1–13 and Exhibits B/C/E. No rewording, reordering, or "improvements." A term change is a legal review, not a customization — escalate, do not edit in the studio.
- **The header and footer** (logo, title, hairline, footer text + dynamic page field). Built into the master by `build-mpsa-master.py` / v6.
- **The Exhibit A/D placeholder paragraphs** — intentional; leave them until the signed fee schedule / SOW is attached in Word.
- **The signature lines** (long underscore lines above "Signature") — for wet signatures.

If a user asks to change locked legal text, **do not edit first** — flag the lock and ask whether to override (and if so, whether it's local to this client doc or canonical). This mirrors the HTML templates' locked-page gate.

---

## 6. Starter prompt (the card's "Copy starter prompt" output)

The card's primary action generates a prompt that tells the customization agent what to do. For a `.docx` template it must be **docx-specific** (not the HTML prompt). Reference content:

```text
Customize the LUCI MPSA - Vendor Protective for [CLIENT NAME].

Read ONLY these 2 SKILL files for instructions (in the OneDrive "Cursor Branding Files" folder):
- OneDrive "Cursor Branding Files" folder/ui_kits/internal-portal/customization/_brand/SKILL.md
- OneDrive "Cursor Branding Files" folder/ui_kits/internal-portal/customization/mpsa/SKILL.md

This is a WORD (.docx) template, not an HTML template. The agent fills the
blanks from Mike's uploaded proposal; the legal boilerplate is locked. There
is no fit-check / pack-content / render-pdf step — those are HTML/PDF-only.
The deliverable is the native .docx.

Create a client workspace (the script detects the .docx master):
  scripts/create-client-workspace.sh "[CLIENT NAME]" mpsa-vendor-protective mpsa
  → ~/Desktop/LUCI Docs/[client-name]/clients/[client-name]-mpsa.docx

Fill the blanks from Mike's proposal (see the template SKILL.md blank map):
  python3 scripts/fill-mpsa.py --out <working .docx> \
    --client "..." --client-entity "..." --client-address "..." \
    --facility "..." --notice-address "..." --effective-date "..." \
    --luci-signer "..." --luci-title "..." --customer-signer "..." --customer-title "..."

Preview (dev server renders the .docx as read-only HTML):
  cd ~/Desktop/LUCI\ Docs/[client-name] && python3 ui_kits/internal-portal/customization/luci-dev-server.py
  http://127.0.0.1:8771/clients/[client-name]-mpsa.docx
  Download .docx from the toolbar (or add ?download=1 for the raw Word file).

Client notes:
[customer legal name + entity type (no leading "a"), address, facility,
 notice address, signers, effective date — from Mike's proposal]
```

The web app should generate the equivalent of this for its own customization agent. The key differences from the HTML starter prompt: it names `fill-mpsa.py` (not fit-check/pack/render-pdf), the `.docx` preview URL, and the Download-.docx export.

---

## 7. Preview (docx → HTML, read-only)

Browsers cannot open a `.docx` directly, so the studio preview is a **read-only HTML render** of the Word document.

- **Renderer:** mammoth (Python: `mammoth.convert_to_html`; or mammoth.js in a JS stack). It produces clean HTML (headings, paragraphs, tables, lists) from the `.docx` body.
- **Header/footer/logo do not render in the HTML preview** — mammoth renders the body only. Show a small note ("Header, footer, and LUCI logo render in Microsoft Word. To edit text, use Download .docx and open in Word.") so the user isn't surprised. The preview is for verifying the **filled blanks**, not the full chrome.
- **Read-only — no click-to-edit.** Unlike the HTML templates, the user cannot type into the preview. Text tweaks happen in Word after export. Do not wire up an edit-bar / save-DOM flow for the `.docx` preview.
- **Toolbar:** a "Download .docx" button (the primary action) and the filename. The Cursor studio uses a sticky top toolbar (dark, mint pill button). Style per the web app's design system.
- **Cache-busting:** serve the preview with `Cache-Control: no-cache, must-revalidate` so re-fills show immediately.

### Reference preview implementation (Cursor studio)

`GET /clients/<file>.docx` → the dev server renders the `.docx` to HTML via mammoth, wraps it in a styled page (max-width ~8.5in, white "sheet" on a gray mat, Calibri-ish body to echo Word), and serves `text/html`. `GET /clients/<file>.docx?download=1` → serves the raw `.docx` with `Content-Type: application/vnd.openxmlformats-officedocument.wordprocessingml.document` and `Content-Disposition: attachment; filename="<file>.docx"`. The web app should provide the same two behaviors (preview HTML + raw download).

---

## 8. Export (native .docx download)

The deliverable is the **native `.docx`** — not a PDF. The user downloads the filled Word file, opens it in Word, attaches Exhibit A + D, and sends for signature.

- **Filename convention (house rule, automatic):** `<ClientName>-MPSA <M+D+YY>.docx` — e.g. `Elwha River Casino-MPSA 81326.docx` (Aug 13 '26). The client name is read from the document/proposal; the date is today's export date (month/day, no leading zeros). Apply this convention to every MPSA export; do not let the user rename it ad hoc. (This mirrors the HTML templates' PDF naming convention `<ClientName>-<DocType> <M+D+YY>.pdf`.)
- **No PDF render.** Do not offer a "Download PDF" for the MPSA. If a PDF is ever needed, the user prints to PDF from Word (the header/footer/page field render correctly there). A headless-Chrome PDF of the mammoth HTML preview would be lossy and is not the deliverable.
- **Content-Type:** `application/vnd.openxmlformats-officedocument.wordprocessingml.document`; `Content-Disposition: attachment; filename="<convention>.docx"`.

---

## 9. Tooling / dependencies

The reference Cursor studio uses Python; the web app may use a different stack but must replicate the behavior. Recommended mapping:

| Capability | Reference (Python) | Web-app options |
|---|---|---|
| Read/fill `.docx` | `python-docx` (run-by-run underscore replacement) | `python-docx` in a backend service; or `docx` / `docx-templater` (Node); or a Python sidecar |
| `.docx` → HTML preview | `mammoth` | `mammoth` (Python) or `mammoth.js` (browser/Node) — same library, same output |
| Header builder (master-only) | `scripts/build-mpsa-master.py` (python-docx + the LUCI logo PNG) | Run the reference script as a backend step, or port the header construction |
| Client workspace | `scripts/create-client-workspace.sh` (copies master, symlinks assets) | A backend endpoint that copies the master `.docx` to a per-client file |

**Install (reference):** `pip3 install python-docx mammoth` (already in `requirements.txt`). The web app's backend should declare equivalents.

**One master, per-client copies.** The master `.docx` is never modified and never resized to fit a client. Each client gets its own copy; only the copy's blanks are filled. This mirrors the canonical-asset doctrine the HTML templates follow.

---

## 10. Edge cases & do-nots

- **Entity type has no leading "a".** The template already says `a __________`; pass `Nevada limited liability company` (not `a Nevada…`), or it reads "a a Nevada…".
- **Don't invent the entity type or signer.** If Mike's proposal doesn't state the legal entity type or the signer, leave the blank underscored and flag it for Mike to fill in Word. A wrong entity type on a signed contract is a legal error.
- **Don't fill the signature lines** (the long underscore lines above "Signature") — those are for wet signatures.
- **Don't delete the Exhibit A/D placeholder paragraphs** — they are intentional. Leave them until the signed fee schedule / SOW is attached in Word.
- **Don't run `pack-content.py`, `fit-check.py`, or `render-pdf.sh`** on a `.docx` — they are HTML/PDF-only and do not operate on Word files. The MPSA has no page-packing or footer-numbering step (Word handles pagination and the dynamic page field).
- **Don't edit the legal boilerplate** (Sections 1–13, Exhibits B/C/E), header, or footer. See §5 locked regions.
- **Rebuilding the header** is a master-only step (`build-mpsa-master.py`), run only if v6 is re-copied or the header design changes. Do not run it on a client copy.

---

## 11. Acceptance criteria

The MPSA template is done in the web app when:

- [ ] The studio card shows "MPSA - Vendor Protective" with a DOCX badge (no iframe thumbnail, no portal-HTML "Open preview" link), and a "Copy starter prompt" action that emits the docx-specific prompt (§6).
- [ ] Creating a client copy produces `<client-slug>-mpsa.docx` from the master, with the header (logo + title + hairline) and footer (dynamic page field) intact.
- [ ] Filling from a sample proposal populates all eight blanks (§3) and leaves unprovided ones underscored; the entity type has no doubled "a".
- [ ] The preview renders the filled `.docx` as read-only HTML (mammoth) with a Download-.docx toolbar; the filled values are visible in the preview.
- [ ] Download yields the native `.docx` (correct Content-Type) named `<ClientName>-MPSA <M+D+YY>.docx`.
- [ ] Legal boilerplate, header, footer, signature lines, and Exhibit A/D placeholders are unchanged after fill.
- [ ] No HTML-pipeline tools (fit-check / pack-content / render-pdf) are invoked on the `.docx`.

---

## Reference files

- Master: `ui_kits/sales/mpsa-vendor-protective.docx`
- Template SKILL: `ui_kits/internal-portal/customization/mpsa/SKILL.md`
- Brand SKILL: `ui_kits/internal-portal/customization/_brand/SKILL.md`
- Fill script: `scripts/fill-mpsa.py`
- Header builder: `scripts/build-mpsa-master.py`
- Dev server (preview + download): `ui_kits/internal-portal/customization/luci-dev-server.py` (see `_render_docx_html` + the `.docx` branch in `do_GET`)
- Studio UI card + starter-prompt branch: `ui_kits/internal-portal/index.html` (see `CURSOR_TEMPLATES` `mpsa` entry + `starterPromptForTemplate` `isDocx` branch)
