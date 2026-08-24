# Aliante Race & Sports — mock movie trailer prompt

A templated "In a world…" trailer for the Aliante LED wall project. Grounded in the real install (Jason walkthrough transcript, 07-15) and the real room (`OneDrive/.../Project Media/Aliante LED`).

**Runtime:** ~50 seconds, 10 shots. Most generators cap at 5–8s per clip, so each shot below is a standalone prompt — generate them individually and assemble in edit.

**Render at 16:9.** Add 2.39:1 letterbox bars in the edit for the anamorphic trailer feel. (Rendering 2.39 natively means recropping for LinkedIn later.)

---

## The creative premise — read this before generating

The joke, and the reason it works, is that the trailer treats **trade work with total gravity**. Customs delays, a quarter-inch high spot in plywood, six data jumpers per node, a tidy rack — shot like the fate of the world hangs on them. That contrast only lands if the *rooms, materials, people, and gear are documentary-real*. A glossy sci-fi render kills it.

So the grade is cinematic on purpose (this is a deliberate genre parody, an intentional exception to the "no cinematic" line in `luci-image-prompt-rules.mdc`), but everything inside the frame stays real: actual casino carpet, actual scissor lifts, actual plastic sheeting, actual tired guys in work shirts. **Cinematic light, documentary content.**

---

## Master style block — prepend to every shot prompt

> Cinematic movie-trailer footage, shot on ARRI Alexa with anamorphic prime lenses, 2.39:1, shallow-to-deep depth of field, natural lens flares and mild vignetting, fine 35mm grain. Teal-and-amber trailer grade, deep crushed blacks, high contrast, practical in-situ lighting only — LED screens, work lights, and warm casino downlights are the sources. Real, unglamorous casino construction environment: swirling patterned carpet, dark wood paneling, plastic sheeting, scissor lifts, sawdust, cable spools. Real non-model working people in work shirts and hard hats, focused and tired, never smiling at camera, never posing. Handheld with subtle camera weight. Photorealistic live-action, not animation.

## Master negative prompt — append to every shot prompt

> Negative prompt: generic stock photo, polished, sterile, showroom, perfect symmetry, futuristic, sci-fi, blue haze, purple haze, HDR, oversaturated, illustration, 3D render, CGI, cartoon, posed model, smiling at camera, thumbs up, hard hat photoshoot, gambling glamour, roulette wheel, poker chips, fanned cards, Vegas skyline, slot machine close-up, watermark, text overlay, distorted hands, extra fingers, warped faces, garbled text on screens.

---

## Shot list

Voiceover in the classic trailer-narrator register — slow, gravelly, one line per breath. On-screen text cards are cut between shots, not burned into them; generate title cards separately or build them in the edit so the type is clean.

---

### Shot 1 — the world (0:00–0:05)

**VO:** "In a world… where every screen answers to a different master…"

> [Master style block] Slow push-in down a dim back-of-house casino corridor at night. Four mismatched equipment racks line the wall, packed with proprietary boxes, tangled coax and ethernet zip-tied in bundles, a bristling power strip, grey conduit overhead. Each rack's status LEDs blink out of sync in a different color. No people. Dust on the black metal, scuffed vinyl floor. Lit only by a single warm caged work light and the cold rack LEDs — harsh, directional, deep shadow. 24mm anamorphic, slow dolly forward, deep depth of field. [Master negative prompt]

---

### Shot 2 — the divide (0:05–0:10)

**VO:** "Where the sportsbook lives on one system… and the rest of the property lives on another."

> [Master style block] A wide, dark, empty casino sportsbook before dawn — long curved wood betting counter, plush leather lounge chairs, a bank of odds-board displays glowing cold blue along the back wall showing dense white betting lines. One lone operations manager in a polo stands at the far end, small in frame, back to camera, looking up at the boards. Swirling blue-and-tan patterned carpet, dark wood paneling, coffered ceiling with recessed spots mostly off. The screens are the only real light. 21mm anamorphic, static wide, deep depth of field, subtle handheld drift. [Master negative prompt]

**Text card after:** `SOME WALLS ARE BUILT.`

---

### Shot 3 — the arrival (0:10–0:14)

