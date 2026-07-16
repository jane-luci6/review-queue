#!/usr/bin/env python3
"""Render deck-specific crops of the canonical system-architecture diagram.

Outputs (in ui_kits/sales/assets/):
  - luci-system-architecture-flow.png       (sand canvas — blends into a sand slide)
  - luci-system-architecture-flow.dark.png  (transparent canvas — blends into a dark slide;
                                             colors remapped for dark theme, layout identical)

Also writes rack.dark.png (steel-navy rack on transparent) next to the canonical rack.png.
"""
import re, base64, subprocess, time, pathlib, sys
import numpy as np
from PIL import Image, ImageFilter

DG = pathlib.Path(__file__).resolve().parent.parent.parent / "assets" / "diagrams"
SALES_ASSETS = pathlib.Path(__file__).resolve().parent / "assets"
CANON = (DG / "luci-system-architecture.svg").read_text()
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
PORT = 8098

# ── Rack → rack.dark.png: steel-navy body + light equipment outlines ──────────
# The rack is a solid navy enclosure with transparent gaps between equipment
# units. Lift the navy to steel-navy (visible on dark, still dark-themed), then
# trace light outlines around each unit + the silhouette so the equipment reads.
rack = np.array(Image.open(DG / "rack.png").convert("RGBA"))
rgb = rack[:, :, :3].astype(np.float32)
alpha = rack[:, :, 3]

# Lift navy body to steel-navy; leave mint/gold LED accents untouched.
navy = (rgb[:, :, 0] < 70) & (rgb[:, :, 1] < 100) & (rgb[:, :, 2] < 120)
base = rgb.copy()
base[navy] = np.clip(rgb[navy] + np.array([36, 54, 62], dtype=np.float32), 0, 255)

# Light outlines around each equipment unit + the silhouette. The rack has
# transparent gaps between units; place a ~3px light ring in the gap just outside
# each unit so the equipment reads at slide scale while the unit faces stay steel.
opaque = alpha > 10
_op = Image.fromarray((opaque.astype(np.uint8) * 255))
dilated = np.array(_op.filter(ImageFilter.MaxFilter(7))) > 0   # expand ~3px into the gap
ring = dilated & ~opaque                                        # the band in the gap
LIGHT = np.array([220, 232, 236], dtype=np.float32)  # #DCE8EC
base[ring] = LIGHT
out_alpha = alpha.astype(np.float32).copy()
out_alpha[ring] = 255  # make the outline opaque (it sits in the transparent gap)

out = np.concatenate([base, out_alpha[:, :, None]], axis=2).clip(0, 255).astype(np.uint8)
Image.fromarray(out).save(DG / "rack.dark.png")
print("wrote rack.dark.png")


def neutralize(svg: str) -> str:
    """Drop the internal LUCI grouping panel + rack glow so nothing reads as a box."""
    svg = svg.replace(
        '<rect x="350" y="176" width="700" height="462" rx="46" fill="#A6B0B6" fill-opacity="0.42" filter="url(#feather)"/>',
        '<rect x="350" y="176" width="700" height="462" rx="46" fill="#A6B0B6" fill-opacity="0"/>')
    svg = svg.replace(
        '<ellipse cx="487" cy="409" rx="145" ry="280" fill="url(#sysGlow)" opacity="0.38"/>',
        '<ellipse cx="487" cy="409" rx="145" ry="280" fill="url(#sysGlow)" opacity="0"/>')
    return svg


def pin_size(svg: str, w: int = 1500, h: int = 1024) -> str:
    return re.sub(r'<svg ', f'<svg width="{w}" height="{h}" ', svg, count=1)


# ── SAND variant (baked sand canvas, RGB) ─────────────────────────────────────
sand = CANON.replace(
    '<rect x="0" y="0" width="1500" height="1024" fill="#F5F8FA"/>',
    '<rect x="0" y="0" width="1500" height="1024" fill="#E5E3DF"/>')
sand = neutralize(sand)
sand = pin_size(sand)


# ── DARK variant (transparent canvas, RGBA; colors inverted only) ─────────────
dark = CANON

