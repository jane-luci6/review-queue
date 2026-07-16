#!/usr/bin/env python3
"""Bake the approved deck layout into the canonical system-architecture diagram,
and create a matching dark canonical variant.

The deck render (_arch_render.py) previously applied these layout fixes as string
replacements at render time, leaving the canonical SVG untouched. Now that the
layout is approved, we bake it into the canonical so every consumer (hub viewer,
sales docs, website) gets the same geometry, and we add a dark canonical variant
for navy surfaces.

Inputs/outputs (all in assets/diagrams/):
  reads:   luci-system-architecture.svg  (original light, 1440 wide, original layout)
           rack.png                      (canonical rack art)
  writes:  luci-system-architecture.svg       (light, baked layout, 1500 wide)  [in place]
           luci-system-architecture.dark.svg  (dark, baked layout, transparent, self-contained)
           luci-system-architecture.png       (light, RGB, 1500x1024 @3x)
           luci-system-architecture.dark.png  (dark, RGBA, 1500x1024 @3x)
           rack.dark.png                      (steel-navy rack on transparent, for the dark embed)
"""
import re, base64, subprocess, time, pathlib, sys
import numpy as np
from PIL import Image, ImageFilter

DG = pathlib.Path(__file__).resolve().parent.parent.parent / "assets" / "diagrams"
CANON_PATH = DG / "luci-system-architecture.svg"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
PORT = 8099


def chk(s: str, old: str, label: str) -> str:
    """Replace old->new is done by caller; here we just assert old is present once."""
    n = s.count(old)
    if n != 1:
        print(f"  !! [{label}] expected 1 match, found {n}: {old[:70]!r}")
    return s


# ── 0. rack.dark.png: steel-navy body + light equipment outlines ──────────────
# (mirrors _arch_render.py so this script is self-contained)
rack = np.array(Image.open(DG / "rack.png").convert("RGBA"))
rgb = rack[:, :, :3].astype(np.float32)
alpha = rack[:, :, 3]
navy = (rgb[:, :, 0] < 70) & (rgb[:, :, 1] < 100) & (rgb[:, :, 2] < 120)
base = rgb.copy()
base[navy] = np.clip(rgb[navy] + np.array([36, 54, 62], dtype=np.float32), 0, 255)
opaque = alpha > 10
_op = Image.fromarray((opaque.astype(np.uint8) * 255))
dilated = np.array(_op.filter(ImageFilter.MaxFilter(7))) > 0
ring = dilated & ~opaque
LIGHT = np.array([220, 232, 236], dtype=np.float32)  # #DCE8EC
base[ring] = LIGHT
out_alpha = alpha.astype(np.float32).copy()
out_alpha[ring] = 255
out = np.concatenate([base, out_alpha[:, :, None]], axis=2).clip(0, 255).astype(np.uint8)
Image.fromarray(out).save(DG / "rack.dark.png")
print("wrote rack.dark.png")

light = CANON_PATH.read_text()

# ── 1. Bake the approved deck layout into the light canonical ─────────────────
# Canvas: widen 1440 -> 1500 so the +77-shifted right zone doesn't clip.
chk(light, 'viewBox="0 0 1440 1024"', "viewBox")
chk(light, '<rect x="0" y="0" width="1440" height="1024" fill="#F5F8FA"/>', "canvas")
chk(light, '<rect x="350" y="176" width="630" height="462" rx="46" fill="#A6B0B6" fill-opacity="0.42" filter="url(#feather)"/>', "feather")
light = light.replace('viewBox="0 0 1440 1024"', 'viewBox="0 0 1500 1024"')
light = light.replace('<rect x="0" y="0" width="1440" height="1024" fill="#F5F8FA"/>',
                      '<rect x="0" y="0" width="1500" height="1024" fill="#F5F8FA"/>')
# LUCI zone tint: widen 630 -> 700 so it still covers the +70-shifted control cluster.
light = light.replace('<rect x="350" y="176" width="630" height="462" rx="46" fill="#A6B0B6" fill-opacity="0.42" filter="url(#feather)"/>',
                      '<rect x="350" y="176" width="700" height="462" rx="46" fill="#A6B0B6" fill-opacity="0.42" filter="url(#feather)"/>')

# (a) Breathing room: shift the control-device cluster +70 off the rack.
light = light.replace('translate(826,400) scale(1.24) translate(-786,-400)',
                      'translate(896,400) scale(1.24) translate(-786,-400)')