**VO:** "They came from customs. They came on a Saturday. They came with more crates than floor."

> [Master style block] Early Saturday morning at a casino loading dock, overcast desert light. A semi trailer backed in with its doors open, revealing a dense stack of wooden shipping crates stenciled with shipping marks. Two workers in work shirts wrestle a pallet jack under a crate; a third stands in the trailer, hands on hips, assessing. Crates already unloaded crowd the dock apron with barely any room left to walk. Cold blue dawn light against the warm sodium glow spilling from the dock doorway. 28mm anamorphic, handheld, slightly low angle looking up at the stack. [Master negative prompt]

---

### Shot 4 — the enemy (0:14–0:19)

**VO:** "One crew. One curved wall. And a quarter of an inch… that stood between them and perfect."

> [Master style block] Extreme close-up, macro: a worker's weathered hand runs flat along a raw plywood substrate wall, fingertips catching on a proud seam where two sheets meet unevenly. A metal straightedge lies against the surface, a sliver of daylight visible under it at the high spot. Sawdust on the surface, a pencil mark nearby. Razor-shallow depth of field, the seam tack sharp, everything else falling off. Single hard raking work light from the side to exaggerate the bump's shadow. 50mm anamorphic macro, static, breath-tight. [Master negative prompt]

**Text card after:** `THIS ONE HAD TO BE FLAT.`

---

### Shot 5 — the fight (0:19–0:24)

**VO:** "This summer… they planed the wall by hand."

> [Master style block] Mid-shot of a worker in a dust-covered work shirt and safety glasses running a handheld power planer along a curved plywood wall, a plume of wood shavings arcing out into a shaft of work light. A drift of shavings and debris piles on the plastic-sheeted floor below. Behind him, the curved black steel LED frame structure recedes into darkness, half-built. Motion blur on the shavings, hard side light, heavy atmospheric dust in the beam. 35mm anamorphic, handheld, slight low angle. [Master negative prompt]

---

### Shot 6 — the montage (0:24–0:31)

*Cut this as three fast beats, roughly 2 seconds each, accelerating.*

**VO:** "Six runs to every node. Three up. Three down."

> **6a.** [Master style block] Close-up of gloved hands seating a bundle of six colored data jumpers into an LED panel receiver card behind a wall frame, three cables routed upward and three downward in a clean fan. Tight, cramped, lit by a headlamp. 50mm anamorphic, handheld, very shallow depth of field. [Master negative prompt]

> **6b.** [Master style block] A worker on a raised scissor lift in a dark casino interior, silhouetted against the half-lit LED wall he is setting a panel into, one bright panel snapping alive mid-motion and throwing colored light across his face and the lift rail. Plastic sheeting and stacked chairs below. 24mm anamorphic, low angle looking up, handheld. [Master negative prompt]

> **6c.** [Master style block] A dense back-of-house equipment rack seen straight on, being patched — a hand pushing a blue Cat6 cable home, dozens of neatly dressed and hand-labeled cables sweeping in ordered bundles down the rack's rear rails. Cold rack LEDs and a warm work light. 35mm anamorphic, static, deep depth of field. [Master negative prompt]

**Text card after:** `TWENTY-FOUR ZONES.` → `ONE CANVAS.`

---

### Shot 7 — the silence (0:31–0:36)

*Music drops out completely. This is the trailer's breath.*

**VO:** *(nothing — silence)*

> [Master style block] Very tight over-the-shoulder shot in a darkened sportsbook: a single index finger hovers over, then touches, one control on a tablet screen held in a technician's hand. The tablet is the only light source, underlighting the hand and jaw. Everything beyond is black and out of focus. Absolute stillness. 85mm anamorphic, locked off, razor-shallow depth of field, the fingertip and the screen edge in focus. [Master negative prompt]

---

### Shot 8 — the reveal (0:36–0:42)

**VO:** *(silence holds one beat, then a low bass hit lands with the wall)*

