from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
import os
HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, 'assets')
DIAG = os.path.join(HERE, 'assets', 'diagrams')
CANON = os.path.join(HERE, '..', '..', 'assets', 'diagrams')
NAVY_DEEP = RGBColor(0x0A, 0x16, 0x1C)
OFF_WHITE = RGBColor(0xF5, 0xF8, 0xFA)
MINT = RGBColor(0x68, 0xE3, 0xBE)
MINT_DARK = RGBColor(0x2B, 0x9E, 0x80)
GOLD = RGBColor(0xED, 0xD0, 0x86)
INK = RGBColor(0x35, 0x4F, 0x5C)
INK_STRONG = RGBColor(0x1C, 0x2B, 0x33)
NAVY_MUTED = RGBColor(0x49, 0x61, 0x6E)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
OW82 = RGBColor(0xEB, 0xF5, 0xF8)
SLOT_BG = RGBColor(0x12, 0x1A, 0x22)
LOGO_BG = RGBColor(0x14, 0x20, 0x28)
FD = 'Syncopate'
FH = 'Space Grotesk'
FB = 'Inter'
SW = Inches(13.333)
SH = Inches(7.5)
PAD = Inches(0.85)
PTOP = Inches(0.6)
FY = Inches(7.05)

def spc(p, v):
    p._p.get_or_add_pPr().set('spc', str(int(v)))

def txt(s, l, t, w, h, a=MSO_ANCHOR.TOP):
    b = s.shapes.add_textbox(l, t, w, h)
    tf = b.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = a
    tf.margin_left = Emu(0); tf.margin_right = Emu(0)
    tf.margin_top = Emu(0); tf.margin_bottom = Emu(0)
    return b, tf

def rn(p, t, f=FH, sz=18, b=False, c=INK, sp=None):
    r = p.add_run(); r.text = t
    r.font.name = f; r.font.size = Pt(sz); r.font.bold = b; r.font.color.rgb = c
    if sp is not None:
        spc(p, sp)
    return r

def bg(s, c):
    s.background.fill.solid(); s.background.fill.fore_color.rgb = c

def kick(s, t, c=MINT):
    b, tf = txt(s, PAD, PTOP, Inches(6), Inches(0.3))
    rn(tf.paragraphs[0], t.upper(), f=FH, sz=11, b=True, c=c, sp=220)

def tit(s, runs, top=Inches(1.05), sz=34, ls=1.1):
    b, tf = txt(s, PAD, top, Inches(11.6), Inches(1.4))
    p = tf.paragraphs[0]; p.line_spacing = ls
    for t, c in runs:
        rn(p, t, f=FH, sz=sz, b=True, c=c); spc(p, -25)
    return b

def rule(s, top, l=PAD, c=GOLD, w=Inches(0.6)):
    sh = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, l, top, w, Pt(4))
    sh.fill.solid(); sh.fill.fore_color.rgb = c
    sh.line.fill.background(); sh.shadow.inherit = False

def foot(s, n, dark=True):
    b, tf = txt(s, PAD, FY, Inches(2), Inches(0.3))
    rn(tf.paragraphs[0], f'{n:02d}', f=FH, sz=10, b=True, c=(OW82 if dark else NAVY_MUTED), sp=140)
    b2, tf2 = txt(s, Inches(11.0), FY, Inches(1.5), Inches(0.3))
    tf2.paragraphs[0].alignment = PP_ALIGN.RIGHT
    rn(tf2.paragraphs[0], 'LUCI', f=FD, sz=10, b=True, c=(MINT if dark else NAVY_MUTED), sp=180)

def fit(s, path, l, t, mw, mh):
    from PIL import Image
    iw, ih = Image.open(path).size
    ar = iw / ih; bar = mw / mh
    if ar > bar:
        w = mw; h = int(mw / ar)
    else:
        h = mh; w = int(mh * ar)
    return s.shapes.add_picture(path, l + (mw - w) // 2, t + (mh - h) // 2, w, h)

def slot(s, l, t, w, h, label='Photo'):
    sh = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, l, t, w, h)
    sh.fill.solid(); sh.fill.fore_color.rgb = SLOT_BG
    sh.line.color.rgb = MINT; sh.line.width = Pt(1); sh.shadow.inherit = False
    tf = sh.text_frame; tf.word_wrap = True
    p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
    rn(p, label, f=FH, sz=11, b=True, c=MINT, sp=200)

