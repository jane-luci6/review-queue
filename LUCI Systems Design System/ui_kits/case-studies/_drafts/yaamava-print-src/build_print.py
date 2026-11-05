import re, sys
F = "/tmp/frag/"
OUT = "/Users/janehaynie/Documents/Cursor Projects/luci-design/LUCI Systems Design System/ui_kits/case-studies/_drafts/yaamava-partnership-print.html"

def frag(name):
    return open(F + name).read()

about = frag("about.html")
pages = [
    ["00-hero.html", "10-timeline.html"],
    ["20-foundation.html"],
    ["30-expansion.html"],
    ["40-nine09.html"],
    ["50-eight-years.html", "91-ledger.html"],
    ["95-next.html", "99-cta.html"],
]

css = frag("canon.css") + frag("v2.css") + open("/tmp/print.css").read()

body = []
for i, names in enumerate(pages, 1):
    inner = "\n".join(frag(n) for n in names).replace("<!--ABOUT-->", about)
    body.append(f'<div class="pg pg--{i}">\n{inner}\n</div>')

html = f"""<!DOCTYPE html>
<html lang="en"><head>
<meta charset="utf-8">
<title>Yaamava&rsquo; Resort &amp; Casino &mdash; LUCI Case Study</title>
<link rel="stylesheet" href="../../../assets/fonts/luci-brand-fonts.css">
<style>
{css}
</style>
</head>
<body>
<article class="cs-page"><div class="cs-page__sheet">
{chr(10).join(body)}
</div></article>
</body></html>
"""

html = re.sub(r"yaamava-mockup-assets/(p-[a-z0-9\-]+\.jpg)", r"../assets/yaamava/partnership/\1", html)
for n in ["event-entry-led-web.jpg", "gaming-floor-led-web.jpg", "sportsbook-led-web.jpg", "install-column-commission-web.jpg"]:
    html = html.replace("yaamava-mockup-assets/" + n, "../assets/yaamava/" + n)
html = (html.replace("yaamava-mockup-assets/logos/", "../../../assets/logos/")
            .replace("yaamava-mockup-assets/luci-rack-web.jpg", "../assets/luci-rack-web.jpg")
            .replace("yaamava-mockup-assets/mesh/", "../assets/mesh/"))
assert "yaamava-mockup-assets" not in html
open(OUT, "w").write(html)
print("wrote", OUT, len(html))
