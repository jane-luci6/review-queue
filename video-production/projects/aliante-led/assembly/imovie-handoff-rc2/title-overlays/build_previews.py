#!/usr/bin/env python3
"""Render two title-overlay previews for Aliante RC2 iMovie handoff.

Outputs (into ./previews/):
  01-main-title-c00-transparent.png   — Syncopate ALL CAPS, mint, centered (the one display moment)
  02-space-grotesk-c02-transparent.png — Space Grotesk Bold, white, lower-third
  01-main-title-c00-preview.jpg        — c00 overlay composited over a frame from clip 001 (s01)
  02-space-grotesk-c02-preview.jpg      — c02 overlay composated over a frame from clip 002 (s02)

Locked copy (verbatim from titles.md):
  c00: "Aliante Casino + Hotel"  -> rendered ALL CAPS as "ALIANTE CASINO + HOTEL"
  c02: "100,000+ square feet of gaming."  -> rendered verbatim

Type rules for this beat (Jane locked):
  - Main title only: Syncopate, ALL CAPS, centered on screen
  - All other onscreen text: Space Grotesk

Visual system: existing LUCI branding. Mint is primary accent on dark for the
display moment (per case-study hero pattern); body copy is white on a soft,
translucent dark backing (clean cinematic restraint, not a caption box).
"""
from __future__ import annotations
import subprocess
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# ---- Paths
HERE = Path(__file__).resolve().parent
PREV = HERE / "previews"
TIMELINE = HERE.parent / "timeline"
FONTS = Path("/Users/janehaynie/Documents/Cursor Projects/luci-design/LUCI Systems Design System/assets/fonts")
PREV.mkdir(parents=True, exist_ok=True)

# ---- Canvas
W, H = 1920, 1080

# ---- LUCI brand tokens (dark-bg treatment, per .cursor/rules)
MINT = (104, 227, 190, 255)        # --mint  #68E3BE  (primary accent on dark)
NAVY_DEEP = (10, 22, 28)           # --navy-deep  #0A161C
WHITE = (255, 255, 255, 255)

SYNC = FONTS / "Syncopate-Bold.ttf"
SPACE = FONTS / "SpaceGrotesk-SemiBold.ttf"  # bold-ish weight for body cards
SPACE_BOLD = FONTS / "SpaceGrotesk-SemiBold.ttf"


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(f"cmd failed: {' '.join(str(c) for c in cmd[:4])}...\n{r.stderr[-1500:]}")
    return r


def soft_dark_backing(canvas, box, pad_x=52, pad_y=34, radius=26, alpha=150, blur=10):
    """Paint a soft, translucent dark rounded-rectangle backing behind a text box.
    Edges are gaussian-blurred so it reads as a cinematic scrim, not a hard caption box."""
    x0, y0, x1, y1 = box
    scrim = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    sd = ImageDraw.Draw(scrim)
    sx0 = max(0, x0 - pad_x)
    sy0 = max(0, y0 - pad_y)
    sx1 = min(W, x1 + pad_x)
    sy1 = min(H, y1 + pad_y)
    # outer soft halo
    sd.rounded_rectangle([sx0, sy0, sx1, sy1], radius=radius + 6,
                         fill=(NAVY_DEEP[0], NAVY_DEEP[1], NAVY_DEEP[2], int(alpha * 0.55)))
    scrim = scrim.filter(ImageFilter.GaussianBlur(radius=blur))
    # inner core (sharper, slightly stronger)
    sd2 = ImageDraw.Draw(scrim)
    sd2.rounded_rectangle([sx0 + 8, sy0 + 8, sx1 - 8, sy1 - 8], radius=radius,
                          fill=(NAVY_DEEP[0], NAVY_DEEP[1], NAVY_DEEP[2], alpha))
    return scrim


def measure(draw, text, font):
    bbox = draw.textbbox((0, 0), text, font=font)
    return bbox[2] - bbox[0], bbox[3] - bbox[1], bbox[1]  # width, height, top_offset