light = light.replace('<text class="uiclabel" x="786" y="232">CONTROL FROM ANY DEVICE</text>',
                      '<text class="uiclabel" x="856" y="232">CONTROL FROM ANY DEVICE</text>')
light = light.replace('<ellipse cx="786" cy="506" rx="162" ry="7"',
                      '<ellipse cx="856" cy="506" rx="162" ry="7"')
light = light.replace('M340,706 L340,726 L968,726 L968,706',
                      'M340,706 L340,726 L1045,726 L1045,706')
# (b) Cluster->output connectors: start +70 (cluster shifted); end +77 at the
#     shifted right icons so devices->right-icons gap == left-icons->rack gap.
light = light.replace('<line x1="950" y1="392" x2="1088" y2="208"',
                      '<line x1="1020" y1="392" x2="1165" y2="197"')
light = light.replace('<line x1="952" y1="399" x2="1088" y2="305"',
                      '<line x1="1022" y1="399" x2="1165" y2="307"')
light = light.replace('<line x1="954" y1="406" x2="1088" y2="405"',
                      '<line x1="1024" y1="406" x2="1165" y2="414"')
light = light.replace('<line x1="952" y1="413" x2="1088" y2="505"',
                      '<line x1="1022" y1="413" x2="1165" y2="517"')
light = light.replace('<line x1="950" y1="420" x2="1088" y2="602"',
                      '<line x1="1020" y1="420" x2="1165" y2="622"')
# (c) Left source icons -> re-space by even BLOCK (label+icon) gaps spanning the
#     rack height; connector y1 = each icon's visual center. Align left labels
#     at x=0, y=-34.
light = light.replace('translate(165,205)', 'translate(165,216)')
light = light.replace('translate(165,305)', 'translate(165,322)')
light = light.replace('translate(165,405)', 'translate(165,437)')
light = light.replace('translate(165,505)', 'translate(165,540)')
light = light.replace('translate(165,605)', 'translate(165,634)')
light = light.replace('<line x1="206" y1="210" x2="351" y2="356"',
                      '<line x1="206" y1="220" x2="351" y2="356"')
light = light.replace('<line x1="206" y1="305" x2="351" y2="386"',
                      '<line x1="206" y1="328" x2="351" y2="386"')
light = light.replace('<line x1="206" y1="405" x2="351" y2="409"',
                      '<line x1="206" y1="437" x2="351" y2="409"')
light = light.replace('<line x1="206" y1="505" x2="351" y2="432"',
                      '<line x1="206" y1="540" x2="351" y2="432"')
light = light.replace('<line x1="206" y1="600" x2="351" y2="462"',
                      '<line x1="206" y1="632" x2="351" y2="462"')
light = light.replace('<text class="dlabel" x="2" y="-28">Local A/V</text>',
                      '<text class="dlabel" x="0" y="-34">Local A/V</text>')
light = light.replace('<text class="dlabel" x="2" y="-32">Music</text>',
                      '<text class="dlabel" x="0" y="-34">Music</text>')
# (d) Right output icons -> re-space by even edge gaps spanning the rack height,
#     AND shift +77 (with (f)) so the right gap matches the left gap.
light = light.replace('translate(1135,205)', 'translate(1212,191)')
light = light.replace('translate(1135,305)', 'translate(1212,308)')
light = light.replace('translate(1135,405)', 'translate(1212,414)')
light = light.replace('translate(1135,505)', 'translate(1212,525)')
light = light.replace('translate(1135,605)', 'translate(1212,622)')
# (e) "Background Music & Paging": trim the speaker sound waves so the 2-line
#     label clears them at x=50, aligned with the other right labels.
light = light.replace('<path d="M24,-12 q9,16 0,32"/>', '<path d="M20,-9 q5,13 0,26"/>')
light = light.replace('<path d="M32,-18 q13,22 0,44"/>', '<path d="M24,-13 q5,17 0,26"/>')
# (f) Shift the right output zone's bracket + captions +77 so devices->right-icons
#     gap == left-icons->rack gap, keeping the middle breathing room from (a).
light = light.replace('<path d="M1104,706 L1104,726 L1392,726 L1392,706"/>',
                      '<path d="M1181,706 L1181,726 L1469,726 L1469,706"/>')
light = light.replace('<text class="zone" x="1248" y="748">WHAT LUCI CONTROLS</text>',
                      '<text class="zone" x="1325" y="748">WHAT LUCI CONTROLS</text>')
light = light.replace('<text class="archnote" x="1248" y="770">Delivered over your network</text>',
                      '<text class="archnote" x="1325" y="770">Delivered over your network</text>')

