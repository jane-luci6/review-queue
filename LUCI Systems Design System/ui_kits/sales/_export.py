#!/usr/bin/env python3
"""Render every sales-deck slide at 2x and combine into a single PDF in ~/Downloads."""
import re, subprocess, time, pathlib, sys
from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent  # LUCI Systems Design System
SALES = pathlib.Path(__file__).resolve().parent
deck = (SALES / "sales-deck.html").read_text()
sections = re.findall(r'<section class="slide[^"]*".*?</section>', deck, re.DOTALL)

OUT = SALES / "_export"
OUT.mkdir(exist_ok=True)
# clear stale frames
for f in OUT.glob("*.png"):
    f.unlink()

PORT = 8099
srv = subprocess.Popen([sys.executable, "-m", "http.server", str(PORT)], cwd=str(ROOT),
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
time.sleep(1.2)

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
base = f"http://localhost:{PORT}/ui_kits/sales/"
SCALE = 2.0  # 1280x720 -> 2560x1440

frames = []
for i, sec in enumerate(sections, 1):
    n = str(i).zfill(2)
    m = re.search(r'id="(s\d+)"', sec)
    sid = m.group(1) if m else n
    harness = (
        '<!DOCTYPE html><html><head><meta charset="UTF-8">'
        f'<base href="{base}">'
        '<link rel="stylesheet" href="../../assets/fonts/luci-brand-fonts.css">'
        '<link rel="stylesheet" href="sales-deck.css">'
        '<style>html,body{margin:0;padding:0;background:#06090C;}</style>'
        '</head><body>' + sec + '</body></html>'
    )
    hp = OUT / f"s{sid}.html"
    hp.write_text(harness)
    out = OUT / f"s{sid}.png"
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-sandbox",
                    "--hide-scrollbars", f"--force-device-scale-factor={SCALE}",
                    "--window-size=1280,720", "--default-background-color=00000000",
                    "--virtual-time-budget=4000",
                    f"--screenshot={out}", f"http://localhost:{PORT}/ui_kits/sales/_export/s{sid}.html"],
                   check=False)
    frames.append(out)
    print(f"  slide {sid} -> {out.name} ({out.stat().st_size//1024} KB)")

srv.terminate()

# Combine into a single PDF (each frame = one landscape 16:9 page)
imgs = [Image.open(f).convert("RGB") for f in frames]
dest = pathlib.Path.home() / "Downloads" / "LUCI-Sales-Deck.pdf"
imgs[0].save(dest, save_all=True, append_images=imgs[1:])
print(f"\nPDF saved: {dest}  ({dest.stat().st_size//1024} KB, {len(imgs)} pages, {imgs[0].size[0]}x{imgs[0].size[1]}px)")