def render_main_title(text: str, out: Path):
    """c00 — Syncopate ALL CAPS, mint, centered. The one display moment."""
    canvas = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(canvas)
    display = text.upper()  # ALL CAPS
    font = ImageFont.truetype(str(SYNC), 72)
    tw, th, top_off = measure(draw, display, font)
    # centered horizontally and vertically
    x = (W - tw) // 2
    y = (H - th) // 2 - top_off
    # soft dark backing behind the title for legibility over moving footage
    box = (x, y + top_off, x + tw, y + top_off + th)
    canvas = Image.alpha_composite(canvas, soft_dark_backing(canvas, box,
                                                              pad_x=64, pad_y=40,
                                                              radius=30, alpha=140, blur=12))
    draw = ImageDraw.Draw(canvas)
    draw.text((x, y), display, font=font, fill=MINT)
    canvas.save(out)


def render_body(text: str, out: Path):
    """c02 — Space Grotesk Bold, white, lower-third. Cinematic restraint, not a caption box."""
    canvas = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(canvas)
    font = ImageFont.truetype(str(SPACE_BOLD), 42)
    tw, th, top_off = measure(draw, text, font)
    # lower-third placement: sit roughly 160px up from the bottom
    x = (W - tw) // 2
    y = (H - 160) - (th // 2) - top_off
    box = (x, y + top_off, x + tw, y + top_off + th)
    canvas = Image.alpha_composite(canvas, soft_dark_backing(canvas, box,
                                                              pad_x=52, pad_y=34,
                                                              radius=26, alpha=150, blur=10))
    draw = ImageDraw.Draw(canvas)
    draw.text((x, y), text, font=font, fill=WHITE)
    canvas.save(out)


def grab_frame(clip: Path, ts: float, out: Path):
    """Extract one 1920x1080 frame at timestamp ts from clip."""
    run([
        "ffmpeg", "-y", "-ss", f"{ts:.3f}", "-i", str(clip),
        "-frames:v", "1", "-vf", "scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080",
        "-q:v", "2", str(out),
    ])


def composite(frame_png: Path, overlay_png: Path, out: Path):
    """Alpha-composite the transparent overlay onto the frame, save as JPG preview."""
    bg = Image.open(frame_png).convert("RGBA")
    ov = Image.open(overlay_png).convert("RGBA")
    comp = Image.alpha_composite(bg, ov).convert("RGB")
    comp.save(out, quality=92)


def main():
    # --- Locked copy (verbatim from titles.md) ---
    c00_text = "Aliante Casino + Hotel"          # rendered ALL CAPS Syncopate
    c02_text = "100,000+ square feet of gaming."  # rendered verbatim Space Grotesk

    # --- Transparent overlays ---
    p_c00 = PREV / "01-main-title-c00-transparent.png"
    p_c02 = PREV / "02-space-grotesk-c02-transparent.png"
    render_main_title(c00_text, p_c00)
    render_body(c02_text, p_c02)
    print(f"WROTE {p_c00.name}  ({p_c00.stat().st_size} bytes)")
    print(f"WROTE {p_c02.name}  ({p_c02.stat().st_size} bytes)")

    # --- Composites over representative frames from matching timeline clips ---
    # c00 over clip 001 (s01): title window 1.5-4.0s into the full cut = into clip 001.
    #     Grab a frame near the middle of that window (~2.5s into clip 001).
    clip001 = TIMELINE / "001-s01-Casino 2-title-open-casino.mp4"
    frame001 = PREV / "_frame-001-s01.png"
    grab_frame(clip001, 2.5, frame001)
    prev_c00 = PREV / "01-main-title-c00-preview.jpg"
    composite(frame001, p_c00, prev_c00)
    print(f"WROTE {prev_c00.name}  ({prev_c00.stat().st_size} bytes)")

    # c02 over clip 002 (s02): title window 6.3-9.7s into the full cut.
    #     Clip 001 is 6.0s, so the title starts ~0.3s into clip 002 and runs to ~3.7s.
    #     Grab a frame near the middle of that window (~2.0s into clip 002).
    clip002 = TIMELINE / "002-s02-Casino 1-gaming-100k.mp4"
    frame002 = PREV / "_frame-002-s02.png"
    grab_frame(clip002, 2.0, frame002)
    prev_c02 = PREV / "02-space-grotesk-c02-preview.jpg"
    composite(frame002, p_c02, prev_c02)
    print(f"WROTE {prev_c02.name}  ({prev_c02.stat().st_size} bytes)")

    # --- Clean up intermediate frame files ---
    for f in (frame001, frame002):
        if f.exists():
            f.unlink()

    print("\nDONE. Preview files in:")
    print(f"  {PREV}")


if __name__ == "__main__":
    main()