def note(s, t):
    s.notes_slide.notes_text_frame.text = t

def logo(s, top=Inches(0.55), h=Inches(0.5)):
    s.shapes.add_picture(os.path.join(CANON, 'luci-full-mint.png'), PAD, top, height=h)

def ns():
    return prs.slides.add_slide(prs.slide_layouts[6])

prs = Presentation()
prs.slide_width = SW; prs.slide_height = SH

# 01 COVER
s = ns(); bg(s, NAVY_DEEP); logo(s)
b, tf = txt(s, PAD, Inches(2.5), Inches(11.6), Inches(2.2))
p = tf.paragraphs[0]; p.line_spacing = 1.04
rn(p, 'The orchestration engine', f=FH, sz=40, b=True, c=WHITE); spc(p, -30)
p2 = tf.add_paragraph(); p2.line_spacing = 1.04
rn(p2, 'for enterprise multimedia.', f=FH, sz=40, b=True, c=WHITE); spc(p2, -30)
rule(s, Inches(4.95), c=GOLD)
b, tf = txt(s, PAD, Inches(5.9), Inches(4), Inches(0.3))
rn(tf.paragraphs[0], 'PREPARED FOR', f=FH, sz=11, b=True, c=MINT, sp=220)
sl = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, PAD, Inches(6.35), Inches(3.2), Inches(0.7))
sl.fill.solid(); sl.fill.fore_color.rgb = LOGO_BG
sl.line.color.rgb = MINT; sl.line.width = Pt(1); sl.shadow.inherit = False
rn(sl.text_frame.paragraphs[0], 'Client logo', f=FH, sz=12, c=OW82)
note(s, 'Drop the client logo in the slot below Prepared for. Cover line is the tagline - leave it.')

# 02 AGENDA
s = ns(); bg(s, NAVY_DEEP); logo(s)
kick(s, 'Agenda')
tit(s, [('Here is how we will spend our time.', WHITE)])
items = ['Review of scope', 'Why LUCI was created', 'The LUCI solution', 'What is included', 'The LUCI value', 'The team', 'Our clients', 'What happens next - then the demo']
b, tf = txt(s, PAD, Inches(2.6), Inches(11.6), Inches(4.2))
for i, it in enumerate(items):
    p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
    p.line_spacing = 1.0; p.space_after = Pt(14)
    rn(p, f'{i+1:02d}  ', f=FH, sz=18, b=True, c=MINT)
    rn(p, it, f=FB, sz=18, c=OW82)
foot(s, 2)
note(s, 'Your roadmap. Say it, move on. The team and the two journey slides belong on the agenda.')

# 03 REVIEW OF SCOPE
s = ns(); bg(s, NAVY_DEEP); logo(s)
kick(s, 'Review of scope')
tit(s, [('The floor ', WHITE), ('we will orchestrate.', GOLD)])
b, tf = txt(s, PAD, Inches(2.7), Inches(4.6), Inches(3.5))
for i, line in enumerate(['Video', 'Signage', 'Audio', 'Lighting']):
    p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
    p.line_spacing = 1.3; p.space_after = Pt(16)
    rn(p, line, f=FH, sz=20, b=True, c=OW82)
    rn(p, '  -  edit to the room', f=FB, sz=13, c=NAVY_MUTED)
slot(s, Inches(6.0), Inches(2.7), Inches(6.5), Inches(3.5), 'Hero photo')
foot(s, 3)
note(s, 'The thin early-call slide Mark talks. Edit the four lines to the property. Spoken close: ask for a DSP file and a display count.')

