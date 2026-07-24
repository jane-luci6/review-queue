# Website hero — Operations persona cover
## Claude video prompt — **AI-generated footage only** (copy everything below the line)

---

You are producing a **~20-second looping website hero video** for LUCI Systems’ Operations persona page. **Generate all visuals with AI** — no stock footage, no client B-roll, no real property photography, and **do not reuse** the existing industry hero clips (sportsbook / hotel lobby / arena / airport / convention).

**Master:** 1920×820 (or 1920×1080 cropped to ~21:9 in post), 30fps, H.264, **muted** (no music, no VO — this loops under page copy).  
**No on-screen text, no logos, no LUCI UI chrome** — titles live in the website HTML over a dark scrim.

**Page:** lucisystems.com / who-we-serve / operations  
**Audience:** Operations leaders who run the floor — hotels, casinos, arenas, terminals, convention centers.

---

### Messaging driver (visual only — no captions in the video)

- Show **ops professionals at work**: walking the property, coordinating by radio/tablet, checking zones, making a quiet call before a moment hits.
- Feel: calm competence, not chaos. Premium hospitality / venue ops — not technicians in a rack room, not guests playing slots.
- **Industry-agnostic:** mix hotel lobby, gaming floor aisle, arena concourse, terminal corridor, banquet/pre-function — same team energy, different spaces. No named properties, no readable brand signage.
- Always **A/V** in any written materials. Never “layer” as a noun for LUCI.

---

### Workflow (do this in order)

1. **Generate** each shot below with AI video. Prefer continuous human motion (walking, turning, pointing, checking a tablet) over empty architecture pans.
2. **Match grade** across shots: cool-neutral premium interiors, slightly desaturated, soft bokeh backgrounds — not neon Vegas cliché, not harsh fluorescent BOH.
3. **Assemble** with short crossfades (~0.4–0.6s). First and last frames should feel similar enough that the loop doesn’t hard-jump.
4. **Export** muted H.264 master (`luci-operations-hero.mp4`) + one poster still (`operations-hero-poster.jpg` at ~2s in).
5. Deliver the two files to Cursor; they go in `luci-website/public/videos/` and `public/images/who-we-serve/`.

**People continuity:** mid-30s to mid-50s ops pros, diverse, business-casual or smart property uniform (dark blazer / radio / badge — **no client logos on badges**). Tablet or handheld radio as the props. Never look at camera. Guests only as soft background bokeh if present at all.

---

### Assembly timeline (~20 seconds, looping)

| Time | Shot ID | Action |
|------|---------|--------|
| 0:00–0:04 | **WALK-LOBBY** | Ops lead walks a hotel/resort lobby aisle, tablet in hand, soft LED screens behind |
| 0:04–0:08 | **COORD-FLOOR** | Two ops pros briefly coordinate on a gaming-floor aisle (radio/tablet), energy of the floor soft behind them |
| 0:08–0:12 | **CONCOURSE** | Single ops pro walks an arena or venue concourse, checks a wall display, keeps moving |
| 0:12–0:16 | **TERMINAL** | Ops / facilities lead walks a bright terminal corridor past digital boards (boards abstract — no readable flights/text) |
| 0:16–0:20 | **PREFUNCTION** | Ops pro in banquet pre-function / convention hallway, tablet, soft push toward doors about to open — ends facing roughly same direction as WALK-LOBBY for loop |

---

### AI generation prompts (one per shot)

#### WALK-LOBBY — Hotel lobby walk (4s)
**Type:** AI video — tracking / gimbal follow from side-rear ¾.

**Prompt:**
> Cinematic tracking shot following a professional hotel operations manager in their mid-40s walking through a modern upscale hotel lobby, dark blazer, holding a tablet, purposeful calm walk, large digital wall displays in soft focus showing abstract colorful motion graphics with no readable text, warm premium hospitality lighting, polished floors, anonymous luxury resort interior, no logos, no brand names, shallow depth of field, documentary corporate style, 4 seconds, smooth gimbal motion

**Negative:** looking at camera, smiling pose, neon Vegas, casino chips, readable screen text, logo on tablet UI, stock smiling receptionist, selfie angle, rack room, cables

---

#### COORD-FLOOR — Two ops pros on gaming aisle (4s)
**Type:** AI video — medium wide, slight slow push.

**Prompt:**
> Two operations professionals standing briefly in a modern casino gaming floor aisle coordinating, one with a handheld radio, one with a tablet, mid conversation then one nods and walks off frame, slot machines and LED screens soft bokeh in background with no readable game titles or logos, premium cool-warm lighting, anonymous casino interior, calm competent energy not celebration, cinematic documentary, 4 seconds, subtle camera push-in

**Negative:** jackpot celebration, confetti, guests cheering, looking at camera, dealer table close-up, readable jackpot amounts, tribal casino art, smoking, neon strip exterior

---

#### CONCOURSE — Arena / venue walk (4s)
**Type:** AI video — side tracking.

**Prompt:**
> Operations staff member walking along a modern sports arena concourse, smart casual dark attire with radio clipped, glancing at a large digital display board showing abstract graphics only no scores or text, wide corridor, soft crowd bokeh far in background, cool stadium lighting with warm accents, anonymous venue architecture, cinematic corporate documentary, smooth lateral tracking, 4 seconds

**Negative:** team jerseys with real logos, readable scoreboard, beer ads, looking at camera, handheld shake, empty abandoned stadium, construction

---

#### TERMINAL — Airport / transit corridor (4s)
**Type:** AI video — following from behind then slight orbit.

**Prompt:**
> Facilities or operations lead walking through a bright modern airport terminal corridor, tablet in hand, passing overhead digital information boards with abstract non-readable graphics, clean glass and steel architecture, soft traveler bokeh, cool daylight interior, calm purposeful walk, anonymous international terminal, cinematic documentary, 4 seconds, smooth camera follow

**Negative:** readable flight numbers, airline logos, security checkpoint drama, looking at camera, stock suitcase montage, rush chaos

---

#### PREFUNCTION — Convention / banquet hallway (4s)
**Type:** AI video — slow push toward doors; end frame faces similar direction to WALK-LOBBY for loop.

**Prompt:**
> Operations coordinator walking a modern convention center pre-function hallway toward banquet doors, tablet under arm, soft LED wayfinding screens with abstract shapes no readable event names, elegant carpet and high ceilings, warm hospitality lighting, about to open an event, calm readiness, anonymous convention center, cinematic corporate documentary, gentle push-in, 4 seconds

**Negative:** trade-show booth chaos, readable banners, looking at camera, party balloons, stock handshake, empty dark hallway

---

### Grade & loop notes

- Match skin tones and contrast across all five shots so the crossfades feel like one evening / one shift.
- Prefer **over-the-shoulder and ¾ rear** angles so faces stay secondary to action.
- Export **muted**. Website adds its own scrim + copy.
- Loop test: last 8 frames of PREFUNCTION should dissolve cleanly into first 8 frames of WALK-LOBBY.

---

### Deliverables

1. `luci-operations-hero.mp4` — ~20s, muted, H.264, 1920×820 or 1920×1080  
2. `operations-hero-poster.jpg` — still from ~0:02  

Drop both into Cursor chat (or into `luci-website/public/videos/` and `public/images/who-we-serve/`) and ask to wire / deploy.
