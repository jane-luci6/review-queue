#!/usr/bin/env python3
"""Port use-case content from the customer FAG (web) into the prospect FAG (PDF).

- 6 desc-only UCs (01,06,09,12,21,22): port desc + benefits from customer; keep prospect head + try-row.
- 8 REPLACED UCs (03,07,08,11,13,14,16,24): port head + desc + benefits from customer; write a fresh Today/On LUCI try-row.
- 10 already-matching UCs: untouched.
"""
from __future__ import annotations
import re
from pathlib import Path

SALES = Path(__file__).resolve().parent.parent / "ui_kits" / "sales"
CUST = SALES / "field-activation-guide-web.html"
PROSP = SALES / "field-activation-guide-prospect.html"

DESC_ONLY = {1, 6, 9, 12, 21, 22}
REPLACED = {3, 7, 8, 11, 13, 14, 16, 24}

# Fresh Today/On LUCI rows for the 8 REPLACED UCs (matches the prospect's fragment style).
FRESH_TRY = {
    3: ("a video wall lives in one layout, and a change means an integrator visit.",
         "run it full or split it into zones, and switch with a tap or on a schedule."),
    7: ("a page means a walk to the booth and the music cuts out.",
         "page from anywhere and the music dips for the moment, then returns on its own."),
    8: ("a tournament means a manual wall reconfig or an integrator visit.",
         "full-wall or zoned presets switch with a tap or at tip-off, then revert when it&rsquo;s over."),
    11: ("a source change means a ticket and a truck roll to the rack.",
          "edit the source yourself and every display using it picks up the change."),
    13: ("a new endpoint means an integrator truck roll and a wait.",
          "enter its IP, name it, assign a venue, and it&rsquo;s on the map yourself."),
    14: ("a common issue means a phone call to the integrator or a vendor ticket.",
          "self-serve the common issues from one spot your team can reach any time."),
    16: ("a dead screen is noticed by a guest first, or caught on a walk-around.",
          "the map clusters every device and flags the one that needs attention before a guest does."),
    24: ("every login starts at a default view and you pan and zoom to find your bearings.",
          "the dashboard opens right where your walk begins, with no panning or zooming."),
}


def esc(s: str) -> str:
    # Customer HTML already uses &rsquo;/&mdash;/&amp; entities — only convert any stray literal
    # curly-apostrophe / em-dash to entities; never touch an existing & (it's already &amp;).
    return s.replace("\u2019", "&rsquo;").replace("\u2014", "&mdash;")


def cust_ucs():
    src = CUST.read_text(encoding="utf-8")
    out = []
    for m in re.finditer(r'<div class="fag-uc">(.*?)(?=<div class="fag-uc">|</section>)', src, re.S):
        b = m.group(1)
        h = re.search(r'<h3 class="fag-uc__title">(.*?)</h3>', b, re.S)
        d = re.search(r'<p class="fag-uc__desc">(.*?)</p>', b, re.S)
        ul = re.search(r'<ul class="fag-uc__benefits">(.*?)</ul>', b, re.S)
        hh = esc(h.group(1)) if h else ""
        dd = esc(d.group(1)) if d else ""
        lis = [esc(li) for li in re.findall(r'<li>(.*?)</li>', ul.group(1), re.S)] if ul else []
        out.append((hh, dd, lis))
    return out


def main():
    cust = cust_ucs()
    assert len(cust) == 24, f"customer UCs: {len(cust)}"
    src = PROSP.read_text(encoding="utf-8")
    # Isolate each <li class="doc-uc"> block by the position of the NEXT such opener (not by
    # </li>, which collides with the nested benefits <li> items).
    opens = [m.start() for m in re.finditer(r'<li class="doc-uc">', src)]
    assert len(opens) == 24, f"prospect UC openers: {len(opens)}"
    end = src.find('</ul>\n      </section>', opens[23])
    bounds = [(opens[i], opens[i + 1]) for i in range(23)] + [(opens[23], end)]
    head = src[:opens[0]]
    tail = src[end:]
    blocks = [src[a:b] for (a, b) in bounds]

    for i in range(24):
        uc = i + 1
        block = blocks[i]
        ch, cd_, cb = cust[i]
        if uc in DESC_ONLY:
            block = re.sub(r'(<p class="doc-uc__desc">).*?(</p>)', rf'\g<1>{cd_}\g<2>', block, count=1, flags=re.S)
            new_ul = '<ul class="doc-uc__benefits">\n              ' + '\n              '.join(f'<li>{li}</li>' for li in cb) + '\n            </ul>'
            block = re.sub(r'<ul class="doc-uc__benefits">.*?</ul>', new_ul, block, count=1, flags=re.S)
        elif uc in REPLACED:
            block = re.sub(r'(<p class="doc-uc__head">).*?(</p>)', rf'\g<1>{ch}\g<2>', block, count=1, flags=re.S)
            block = re.sub(r'(<p class="doc-uc__desc">).*?(</p>)', rf'\g<1>{cd_}\g<2>', block, count=1, flags=re.S)
            new_ul = '<ul class="doc-uc__benefits">\n              ' + '\n              '.join(f'<li>{li}</li>' for li in cb) + '\n            </ul>'
            block = re.sub(r'<ul class="doc-uc__benefits">.*?</ul>', new_ul, block, count=1, flags=re.S)
            today, onluci = FRESH_TRY[uc]
            new_try = ('<p class="doc-uc__try"><span class="doc-uc__try-row doc-uc__try-row--old">'
                       '<span class="doc-uc__try-key">Today</span>'
                       f'<span class="doc-uc__try-val">{today}</span></span>'
                       '<span class="doc-uc__try-row doc-uc__try-row--new">'
                       '<span class="doc-uc__try-key">On LUCI</span>'
                       f'<span class="doc-uc__try-val">{onluci}</span></span></p>')
            block = re.sub(r'<p class="doc-uc__try">.*?</p>', new_try, block, count=1, flags=re.S)
        blocks[i] = block

    PROSP.write_text(head + ''.join(blocks) + tail, encoding="utf-8")
    print(f"Ported {len(DESC_ONLY)} desc-only + {len(REPLACED)} replaced UCs into {PROSP.name}")


if __name__ == "__main__":
    main()
