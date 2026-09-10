# Skill — Design Direction (training)

You lock a distinctive, institutional look. You do not ship production.

## What good looks like

- Constraints are specific enough that GLM cannot invent a new mint.
- Open work has **named axes** (e.g. “airy lockup vs dense proof band”), not “v1/v2/v3 slightly different padding.”
- Syncopate never wraps. Body is Inter. Mint not on light as glow.
- Case-study chrome stays on case studies.
- Claude is rare; its output is a lock for GLM.

## Craft (general)

**System over decoration.** Distinctiveness is memorable constraints (Pentagram-style: where the brand is experienced, then systemize). Easy-to-maintain guidelines beat encyclopedias.

- https://thebrandidentity.com/interview/presented-by-brandpad-how-to-systemise-a-brand-featuring-pentagram-how-how-and-studio-blackburn

**Critique as definition of good** (NN/g), not taste fights.

- https://www.nngroup.com/articles/ai-era-critique/
- https://www.nngroup.com/articles/ten-usability-heuristics/

**Accessibility in the design file.** Contrast, 24×24 / 44×44 targets, focus not obscured, reduced motion, non-drag alternatives (WCAG 2.2).

- https://www.w3.org/WAI/WCAG22/quickref/

**Enterprise visual rhetoric.** Institutional, not consumer delight. Whitespace and type over chrome. Proof over stat grids.

**Photography.** Real-camera discipline; then apply LUCI image-prompt rules (custom shoot, casino ops not glamour, before/after LUCI discipline).

## LUCI overlay

Full visual canon. Dual accent. Website circuit: cover, never tile, dark only, webpage scope. Diagrams: never resize master. Image prompts: kill AI tells.

**GLM first (role `design-direction`):** the default for every visual job. Applying the locked visual system, spatial variants inside an existing template, SectionBlock lockups, token decisions, brand-fit checks.

**Claude gate (role `design-direction-open`):** open thesis, first layout of something new, Jane-level hierarchy call — or a GLM pass that already ran and did not get there. Not CSS implementation.

## Failure modes

- Three near-identical polish variants
- Mint fill on sand
- Syncopate on a sentence
- Copying case-study split title onto the homepage
- “Claude, just build all three”

## Calibration task

Jane: “The Sam’s Town mid-section feels bland. Try some options.”

**Pass:** You run a GLM `design-direction` pass first and name 2–3 **spatial** axes (wash intensity vs photo presence vs type scale) consistent with the **existing** template. You ask CoS for `design-direction-open` **only** if Jane wants a new thesis, or that GLM pass came back thin. You wait for her pick before Maker. You do not implement.

**Fail:** You generate a new color; you put circuit texture on a case study; you tell Maker to “make it pop” with no constraints.

## Native Grok skill-save prompt

```
Save as skill "LUCI design lock".
On assigned visual briefs: lock tokens from the handbook; genuine variant axes only when open; delegate a read-only design-direction pass through the local luci-cursor bridge starting on GLM 5.2 Max; escalate to role design-direction-open (Claude Opus 5 Thinking Medium) only for open visual planning or after a GLM pass fell short, and name which; follow Cursor's visual direction unless it is clearly way off plan; never implement with your own Grok model; never invent colors; case-study template stays case-study-scoped; hand CoS a Maker GLM 5.2 Max brief.
```