# 04 WHY LUCI WAS CREATED
s = ns(); bg(s, NAVY_DEEP); logo(s)
kick(s, 'Why LUCI was created')
tit(s, [('Custom systems were the problem.', WHITE)])
rule(s, Inches(2.0), c=MINT)
b, tf = txt(s, PAD, Inches(2.6), Inches(9.5), Inches(3.8))
p = tf.paragraphs[0]; p.line_spacing = 1.55
rn(p, 'We came up as integrators, owners, and operators. Early versions of this idea ran inside casino properties. The custom systems were slow to deploy, hard to maintain, and rigid when the property changed. LUCI is the standard that replaced them.', f=FB, sz=20, c=OW82)
foot(s, 4)
note(s, 'The one slide in Mike voice. Spoken off-slide: fifty years and the Ameristar and Pinnacle names. The logo wall carries proof visually.')

# 05 TWO FORCES
s = ns(); bg(s, OFF_WHITE)
kick(s, 'The LUCI solution', c=MINT_DARK)
tit(s, [('Two forces ', INK_STRONG), ('working as one.', MINT_DARK)])
fit(s, os.path.join(DIAG, 'luci-what-luci-is.jpg'), PAD, Inches(2.4), Inches(7.6), Inches(2.6))
pillars = ['Complete visibility across your property', 'Align your teams by default', 'Fully activate the guest experience', 'An A/V platform that scales and improves']
b, tf = txt(s, PAD, Inches(5.2), Inches(11.6), Inches(1.8))
for i, ph in enumerate(pillars):
    p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
    p.line_spacing = 1.0; p.space_after = Pt(8)
    rn(p, '-  ', f=FH, sz=14, b=True, c=MINT_DARK)
    rn(p, ph, f=FB, sz=15, c=INK)
foot(s, 5, dark=False)
note(s, 'Defines the solution: platform plus embedded team. Four lines under the diagram.')

# 06 ONE INTERFACE
s = ns(); bg(s, NAVY_DEEP); logo(s)
kick(s, 'The LUCI solution')
tit(s, [('One interface to ', WHITE), ('control, automate, and execute', GOLD), (' the entire guest experience.', WHITE)], sz=30)
fit(s, os.path.join(ASSETS, 'interface-floor-view.png'), Inches(0.5), Inches(2.5), Inches(7.0), Inches(4.3))
steps = [('01', 'Control', 'Adjust lights, sound, screens, signage - any zone, by hand or auto.'), ('02', 'Automate', 'Build scenes once - game time, happy hour, morning reset.'), ('03', 'Execute', 'The whole room delivers the moment, in sync - no staff scrambling.')]
b, tf = txt(s, Inches(7.8), Inches(2.7), Inches(4.8), Inches(4.0))
for i, (n, v, bd) in enumerate(steps):
    p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
    p.line_spacing = 1.0; p.space_after = Pt(6)
    rn(p, f'{n}  ', f=FH, sz=16, b=True, c=MINT)
    rn(p, v, f=FH, sz=18, b=True, c=WHITE)
    p2 = tf.add_paragraph(); p2.line_spacing = 1.4; p2.space_after = Pt(14)
    rn(p2, bd, f=FB, sz=13, c=OW82)
foot(s, 6)
note(s, 'The screen the old materials never showed. Walk the floor view, then the three verbs.')

