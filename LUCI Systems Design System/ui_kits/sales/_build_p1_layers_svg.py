#!/usr/bin/env python3
"""Build a layered SVG of the What's New page 1 for Compositor.
Each element is a named <g> group so Compositor shows them as separate layers.
"""
import base64

def b64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

MESH = b64("preview-mesh.png")          # 1000x563 rasterized mesh
MAP  = b64("assets/_p1-map-1400.png")    # 1400x798 map
LOGO = b64("assets/logos/luci-wordmark-white-320.png")  # 320x74

# color tokens
NAVY="#0A161C"; OFF="#F5F8FA"; INK="#1C2B33"; INK2="#354F5C"
MINT="#68E3BE"; MINTL="#2b9e80"; MUT="#49616E"
GHOST_MINT='rgba(43,158,128,0.28)'

# fonts
FD="'Syncopate','Arial Black',sans-serif"   # display
FH="'Space Grotesk','Trebuchet MS',sans-serif" # structure
FB="'Inter','Space Grotesk',sans-serif"      # body

parts = []
parts.append(f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" '
             f'viewBox="0 0 816 1056" width="816" height="1056">\n')
parts.append(f'<title>LUCI 2.0 What\'s New — Page 1 (layered)</title>\n')
parts.append('<desc>Layered export for Compositor. Toggle/hide groups to inspect each element.</desc>\n')

# ---- HEADER background (0..236) ----
parts.append('<g id="layer-header-bg" inkscape:label="header-bg" '
             'xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape">\n')
parts.append(f'<rect x="0" y="0" width="816" height="236" fill="{NAVY}"/>\n')
parts.append('</g>\n')

# ---- HEADER mesh texture (cover, 62%/28% focus, opacity .55) ----
parts.append('<g id="layer-header-mesh" inkscape:label="header-mesh" '
             'xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape">\n')
parts.append(f'<clipPath id="clip-head"><rect x="0" y="0" width="816" height="236"/></clipPath>\n')
# cover: mesh 1000x563 (aspect 1.776) -> cover 816x236 (aspect 3.49): scale by width -> 816 wide, 459 tall; focus 28% vertical -> offset -62
parts.append(f'<image x="0" y="-62" width="816" height="459" '
             f'xlink:href="data:image/png;base64,{MESH}" opacity="0.55" '
             f'preserveAspectRatio="xMidYMid slice" clip-path="url(#clip-head)"/>\n')
parts.append('</g>\n')

# ---- HEADER logo ----
parts.append('<g id="layer-header-logo" inkscape:label="header-logo" '
             'xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape">\n')
parts.append(f'<image x="56" y="32" width="121" height="28" '
             f'xlink:href="data:image/png;base64,{LOGO}"/>\n')
parts.append('</g>\n')

# ---- HEADER announce ----
parts.append('<g id="layer-header-announce" inkscape:label="header-announce" '
             'xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape">\n')
parts.append(f'<text x="56" y="92" font-family="{FH}" font-weight="700" font-size="10" '
             f'letter-spacing="2.4" fill="{MINT}">A NEW VERSION OF LUCI IS COMING</text>\n')
parts.append('</g>\n')

# ---- HEADER theme headline ----
parts.append('<g id="layer-header-theme" inkscape:label="header-theme" '
             'xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape">\n')
parts.append(f'<text x="56" y="128" font-family="{FD}" font-weight="700" font-size="30" '
             f'letter-spacing="1.5" fill="{OFF}">THE <tspan fill="{MINT}">POWER OF PROGRAMMING</tspan></text>\n')
parts.append(f'<text x="56" y="161" font-family="{FD}" font-weight="700" font-size="30" '
             f'letter-spacing="1.5" fill="{OFF}">IS IN YOUR HANDS</text>\n')
parts.append('</g>\n')

# ---- HEADER release date ----
parts.append('<g id="layer-header-date" inkscape:label="header-date" '
             'xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape">\n')
parts.append(f'<text x="56" y="216" font-family="{FH}" font-weight="700" font-size="9.5" '
             f'letter-spacing="2.2" fill="rgba(235,245,248,0.5)">RELEASE DATE</text>\n')
parts.append(f'<text x="146" y="216" font-family="{FH}" font-weight="700" font-size="20" '
             f'fill="{MINT}">January 19</text>\n')
parts.append('</g>\n')

# ---- FIELD map (236..1020) cover, bottom-right anchor ----
parts.append('<g id="layer-map" inkscape:label="map" '
             'xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape">\n')
parts.append(f'<clipPath id="clip-field"><rect x="0" y="236" width="816" height="784"/></clipPath>\n')
# map 1400x798 (aspect 1.755) -> cover 816x784 (aspect 1.04): scale by height -> 784 tall, 1375 wide; 100% focus -> x offset -559
parts.append(f'<image x="-559" y="236" width="1375" height="784" '
             f'xlink:href="data:image/png;base64,{MAP}" '
             f'preserveAspectRatio="xMidYMid slice" clip-path="url(#clip-field)"/>\n')