# Embed rack.png so the light canonical is self-contained (renders in <img>,
# PDF export, copies) -- mirrors luci-what-luci-is.svg.
rack_light_b64 = base64.b64encode((DG / "rack.png").read_bytes()).decode()
light = light.replace('href="rack.png?v=4"', f'href="data:image/png;base64,{rack_light_b64}"')

# Drop shadows read awkwardly on the light canvas, so neutralize the three
# feDropShadow filters (sysSoft under rack+devices, iconLite under the icons,
# legShadow under the rack-components legend) by zeroing their flood-opacity.
# The feather (zone-tint blur) and sysGlow (gradient glow) are not drop shadows
# and stay. Keep a shadow-preserving copy for the dark variant, where the soft
# shadows add depth against navy.
light_with_shadows = light
light = light.replace('flood-color="#081218" flood-opacity="0.3"', 'flood-color="#081218" flood-opacity="0"')
light = light.replace('flood-color="#1A2B33" flood-opacity="0.12"', 'flood-color="#1A2B33" flood-opacity="0"')
# Flatten the remaining atmospheric elements so the light canvas is fully clean:
# the feathered LUCI zone tint, the rack's mint glow, and the devices' floor
# contact mark. All are zeroed (kept as no-ops, not deleted) so the dark variant
# and the deck render can re-enable the ones they still want.
light = light.replace('<rect x="350" y="176" width="700" height="462" rx="46" fill="#A6B0B6" fill-opacity="0.42" filter="url(#feather)"/>',
                      '<rect x="350" y="176" width="700" height="462" rx="46" fill="#A6B0B6" fill-opacity="0" filter="url(#feather)"/>')
light = light.replace('<ellipse cx="487" cy="409" rx="145" ry="280" fill="url(#sysGlow)" opacity="0.38"/>',
                      '<ellipse cx="487" cy="409" rx="145" ry="280" fill="url(#sysGlow)" opacity="0"/>')
light = light.replace('<ellipse cx="856" cy="506" rx="162" ry="7" fill="#10232D" fill-opacity="0.10"/>',
                      '<ellipse cx="856" cy="506" rx="162" ry="7" fill="#10232D" fill-opacity="0"/>')

CANON_PATH.write_text(light)
print("baked light canonical -> luci-system-architecture.svg (1500 wide, fully flat)")

# ── 2. Dark canonical: baked layout + dark colors + transparent canvas ────────
dark = light_with_shadows  # start from the shadow-preserving baked light (rack embedded)

# Transparent canvas (the dark stage/viewer provides the navy background).
dark = dark.replace('<rect x="0" y="0" width="1500" height="1024" fill="#F5F8FA"/>',
                    '<rect x="0" y="0" width="1500" height="1024" fill="none"/>')
# Drop the LUCI zone tint + rack glow so nothing reads as a box on dark.
dark = dark.replace('<rect x="350" y="176" width="700" height="462" rx="46" fill="#A6B0B6" fill-opacity="0.42" filter="url(#feather)"/>',
                    '<rect x="350" y="176" width="700" height="462" rx="46" fill="#A6B0B6" fill-opacity="0"/>')
dark = dark.replace('<ellipse cx="487" cy="409" rx="145" ry="280" fill="url(#sysGlow)" opacity="0.38"/>',
                    '<ellipse cx="487" cy="409" rx="145" ry="280" fill="url(#sysGlow)" opacity="0"/>')
# Rack -> embedded rack.dark.png (swap the light rack base64 for the dark one).
rack_dark_b64 = base64.b64encode((DG / "rack.dark.png").read_bytes()).decode()
dark = dark.replace(f'href="data:image/png;base64,{rack_light_b64}"',
                    f'href="data:image/png;base64,{rack_dark_b64}"')

# arwN marker arrowhead -> light (do before the global fill="#10232D" bezel lift).
dark = dark.replace(
    '<marker id="arwN" markerWidth="9" markerHeight="9" refX="6.5" refY="3" orient="auto" markerUnits="userSpaceOnUse">\n      <path d="M0,0 L6.5,3 L0,6 Z" fill="#10232D"/>',
    '<marker id="arwN" markerWidth="9" markerHeight="9" refX="6.5" refY="3" orient="auto" markerUnits="userSpaceOnUse">\n      <path d="M0,0 L6.5,3 L0,6 Z" fill="#DCE8EC"/>')