> [Master style block] The hero shot. A massive curved LED video wall sweeping the entire length of a casino sportsbook ignites all at once from black, flooding the room with light — live sports content across the full canvas, a row of blue odds boards glowing beneath it. Below, empty plush leather lounge seating, a long curved polished-wood betting rail, rich patterned carpet catching the color. The wall is the sole light source, throwing color across every surface and up into the dark coffered ceiling. Slow, majestic dolly-back and slight tilt up to take in the wall's full curve. 18mm anamorphic, deep depth of field, natural anamorphic flare off the brightest panels. [Master negative prompt]

---

### Shot 9 — the crowd (0:42–0:46)

**VO:** "Hundreds of A/V endpoints…"

> [Master style block] The same sportsbook now full and alive on a game night, shot from behind the last row of seating. Real patrons — a mix of ages and builds, in casual clothes — seated and standing, faces upturned and lit by the wall, one man half out of his chair mid-reaction, hands in the air. Backs of heads and shoulders in the foreground silhouette. Drinks and phones on the small tables. The wall's glow is the key light; warm downlights pool in the aisles. 24mm anamorphic, handheld, deep depth of field. [Master negative prompt]

---

### Shot 10 — the tag (0:46–0:52)

**VO:** "…one interface."

> [Master style block] Slow pull back to a very wide, high, symmetrical view of the full sportsbook at peak — the curved wall blazing across the frame, the room full, everything running. Hold, then let the image fall to black. 16mm anamorphic, slow steady pull back. [Master negative prompt]

**End cards, cut in on black:**

```
LUCI
THE ORCHESTRATION ENGINE FOR ENTERPRISE MULTIMEDIA
```

```
ALIANTE RACE & SPORTS
NOW PLAYING ON ONE INTERFACE
```

---

## Sound design

- **0:00–0:14** — low sustained sub drone, sparse. A single deep bass hit on each text card.
- **0:14–0:31** — braams enter and build; the montage cuts land on an accelerating percussive pulse (the classic trailer "riser stack").
- **0:31–0:36** — **total silence.** Nothing but faint room tone. This is the most important six seconds in the trailer; do not let the tool score over it.
- **0:36** — one enormous bass hit synced exactly to the wall igniting, then the full orchestral/electronic payoff swells under the last three shots.
- **0:52** — hard cut to silence on the black end card.

---

## Two versions to generate

Per the client-naming rule in `luci-social-media.mdc`, a named client video needs the client's OK on file.

- **Named cut** — end card reads `ALIANTE RACE & SPORTS`. Hold until Aliante signs off.
- **Unnamed cut** — swap the end card to `ONE PROPERTY. ONE INTERFACE.` and drop the "RACE & SPORTS" signage from any generated frame. Safe to post now.

Also worth noting: if this is headed for LinkedIn, the same rule retires in-progress install content. These are AI-generated depictions rather than real field photos, so it isn't a direct violation — but shots 3 through 6 read as a build in progress. Cleanest path is to hold the trailer until after Aliante's public reveal, then it's completed-state case-study content.

---

## Use the real footage where you can

There's genuine footage in `Project Media/Aliante LED` that will beat anything a generator produces, and mixing it in is what will sell the whole thing as real:

- `IMG_4888.jpeg`, `IMG_4859.jpeg` — the finished wall, wide. Strong candidates for **shot 8**.
- `IMG_5337.jpeg`, `IMG_5338.jpeg` — the book alive with people. Good for **shot 9**.
- `IMG_5029.jpeg` — the odds boards lit during construction with the scissor lift and plastic sheeting still up. Excellent, hard-to-fake **shot 6b**.
- `IMG_5232.jpeg` — the "RACE & SPORTS" signage and ticker. Natural establishing plate for **shot 2**.
- `IMG_4850.mov`, `IMG_5234.mov`, `IMG_5242.mov` — motion. Worth reviewing before generating anything for shots 8 and 10.

Use AI for the shots nobody filmed — the corridor of mismatched racks, the macro on the plywood seam, the finger on the tablet. Use the camera roll for the wall itself.

---

## Copy that stays exact

The end-card tagline is verbatim brand copy: **"The Orchestration Engine for Enterprise Multimedia."** Don't let a generator paraphrase it, and don't let it render the type — build the end cards in the edit so the wordmark and tagline are clean and correctly spelled.

"A/V" is always written with the slash, including in the voiceover script and any burned-in text.
