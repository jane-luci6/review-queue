#!/usr/bin/env python3
"""Render one-off card 02: "Across more than 40 acres" (no period).

BODY-TREATMENT-LOCK.md rev 2 — two-layer build (bed + plate), N-class geometry.
One-off card in cards/ (not part of c02-c19 titles.md sequence).

Per-card override (this card only, NOT a house-rule change):
  - No mint rule (Jane removed it on card 01; do not bring it back).
  - No mint type — no display numeral; all words off-white Medium incl "40".
  - The lock still governs every other body card (c02-c19) unchanged.

Variant N: one calm line (fits ~700px inside 864 measure). Left x=160,
last baseline y=920, N-class plate top edge y=728. Type off-white Medium 52
(readable, ~48-56; matches card 01 body text for consistency).

Composite order: footage -> bed -> plate -> type (with shadow). No mint rule.
Never ship plate without bed. No pill, no radius, no centered text.
"""
from __future__ import annotations
import subprocess
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

HERE = Path(__file__).resolve().parent
CARDS = HERE / "cards"
TIMELINE = HERE.parent / "timeline"
FONTS = Path("/Users/janehaynie/Documents/Cursor Projects/luci-design/LUCI Systems Design System/assets/fonts")
CARDS.mkdir(parents=True, exist_ok=True)

W, H = 1920, 1080
OFF_WHITE = (245, 248, 250)   # #F5F8FA
NAVY_DEEP = (10, 22, 28)      # #0A161C
FONT_MEDIUM = FONTS / "SpaceGrotesk-Medium.ttf"

LEFT_X = 160
LAST_BASELINE_Y = 920

BED_PEAK = 0.45
BED_TOP_Y = 380
BED_BOTTOM_Y = 1080
BED_H_FALLOFF_START = 980
BED_H_FALLOFF_END = 1920
BED_H_FALLOFF_END_MULT = 0.30

PLATE_DENSITY = 0.62
PLATE_TOP_Y = 728             # N-class
PLATE_FULL_DENSITY_X = 1024
PLATE_FALLOFF_END_X = 1536
PLATE_FEATHER_PX = 8

SHADOW_ALPHA = 0.50
SHADOW_OFFSET = (0, 3)
SHADOW_BLUR = 22

LINE_TEXT = "Across more than 40 acres"
MEDIUM_SIZE = 52
MEDIUM_OPACITY = 1.0
MEDIUM_TRACKING = 0.52      # +0.01em at 52px


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(f"cmd failed: {' '.join(str(c) for c in cmd[:4])}...\n{r.stderr[-1500:]}")
    return r


def _smoothstep(t):
    t = np.clip(t, 0.0, 1.0)
    return t * t * (3.0 - 2.0 * t)


def build_bed():
    ys = np.arange(H, dtype=np.float32)
    v_alpha = np.zeros(H, dtype=np.float32)
    mask = ys >= BED_TOP_Y
    t_v = (ys[mask] - BED_TOP_Y) / (BED_BOTTOM_Y - BED_TOP_Y)
    v_alpha[mask] = BED_PEAK * (t_v * t_v)
    xs = np.arange(W, dtype=np.float32)
    h_mult = np.ones(W, dtype=np.float32)
    mask_h = xs > BED_H_FALLOFF_START
    t_h = (xs[mask_h] - BED_H_FALLOFF_START) / (BED_H_FALLOFF_END - BED_H_FALLOFF_START)
    h_mult[mask_h] = 1.0 - (1.0 - BED_H_FALLOFF_END_MULT) * (t_h * t_h)
    alpha_2d = v_alpha[:, None] * h_mult[None, :]
    alpha_8 = np.clip(alpha_2d * 255.0, 0, 255).astype(np.uint8)
    rgba = np.zeros((H, W, 4), dtype=np.uint8)
    rgba[..., 0] = NAVY_DEEP[0]
    rgba[..., 1] = NAVY_DEEP[1]
    rgba[..., 2] = NAVY_DEEP[2]
    rgba[..., 3] = alpha_8
    return Image.fromarray(rgba).convert("RGBA")