# Device UI bars: keep them light so the screens still read on dark.
dark = dark.replace('fill="#FFFFFF" opacity="0.18"', 'fill="#DCE8EC" opacity="0.32"')
dark = dark.replace('fill="#FFFFFF" opacity="0.10"', 'fill="#DCE8EC" opacity="0.20"')
# Icon / display fills: white -> dark navy (outline icons with light strokes).
dark = dark.replace('fill="#FFFFFF"', 'fill="#0E1F28"')
# Navy strokes -> light.
dark = dark.replace('stroke="#10232D"', 'stroke="#DCE8EC"')
# Navy bezels + contact shadow -> lifted navy (visible against the dark stage).
dark = dark.replace('fill="#10232D"', 'fill="#1A2E38"')
# Monitor stand/bezel grey -> lifted.
dark = dark.replace('#2A3D47', '#3D5563')
# Grey connectors + arwG marker -> lighter grey.
dark = dark.replace('fill="#9DAAB2"', 'fill="#8AA3B0"')
# CSS class fills (colon syntax).
dark = dark.replace('fill:#3F5965', 'fill:#A8BCC6')   # .kick/.zone/.archnote/.uiclabel/.csub/.dsub
dark = dark.replace('fill:#56707C', 'fill:#9DB4C0')   # .cap
dark = dark.replace('fill:#9DAAB2', 'fill:#9DB4C0')   # .znote
dark = dark.replace('fill:#176B54', 'fill:#2b9e80')   # .conlbl/.rackleg-* (retired green -> mint)
# All navy CSS text -> light, then restore .racknum (the numbers sit on gold
# badges, so they stay navy -- light-on-gold is low contrast). The canonical
# uses font-size:15px; the deck render enlarges it to 18px before this restore.
dark = dark.replace('fill:#10232D', 'fill:#EBF5F8')
dark = dark.replace('font-size:15px; fill:#EBF5F8; text-anchor:middle; dominant-baseline:central',
                    'font-size:15px; fill:#10232D; text-anchor:middle; dominant-baseline:central')

# Rack-components legend (only the full canonical shows it; the deck crop excludes
# it). Box -> lifted navy panel; body-ink + muted text -> light now that the box
# is dark. Gold badges + mint header already read on dark.
dark = dark.replace('fill="#EEF2F4"', 'fill="#1A2E38"')   # legend box -> lifted navy panel
dark = dark.replace('fill:#354F5C', 'fill:#DCE8EC')      # .rackleg-i + .leg (body ink -> light)
dark = dark.replace('fill:#49616E', 'fill:#9DB4C0')      # .rackleg-desc (muted -> light muted)

(DG / "luci-system-architecture.dark.svg").write_text(dark)
print("wrote dark canonical -> luci-system-architecture.dark.svg")

# ── 3. Render canonical PNGs (light RGB + dark RGBA, 1500x1024 @3x) ───────────
def pin_size(svg_str, w=1500, h=1024):
    return re.sub(r'<svg ', f'<svg width="{w}" height="{h}" ', svg_str, count=1)

tmp_light = DG / "_arch_canon_light.svg"
tmp_dark = DG / "_arch_canon_dark.svg"
tmp_light.write_text(pin_size(light))
tmp_dark.write_text(pin_size(dark))

srv = subprocess.Popen([sys.executable, "-m", "http.server", str(PORT)], cwd=str(DG),
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
time.sleep(1.2)


def shoot(name, out_path, w=1500):
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-sandbox",
                    "--hide-scrollbars", "--force-device-scale-factor=3",
                    f"--window-size={w},1024", "--default-background-color=00000000",
                    f"--screenshot={out_path}", f"http://localhost:{PORT}/{name}"], check=False)


full_light_png_tmp = DG / "_arch_canon_light.png"
full_dark_png_tmp = DG / "_arch_canon_dark.png"
shoot("_arch_canon_light.svg", full_light_png_tmp)
shoot("_arch_canon_dark.svg", full_dark_png_tmp)

Image.open(full_light_png_tmp).convert("RGB").save(DG / "luci-system-architecture.png")
Image.open(full_dark_png_tmp).save(DG / "luci-system-architecture.dark.png")
lsz = Image.open(DG / "luci-system-architecture.png").size
dsz = Image.open(DG / "luci-system-architecture.dark.png").size
print(f"rendered canonical PNGs: light {lsz}, dark {dsz}")

srv.terminate()
time.sleep(0.3)
for f in (tmp_light, tmp_dark, full_light_png_tmp, full_dark_png_tmp):
    f.unlink(missing_ok=True)
print("cleaned temp files")
