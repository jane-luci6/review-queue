# LUCI Post 001 — What runs your property?

**Status:** Ready to post
**Format:** LinkedIn document carousel (4 slides)
**Category:** Educational
**Suggested date:** Wed 29 Jul 2026

---

## Upload

Upload `luci-post-001-orchestration-engine.pdf` as a **document**, not as images.
On LinkedIn: *Create post → + → Add a document → upload the PDF → give it a title.*

**Document title field:** `What runs your property?`

The individual `slide-01…04.png` files are here as backups in case you want to
repost single frames later, or reuse a slide in a deck. Don't upload them as a
four-image post — that loses the swipe behaviour.

---

## Caption — copy everything between the lines

---
What runs your property?

Point solutions. Control panels. Dashboards. Each one solves a piece of it — until you need everything working together.

An orchestration engine manages every point solution, every control panel, every dashboard from one interface — built to grow with your property.

See what that looks like on a live floor map → https://lucisystems.com/luci
---

## Link behaviour — important

The `SEE IT IN ACTION → LUCISYSTEMS.COM/LUCI` pill on slide 4 **is** a real
hyperlink in the PDF, so it works if someone downloads or opens the file in a
normal PDF reader. It will **not** be clickable inside LinkedIn — LinkedIn
rasterises carousel documents to flat images. That's why the link is also in the
caption; the caption link is the one that will actually get clicked.

Optional alternative: LinkedIn sometimes suppresses reach on posts containing
outbound links. If you want to test that, drop the URL from the caption, end with
"link in comments," and post the link as your own first comment.

**Before posting:** confirm `lucisystems.com/luci` is live. If the landing page
isn't published yet, either hold this post or swap the caption link for the
homepage.

---

## Design notes

- Slides 01–03 sit on the brochure's light cream field, Space Grotesk headlines,
  navy icon tiles with gold glyphs.
- Slide 04 flips to dark navy with a Syncopate headline — the field and typeface
  change are what mark it as the answer. Mint appears only on this slide.
- Source script: `outputs/render_p2_carousel8.py` (run as `sync4`), PDF assembled
  by `outputs/build_p2_pdf.py`.
