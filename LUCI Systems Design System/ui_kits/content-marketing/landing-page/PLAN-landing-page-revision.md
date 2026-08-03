# Landing page revision plan

**Problem:** the current page is a condensed homepage. That's the wrong shape.
Someone arriving here clicked a specific post — they already know roughly what
LUCI is and they're choosing whether to take it seriously. The homepage's job is
to orient a stranger and route them onward. This page's job is to convince someone
already leaning in. Those need different content, not the same content at 60% length.

---

## What the research says

Five findings that actually change the design:

1. **Traffic temperature changes what the page needs.** Cold search traffic needs
   context and proof depth; warm traffic needs *faster objection resolution and
   clearer action paths*. Social traffic is warm-but-browsing — it needs relevance
   established in seconds, then a short path to the ask. Repeating awareness-level
   content to a warm visitor is the specific failure mode we have right now.

2. **The 2026 hero standard is demonstration, not tagline.** The benchmark has
   moved from static positioning statements to heroes that *visually show product
   value within 3–5 seconds*. "Control your whole property." is a claim. A moving
   or annotated interface is evidence.

3. **One CTA beats several.** Single-CTA pages convert around 13.5% vs 10.5% for
   multi-CTA. Every additional link is an exit.

4. **Form length is the biggest single lever.** One documented case cut fields from
   11 to 4 and conversions rose 120%; a B2B SaaS field-reduction test showed ~15.7%
   lift. 4–5 fields is the recommended range for a demo request.

5. **Trust signals belong next to the form, not in their own band.** Omitting trust
   signals near the form raises abandonment by roughly 12%. Proof should sit at the
   moment of decision, and be spread through the page rather than crammed into one
   strip.

Benchmark to hold ourselves to: B2B SaaS landing pages average 2–5% conversion;
top performers hit 8–15%.

**Honest caveat on all of the above:** these are averages drawn from
high-volume SaaS. LUCI sells to a small number of very high-value properties. At
low traffic we will never have the volume for statistically meaningful A/B tests,
and a slightly *higher*-friction form that qualifies better may be worth more than
a higher raw conversion rate. So treat these as design principles, not targets to
chase. One qualified GM beats forty curious tyre-kickers.

---

## The core shift

| Homepage does | This page should do |
|---|---|
| Explains the category | Assumes they get the category |
| Positions with claims | Proves with specifics and numbers |
| Serves six audiences | Serves the one who clicked |
| Routes to many places | Routes to one action |
| Sells the vision | Removes the reasons not to book |

**Guiding rule:** if a section would work unchanged on the homepage, it probably
shouldn't be here.

---

## Proposed changes, in priority order

### 1. Rebuild the hero around demonstration, and put the form in it
The single biggest change. Right now the hero is a headline plus a static map, and
the form is five sections away.

- Replace the positioning headline with a **specific, concrete promise** —
  something closer to "See every screen, speaker and light on your property from
  one map" than "Control your whole property."
- Make the visual **do something**: a short silent looping screen capture of a
  scene firing across zones, or the map with an annotated call-out. Video/motion
  is the 2026 standard here and we already have a screen-recording brief drafted
  for the feature-highlight series that could produce it.
- Put the **form directly in the hero**, right-hand column. Warm visitors
  shouldn't scroll to convert.

### 2. Cut the silo / "run them all" section
This is awareness-building for someone who doesn't yet see the problem. Anyone
arriving from the orchestration carousel just *read* that argument — the carousel
makes exactly this case across four slides. Repeating it is the main reason the
page feels homepage-ish. Compress to a single sentence in the hero sub-line, or cut.

### 3. Add an objections block — the highest-value addition
This is content a homepage can't afford and a landing page needs. What actually
stops a GM booking:

- *Do we have to rip out what we already own?* (no — LUCI sits on existing hardware)
- *How long does deployment take?* (the Ameristar answer: three days)
- *Who has to run it day to day?* (your team, not the integrator)
- *Does it work with our brand of displays / DSP / signage?*
- *What happens to our existing control panels?*