# 07 HOW LUCI CONNECTS
s = ns(); bg(s, NAVY_DEEP); logo(s)
kick(s, 'The LUCI solution')
tit(s, [('How LUCI ', WHITE), ('connects.', GOLD)])
fit(s, os.path.join(ASSETS, 'luci-system-architecture-flow.dark.png'), PAD, Inches(2.3), Inches(11.6), Inches(4.5))
foot(s, 7)
note(s, 'The application guide. Sources in, one rack, out to displays, signage, walls, lighting, audio. Point at the rack.')
# 08 SIX CAPABILITIES
s = ns(); bg(s, OFF_WHITE)
kick(s, 'What is included', c=MINT_DARK)
tit(s, [('Six capabilities define ', INK_STRONG), ('the platform', MINT_DARK)])
caps = ['feature-map-dashboard', 'feature-open-integration', 'feature-pin-control', 'feature-monitoring', 'feature-presets', 'feature-automation']
names = ['Map-based dashboard', 'Open integration', 'PIN-delegated control', 'Predictive monitoring and alerts', 'Presets and scheduling', 'Automation and triggers']
cw = Inches(3.6); ch = Inches(2.0); gx = Inches(0.25); gy = Inches(0.3)
x0 = PAD; y0 = Inches(2.5)
for i, (slug, nm) in enumerate(zip(caps, names)):
    col = i % 3; row = i // 3
    x = x0 + col * (cw + gx); y = y0 + row * (ch + gy)
    card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cw, ch)
    card.fill.solid(); card.fill.fore_color.rgb = OFF_WHITE
    card.line.color.rgb = RGBColor(0xDB, 0xE1, 0xE4); card.line.width = Pt(0.75); card.shadow.inherit = False
    fit(s, os.path.join(ASSETS, 'features', slug + '.jpg'), x + Inches(0.15), y + Inches(0.15), cw - Inches(0.3), Inches(1.1))
    b, tf = txt(s, x + Inches(0.2), y + Inches(1.35), cw - Inches(0.4), Inches(0.5))
    rn(tf.paragraphs[0], nm, f=FH, sz=13, b=True, c=INK_STRONG)
foot(s, 8, dark=False)
note(s, 'What is included: the six capabilities. Skim them in an executive room; talk the ledger next.')

# 09 CONSOLIDATION LEDGER
s = ns(); bg(s, NAVY_DEEP); logo(s)
kick(s, 'The LUCI value')
tit(s, [('Less hardware. Fewer vendors. ', WHITE), ('Your team in control.', GOLD)])
fit(s, os.path.join(DIAG, 'luci-consolidation-ledger.jpg'), Inches(3.5), Inches(2.3), Inches(6.3), Inches(4.5))
foot(s, 9)
note(s, 'The lightbulb. Racks of gear down to one rack. Replaces the old percentage slide. Stand on the counts already on the diagram.')

# 10 THE TEAM
s = ns(); bg(s, OFF_WHITE)
kick(s, 'The team', c=MINT_DARK)
tit(s, [('The team that builds it ', INK_STRONG), ('runs it.', MINT_DARK)])
fit(s, os.path.join(DIAG, 'embedded-operation-orbit.jpg'), PAD, Inches(2.4), Inches(11.6), Inches(4.0))
foot(s, 10, dark=False)
note(s, 'The consultative-support beat. One accountable team from design through year five. Mike can still say the director line.')

# 11 CLIENTS
s = ns(); bg(s, NAVY_DEEP); logo(s)
kick(s, 'Our clients')
tit(s, [('Running where ', WHITE), ('downtime is not an option.', GOLD)])
logos = ['client-logo-01t.png', 'client-logo-02t.png', 'client-logo-03t.png', 'client-logo-04t.png']
ly = Inches(2.7)
for i, lg in enumerate(logos):
    fit(s, os.path.join(ASSETS, lg), PAD, ly + i * Inches(0.95), Inches(11.6), Inches(0.8))
foot(s, 11)
note(s, 'The logo wall. No named clients in copy - the logos carry it. Replaces the old percentage slide visually.')

