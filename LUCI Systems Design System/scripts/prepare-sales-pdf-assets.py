#!/usr/bin/env python3
"""Prepare print-sized raster assets for sales-document PDF export."""
from __future__ import annotations

import http.server
import os
import shutil
import subprocess
import sys
import threading
import time
from pathlib import Path

try:
    from PIL import Image
    import numpy as np
    _HAS_PIL = True
except ImportError:
    _HAS_PIL = False

ROOT = Path(__file__).resolve().parent.parent
SALES_ASSETS = ROOT / "ui_kits" / "sales" / "assets"
SALES = ROOT / "ui_kits" / "sales"
CANON_DIAGRAMS = ROOT / "assets" / "diagrams"
CANON_LOGOS = ROOT / "assets" / "logos"
CANON_TEXTURES = ROOT / "assets" / "textures"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
PORT = 8799

# Raster resize targets (source may be PNG or prior export).
TARGETS = {
    "diagrams/luci-system-architecture.jpg": {
        "source": CANON_DIAGRAMS / "luci-system-architecture.png",
        "max_width": 1600,
        "max_height": 1092,
        "jpeg_quality": 80,
    },
    "client-logo-02.jpg": {
        "source": SALES_ASSETS / "client-logo-02.png",
        "max_width": 1000,
        "jpeg_quality": 82,
    },
    "interface-floor-view.jpg": {
        "source": SALES_ASSETS / "interface-floor-view.orig.png",
        "max_width": 2000,
        "jpeg_quality": 88,
    },
    "interface-floor-view-budgetary.jpg": {
        "source": SALES_ASSETS / "interface-floor-view.orig.png",
        "max_width": 1800,
        "jpeg_quality": 86,
    },
    "textures/texture-3.jpg": {
        "source": CANON_TEXTURES / "texture-3.png",
        "max_width": 400,
        "max_height": 284,
        "jpeg_quality": 78,
    },
    "textures/texture-circuit-header-mintgold.jpg": {
        "source": CANON_TEXTURES / "texture-circuit-header-mintgold.png",
        "max_width": 480,
        "jpeg_quality": 80,
    },
    "textures/texture-circuit-navy-mint.jpg": {
        "source": CANON_TEXTURES / "texture-circuit-navy-mint.png",
        "max_width": 360,
        "jpeg_quality": 80,
    },
    "textures/sow-page-bg-baked-print.jpg": {
        "source": CANON_TEXTURES / "sow-page-bg-baked.jpg",
        "max_width": 1200,
        "max_height": 1550,
        "jpeg_quality": 72,
    },
    "logos/luci-wordmark-black-320.png": {
        "source": CANON_LOGOS / "luci-full-mintmark-blacktext.png",
        "max_width": 320,
        "png": True,
        "alpha": True,
    },
    "logos/luci-wordmark-white-320.png": {
        "source": CANON_LOGOS / "luci-full-mintmark-white.png",
        "max_width": 320,
        "png": True,
        "alpha": True,
    },
    "logos/paragon-casino-resort-print.png": {
        "source": CANON_LOGOS / "paragon-casino-resort.png",
        "max_width": 560,
        "png": True,
        "alpha": True,
    },
}

# SVG → JPEG (stops Chrome from rasterizing diagrams at 2000–2500px in print).
SVG_RASTER = [
    ("diagrams/luci-what-luci-is.svg", "diagrams/luci-what-luci-is.jpg", 1400, 750, 90, "F5F8FA"),
    ("diagrams/embedded-operation-orbit-names.svg", "diagrams/embedded-operation-orbit-names.png", 1500, 830, None, "E5E3DF"),
    ("case-relocation.svg", "case-relocation.jpg", 700, 368, 85, "F5F8FA"),
    ("features/feature-map-dashboard.svg", "features/feature-map-dashboard.jpg", 700, 394, 82),
    ("features/feature-open-integration.svg", "features/feature-open-integration.jpg", 700, 394, 82),
    ("features/feature-pin-control.svg", "features/feature-pin-control.jpg", 700, 394, 82),
    ("features/feature-monitoring.svg", "features/feature-monitoring.jpg", 700, 394, 82),
    ("features/feature-presets.svg", "features/feature-presets.jpg", 700, 394, 82),
    ("features/feature-automation.svg", "features/feature-automation.jpg", 700, 394, 82),
    ("diagrams/luci-consolidation-ledger.svg", "diagrams/luci-consolidation-ledger.jpg", 1320, 1246, 85),
    ("diagrams/embedded-operation-orbit.svg", "diagrams/embedded-operation-orbit.jpg", 1000, 556, 88, "F5F8FA"),
    # Brochure PDF — lossless PNG at print width so orbit labels stay sharp in Acrobat.
    ("diagrams/embedded-operation-orbit.svg", "diagrams/embedded-operation-orbit-brochure.png", 1800, 1000, None, "F5F8FA"),
]

