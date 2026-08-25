#!/usr/bin/env python3
"""Build the New LUCI go-to-market brief as a Word doc.

Pairs with the Preliminary Feature List. Same voice rules: operational, A/V,
no layer, no %, no client names, no internal-only terms anywhere including IT depth.
"""

from pathlib import Path

from docx import Document
from docx.shared import Pt, RGBColor

OUT = Path.home() / "Desktop" / "New LUCI - Go-to-Market Brief.docx"

NAVY = RGBColor(0x35, 0x4F, 0x5C)
MINT_DARK = RGBColor(0x2B, 0x9E, 0x80)
INK = RGBColor(0x1F, 0x2C, 0x33)
MUTED = RGBColor(0x5C, 0x6B, 0x74)

HEAD_FONT = "Arial"
BODY_FONT = "Calibri"


def set_font(run, name=BODY_FONT, size=11, bold=False, color=INK, italic=False):
    run.font.name = name
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.italic = italic
    run.font.color.rgb = color


def para(doc, text="", size=11, bold=False, color=INK, italic=False,
         space_after=8, space_before=0, name=BODY_FONT):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.space_before = Pt(space_before)
    if text:
        set_font(p.add_run(text), name=name, size=size, bold=bold, color=color, italic=italic)
    return p


def section_heading(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(22)
    p.paragraph_format.space_after = Pt(4)
    set_font(p.add_run(text.upper()), name=HEAD_FONT, size=13, bold=True, color=MINT_DARK)
    rule = doc.add_paragraph()
    rule.paragraph_format.space_after = Pt(10)
    set_font(rule.add_run("\u2014" * 28), name=HEAD_FONT, size=9, color=MINT_DARK)


def sub_heading(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after = Pt(4)
    set_font(p.add_run(text), name=HEAD_FONT, size=12, bold=True, color=NAVY)


def bullets(doc, items):
    for item in items:
        p = doc.add_paragraph(style="List Bullet")
        p.paragraph_format.space_after = Pt(4)
        if isinstance(item, tuple):
            lead, rest = item
            set_font(p.add_run(lead), size=11, bold=True, color=INK)
            set_font(p.add_run(rest), size=11, color=INK)
        else:
            set_font(p.add_run(item), size=11, color=INK)


def add_table(doc, headers, rows):
    table = doc.add_table(rows=1 + len(rows), cols=len(headers))
    table.style = "Light Grid Accent 1"
    hdr = table.rows[0].cells
    for i, h in enumerate(headers):
        hdr[i].text = ""
        run = hdr[i].paragraphs[0].add_run(h)
        set_font(run, name=HEAD_FONT, size=10, bold=True, color=NAVY)
    for r, row in enumerate(rows, 1):
        for c, cell_text in enumerate(row):
            cell = table.rows[r].cells[c]
            cell.text = ""
            run = cell.paragraphs[0].add_run(cell_text)
            set_font(run, size=10, color=INK)


doc = Document()
for name in ("Normal", "List Bullet"):
    style = doc.styles[name]
    style.font.name = BODY_FONT
    style.font.size = Pt(11)
    style.font.color.rgb = INK

for section in doc.sections:
    section.top_margin = section.bottom_margin = Pt(54)
    section.left_margin = section.right_margin = Pt(58)

title = doc.add_paragraph()
title.paragraph_format.space_after = Pt(2)
set_font(title.add_run("New LUCI \u2014 Go-to-Market Brief"),
        name=HEAD_FONT, size=20, bold=True, color=NAVY)

sub = doc.add_paragraph()
sub.paragraph_format.space_after = Pt(2)
set_font(sub.add_run("Working document for Mike \u2014 pairs with the Preliminary Feature List"),
        name=BODY_FONT, size=12, color=MUTED)

# ── 1. How to use ──────────────────────────────────────────────────
section_heading(doc, "How to use this")
para(doc, "This is a working document, not a locked plan. It pairs with the Preliminary Feature List: that doc says what we are promoting; this one says how we promote it. Re-bucket the pillars, edit the phase plan, and flag anything in red for Mike. Nothing here ships until Mike signs off.")

# ── 2. Positioning ────────────────────────────────────────────────
section_heading(doc, "Positioning statement")
para(doc, "For property operations leadership at enterprise hospitality and gaming, LUCI is the A/V orchestration platform that puts control, accountability, and support where the work actually happens \u2014 in the venue, on the floor, in the brand \u2014 unlike a traditional control system that lives in a back office and requires an integrator to change. Credible because of the embedded team that stays on property and the one-interface architecture across the install base.")

# ── 3. Messaging pillars ─────────────────────────────────────────
section_heading(doc, "Messaging pillars")
para(doc, "Five repeatable themes. Each one is proven by a primary feature from the Feature List. We want to be known for these, not for the feature names.",
     size=11, color=MUTED, italic=True, space_after=6)

sub_heading(doc, "1. Control where the work happens")
bullets(doc, [
    ("The story: ", "The platform goes to the room, not just the back office. A bartender, an events manager, a cabana guest \u2014 control lives in the space where the work happens."),
    ("Proven by: ", "Venue panels (primary). Audio group control (primary) supports it \u2014 group balance survives the first time someone reaches for a slider in the room."),
    ("Do not cross: ", "This is not a kiosk sale or a hardware SKU. It is control in the venue. Do not lead with the tablet; lead with the person and the space."),
])

sub_heading(doc, "2. The next look, ready before the moment")
bullets(doc, [
    ("The story: ", "The floor keeps running while the next look is built. Apply on cue, so the change lands when the event actually starts."),
    ("Proven by: ", "Staging (primary). Save the staged set as a preset; time it and it is a scheduled preset."),
    ("Do not cross: ", "Do not lead with \u201cpresets\u201d as a feature name. Presets are the mechanism; staging is the story."),
])

sub_heading(doc, "3. One record of what changed")
bullets(doc, [
    ("The story: ", "Every action recorded against a person and a time. A fault has a duration, not an anecdote. One source of truth for what is on and what changed."),
    ("Proven by: ", "Audit trails (primary). Live map accuracy (secondary) and add any endpoint (secondary) keep the map the source of truth."),
    ("Do not cross: ", "No internal identifiers, no \u201cwe see everything,\u201d no \u201c100% visibility.\u201d Out-of-band changes appear for most third-party types, not all."),
])

sub_heading(doc, "4. Help where you already are")
bullets(doc, [
    ("The story: ", "Support lives in the product, on the thing that is wrong, not at the end of a phone tree. The embedded team is accountable, built in, not bolted on."),
    ("Proven by: ", "In-product support (primary)."),
    ("Do not cross: ", "No auto-tickets from every down device. No \u201c24/7\u201d claims. A person initiates so the property controls what escalates."),
])

sub_heading(doc, "5. The platform, in your brand")
bullets(doc, [
    ("The story: ", "The interface carries the property\u2019s own photography, marks, and colors. The platform disappears into the brand, not the other way around."),
    ("Proven by: ", "Property-branded interface (primary)."),
    ("Do not cross: ", "Do not lead with \u201cthemes\u201d as a feature. Lead with the property seeing itself. Theme is the mechanism, not the story."),
])

# ── 4. Do-not-say list ─────────────────────────────────────────
section_heading(doc, "Do-not-say list")
para(doc, "Banned across all launch materials, including the IT brief. Voice rules from the Messaging Guide apply.",
     size=11, color=MUTED, italic=True, space_after=6)
bullets(doc, [
    "Layer as a noun for LUCI. Use orchestration engine, platform, infrastructure, runs, operates, integrates, consolidates.",
    "\u201cAV\u201d or \u201cA-V\u201d. Always A/V in body, headlines, captions, alt text, and on visuals.",
    "Percentage claims, revenue lift, handle %, payback period, guest satisfaction scores.",
    "Named clients in public materials unless cleared for a specific case study.",
    "Revolutionize, transform, empower, absurdly simple, easy to use, intuitive, game-changing, best-in-class.",
    "Owner\u2019s rep. Use LUCI FDE or the embedded team.",
    "Internal product terms: Hub, CoreX, the tunnel vendor, correlation IDs, Superbase, Cloudflare. Not in public or IT materials.",
    "\u201cWe tunnel into your whole network.\u201d Frame the private tunnel as one paired connection, not standing inbound access.",
    "Auto-opened tickets from every down device. A person initiates.",
    "Panel-level presets as shipping, until product confirms. Do not claim as live.",
    "A specific kiosk or panel hardware SKU and price, until Mike confirms procurement.",
    "Multi-site map or real floor plans on real coordinates. Not yet.",
])

# ── 5. Two audiences ────────────────────────────────────────────
section_heading(doc, "Two audiences, two motions")
para(doc, "We have an install base and a net-new prospect pool. They need different treatment; do not run the same copy at both.",
     size=11, color=MUTED, italic=True, space_after=6)

sub_heading(doc, "Existing clients \u2014 a release, not a launch")
bullets(doc, [
    "They are getting the new version. The question is upgrade logistics, what changes for them, and what the new features unlock that they are paying for elsewhere.",
    "Motion: customer-success, not demand-gen. Pre-brief before public, upgrade timeline, what to do (if anything).",
    "Channel: direct email from the embedded team or Mike, not the LinkedIn announcement.",
])

sub_heading(doc, "Net-new prospects \u2014 a launch")
bullets(doc, [
    "They do not know LUCI. The campaign leads with the primary features as proof of the orchestration thesis.",
    "Motion: demand-gen. Teaser, announce, deep-dive, sustain.",
    "Channel: LinkedIn, website, sales deck, one-pager, the IT brief for technical buyers.",
])

# ── 6. Phase plan ──────────────────────────────────────────────
section_heading(doc, "Phase plan")
para(doc, "A launch is a sequence, not an event. The day-0 post is the middle of the campaign, not the end. Dates are relative (T-12 to T+90) until the ship date is set.",
     size=11, color=MUTED, italic=True, space_after=6)

add_table(doc,
    ["Phase", "Timing", "What must be true", "Owner"],
    [
        ["Discover & Define", "T-12 to T-8",
         "ICP known, buying committee mapped, competitive frame refreshed for this release", "Jane + Mike"],
        ["Positioning & Messaging", "T-8 to T-6",
         "This brief signed off; messaging pillars locked; do-not-say list agreed", "Jane, Mike approves"],
        ["Internal enablement", "T-7 to T-4",
         "FDEs, support, and sales briefed before the market sees anything; talk track and battlecard drafted", "Jane + Richard/Nick"],
        ["Build & Stage", "T-4 to T-1",
         "All external assets drafted and in QA; website staged; email to existing clients queued", "Jane"],
        ["Launch & Accelerate", "T-0 to T+2w",
         "Coordinated LinkedIn + website + sales + email-to-install-base; daily check-ins first 72 hours", "Jane + Mike"],
        ["Measure & Iterate", "T+2w to T+90d",
         "Pipeline, demos booked, upgrade confirmations, support volume reviewed; messaging iterated on what reps hear", "Jane + Mike"],
    ])

# ── 7. Channel & asset map ────────────────────────────────────
section_heading(doc, "Channel and asset map")
para(doc, "Filtered to channels LUCI actually has. Email sequences outperform single blasts, but for our motion that means 2-3 touches, not 5.",
     size=11, color=MUTED, italic=True, space_after=6)

add_table(doc,
    ["Channel", "Asset", "Phase"],
    [
        ["LinkedIn", "Announcement post + 1-2 feature highlights (real screenshots)", "T-0 + sustain"],
        ["The Signal newsletter", "Teaser blurb; full article after launch", "T-1, T+7"],
        ["Website", "Feature or pillar page update; homepage callout if scope warrants", "T-0, staged"],
        ["Sales deck", "Slide(s) update + talk track", "T-4 (enablement)"],
        ["One-pager / spec sheet", "Update what LUCI is and is not", "T-2"],
        ["Case study", "If a pilot property co-developed and named tie-in cleared", "T+30 (sustain)"],
        ["IT brief", "The IT Technical Details section from the Feature List, as a deeper leave-behind", "T-2"],
        ["Email to existing clients", "Upgrade logistics, what changes, what to do", "T-1, T-0, T+10"],
        ["Internal", "FDE and support pre-brief, FAQ, short Loom", "T-7 (before external)"],
    ])

# ── 8. KPIs ──────────────────────────────────────────────────
section_heading(doc, "What \u201cworked\u201d means")
para(doc, "Defined before launch, not debated after. The credible metrics for our motion, not vanity metrics.",
     size=11, color=MUTED, italic=True, space_after=6)
bullets(doc, [
    ("Qualified pipeline created. ", "Net-new prospects entering or advancing a sales conversation."),
    ("Demos booked. ", "A scheduled demo tied to the launch, not just content engagement."),
    ("Existing-client upgrade confirmations. ", "How many install-base properties have confirmed the upgrade and a timeline."),
    ("Support ticket volume. ", "If it spikes after release, it is a messaging gap, not a product gap. Watch it."),
    ("Feature adoption (90 days in). ", "Which existing clients are actively using venue panels, staging, or audit trails \u2014 the proof the features landed."),
])

# ── 9. Persona phrasing ────────────────────────────────────────
section_heading(doc, "Persona phrasing")
para(doc, "One campaign. IT brief is the only extra artifact. Same feature, different first sentence \u2014 phrasing in the messaging spine, not a separate kit.",
     size=11, color=MUTED, italic=True, space_after=6)
add_table(doc,
    ["Persona", "First sentence for the same feature (venue panels)", "Where they go deeper"],
    [
        ["Operations / A/V",
         "A bartender, an events manager, a cabana guest \u2014 control in the space.",
         "Standard one-pager"],
        ["IT",
         "One scoped control surface with no route into the administrative application.",
         "The IT brief (private tunnel, identity, audit depth)"],
        ["Marketing / guest experience",
         "The login looks like us; the panel looks like the venue.",
         "Standard one-pager"],
        ["Leadership / finance",
         "One accountable team, one interface, one record of what changed.",
         "Standard one-pager"],
    ])

# ── 10. Open decisions for Mike ────────────────────────────────
section_heading(doc, "Open decisions for Mike")
para(doc, "These only Mike can decide. They block assets and timing. Flagged in red in the working copy.",
     size=11, color=MUTED, italic=True, space_after=6)
bullets(doc, [
    ("Pricing and packaging. ", "Is the new version included for existing clients, a paid upgrade, or a module? Are venue panels a hardware sale? This shapes every asset."),
    ("Panel hardware. ", "Are we selling the glass, reselling a partner\u2019s, or describing capability only?"),
    ("Panel-level presets. ", "Assume shipping for marketing, or hold until product confirms?"),
    ("Pilot property for the case study. ", "Is there a co-developed property we can name, or do we go unnamed?"),
    ("Ship date and announce gap. ", "Same-day availability, or announce-then-ship? Sets the T-0 for the whole plan."),
    ("Competitive frame. ", "What do we say when a prospect says \u201cwe already have a control system\u201d or \u201cour integrator handles that\u201d?"),
])

# ── Save ────────────────────────────────────────────────────
doc.save(OUT)
print(f"Wrote {OUT}")
