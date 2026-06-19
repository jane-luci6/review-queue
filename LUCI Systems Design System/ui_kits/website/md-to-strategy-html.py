#!/usr/bin/env python3
"""One-off generator: website-strategy.md → website-strategy.html (LUCI review doc)."""
import base64
import re
import html
from pathlib import Path

HERE = Path(__file__).parent
MD = HERE / "website-strategy.md"
OUT = HERE / "website-strategy.html"
LOGO_PNG = HERE.parent.parent / "assets" / "logos" / "luci-full-white.png"
LOGO_SRC = "data:image/png;base64," + base64.b64encode(LOGO_PNG.read_bytes()).decode()

def slug(text: str) -> str:
    t = re.sub(r"[^\w\s-]", "", text.lower())
    return re.sub(r"[-\s]+", "-", t).strip("-")

def inline(s: str) -> str:
    s = html.escape(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"\*(.+?)\*", r"<i>\1</i>", s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(
        r"\[([^\]]+)\]\(([^)]+)\)",
        r'<a href="\2">\1</a>',
        s,
    )
    return s

def parse_table(lines: list[str]) -> str:
    rows = []
    for line in lines:
        if not line.strip().startswith("|"):
            break
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if all(re.match(r"^:?-+:?$", c) for c in cells):
            continue
        rows.append(cells)
    if not rows:
        return ""
    out = ['<ul class="doc-rows">']
    start = 0
    if len(rows) > 1 and len(rows[0]) == len(rows[1]):
        # use first row as header hints only if second row looks like data
        pass
    for row in rows:
        label = inline(row[0]) if row else ""
        if len(row) == 1:
            val = ""
        elif len(row) == 2:
            val = f'<p class="doc-prose">{inline(row[1])}</p>'
        else:
            parts = [f"<p class=\"doc-prose\"><b>{inline(row[i])}</b></p>" if i == 1 else f'<p class="doc-prose">{inline(row[i])}</p>' for i in range(1, len(row))]
            val = "".join(parts)
        out.append(
            f'<li><span class="doc-rows__label">{label}</span>'
            f'<span class="doc-rows__value">{val}</span></li>'
        )
    out.append("</ul>")
    return "\n".join(out)

def parse_md(text: str) -> tuple[list[tuple[str, str]], list[str]]:
    """Returns (toc entries, section html chunks)."""
    lines = text.splitlines()
    toc: list[tuple[str, str]] = []
    sections: list[str] = []
    i = 0
    intro: list[str] = []
    while i < len(lines):
        if lines[i].startswith("## "):
            break
        if not lines[i].startswith("# "):
            intro.append(lines[i])
        i += 1
    if intro:
        sections.append(
            '<section class="doc-section">' + render_body(intro) + "</section>"
        )
    while i < len(lines):
        if not lines[i].startswith("## "):
            i += 1
            continue
        title = lines[i][3:].strip()
        sid = slug(title)
        toc.append((title, sid))
        i += 1
        body: list[str] = []
        while i < len(lines) and not lines[i].startswith("## "):
            body.append(lines[i])
            i += 1
        sections.append(
            f'<section class="doc-section"><h2 class="doc-chapter" id="{sid}">{html.escape(title)}</h2>'
            + render_body(body)
            + "</section>"
        )
    return toc, sections

def render_body(body: list[str]) -> str:
    out: list[str] = []
    j = 0
    while j < len(body):
        line = body[j]
        if line.strip() in ("", "---"):
            j += 1
            continue
        if line.startswith("### "):
            out.append(f'<h3 class="doc-subsection__title">{inline(line[4:].strip())}</h3>')
            j += 1
            continue
        if line.strip().startswith("|"):
            tbl = []
            while j < len(body) and body[j].strip().startswith("|"):
                tbl.append(body[j])
                j += 1
            out.append(parse_table(tbl))
            continue
        if line.startswith("```"):
            lang = line[3:].strip()
            j += 1
            block = []
            while j < len(body) and not body[j].startswith("```"):
                block.append(html.escape(body[j]))
                j += 1
            if j < len(body):
                j += 1
            pre = "\n".join(block)
            out.append(
                f'<pre class="doc-snippet" aria-label="{html.escape(lang or "code")}">{pre}</pre>'
            )
            continue
        if line.startswith("- ") or line.startswith("* "):
            items = []
            while j < len(body) and (
                body[j].startswith("- ") or body[j].startswith("* ")
            ):
                items.append(f"<li><p class=\"doc-prose\">{inline(body[j][2:].strip())}</p></li>")
                j += 1
            out.append('<ul class="doc-list">' + "".join(items) + "</ul>")
            continue
        if line.startswith("> "):
            quote = []
            while j < len(body) and body[j].startswith("> "):
                quote.append(inline(body[j][2:].strip()))
                j += 1
            out.append(
                '<aside class="doc-callout doc-callout--key">'
                + "".join(f'<p class="doc-prose">{q}</p>' for q in quote)
                + "</aside>"
            )
            continue
        if re.match(r"^\d+\.\s", line):
            items = []
            num_re = re.compile(r"^\d+\.\s*")
            while j < len(body) and re.match(r"^\d+\.\s", body[j]):
                text = num_re.sub("", body[j])
                items.append(f'<li><p class="doc-prose">{inline(text)}</p></li>')
                j += 1
            out.append('<ol class="doc-list">' + "".join(items) + "</ol>")
            continue
        para = [line]
        j += 1
        while j < len(body) and body[j].strip() and not body[j].startswith((
            "#", "|", "-", "*", ">", "```"
        )) and not re.match(r"^\d+\.\s", body[j]):
            para.append(body[j])
            j += 1
        out.append(f'<p class="doc-prose">{inline(" ".join(para))}</p>')
    return "".join(out)

def main():
    md = MD.read_text(encoding="utf-8")
    title_m = re.search(r"^# (.+)$", md, re.M)
    title = title_m.group(1) if title_m else "Website strategy"
    status_m = re.search(r"\*\*Status:\*\* (.+)", md)
    status = status_m.group(1) if status_m else "Draft"
    toc, sections = parse_md(md)
    toc_html = "".join(
        f'<li><a href="#{sid}">{html.escape(t)}</a></li>' for t, sid in toc
    )
    lib = (
        '<li><a href="../review/messaging/messaging-guide.html">Messaging guide</a>'
        "<span>Canonical copy</span></li>"
        '<li><a href="LUCI_Messaging_Framework_V6-reference.html">Messaging Framework V6</a>'
        "<span>Reference</span></li>"
        '<li><a href="website-strategy.html" class="is-current">Website strategy</a>'
        "<span>Updated Jun 2026</span></li>"
        '<li><a href="website-ia-wireframe.html">IA wireframe</a>'
        "<span>Section map · no copy</span></li>"
    )
    body = "\n".join(sections)
    html_out = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="robots" content="noindex, nofollow">
  <title>{html.escape(title)}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Syncopate:wght@700&family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../review/messaging/messaging-docs.css">
  <style>
    .doc-snippet {{
      margin: 16px 0 24px;
      padding: 18px 20px;
      max-width: var(--read);
      font-family: var(--body);
      font-size: 13px;
      line-height: 1.55;
      color: var(--navy);
      background: var(--off-white);
      border-left: 4px solid var(--mint);
      white-space: pre-wrap;
      overflow-x: auto;
    }}
    .doc-list {{ list-style: none; margin: 0 0 20px; padding: 0; max-width: var(--read); }}
    .doc-list li {{ padding: 10px 0; border-bottom: 1px solid var(--rule-light); }}
    .doc-list li:last-child {{ border-bottom: none; }}
    .doc-prose code {{ font-size: 0.92em; color: var(--navy-mid); }}
  </style>
</head>
<body>
  <div class="resource">
    <header class="resource__masthead">
      <div class="resource__masthead-row">
        <a href="https://lucisystems.com" class="resource__logo"><img src="{LOGO_SRC}" alt="LUCI Systems" width="120" height="24"></a>
        <span class="resource__badge">Website planning</span>
      </div>
      <h1 class="resource__hero-title">{html.escape(title)}</h1>
      <p class="resource__hero-deck">IA, homepage map, two pillars, proof rules — lucisystems.com refresh</p>
      <p class="resource__meta">{html.escape(status)} · Source: <code>website-strategy.md</code></p>
      <nav class="resource__crumbs" aria-label="Breadcrumb">
        <a href="../../index.html">Design hub</a>
        <span>/</span>
        <span aria-current="page">Website strategy</span>
      </nav>
    </header>
    <div class="resource__layout">
      <aside class="resource__sidebar">
        <p class="resource__nav-kicker">Related</p>
        <ul class="resource__library">{lib}</ul>
        <p class="resource__nav-kicker">On this page</p>
        <nav aria-label="On this page"><ul class="resource__toc">{toc_html}</ul></nav>
      </aside>
      <main class="resource__article">
{body}
      </main>
    </div>
  </div>
</body>
</html>
"""
    OUT.write_text(html_out, encoding="utf-8")
    print(f"Wrote {OUT}")

if __name__ == "__main__":
    main()
