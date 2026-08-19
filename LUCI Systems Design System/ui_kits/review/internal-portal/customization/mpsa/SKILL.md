---
name: luci-mpsa
description: >-
  Customize the LUCI Master Purchase and Services Agreement (MPSA — Vendor
  Protective) for a specific customer. Use when a deal is closing and the
  signed master agreement is needed alongside the proposal/SOW. A Word (.docx)
  template — the agent fills the blanks from Mike's uploaded proposal; Mike
  reviews the rendered preview in Cursor and exports the .docx. ~12 pages.
---

# MPSA — Vendor Protective · customization

The LUCI Master Purchase and Services Agreement is the master contract that governs every engagement: license, term, fees, installation, data, warranties, liability, indemnification, and the Exhibits (A fee schedule, B/C support & CARE, D SOW, E software terms). **This is a Word document (`.docx`), not an HTML template** — so the customization model is different from the sales/proposal/SOW templates:

- **Fill the blanks, don't redesign.** The legal boilerplate is locked. The agent's job is to fill the underscore blanks from the values in Mike's uploaded proposal. There is no in-browser click-to-type editing and no `pack-content` / `fit-check` / `render-pdf` step — those are HTML/PDF-only.
- **Preview is read-only.** The dev server renders the `.docx` to HTML (mammoth) so Mike can review the filled agreement in Cursor before export. Text tweaks happen in Word after export — the preview is not an edit surface.
- **Export is the native `.docx`.** The deliverable is the Word file itself (Download .docx from the preview toolbar). No PDF render.

**Workflow (docx-specific):** create the workspace → run `scripts/fill-mpsa.py` with the values extracted from Mike's proposal → start the dev server → open the `.docx` preview in Cursor → Download .docx. See `../_brand/SKILL.md` for the two-folder architecture, voice, and the general customization contract; this file covers only the MPSA blank map and the docx fill workflow.

Voice: see `../_brand/SKILL.md` → Voice & tone. The MPSA is a legal instrument — keep it factual and institutional; do not add marketing register to the body.

## When to use

When a deal is closing and the customer needs the signed master agreement. The MPSA is executed once per customer and governs all future Work Orders; it is **not** a per-project proposal. Mike uploads the proposal (or the deal terms) and the agent fills the MPSA blanks from it. The signed Fee Schedule (Exhibit A) and signed Statement of Work (Exhibit D) are attached to the executed MPSA — they come from the proposal and SOW Mike already produced in the studio.

## The blank map — what to fill

The master is `ui_kits/sales/mpsa-vendor-protective.docx`. It already has a professional header (LUCI logo + "MASTER PURCHASE AND SERVICES AGREEMENT" + hairline) and footer ("LUCI Systems, LLC | Master Purchase & Services Agreement | Confidential | Page <dynamic>") — both **locked**. Only the body blanks below are filled; everything else is locked legal text.

