# LUCI Feature Highlight — Episode 01: PIN-delegated access
## Production brief — reusable format for every future Feature Highlight

---

**Recommended approach: real screen recording, not AI-generated video.**

Unlike the "Control the Whole Property" weekly series (which shows the physical property and has to be AI-generated to avoid on-site/OSHA/reveal issues), this is a **software demo** — there's no client site in frame, no reveal risk. Recording the actual LUCI interface is more credible than simulating it, and it's almost certainly less production work than generating and grading AI footage. Use this brief either way; the AI-generation fallback is at the bottom if screen recording isn't practical for some reason.

---

### Concept

One property. Four different logins. Each login opens a different slice of the map — matched to the role.

**Sequence (real screen recording, ~20-25s):**

| Time | Screen action | On-screen text (add in post) |
|------|---------------|-------------------------------|
| 0:00–0:03 | PIN pad, empty | *Every login sees a different property.* |
| 0:03–0:07 | Enter GM PIN → full map loads, all zones lit | **General Manager** — every zone, every screen |
| 0:07–0:11 | Log out → enter Bartender PIN → map loads with only Sportsbar zone active/selectable, rest dimmed or greyed | **Bartender** — Sportsbar only |
| 0:11–0:15 | Log out → enter Floor Supervisor PIN → Casino Main / RR / South active, rest dimmed | **Floor Supervisor** — casino floor zones |
| 0:15–0:19 | Log out → enter Front Desk PIN → Hotel Lobby only active | **Front Desk** — lobby only |
| 0:19–0:23 | Quick montage: all four logins flash in sequence, end on GM's full map | *Access maps to responsibility.* |
| 0:23–0:25 | End card | LUCI wordmark + lucisystems.com |

**How to capture it:** screen-record the actual PIN entry + map switching in the LUCI interface (same screens as the two floor-map screenshots and the PIN pad screenshot already on file). If the interface doesn't visually dim/hide unavailable zones today, that's worth flagging to product — but for the post itself, dimming can be added in post-production over the recording, same technique used in the static mosaic version already built.

**Post-production:**
- Space Grotesk 700 for headlines/role labels, Inter 400 or DejaVu Sans for sublines — consistent with all other LUCI social graphics.
- Mint (`#2b9e80`) accent color for GM, then a distinct accent per role (blue / gold / purple) — same color-coding as the static mosaic, so the two pieces feel like one system if posted close together.
- Keep all on-screen text inside a centered 1080×1080 safe zone for LinkedIn crop tolerance, same as the weekly series spec.

---

### Caption (draft)

> One property. Four different logins.
>
> The general manager sees every zone. The bartender's PIN opens the sportsbar screens and nothing else. The floor supervisor gets the casino floor. Front desk gets the lobby.
>
> Same system, different view for every role. Access maps to responsibility, by design.

### Alt text (draft)

> Screen recording of the LUCI interface showing four different PIN logins, each unlocking a different set of zones on the same property map: full access for a general manager, sportsbar-only for a bartender, casino-floor zones for a floor supervisor, and lobby-only for front desk.

---

### Do not

- Show any real client name, room number, or identifying property signage on screen.
- Imply this is a security/access-control product beyond what LUCI actually does (zone-based display/audio control, not building security or POS access).
- Exceed ~25 seconds — this is a quick feature demo, not a walkthrough.

---

## Fallback: AI-generated motion-graphic version

If screen recording isn't practical, the static mosaic already built (`p3-real-zone-mosaic.png`) can be animated instead: four panel wipes, each revealing one role's spotlighted zone in sequence, built the same way as an AI/motion-graphics assembly (per-shot prompts below), rather than recording real software.

**MAP-BASE** — reuse the real floor-map screenshot as a static background plate (already real, no AI generation needed for this one).

**SPOTLIGHT-WIPE** (per role, ~3s each): simple radial/rounded-rectangle wipe transition revealing the lit zone while the rest of the frame dims — this is a straightforward After Effects/Canva motion job, not something that needs an AI video model (there's no benefit to generating this synthetically when the source art is already real).

This fallback avoids AI video generation entirely — it's really just "animate the static asset we already have," which is more reliable than generating new AI footage of a UI (AI video models tend to garble on-screen text and UI elements, per the note in the Ep02 casino-floor prompt).

---

**Format going forward:** every future Feature Highlight (e.g. daypart presets, audio zones, scheduling) can reuse this same skeleton — real screen recording of the actual feature in the LUCI interface, role/scenario labels in post, close on the abstraction line for that feature.