# The canonical light now has its drop shadows neutralized (they read awkwardly
# on the light canvas). Re-enable them for the deck's dark render, where the
# soft shadows add depth against the navy slide.
dark = dark.replace('flood-color="#081218" flood-opacity="0"', 'flood-color="#081218" flood-opacity="0.3"')
dark = dark.replace('flood-color="#1A2B33" flood-opacity="0"', 'flood-color="#1A2B33" flood-opacity="0.12"')
# Restore the devices' floor contact mark for the deck dark (the canonical light
# flattens it; on the navy slide it grounds the control cluster).
dark = dark.replace('<ellipse cx="856" cy="506" rx="162" ry="7" fill="#10232D" fill-opacity="0"/>',
                    '<ellipse cx="856" cy="506" rx="162" ry="7" fill="#10232D" fill-opacity="0.10"/>')

# Enlarge text for the deck render only (canonical SVG stays untouched).
# Best-effort bump ~1.3x so labels read at slide scale; layout preserved.
dark = dark.replace('.dlabel   { font-weight:600; font-size:18px;', '.dlabel   { font-weight:600; font-size:24px;')
dark = dark.replace('.clbl     { font-weight:600; font-size:18px;', '.clbl     { font-weight:600; font-size:24px;')
dark = dark.replace('.zone     { font-weight:700; font-size:16px;', '.zone     { font-weight:700; font-size:20px;')
dark = dark.replace('.archnote  { font-weight:600; font-size:15px;', '.archnote  { font-weight:600; font-size:20px;')
dark = dark.replace('.uiclabel  { font-weight:600; font-size:11px;', '.uiclabel  { font-weight:600; font-size:16px;')
dark = dark.replace('.racknum  { font-weight:700; font-size:15px;', '.racknum  { font-weight:700; font-size:18px;')
dark = dark.replace('.dsub     { font-weight:500; font-size:9.5px;', '.dsub     { font-weight:500; font-size:13px;')
dark = dark.replace('.ulabel   { font-weight:500; font-size:9px;', '.ulabel   { font-weight:500; font-size:13px;')
dark = dark.replace('.conlbl   { font-weight:600; font-size:10.5px;', '.conlbl   { font-weight:600; font-size:14px;')

# Transparent canvas so the slide's dark gradient + faint glows show through (no box).
dark = dark.replace(
    '<rect x="0" y="0" width="1500" height="1024" fill="#F5F8FA"/>',
    '<rect x="0" y="0" width="1500" height="1024" fill="none"/>')
dark = neutralize(dark)
# Rack -> rack.dark.png. The canonical now embeds rack.png as base64 (self-
# contained for <img> consumers); swap that base64 for an external rack.dark.png
# ref (the headless render serves assets/diagrams over http, so it resolves).
rack_light_b64 = base64.b64encode((DG / "rack.png").read_bytes()).decode()
dark = dark.replace(f'href="data:image/png;base64,{rack_light_b64}"', 'href="rack.dark.png"')

# arwN marker arrowhead → light (do before the global fill="#10232D" bezel lift).
dark = dark.replace(
    '<marker id="arwN" markerWidth="9" markerHeight="9" refX="6.5" refY="3" orient="auto" markerUnits="userSpaceOnUse">\n      <path d="M0,0 L6.5,3 L0,6 Z" fill="#10232D"/>',
    '<marker id="arwN" markerWidth="9" markerHeight="9" refX="6.5" refY="3" orient="auto" markerUnits="userSpaceOnUse">\n      <path d="M0,0 L6.5,3 L0,6 Z" fill="#DCE8EC"/>')

# Device UI bars: keep them light so the screens still read on dark.
dark = dark.replace('fill="#FFFFFF" opacity="0.18"', 'fill="#DCE8EC" opacity="0.32"')
dark = dark.replace('fill="#FFFFFF" opacity="0.10"', 'fill="#DCE8EC" opacity="0.20"')

# Icon / display fills: white → dark navy (outline icons with light strokes).
dark = dark.replace('fill="#FFFFFF"', 'fill="#0E1F28"')
# Navy strokes → light.
dark = dark.replace('stroke="#10232D"', 'stroke="#DCE8EC"')
# Navy bezels + contact shadow → lifted navy (visible against the dark slide).
dark = dark.replace('fill="#10232D"', 'fill="#1A2E38"')
# Monitor stand/bezel grey → lifted.
dark = dark.replace('#2A3D47', '#3D5563')
# Grey connectors + arwG marker → lighter grey.
dark = dark.replace('fill="#9DAAB2"', 'fill="#8AA3B0"')

