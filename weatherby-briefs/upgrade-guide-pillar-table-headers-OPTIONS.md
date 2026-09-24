# Upgrade Guide — pillar table header OPTIONS

**Section:** “What the release puts in your hands” (`#ug-pillars`)  
**Target:** `.ug-pillar__head` black boxes (`background: #0f1e27`) + `.ug-pillar__num` / `.ug-pillar__name` / `.ug-pillar__ctrl`  
**Scope:** header treatment only. No pillar body / pill copy rewrite. Mint wash section lockups kept. Hero fade abandoned (untouched).

**Compare (bare URL = current black):**
- http://10.10.1.37/luci-upgrade-guide/ *(current)*
- http://10.10.1.37/luci-upgrade-guide/?tableHeaders=subtle
- http://10.10.1.37/luci-upgrade-guide/?tableHeaders=none
- http://10.10.1.37/luci-upgrade-guide/?tableHeaders=alt

Sticky mini picker on the page switches the same variants.

---

## 0 · Current black (default)

Navy/black filled header cells on each pillar card; white name; gold “control”; ghost white number.

**Thesis:** Strong contrast badge — reads as a dark “cap” on the light pillar fills.

---

## A · Subtle mint (`?tableHeaders=subtle`)

Replace black boxes with a soft mint wash + faint mint border; ink-strong name; accent-light “control”; soft navy ghost number. Brand tokens only.

**Thesis:** Quieter header that still feels like a labeled cell, in family with the locked mint-wash section lockups.

---

## B · None (`?tableHeaders=none`)

Remove the boxes altogether. Headers as type only + light mint hairline under the name. Ghost numbers hidden.

**Thesis:** Lightest read — pillars stay cards; titles stop competing with the mint section lockup above.

---

## C · Soft rule (`?tableHeaders=alt`)

Middle ground: soft white fill + hairline border; ink type; accent-light “control”; short split mint|gold-deep rule under the head (brochure duo).

**Thesis:** Still a small header plate, but white/ink instead of black — keeps structure without the dark boxes.

---

## Waiting

Jane pick: **current** | **subtle** | **none** | **alt**. Then strip picker and lock the chosen class.
