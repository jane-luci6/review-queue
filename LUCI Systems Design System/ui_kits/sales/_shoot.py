#!/usr/bin/env python3
import re, subprocess, time, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent  # LUCI Systems Design System
SALES = pathlib.Path(__file__).resolve().parent
deck = (SALES / "sales-deck.html").read_text()
sections = re.findall(r'<section class="slide[^"]*".*?</section>', deck, re.DOTALL)

SHOOT = SALES / "_shoot"
SHOOT.mkdir(exist_ok=True)

PORT = 8099
srv = subprocess.Popen([sys.executable, "-m", "http.server", str(PORT)], cwd=str(ROOT),
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
time.sleep(1.2)

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
base = f"http://localhost:{PORT}/ui_kits/sales/"

for i, sec in enumerate(sections, 1):
    n = str(i).zfill(2)
    # id for filename
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
    hp = SHOOT / f"s{sid}.html"
    hp.write_text(harness)
    out = SHOOT / f"s{sid}.png"
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-sandbox",
                    "--hide-scrollbars", "--force-device-scale-factor=1.5",
                    "--window-size=1280,720", "--default-background-color=00000000",
                    "--virtual-time-budget=4000",
                    f"--screenshot={out}", f"http://localhost:{PORT}/ui_kits/sales/_shoot/s{sid}.html"], check=False)
    print(f"  slide {sid} -> {out.name}")

srv.terminate()
print("done")