# CSS class fills (colon syntax).
dark = dark.replace('fill:#3F5965', 'fill:#A8BCC6')        # .kick/.zone/.archnote/.uiclabel/.csub/.dsub
dark = dark.replace('fill:#56707C', 'fill:#9DB4C0')        # .cap
dark = dark.replace('fill:#9DAAB2', 'fill:#9DB4C0')        # .znote
dark = dark.replace('fill:#176B54', 'fill:#2b9e80')        # .conlbl/.rackleg-* (retired green → mint)
# All navy CSS text → light, then restore .racknum (navy-on-gold numbers stay navy).
dark = dark.replace('fill:#10232D', 'fill:#EBF5F8')
dark = dark.replace('font-size:18px; fill:#EBF5F8; text-anchor:middle; dominant-baseline:central',
                    'font-size:18px; fill:#10232D; text-anchor:middle; dominant-baseline:central')

# ── Layout is now baked into the canonical SVG ────────────────────────────────
# luci-system-architecture.svg is the source of truth: 1500 wide, with the
# approved breathing room (control cluster +70 off the rack), balanced right
# zone (+77 so devices→right-icons gap == left-icons→rack gap), and even
# icon/label spacing. The deck render inherits that geometry directly — no
# deck-only layout edits are needed here. Only the color/canvas remapping for
# the dark theme (above) is deck-specific. Canvas is already 1500 in the
# canonical, so pin_size matches.
dark = pin_size(dark, 1500, 1024)


# ── Render both via headless Chrome ───────────────────────────────────────────
deck_sand = DG / "_arch_deck.svg"
deck_dark = DG / "_arch_deck_dark.svg"
deck_sand.write_text(sand)
deck_dark.write_text(dark)

srv = subprocess.Popen([sys.executable, "-m", "http.server", str(PORT)], cwd=str(DG),
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
time.sleep(1.2)


def shoot(deck_name: str, out_png: pathlib.Path, w: int = 1500) -> tuple[int, int]:
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-sandbox",
                    "--hide-scrollbars", "--force-device-scale-factor=3",
                    f"--window-size={w},1024", "--default-background-color=00000000",
                    f"--screenshot={out_png}", f"http://localhost:{PORT}/{deck_name}"], check=False)
    return Image.open(out_png).size


full_sand = DG / "_arch_deck_full.png"
full_dark = DG / "_arch_deck_dark_full.png"
w, h = shoot("_arch_deck.svg", full_sand)
shoot("_arch_deck_dark.svg", full_dark, 1500)
crop_h = int(round(795 / 1024 * h))  # flow + zone labels (y<=770); exclude rack legend (y>=804)

# Sand → RGB (baked canvas).
Image.open(full_sand).convert("RGB").crop((0, 0, w, crop_h)).save(
    SALES_ASSETS / "luci-system-architecture-flow.png")
# Dark → RGBA (transparent canvas blends into the dark slide), cropped tight to
# content so the diagram fills more of the slide (removes ~16% top whitespace).
# Scan only above crop_h so the rack legend (excluded from the deck) is not included.
_dark = np.array(Image.open(full_dark))[:crop_h]
_da = _dark[:, :, 3]
_op = np.where(_da > 10)
_y0, _y1, _x0, _x1 = _op[0].min(), _op[0].max(), _op[1].min(), _op[1].max()
_m = 40
_box = (max(0, _x0 - _m), max(0, _y0 - _m), min(_dark.shape[1], _x1 + _m), min(_dark.shape[0], _y1 + _m))
Image.open(full_dark).crop(_box).save(SALES_ASSETS / "luci-system-architecture-flow.dark.png")
print(f"rendered {w}x{h}; sand {w}x{crop_h}; dark tight {_box[2]-_box[0]}x{_box[3]-_box[1]}")

srv.terminate()
time.sleep(0.3)
for f in (deck_sand, deck_dark, full_sand, full_dark):
    f.unlink(missing_ok=True)
print("cleaned temp files")