# 12 A CLEAR PATH
s = ns(); bg(s, OFF_WHITE)
kick(s, 'What happens next', c=MINT_DARK)
tit(s, [('A clear ', INK_STRONG), ('path.', MINT_DARK)])
b, tf = txt(s, PAD, Inches(2.3), Inches(4), Inches(0.4))
p = tf.paragraphs[0]
rn(p, 'PHASE 1   ', f=FH, sz=11, b=True, c=MINT_DARK, sp=220)
rn(p, 'The path to the right scope', f=FB, sz=15, c=NAVY_MUTED)
steps1 = [('Demo', 'See LUCI live on a property.'), ('Discovery', 'Create the budget.'), ('Scope', 'Onsite visit - walk the floor.'), ('Proposal', 'Refine the plan, timeline, and price.'), ('Decision', 'You approve; we mobilize.')]
b, tf = txt(s, PAD, Inches(2.9), Inches(11.6), Inches(3.5))
for i, (h, d) in enumerate(steps1):
    p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
    p.line_spacing = 1.0; p.space_after = Pt(10)
    rn(p, f'{i+1:02d}  ', f=FH, sz=15, b=True, c=MINT_DARK)
    rn(p, h, f=FH, sz=16, b=True, c=INK_STRONG)
    rn(p, '   ' + d, f=FB, sz=14, c=INK)
b, tf = txt(s, PAD, Inches(6.4), Inches(6), Inches(0.5))
p = tf.paragraphs[0]; p.line_spacing = 1.3
rn(p, 'You see the full scope ', f=FB, sz=16, b=False, c=INK)
rn(p, 'before any commitment.', f=FB, sz=16, b=True, c=MINT_DARK)
foot(s, 12, dark=False)
note(s, 'Phase 1. Demo, discovery, scope, proposal, decision. Replaces the old 25-line customer-journey slide. He can still talk purchasing and the mutual action plan.')

# 13 STRUCTURED DEPLOYMENT
s = ns(); bg(s, NAVY_DEEP); logo(s)
kick(s, 'What happens next')
tit(s, [('Then a structured ', WHITE), ('deployment.', GOLD)])
b, tf = txt(s, PAD, Inches(2.3), Inches(4), Inches(0.4))
p = tf.paragraphs[0]
rn(p, 'PHASE 2   ', f=FH, sz=11, b=True, c=MINT, sp=220)
rn(p, 'Deployment', f=FB, sz=15, c=OW82)
steps2 = [('Kickoff', 'Team, schedule, plan locked.'), ('Design review', 'Final design confirmed.'), ('Onsite prep', 'Staged and pre-configured.'), ('Onsite', 'Install and integrate.'), ('Go live', 'Live; support continues.')]
b, tf = txt(s, PAD, Inches(2.9), Inches(11.6), Inches(3.5))
for i, (h, d) in enumerate(steps2):
    p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
    p.line_spacing = 1.0; p.space_after = Pt(10)
    rn(p, f'{i+1:02d}  ', f=FH, sz=15, b=True, c=MINT)
    rn(p, h, f=FH, sz=16, b=True, c=WHITE)
    rn(p, '   ' + d, f=FB, sz=14, c=OW82)
b, tf = txt(s, PAD, Inches(6.4), Inches(6), Inches(0.5))
p = tf.paragraphs[0]; p.line_spacing = 1.3
rn(p, 'No surprises ', f=FB, sz=16, b=False, c=OW82)
rn(p, 'every step is collaborative.', f=FB, sz=16, b=True, c=MINT)
foot(s, 13)
note(s, 'Phase 2. Kickoff, design review, onsite prep, onsite, go live. The old installation-journey slide had 25 lines of logistics detail - this is the version to present.')

# 14 CLOSE
s = ns(); bg(s, NAVY_DEEP)
logo(s, Inches(2.4), Inches(0.5))
b, tf = txt(s, PAD, Inches(3.4), Inches(11.6), Inches(1.6))
p = tf.paragraphs[0]; p.line_spacing = 1.1
rn(p, 'Now let us show you LUCI ', f=FH, sz=36, b=True, c=WHITE); spc(p, -25)
rn(p, 'in action.', f=FH, sz=36, b=True, c=MINT); spc(p, -25)
b, tf = txt(s, PAD, Inches(5.6), Inches(8), Inches(0.5))
p = tf.paragraphs[0]
rn(p, 'lucisystems.com  |  info@lucisystems.com', f=FB, sz=14, c=OW82)
note(s, 'Transition to the live demo. Questions happen on the product after this slide - no Q&A card.')

out = os.path.join(HERE, 'sales-deck.pptx')
prs.save(out)
print('saved', out)