def build_plate():
    ys = np.arange(H, dtype=np.float32)
    xs = np.arange(W, dtype=np.float32)
    v_feather = _smoothstep((ys - (PLATE_TOP_Y - PLATE_FEATHER_PX / 2)) / PLATE_FEATHER_PX)
    h_mult = np.ones(W, dtype=np.float32)
    mask_falloff = (xs > PLATE_FULL_DENSITY_X) & (xs <= PLATE_FALLOFF_END_X)
    t_h = (xs[mask_falloff] - PLATE_FULL_DENSITY_X) / (PLATE_FALLOFF_END_X - PLATE_FULL_DENSITY_X)
    h_mult[mask_falloff] = 1.0 - (t_h * t_h)
    h_mult[xs > PLATE_FALLOFF_END_X] = 0.0
    alpha_2d = PLATE_DENSITY * v_feather[:, None] * h_mult[None, :]
    alpha_8 = np.clip(alpha_2d * 255.0, 0, 255).astype(np.uint8)
    rgba = np.zeros((H, W, 4), dtype=np.uint8)
    rgba[..., 0] = NAVY_DEEP[0]
    rgba[..., 1] = NAVY_DEEP[1]
    rgba[..., 2] = NAVY_DEEP[2]
    rgba[..., 3] = alpha_8
    return Image.fromarray(rgba).convert("RGBA")


def _text_width(font, text, tracking):
    bbox = font.getbbox(text)
    w = bbox[2] - bbox[0]
    if len(text) > 1:
        w += int(round(tracking * (len(text) - 1)))
    return w


def draw_line(canvas):
    font_med = ImageFont.truetype(str(FONT_MEDIUM), MEDIUM_SIZE)
    fill = (OFF_WHITE[0], OFF_WHITE[1], OFF_WHITE[2], int(round(255 * MEDIUM_OPACITY)))
    shadow_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow_layer)
    sd.text((LEFT_X + SHADOW_OFFSET[0], LAST_BASELINE_Y + SHADOW_OFFSET[1]),
            LINE_TEXT, font=font_med,
            fill=(NAVY_DEEP[0], NAVY_DEEP[1], NAVY_DEEP[2], 255),
            anchor="ls", tracking=MEDIUM_TRACKING)
    shadow_layer = shadow_layer.filter(ImageFilter.GaussianBlur(radius=SHADOW_BLUR))
    r, g, b, a = shadow_layer.split()
    a = a.point(lambda v: int(v * SHADOW_ALPHA))
    shadow_layer = Image.merge("RGBA", (r, g, b, a))
    canvas = Image.alpha_composite(canvas, shadow_layer)
    draw = ImageDraw.Draw(canvas)
    draw.text((LEFT_X, LAST_BASELINE_Y), LINE_TEXT, font=font_med,
              fill=fill, anchor="ls", tracking=MEDIUM_TRACKING)
    return canvas


def render_card():
    canvas = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    canvas = Image.alpha_composite(canvas, build_bed())
    canvas = Image.alpha_composite(canvas, build_plate())
    canvas = draw_line(canvas)
    return canvas


def grab_frame(clip, ts, out):
    run([
        "ffmpeg", "-y", "-ss", f"{ts:.3f}", "-i", str(clip),
        "-frames:v", "1", "-vf", "scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080",
        "-q:v", "2", str(out),
    ])


def composite(frame_png, overlay_png, out):
    bg = Image.open(frame_png).convert("RGBA")
    ov = Image.open(overlay_png).convert("RGBA")
    comp = Image.alpha_composite(bg, ov).convert("RGB")
    comp.save(out, quality=92)


def main():
    p_overlay = CARDS / "card-02-across-40-acres-transparent.png"
    overlay = render_card()
    overlay.save(p_overlay)
    print(f"WROTE {p_overlay.name}  ({p_overlay.stat().st_size} bytes)")

    font_med = ImageFont.truetype(str(FONT_MEDIUM), MEDIUM_SIZE)
    line_w = _text_width(font_med, LINE_TEXT, MEDIUM_TRACKING)
    line_right = LEFT_X + line_w
    print(f"  line: '{LINE_TEXT}' w={line_w} -> right x={line_right} (limit 1024)")

    clip003 = TIMELINE / "003-s03-Casino 3-gaming-acres.mp4"
    frame003 = CARDS / "_frame-003-s03-card02.png"
    grab_frame(clip003, 2.0, frame003)
    prev = CARDS / "card-02-across-40-acres-preview.jpg"
    composite(frame003, p_overlay, prev)
    print(f"WROTE {prev.name}  ({prev.stat().st_size} bytes)")

    if frame003.exists():
        frame003.unlink()

    print("\nDONE. One-off card 02 files in:")
    print(f"  {CARDS}")


if __name__ == "__main__":
    main()