# Canon-only SVGs referenced from ../../assets/logos/ in HTML.
CANON_SVG_RASTER = [
    ("logos/ameristar-council-bluffs.svg", "logos/ameristar-council-bluffs.jpg", 288, 88, 88),
    ("logos/ameristar-council-bluffs.svg", "logos/ameristar-council-bluffs.png", 288, 88, None),
]

MAX_PDF_RASTER_PX = 1800
BROCHURE_NAVY = (16, 35, 45)

# .cap-page--what .cap-shot printed box (brochure.css print rules, page 1):
#   width  = page_w(8.5in) - left(46% of 8.5in = 3.91in)              = 4.59in
#   height = .cap-what-upper's fixed print height (4.7in); the ±24px  = 4.70in
#            top/bottom bleed on .cap-shot is clipped away by the
#            parent's overflow:hidden, so it never actually shows.
# Measured empirically by rendering a magenta-outlined build and reading
# pixel bounds (see chat history) — matches this arithmetic to <1%.
# object-fit:cover + object-position:right crops the SOURCE image down to
# this aspect, keeping the image's right side. If we bake the feather onto
# the raw (uncropped) source, the crop throws away almost the entire
# feathered region (it lives at the image's left edge). Pre-cropping to this
# exact aspect first means the baked feather is applied to the pixels that
# actually survive into the PDF.
BROCHURE_SHOT_ASPECT = 4.59 / 4.70  # width / height


def brochure_floor_feather_alpha(t: float) -> float:
    """Match .cap-shot__feather linear-gradient stops in brochure.css (container-relative)."""
    if t <= 0.0:
        return 1.0
    if t <= 0.08:
        return 1.0 - (t / 0.08) * 0.15
    if t <= 0.22:
        return 0.85 - ((t - 0.08) / 0.14) * 0.55
    if t <= 0.38:
        return 0.30 - ((t - 0.22) / 0.16) * 0.30
    return 0.0


def bake_brochure_floor_shot(src: Path, dest: Path) -> tuple[Path, tuple[int, int], int]:
    """Crop the floor-plan raster to the printed shot's exact aspect (anchored
    right, matching object-position:right), THEN bake the navy left-edge
    feather onto the surviving pixels so it isn't cropped away by the browser."""
    im = Image.open(src).convert("RGB")
    w, h = im.size
    target_w = round(h * BROCHURE_SHOT_ASPECT)
    if target_w < w:
        im = im.crop((w - target_w, 0, w, h))
    w, h = im.size
    max_w = 1400
    if w > max_w:
        im = im.resize((max_w, round(h * max_w / w)), Image.Resampling.LANCZOS)
        w, h = im.size

    arr = np.array(im, dtype=np.float32)
    xs = np.arange(w, dtype=np.float32) / float(w)
    alphas = np.vectorize(brochure_floor_feather_alpha)(xs)
    navy = np.array(BROCHURE_NAVY, dtype=np.float32)
    for x, alpha in enumerate(alphas):
        if alpha <= 0.0:
            continue
        arr[:, x, :] = arr[:, x, :] * (1.0 - alpha) + navy * alpha
    out = Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8))
    dest.parent.mkdir(parents=True, exist_ok=True)
    out.save(dest, format="JPEG", quality=90, optimize=True, progressive=False)
    return dest, out.size, dest.stat().st_size


def fit(im: Image.Image, max_w: int, max_h: int | None = None) -> Image.Image:
    w, h = im.size
    scale = 1.0
    if max_w and w > max_w:
        scale = min(scale, max_w / w)
    if max_h and h > max_h:
        scale = min(scale, max_h / h)
    if scale >= 1.0:
        return im
    nw, nh = max(1, int(w * scale)), max(1, int(h * scale))
    return im.resize((nw, nh), Image.Resampling.LANCZOS)


def write_raster(im: Image.Image, dest: Path, spec: dict) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    if spec.get("png"):
        mode = "RGBA" if spec.get("alpha") else "RGB"
        im.convert(mode).save(dest, format="PNG", optimize=True)
        return
    im.convert("RGB").save(
        dest,
        format="JPEG",
        quality=int(spec.get("jpeg_quality", 80)),
        optimize=True,
        progressive=False,
    )


