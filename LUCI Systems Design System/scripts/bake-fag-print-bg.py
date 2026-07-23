#!/usr/bin/env python3
"""Bake flattened background JPGs for the FAG prospect PDF.

Chrome turns CSS gradients + mask-images into PDF Shading/Pattern XObjects,
which macOS Preview paints lazily -> the "blink on open". Baking each
textured background into a single raster (navy + glow + tiled pattern +
fade, opacity pre-applied) replaces those vector objects with one image
XObject per surface, which Preview paints instantly.
"""
from __future__ import annotations
import sys
from pathlib import Path
from PIL import Image
import numpy as np

ROOT = Path(__file__).resolve().parent.parent
TEX = ROOT / "assets" / "textures"
OUT = ROOT / "ui_kits" / "sales" / "assets" / "textures"
OUT.mkdir(parents=True, exist_ok=True)

PAT = Image.open(TEX / "texture-circuit-header-mintgold.png").convert("RGBA")
NAVY_DEEP, NAVY, NAVY2 = (10, 22, 28), (16, 35, 45), (12, 31, 40)
MINT = (104, 227, 190)


def navy_gradient(w: int, h: int) -> np.ndarray:
    """162deg vertical-ish gradient: top navy-deep -> 58% navy -> bottom navy2."""
    arr = np.zeros((h, w, 3), dtype=np.float32)
    for y in range(h):
        t = y / max(1, h - 1)
        if t <= 0.58:
            f = t / 0.58
            c = [NAVY_DEEP[i] + (NAVY[i] - NAVY_DEEP[i]) * f for i in range(3)]
        else:
            f = (t - 0.58) / 0.42
            c = [NAVY[i] + (NAVY2[i] - NAVY[i]) * f for i in range(3)]
        arr[y, :] = c
    return arr


def tile_pattern(w: int, h: int, tile_w: int, pos_right: bool = True) -> np.ndarray:
    """Tile the pattern at tile_w px, anchored right (matching background-position:right)."""
    tw = tile_w
    th = round(PAT.size[1] * tw / PAT.size[0])
    pat = np.array(PAT.resize((tw, th), Image.Resampling.LANCZOS), dtype=np.float32)
    rgba = np.zeros((h, w, 4), dtype=np.float32)
    x0 = w - tw if pos_right else 0
    while x0 > -tw:
        y = 0
        while y < h:
            ph = min(th, h - y)
            pw = min(tw, w - x0) if x0 >= 0 else min(tw + x0, w)
            sx = max(0, -x0)
            rgba[y:y + ph, max(0, x0):max(0, x0) + pw] = pat[:ph, sx:sx + pw]
            y += th
        x0 -= tw
    return rgba


def fade_alpha(w: int, stops: list[tuple[float, float]]) -> np.ndarray:
    """Horizontal alpha 0..1 across width, piecewise-linear between (pos, val) stops."""
    xs = np.arange(w, dtype=np.float32) / max(1, w - 1)
    out = np.zeros(w, dtype=np.float32)
    for (p0, v0), (p1, v1) in zip(stops[:-1], stops[1:]):
        m = (p0 <= xs) & (xs <= p1)
        out[m] = v0 + (v1 - v0) * ((xs[m] - p0) / max(1e-6, p1 - p0))
    return out


def mint_glow(w: int, h: int, cx: float, cy: float, rx: float, ry: float, a: float, falloff: float) -> np.ndarray:
    """Radial mint glow alpha 0..a, centered (cx,cy) in fractions, radius (rx,ry) in fractions."""
    yy, xx = np.mgrid[0:h, 0:w]
    dx = (xx / w - cx) / rx
    dy = (yy / h - cy) / ry
    d = np.sqrt(dx * dx + dy * dy)
    a_map = np.clip(1.0 - d / falloff, 0, 1) * a
    return a_map


def bake_cover(w: int, h: int, dest: Path) -> None:
    base = navy_gradient(w, h)
    pat = tile_pattern(w, h, 640, pos_right=True)
    a = fade_alpha(w, [(0.0, 0.0), (0.40, 0.0), (0.68, 0.45), (1.0, 1.0)]) * 0.55
    pat_a = pat[:, :, 3:4] * a[None, :, None]
    rgb = pat[:, :, :3] * (pat_a / 255.0) + base * (1 - pat_a / 255.0)
    Image.fromarray(np.clip(rgb, 0, 255).astype(np.uint8)).save(dest, format="JPEG", quality=82, optimize=True)
    print(f"  {dest.name}  {w}x{h}  {dest.stat().st_size//1024} KB")


def bake_flagband(w: int, h: int, dest: Path) -> None:
    base = navy_gradient(w, h)
    glow_a = mint_glow(w, h, 0.90, -0.28, 1.35, 1.20, 0.16, 0.56)
    base = base * (1 - glow_a[:, :, None]) + np.array(MINT) * glow_a[:, :, None]
    pat = tile_pattern(w, h, 560, pos_right=True)
    a = fade_alpha(w, [(0.0, 0.0), (0.32, 0.0), (0.60, 0.50), (1.0, 1.0)]) * 0.60
    pat_a = pat[:, :, 3:4] * a[None, :, None]
    rgb = pat[:, :, :3] * (pat_a / 255.0) + base * (1 - pat_a / 255.0)
    Image.fromarray(np.clip(rgb, 0, 255).astype(np.uint8)).save(dest, format="JPEG", quality=82, optimize=True)
    print(f"  {dest.name}  {w}x{h}  {dest.stat().st_size//1024} KB")


def bake_uc_tile(dest: Path) -> None:
    """48x48 UC number tile: navy gradient + mint radial glow, baked to a raster."""
    w = h = 96
    base = navy_gradient(w, h)
    glow_a = mint_glow(w, h, 0.30, 0.18, 1.20, 1.40, 0.16, 0.60)
    rgb = base * (1 - glow_a[:, :, None]) + np.array(MINT) * glow_a[:, :, None]
    Image.fromarray(np.clip(rgb, 0, 255).astype(np.uint8)).save(dest, format="PNG", optimize=True)
    print(f"  {dest.name}  {w}x{h}  {dest.stat().st_size//1024} KB")


def bake_nav(dest: Path) -> None:
    """Nav-page right strip: light-navy circuit pattern with a left-fade, on transparent."""
    pat = Image.open(TEX / "texture-circuit-light-navy.png").convert("RGBA")
    w, h = 900, round(900 * pat.size[1] / pat.size[0])
    pat = np.array(pat.resize((w, h), Image.Resampling.LANCZOS), dtype=np.float32)
    a = fade_alpha(w, [(0.0, 0.0), (0.0, 0.0), (0.55, 0.4), (1.0, 1.0)])
    rgba = pat.copy()
    rgba[:, :, 3] = pat[:, :, 3] * a[None, :]
    Image.fromarray(np.clip(rgba, 0, 255).astype(np.uint8)).save(dest, format="PNG", optimize=True)
    print(f"  {dest.name}  {w}x{h}  {dest.stat().st_size//1024} KB")


def main() -> int:
    print("Baking FAG prospect print backgrounds...")
    bake_cover(1275, 1650, OUT / "fag-cover-bg-print.jpg")
    bake_cover(1275, 1650, OUT / "fag-close-bg-print.jpg")
    bake_flagband(1700, 230, OUT / "fag-flagband-bg-print.jpg")
    bake_uc_tile(OUT / "fag-uc-tile-print.png")
    bake_nav(OUT / "fag-nav-bg-print.png")
    print("Done.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