Four or five of these, answered in a sentence each. This is the "friction
reduction" pillar and it's completely missing today.

### 4. Move the consolidation comparison up, and keep it
It's the most differentiated thing on the page — numbers rather than adjectives,
and it's the kind of specific that a warm visitor came for. Should sit immediately
after the hero. Still needs the real row labels from you.

### 5. Make Control / Automate / Execute concrete
Currently three text cards that could describe any platform. Give each one a real
screenshot or a one-line real example ("game time: 40 screens to the feed, lights
to 60%, signage to the promo, in one trigger"). Show the thing, don't name the
thing.

### 6. Cut or halve the four capability cards
"Complete visibility across your property" is homepage positioning. Either cut
them, or reduce to the two that aren't generic and give them specifics.

### 7. Move proof next to the form, and use the case study as a stat
- Ameristar's "three days to a future-ready platform" becomes a stat block or
  pull-quote adjacent to the form — no link needed, so the missing destination
  stops being a blocker.
- Property logos move from their own mid-page strip to just under the form.

### 8. Trim the form to four fields
Currently six. Recommend: **Name · Work email · Property · Role**. Drop "What are
you trying to fix?" — it's the field most likely to stall someone, and it's a
better question for the sales conversation than the form. Role stays only because
it genuinely changes who follows up.

### 9. Keep the nav at one CTA
Already done, and it's right. No site navigation, no footer link to the current
site while the rebrand is in flight.

---

## Proposed section order

1. **Hero** — concrete promise + moving product visual + 4-field form
2. **Consolidation comparison** — the numbers
3. **What it actually does** — Control / Automate / Execute, with real screens
4. **Objections** — rip-and-replace, timeline, who operates it, compatibility
5. **Proof** — Ameristar stat + logos
6. **Closing CTA** — repeat the form or an anchor back to it
7. **Minimal footer**

Seven blocks, one action, no exits. Shorter than the current page despite adding
the objections block, because the awareness content comes out.

---

## What I need from you

- **Comparison table copy** — row labels, plus the `5+ / 12+ / 100+` rows (still outstanding)
- **A decision on the hero visual** — can we get a screen recording, or should I
  build an annotated static version from existing screenshots?
- **Objection answers** — the five questions above, a sentence each. This is the
  part only you and Nick can write.
- **Ameristar case detail** — enough to write the stat block honestly
- **Property logos** — files for the three
- **Confirmation on dropping the silo section** — it's the biggest cut and it's
  currently on the homepage, so worth an explicit yes

---

## Sources

- [Genesys Growth — designing B2B SaaS landing pages](https://genesysgrowth.com/blog/designing-b2b-saas-landing-pages)
- [Genesys Growth — designing demo request pages](https://genesysgrowth.com/blog/designing-demo-request-pages)
- [Growth Spree — B2B SaaS landing page benchmarks & demo conversion](https://www.growthspreeofficial.com/blogs/b2b-saas-landing-page-best-practices-demo-conversion-2026)
- [SaaS Hero — 5 pillars for B2B SaaS landing page CVR](https://www.saashero.net/design/landing-page-optimization-b2b-saas/)
- [SaaS Hero — enterprise landing page design 2026](https://www.saashero.net/design/enterprise-landing-page-design-2026/)
- [Unicorn Platform — B2B landing page examples & framework](https://unicornplatform.com/blog/b2b-landing-page-examples/)
- [Directive Consulting — B2B landing page best practices](https://directiveconsulting.com/blog/blog-b2b-landing-page-best-practices-examples/)
- [Trajectory — B2B website forms for complex sales](https://www.trajectorywebdesign.com/blog/b2b-website-forms/)
- [Instapage — B2B landing page lessons for 2026](https://instapage.com/blog/b2b-landing-page-best-practices)