def prepare_raster(rel: str, spec: dict) -> tuple[Path, tuple[int, int], int]:
    src: Path = spec["source"]
    dest = SALES_ASSETS / rel
    if not src.exists():
        raise FileNotFoundError(f"Missing source for {rel}: {src}")
    im = Image.open(src).convert("RGBA")
    out = fit(im, spec["max_width"], spec.get("max_height"))
    if spec.get("composite_bg"):
        bg = Image.new("RGBA", out.size, (*spec["composite_bg"], 255))
        bg.paste(out, mask=out.split()[3])
        out = bg
    write_raster(out, dest, spec)
    return dest, out.size, dest.stat().st_size


def rasterize_svg(
    rel_src: str,
    rel_dest: str,
    width: int,
    height: int,
    quality: int | None,
    screenshot_bg: str | None = None,
) -> tuple[Path, tuple[int, int], int]:
    src_candidates = [
        SALES_ASSETS / rel_src,
        CANON_DIAGRAMS / Path(rel_src).name,
        CANON_LOGOS / Path(rel_src).name,
    ]
    src = next((p for p in src_candidates if p.exists()), None)
    if not src:
        raise FileNotFoundError(f"Missing SVG source: {rel_src}")

    # Ensure SVG is servable from ui_kits/sales/.
    if not src.is_relative_to(SALES):
        staged = SALES_ASSETS / rel_src
        staged.parent.mkdir(parents=True, exist_ok=True)
        if not staged.exists():
            shutil.copy2(src, staged)
        src = staged

    dest = SALES_ASSETS / rel_dest
    dest.parent.mkdir(parents=True, exist_ok=True)
    png_tmp = dest.with_name(f".{dest.stem}.chrome.png")
    svg_url_path = src.relative_to(SALES)

    # Standalone SVG documents render at their own intrinsic width/height inside
    # Chrome's headless viewport — they do NOT scale to fill the window. Without
    # a wrapper, bumping window-size just adds blank canvas around the same-size
    # content (the diagram looks "shrunk"). Force it to fill the target frame.
    # Some master SVGs declare a root width/height whose aspect ratio doesn't
    # match their own viewBox (e.g. a wide viewBox scaled into a narrower
    # frame). With a plain stretch-fill that mismatch either distorts the
    # art or letterboxes it — and the letterbox bands render in the wrapper
    # page's background, which showed up as a visible "box" seam against a
    # tinted (non-white) page. object-fit: contain avoids distortion, and
    # painting the wrapper + image background the same tone as the target
    # page keeps any letterbox band invisible.
    bg_css = f"#{screenshot_bg}" if screenshot_bg else "transparent"
    wrapper = dest.with_name(f".{dest.stem}.raster.html")
    wrapper.write_text(
        "<!doctype html><html><head><style>"
        f"html,body{{margin:0;padding:0;background:{bg_css};}}"
        f"img{{display:block;width:{width}px;height:{height}px;object-fit:contain;background:{bg_css};}}"
        "</style></head><body>"
        f'<img src="/{svg_url_path.as_posix()}">'
        "</body></html>",
        encoding="utf-8",
    )
    url = f"http://127.0.0.1:{PORT}/{wrapper.relative_to(SALES).as_posix()}"

    os.chdir(SALES)
    httpd = http.server.HTTPServer(("127.0.0.1", PORT), http.server.SimpleHTTPRequestHandler)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    time.sleep(0.25)
    try:
        chrome_cmd = [
            CHROME,
            "--headless=new",
            "--disable-gpu",
            "--hide-scrollbars",
            f"--window-size={width},{height}",
            f"--screenshot={png_tmp}",
        ]
        if screenshot_bg:
            chrome_cmd.append(f"--default-background-color=FF{screenshot_bg}")
        chrome_cmd.append(url)
        subprocess.run(chrome_cmd, check=False)
    finally:
        httpd.shutdown()
        wrapper.unlink(missing_ok=True)

    if not png_tmp.exists():
        raise RuntimeError(f"Chrome failed to rasterize {rel_src}")

    save_png = dest.suffix.lower() == ".png" or quality is None
    if save_png:
        im = Image.open(png_tmp).convert("RGBA")
        arr = np.array(im)
        rgb = arr[:, :, :3].astype(int)
        if screenshot_bg:
            # Knock out the matched page-color matte so the raster carries NO flat
            # rectangle at all — the real CSS background shows through directly.
            # This sidesteps PDF viewers rendering an ICC-tagged raster fill vs an
            # untagged vector fill a hair differently even at identical RGB values
            # (the visible "box" seam a flat color-match alone can't fully avoid).
            target = tuple(int(screenshot_bg[i : i + 2], 16) for i in (0, 2, 4))
            dist = np.abs(rgb - np.array(target)).sum(axis=2)
            knockout = dist <= 12
        else:
            # Knock out Chrome's white matte so logos sit flush on light sheets.
            knockout = (rgb[:, :, 0] >= 250) & (rgb[:, :, 1] >= 250) & (rgb[:, :, 2] >= 250)
        arr[knockout, 3] = 0
        im = Image.fromarray(arr.astype("uint8"))
        im = fit(im, width, height)
        im.save(dest, format="PNG", optimize=True)
        png_tmp.unlink(missing_ok=True)
        return dest, im.size, dest.stat().st_size

    im = Image.open(png_tmp).convert("RGB")
    if screenshot_bg:
        sand = tuple(int(screenshot_bg[i : i + 2], 16) for i in (0, 2, 4))
        px = im.load()
        for y in range(im.height):
            for x in range(im.width):
                r, g, b = px[x, y]
                # Chrome letterbox + JPEG can leave near-white margins; snap to sand.
                if r >= 252 and g >= 225 and b >= 225:
                    px[x, y] = sand
    im = fit(im, width, height)
    im.save(dest, format="JPEG", quality=quality, optimize=True, progressive=False)
    png_tmp.unlink(missing_ok=True)
    return dest, im.size, dest.stat().st_size