`scripts/fill-mpsa.py` fills these blanks run-by-run (the master's formatting and styles are preserved). Omit any value to leave its blank underscored and fill it later in Word.

| # | Location | Blank | Filled from |
|---|----------|-------|-------------|
| 1 | Preamble (¶3) | `dated as of __________` | **Effective Date** — the execution date (format "Month DD, YYYY") |
| 2 | Preamble (¶3) | `and __________ ("Customer")` | **Customer legal name** — the exact entity signing (e.g. "Elwha River Casino") |
| 3 | Preamble (¶3) | `a __________,` | **Customer entity type** — *without* the leading "a" (e.g. "Nevada limited liability company", "Washington tribal corporation"). The template already supplies "a ". |
| 4 | Preamble (¶3) | `principal place of business at __________` | **Customer address** — principal place of business |
| 5 | Recital (¶4) | `facility located at __________` | **Facility address** — the site where the LUCI System is installed (often the same as #4; use "Same as above" if so) |
| 6 | Notices (¶47) | `If to Customer: __________` | **Customer notice address** — where legal notices go (usually "Attn: <role>, <address>") |
| 7 | Signature block (table, LUCI cell) | `Name:` / `Title:` / `Date:` | **LUCI signer** — name, title, date (e.g. Mike Epstein / CEO) |
| 8 | Signature block (table, Customer cell) | `Name:` / `Title:` / `Date:` | **Customer signer** — name, title, date (from Mike / the deal) |

**Signature lines (the long underscore lines above "Signature") are left blank** — they are for wet signatures, not fill-in. Do not replace them.

### Exhibits A & D — attachments, not text blanks

- **Exhibit A (Fee Schedule)** and **Exhibit D (Statement of Work)** are placeholders by design ("This Exhibit A is a placeholder… will be provided from the LUCI Proposal…"). They are **attachments**, not text blanks. After filling the text blanks, attach the signed Fee Schedule (from the proposal's investment summary / line items) to Exhibit A and the signed SOW to Exhibit D. This is done in Word (Insert → attach) or by the agent in a follow-up step — `fill-mpsa.py` does not attach files. Leave the placeholder paragraphs in place until the attachment is ready; do not delete them.
- **Exhibits B, C, E** are standard support/CARE/software terms — **locked**, no per-customer content.

---

## Workflow — fill the MPSA

1. **Create the workspace** (same as HTML templates — the script now detects the `.docx` master):
   ```
   scripts/create-client-workspace.sh "<Customer Name>" mpsa-vendor-protective mpsa
   ```
   → `~/Desktop/LUCI Docs/<client-slug>/clients/<client-slug>-mpsa.docx` (a copy of the master).

2. **Read Mike's uploaded proposal** and extract the eight values above (effective date, customer legal name + entity type + address, facility address, notice address, LUCI signer, customer signer). The proposal's cover, prepared-for block, and investment summary carry most of these.

3. **Fill the blanks:**
   ```
   python3 scripts/fill-mpsa.py \
     --out ~/Desktop/LUCI\ Docs/<client-slug>/clients/<client-slug>-mpsa.docx \
     --client "<Customer legal name>" \
     --client-entity "<entity type, no leading 'a'>" \
     --client-address "<principal place of business>" \
     --facility "<facility address or 'Same as above'>" \
     --notice-address "Attn: <role>, <address>" \
     --effective-date "Month DD, YYYY" \
     --luci-signer "<name>" --luci-title "<title>" \
     --customer-signer "<name>" --customer-title "<title>"
   ```
   Omit `--luci-date` / `--customer-date` to leave the signature dates blank for signing day.

4. **Start the dev server** from the workspace root:
   ```
   cd ~/Desktop/LUCI\ Docs/<client-slug>
   python3 ui_kits/internal-portal/customization/luci-dev-server.py
   ```

5. **Open the preview** in Cursor's in-editor browser: `http://127.0.0.1:8771/clients/<client-slug>-mpsa.docx`
   The `.docx` is rendered as a read-only HTML preview (mammoth). The header, footer, and LUCI logo render in Word; the preview shows the body so Mike can verify the filled blanks. Use **Download .docx** in the toolbar for the raw Word file.

6. **Export:** Download .docx from the toolbar (or `curl http://127.0.0.1:8771/clients/<client-slug>-mpsa.docx?download=1`). Open in Word, attach Exhibit A (signed Fee Schedule) and Exhibit D (signed SOW), and the file is ready to send for signature.

---

## Do not

- **Do not edit the legal boilerplate** — Sections 1–13 and Exhibits B/C/E are locked. No rewording, no reordering, no "improvements." If a term needs to change, that is a legal review, not a customization — escalate to Jane, do not edit in the studio.
- **Do not change the header or footer** — they are part of the master (logo, title, hairline, footer text + dynamic page field). The header was added by `scripts/build-mpsa-master.py`; the footer is the v6 original.
- **Do not add a leading "a" to the customer entity type** — the template already has "a " before the blank; pass the entity type without it (e.g. "Nevada limited liability company", not "a Nevada limited liability company").
- **Do not delete the Exhibit A / D placeholder paragraphs** — they are intentional ("…will be provided from the LUCI Proposal…"). Leave them until the signed Fee Schedule / SOW is attached.
- **Do not fill the signature lines** (the long underscore lines above "Signature") — those are for wet signatures.
- **Do not run `pack-content.py`, `fit-check.py`, or `render-pdf.sh`** on a `.docx` — those are HTML/PDF-only tools and will not operate on Word files. The MPSA has no page-packing or footer-numbering step (Word handles pagination and the dynamic page field).
- **Do not invent the customer's entity type or signer** — if Mike's proposal doesn't state the legal entity type or the signer, leave the blank underscored and flag it for Mike to fill in Word. A wrong entity type on a signed contract is a legal error, not a styling one.

---

## Common tasks

**New MPSA from Mike's proposal**
1. Create the workspace: `scripts/create-client-workspace.sh "<Customer>" mpsa-vendor-protective mpsa`.
2. Read the proposal; extract: effective date, customer legal name, entity type (no "a"), address, facility address, notice address, LUCI signer (name+title), customer signer (name+title).
3. Run `scripts/fill-mpsa.py --out <working .docx> …` with the values.
4. Start the dev server, open `http://127.0.0.1:8771/clients/<slug>-mpsa.docx` in Cursor, verify the filled blanks in the preview.
5. Download .docx, open in Word, attach Exhibit A (signed Fee Schedule) + Exhibit D (signed SOW), send for signature.

**Rebuild the master header** (only if the v6 .docx is re-copied or the header design changes):
```
cp "<new v6>.docx" ui_kits/sales/mpsa-vendor-protective.docx
python3 scripts/build-mpsa-master.py
```
This re-adds the header (logo + title + hairline) and leaves the footer intact. Do not run it on a client copy — it is a master-only step.