parts.append('</g>\n')

# ---- FIELD scrim (left-clearing fade + top fade) ----
parts.append('<g id="layer-scrim" inkscape:label="scrim" '
             'xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape">\n')
parts.append(f'<defs><linearGradient id="scrimH" x1="0" y1="0" x2="1" y2="0">'
             f'<stop offset="0" stop-color="{OFF}" stop-opacity="0.97"/>'
             f'<stop offset="0.40" stop-color="{OFF}" stop-opacity="0.93"/>'
             f'<stop offset="0.62" stop-color="{OFF}" stop-opacity="0.55"/>'
             f'<stop offset="0.78" stop-color="{OFF}" stop-opacity="0.12"/>'
             f'<stop offset="0.92" stop-color="{OFF}" stop-opacity="0"/></linearGradient>\n')
parts.append(f'<linearGradient id="scrimV" x1="0" y1="0" x2="0" y2="1">'
             f'<stop offset="0" stop-color="{OFF}" stop-opacity="0.82"/>'
             f'<stop offset="0.58" stop-color="{OFF}" stop-opacity="0"/></linearGradient></defs>\n')
parts.append(f'<rect x="0" y="236" width="816" height="784" fill="url(#scrimH)"/>\n')
parts.append(f'<rect x="0" y="236" width="816" height="455" fill="url(#scrimV)"/>\n')
parts.append('</g>\n')

# ---- LEAD-IN "LUCI 2.0 brings you" + mint rule ----
parts.append('<g id="layer-leadin" inkscape:label="leadin" '
             'xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape">\n')
parts.append(f'<text x="32" y="280" font-family="{FH}" font-weight="700" font-size="26" '
             f'fill="{INK}">LUCI 2.0 brings you</text>\n')
parts.append(f'<rect x="32" y="293" width="40" height="3" fill="{MINTL}"/>\n')
parts.append('</g>\n')

# ---- NUMERALS (ghost mint) ----
for num, x, y, sz in [("01",28,411,118),("02",424,411,118),("03",26,611,152)]:
    parts.append(f'<g id="layer-numeral-{num}" inkscape:label="numeral-{num}" '
                 f'xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape">\n')
    parts.append(f'<text x="{x}" y="{y}" font-family="{FD}" font-weight="700" font-size="{sz}" '
                 f'fill="{GHOST_MINT}">{num}</text>\n')
    parts.append('</g>\n')

# ---- PROMISES (name + lead) ----
promises = [
    ("01", 36, 366, 19, INK, "Greater control of the room", 387, 13, MUT, "Operate from the room with the controls you need."),
    ("02", 432, 366, 19, INK, "Flexible control of your view", 387, 13, MUT, "Shape the interface around your property and operation."),
    ("03", 36, 555, 22, INK, "Deeper control over security", 576, 13.5, MUT, "See activity, govern access, and bring support closer."),
]
for num, x, ny, ns, nc, name, ly, ls, lc, lead in promises:
    parts.append(f'<g id="layer-promise-{num}" inkscape:label="promise-{num}" '
                 f'xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape">\n')
    parts.append(f'<text x="{x}" y="{ny}" font-family="{FH}" font-weight="700" font-size="{ns}" '
             f'fill="{nc}">{name}</text>\n')
    parts.append(f'<text x="{x}" y="{ly}" font-family="{FB}" font-weight="400" font-size="{ls}" '
             f'fill="{lc}">{lead}</text>\n')
    parts.append('</g>\n')

# ---- FOOTER (1020..1056) ----
parts.append('<g id="layer-footer-bg" inkscape:label="footer-bg" '
             'xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape">\n')
parts.append(f'<rect x="0" y="1020" width="816" height="36" fill="{NAVY}"/>\n')
parts.append('</g>\n')
parts.append('<g id="layer-footer-text" inkscape:label="footer-text" '
             'xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape">\n')
parts.append(f'<text x="56" y="1042" font-family="{FH}" font-weight="700" font-size="9.5" '
             f'letter-spacing="1.7" fill="rgba(104,227,190,0.7)">LUCI</text>\n')
parts.append(f'<text x="760" y="1042" text-anchor="end" font-family="{FH}" font-weight="700" '
             f'font-size="9.5" letter-spacing="1.4" fill="rgba(235,245,248,0.42)">'
             f'WHAT&#8217;S NEW &#183; FOR LUCI CUSTOMERS AND PROSPECTS</text>\n')
parts.append('</g>\n')

parts.append('</svg>\n')

with open("new-luci-whats-new-p1-layers.svg", "w") as f:
    f.write("".join(parts))

import os
print("wrote new-luci-whats-new-p1-layers.svg  size:", os.path.getsize("new-luci-whats-new-p1-layers.svg"))