def audit_sales_rasters() -> list[str]:
    warnings: list[str] = []
    for path in list(SALES_ASSETS.rglob("*.png")) + list(SALES_ASSETS.rglob("*.jpg")):
        if path.name.endswith(".orig.png"):
            continue
        try:
            w, _h = Image.open(path).size
        except OSError:
            continue
        if w > MAX_PDF_RASTER_PX:
            warnings.append(f"{path.relative_to(ROOT)} is {w}px wide (>{MAX_PDF_RASTER_PX})")
    return warnings


def main() -> int:
    if not _HAS_PIL:
        print("Warning: Pillow/numpy not installed — skipping raster optimization.", file=sys.stderr)
        print("  The PDF will still render with existing assets.", file=sys.stderr)
        print("  To enable optimization: pip3 install Pillow numpy", file=sys.stderr)
        return 0

    if not Path(CHROME).exists():
        print(f"Chrome not found at {CHROME}", file=sys.stderr)
        return 1

    print("Preparing sales PDF raster assets…")
    for rel, spec in TARGETS.items():
        dest, dims, nbytes = prepare_raster(rel, spec)
        print(f"  {dest.relative_to(ROOT)}  {dims[0]}×{dims[1]}  {nbytes // 1024} KB")

    for entry in SVG_RASTER:
        src_rel, dest_rel, w, h, q = entry[:5]
        bg = entry[5] if len(entry) > 5 else None
        try:
            dest, dims, nbytes = rasterize_svg(src_rel, dest_rel, w, h, q, bg)
            print(f"  {dest.relative_to(ROOT)}  {dims[0]}×{dims[1]}  {nbytes // 1024} KB  (from {src_rel})")
        except FileNotFoundError as e:
            print(f"  skip {dest_rel}: {e}")

    for entry in CANON_SVG_RASTER:
        src_rel, dest_rel, w, h, q = entry[:5]
        bg = entry[5] if len(entry) > 5 else None
        try:
            dest, dims, nbytes = rasterize_svg(src_rel, dest_rel, w, h, q, bg)
            print(f"  {dest.relative_to(ROOT)}  {dims[0]}×{dims[1]}  {nbytes // 1024} KB  (from {src_rel})")
        except FileNotFoundError as e:
            print(f"  skip {dest_rel}: {e}")

    floor_src = SALES_ASSETS / "interface-floor-view.orig.png"
    if floor_src.exists():
        dest, dims, nbytes = bake_brochure_floor_shot(
            floor_src, SALES_ASSETS / "interface-floor-view-brochure.jpg"
        )
        print(f"  {dest.relative_to(ROOT)}  {dims[0]}×{dims[1]}  {nbytes // 1024} KB  (feather baked)")

    warns = audit_sales_rasters()
    if warns:
        print("\nRaster width warnings:")
        for w in warns:
            print(f"  ⚠ {w}")
    print("Done.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
