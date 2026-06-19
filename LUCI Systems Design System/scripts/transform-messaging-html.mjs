/**
 * Post-process Word/textutil HTML → LUCI resource reader markup.
 */
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const LOGO_PNG = path.resolve(__dirname, '..', 'assets', 'logos', 'luci-full-white.png');
const LOGO = `data:image/png;base64,${fs.readFileSync(LOGO_PNG).toString('base64')}`;
const MESSAGING_CSS = 'messaging-docs.css';

/** Approved lockup — applied after Word sync so HTML stays canonical when .docx lags. */
export const CANONICAL_TAGLINE = 'The Orchestration Engine for Enterprise Multimedia';

const TAGLINE_REPLACEMENTS = [
  [/The Multimedia Orchestration Engine for Enterprise Properties/gi, CANONICAL_TAGLINE],
  [/The Smarter Platform for Enterprise Multimedia/gi, CANONICAL_TAGLINE],
];

export function applyCanonicalMessagingCopy(html) {
  let out = html;
  for (const [pattern, replacement] of TAGLINE_REPLACEMENTS) {
    out = out.replace(pattern, replacement);
  }
  return out;
}

/** Hand-maintained messaging pages (no OneDrive .docx) — included in library nav + manifest. */
export const SUPPLEMENTAL_LIBRARY_DOCS = [
  {
    id: 'luci-system-diagram',
    title: 'LUCI system diagram',
    url: '/messaging/luci-system-diagram.html',
  },
];

function formatDocNote(iso) {
  if (!iso) return '';
  return (
    'Updated ' +
    new Date(iso).toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' })
  );
}

/** Insert diagram page into library list after messaging guide. */
export function mergeLibraryDocs(docs, manifest = { docs: [] }) {
  const supplemental = SUPPLEMENTAL_LIBRARY_DOCS.map((d) => {
    const m = (manifest.docs || []).find((x) => x.id === d.id);
    return {
      id: d.id,
      title: d.title,
      url: d.url,
      note: formatDocNote(m?.htmlModified || m?.sourceModified),
    };
  });
  const out = [];
  for (const d of docs) {
    out.push(d);
    if (d.id === 'messaging-guide') out.push(...supplemental);
  }
  return out;
}

const MESSAGING_GUIDE_DIAGRAM_FIGURE = `<figure class="doc-figure doc-figure--diagram" id="the-luci-system">
<img src="diagrams/luci-system-diagram-v3.svg?v=6" alt="LUCI System — LUCI and Systems orchestrate the Standard A/V environment" width="680" height="391">
<figcaption class="doc-figure__caption"><strong>The LUCI System.</strong> LUCI + Systems orchestrate the accumulated Standard A/V environment your team already runs. <a href="luci-system-diagram.html">Full diagram page</a> (flat working canvas + source files).</figcaption>
</figure>`;

const MESSAGING_GUIDE_VOICE_ENGINE_RULE =
  '<p class="doc-prose"><b>Engine and verbs — not layers.</b></p>' +
  '<p class="doc-prose">Never use <i>layer</i> as a noun for LUCI (orchestration layer, application layer, middleware layer). Describing accumulation in the <i>client’s</i> stack is fine; naming LUCI itself a layer is not.</p>' +
  '<p class="doc-prose"><b>Leading choices:</b> <b>orchestration engine</b> (positioning, tagline) and <b>LUCI orchestrates…</b> (headlines, capability copy). Other approved verbs and nouns are fine — <i>runs, operates, integrates, consolidates, refines, platform, infrastructure</i> — when they fit the sentence better.</p>' +
  '<p class="doc-prose"><b>Watch repetition.</b> If <i>engine</i> or <i>orchestrates</i> appears more than once in a short passage (deck section, page, email), rotate to a precise alternative. Same word three times reads like a crutch, not a voice.</p>';

const MESSAGING_GUIDE_BOILERPLATE_CALLOUT =
  '<aside class="doc-callout doc-callout--key"><p class="doc-prose">LUCI Systems orchestrates every layer of technology running your property — AV, signage, building, and operational infrastructure — from a single interface your team controls from anywhere. Rather than adding layers to your stack, LUCI reduces the variables, hardware, and interfaces your team has to manage. When onsite experience and operational continuity are non-negotiable, LUCI delivers coordinated, real-time execution, end to end.</p></aside>';

const MESSAGING_GUIDE_MIDDLE = `<section class="doc-section"><h2 class="doc-chapter" id="message-pillars">MESSAGE PILLARS</h2>
<p class="doc-prose doc-prose--kicker"><i>Four pillars that anchor every communication. Each stands alone and serves any buyer.</i></p>
<ul class="doc-stack">
<li class="doc-stack__item"><p class="doc-stack__head"><span class="doc-stack__num">01</span><b>Complete visibility and control across your property</b></p><p class="doc-stack__body">One interface surfaces every endpoint, zone, and system across your property. Every team sees the same picture and acts from the same place.</p></li>
<li class="doc-stack__item"><p class="doc-stack__head"><span class="doc-stack__num">02</span><b>Align your teams by default</b></p><p class="doc-stack__body">LUCI connects every team to the same system, so your organization can stop negotiating internally and start executing towards a shared vision.</p></li>
<li class="doc-stack__item"><p class="doc-stack__head"><span class="doc-stack__num">03</span><b>Fully activate the guest experience</b></p><p class="doc-stack__body">Turn passive screens into purposeful moments by planning, programming, and responding to guest signals in real time — turning your A/V infrastructure into a strategic tool for revenue, retention, and brand.</p></li>
<li class="doc-stack__item"><p class="doc-stack__head"><span class="doc-stack__num">04</span><b>Invest in the only A/V that gets more valuable over time</b></p><p class="doc-stack__body">Traditional A/V depreciates and expires. LUCI doesn't. We refine our software, integrations, and operational capability on a predictable annual line item so Year Five is more capable than Year One.</p></li>
</ul>
</section><section class="doc-section"><h2 class="doc-chapter" id="the-systems">THE SYSTEMS</h2>
<p class="doc-prose doc-prose--kicker"><i>Six named services. Together, they are the embedded organization that makes the platform work — and keep working — in the real world.</i></p>
<ul class="doc-stack">
<li class="doc-stack__item"><p class="doc-stack__head"><span class="doc-stack__num">01</span><b>LUCI FDE — Forward-Deployed Engineering</b></p><p class="doc-stack__body">Full-stack engineers who embed inside the client's environment — from scoping through continuous refinement. A LUCI FDE is not a consultant, a solutions architect, or a support representative. They work inside the client's environment, build production systems that hold up under real operational conditions, and remain accountable for those systems long after deployment.</p><p class="doc-stack__note">Delivers: one accountable team across the full lifecycle. The engineer who walks the property on day one is the engineer who supports it in year five. LUCI Systems does not hand off engagements.</p></li>
<li class="doc-stack__item"><p class="doc-stack__head"><span class="doc-stack__num">02</span><b>Design &amp; Deployment</b></p><p class="doc-stack__body">In-person scoping, architecture, and standing-up of the platform — by the team that will stay. The FDE team maps the existing environment across IT, AV, operations, marketing, and finance; designs the target architecture against the LUCI standard; consolidates the infrastructure; and stands up the platform, phased so value lands before the full build is finished.</p><p class="doc-stack__note">Delivers: a deployment scoped to the property's reality, executed by the people who will own it — not subcontracted, not handed off.</p></li>
<li class="doc-stack__item"><p class="doc-stack__head"><span class="doc-stack__num">03</span><b>Owner's-Rep Partnership</b></p><p class="doc-stack__body">A standing extension of the client's enterprise — strategic, embedded, accountable. LUCI Systems functions as the client's in-house technology leadership for the guest-facing environment: planning multi-year roadmaps, owning vendor relationships, advising on capital strategy, and representing the property's interests in every technical decision.</p><p class="doc-stack__note">Delivers: senior technology leadership the property doesn't have to build, staff, or replace — present continuously, accountable to the property's goals.</p></li>
<li class="doc-stack__item"><p class="doc-stack__head"><span class="doc-stack__num">04</span><b>Training &amp; Enablement</b></p><p class="doc-stack__body">A standardized curriculum that makes the client's team fluent in LUCI. Training is not an afterthought or a PDF — it is a structured program: role-based instruction, hands-on enablement, and documentation that lives inside the platform. New staff onboard against the same standard; institutional knowledge survives turnover.</p><p class="doc-stack__note">Delivers: a team that runs the platform with confidence, and a property that doesn't lose capability when a key person leaves.</p></li>
<li class="doc-stack__item"><p class="doc-stack__head"><span class="doc-stack__num">05</span><b>Support &amp; Operations</b></p><p class="doc-stack__body">The backbone — the process starts and ends with support. The same FDE team that designed and deployed the platform is the team that answers when something needs attention. No tiered queue. No establishing which vendor owns the incident. One team owns the diagnosis and the resolution, on the property's schedule — including the off-hours when it matters most.</p><p class="doc-stack__note">Delivers: one accountable owner, faster resolution because context is never rebuilt, coverage that matches a property that never closes, and incentives aligned with uptime rather than ticket volume.</p></li>
<li class="doc-stack__item"><p class="doc-stack__head"><span class="doc-stack__num">06</span><b>Continuous Refinement</b></p><p class="doc-stack__body">The discipline that makes the platform appreciate, year over year. Every incident and operational pattern the Systems encounter becomes an input to the next platform release. Problems aren't just fixed at one property — they are engineered out of the platform so no property meets them again. Annually, the embedded team revisits the roadmap: integrations extend, automation sharpens, the standard gets tighter.</p><p class="doc-stack__note">Delivers: a platform that is more capable in year five than the day it was deployed, on the same line item — and a property that inherits every improvement without a migration.</p></li>
</ul>
</section><section class="doc-section"><h2 class="doc-chapter" id="our-four-commitments">OUR FOUR COMMITMENTS</h2>
<ul class="doc-stack">
<li class="doc-stack__item"><p class="doc-stack__head"><span class="doc-stack__num">01</span><b>Support begins before deployment.</b></p><p class="doc-stack__body">Every LUCI engagement starts with the FDE team embedded in the property. Support begins on day one.</p></li>
<li class="doc-stack__item"><p class="doc-stack__head"><span class="doc-stack__num">02</span><b>The team that builds your system is the team that supports it.</b></p><p class="doc-stack__body">The engineer who walks the property on day one is the engineer who answers the call in year five.</p></li>
<li class="doc-stack__item"><p class="doc-stack__head"><span class="doc-stack__num">03</span><b>One team owns every incident, end to end.</b></p><p class="doc-stack__body">There is no ticket queue, no escalation path, no third party. LUCI owns diagnosis and resolution.</p></li>
<li class="doc-stack__item"><p class="doc-stack__head"><span class="doc-stack__num">04</span><b>The platform gets more capable every day.</b></p><p class="doc-stack__body">Continuous refinement means every release, every engagement, every year adds capability.</p></li>
</ul>
</section>`;

const MESSAGING_GUIDE_WHO_HEARS = `<section class="doc-section"><h2 class="doc-chapter" id="who-hears-what">WHO HEARS WHAT</h2>
<p class="doc-prose doc-prose--kicker"><i>Lead with the pillar most relevant to the person in the room.</i></p>
<ul class="doc-rows">
<li><span class="doc-rows__label">CEO / GM</span><span class="doc-rows__value"><p class="doc-prose"><b>Pillars 01 + 03</b></p><p class="doc-prose">Full property visibility, guest experience as a strategic output.</p></span></li>
<li><span class="doc-rows__label">CIO / IT Director</span><span class="doc-rows__value"><p class="doc-prose"><b>Pillars 01 + 04</b></p><p class="doc-prose">Standard infrastructure, open APIs, no proprietary hardware to manage or refresh.</p></span></li>
<li><span class="doc-rows__label">CFO</span><span class="doc-rows__value"><p class="doc-prose"><b>Pillar 04</b></p><p class="doc-prose">Predictable annual line item, no refresh cycles, investment that compounds over time.</p></span></li>
<li><span class="doc-rows__label">CMO / Marketing Director</span><span class="doc-rows__value"><p class="doc-prose"><b>Pillar 03</b></p><p class="doc-prose">Real-time programmability across every zone, screen, and guest moment.</p></span></li>
</ul>
</section>`;

const MESSAGING_GUIDE_TOC =
  '<nav aria-label="On this page"><ul class="resource__toc">' +
  '<li><a href="#how-to-use-this-document">HOW TO USE THIS DOCUMENT</a></li>' +
  '<li><a href="#tagline">TAGLINE</a></li>' +
  '<li><a href="#the-luci-worldview">THE LUCI WORLDVIEW</a></li>' +
  '<li><a href="#the-offering">THE OFFERING</a></li>' +
  '<li><a class="is-sub" href="#the-luci-system">THE LUCI SYSTEM</a></li>' +
  '<li><a href="#message-pillars">MESSAGE PILLARS</a></li>' +
  '<li><a href="#the-systems">THE SYSTEMS</a></li>' +
  '<li><a href="#our-four-commitments">OUR FOUR COMMITMENTS</a></li>' +
  '<li><a href="#who-hears-what">WHO HEARS WHAT</a></li>' +
  '<li><a href="#key-features">KEY FEATURES</a></li>' +
  '<li><a href="#what-luci-is-and-isnt">WHAT LUCI IS AND ISN’T</a></li>' +
  '</ul></nav>';

/** Canonical structure — re-applied after each Word sync of messaging-guide. */
export function applyMessagingGuideEnhancements(bodyHtml, tocHtml) {
  let body = bodyHtml;

  body = body.replace(/<p class="doc-prose"><i><\/i><br><\/p>/g, '');
  body = body.replace(/<p class="doc-prose"><b><\/b><br><\/p>/g, '');

  if (!body.includes('id="the-luci-system"')) {
    const offeringIntro =
      /<p class="doc-prose">LUCI Systems is two forces in one:[\s\S]*?<\/p>(\s*)(?=<ul class="doc-rows">)/;
    if (offeringIntro.test(body)) {
      body = body.replace(offeringIntro, (m) => `${m}\n\n${MESSAGING_GUIDE_DIAGRAM_FIGURE}\n\n`);
    }
  }

  body = body.replace(
    /<\/ul>[\s\S]*?<\/section><section class="doc-section"><h2 class="doc-chapter" id="the-offering">THE OFFERING<\/h2>[\s\S]*?<ul class="doc-rows">[\s\S]*?<\/ul>[\s\S]*?(?=<\/section><section class="doc-section"><h2 class="doc-chapter" id="message-pillars">)/,
    (m) => m.replace(/<p class="doc-prose"><b>Our four commitments<\/b><\/p>[\s\S]*?(?=<\/section><section class="doc-section"><h2 class="doc-chapter" id="message-pillars">)/, '')
  );

  const offeringCommitments =
    /(<ul class="doc-rows">[\s\S]*?<\/ul>)(\s*)(<p class="doc-prose"><b>Our four commitments<\/b><\/p>[\s\S]*?)(<\/section><section class="doc-section"><h2 class="doc-chapter" id="message-pillars">)/;
  if (offeringCommitments.test(body)) {
    body = body.replace(offeringCommitments, '$1$2$4');
  }

  body = body.replace(
    /<section class="doc-section"><h2 class="doc-chapter" id="message-pillars">[\s\S]*?<\/section><section class="doc-section"><h2 class="doc-chapter" id="who-hears-what">[\s\S]*?<\/section>/,
    MESSAGING_GUIDE_MIDDLE + MESSAGING_GUIDE_WHO_HEARS
  );

  body = applyMessagingGuideVoicePatches(body);

  return { bodyHtml: body, tocHtml: MESSAGING_GUIDE_TOC };
}

/** Voice + approved-language patches — re-applied after Word sync. */
function applyMessagingGuideVoicePatches(body) {
  let out = body;

  if (out.includes('id="the-luci-system"')) {
    out = out.replace(
      /<figure class="doc-figure doc-figure--diagram" id="the-luci-system">[\s\S]*?<\/figure>/,
      MESSAGING_GUIDE_DIAGRAM_FIGURE
    );
  }

  out = out.replace(
    /<aside class="doc-callout doc-callout--key"><p class="doc-prose">LUCI Systems orchestrates[\s\S]*?<\/aside>/,
    MESSAGING_GUIDE_BOILERPLATE_CALLOUT
  );

  if (!out.includes('Watch repetition')) {
    out = out.replace(
      /<p class="doc-prose"><b>Engine and verbs — not layers\.<\/b><\/p>[\s\S]*?(?=<p class="doc-prose"><b>Declarative over promotional\.<\/b><\/p>)/,
      `${MESSAGING_GUIDE_VOICE_ENGINE_RULE}\n`
    );
    if (!out.includes('Watch repetition')) {
      out = out.replace(
        /<p class="doc-prose"><b>Institutions, not adjectives\.<\/b><\/p>/,
        `${MESSAGING_GUIDE_VOICE_ENGINE_RULE}\n<p class="doc-prose"><b>Institutions, not adjectives.</b></p>`
      );
    }
  }

  out = out.replace(
    /<li class="li32">Infrastructure, platform, operating system, operating layer<\/li>/,
    '<li class="li32">Orchestration engine, platform, infrastructure</li>\n          <li class="li32">LUCI orchestrates, runs, operates, integrates, consolidates, refines</li>'
  );

  if (!out.includes('Layer — when naming LUCI')) {
    out = out.replace(
      /<li class="li34">Named clients in public materials<\/li>/,
      '<li class="li34">Layer — when naming LUCI (orchestration layer, application layer, “one layer for…”). Use engine or “LUCI orchestrates…” instead</li>\n          <li class="li34">Named clients in public materials</li>'
    );
  }

  return out;
}

export function stripTags(html) {
  return html.replace(/<[^>]+>/g, '');
}

export function textFromHtml(fragment) {
  return stripTags(fragment)
    .replace(/\u00a0/g, ' ')
    .replace(/\s+/g, ' ')
    .trim();
}

export function slugify(text) {
  return text
    .toLowerCase()
    .replace(/[^\w\s-]/g, '')
    .replace(/\s+/g, '-')
    .replace(/-+/g, '-')
    .replace(/^-|-$/g, '')
    .slice(0, 64);
}

function cleanAppleSpaces(html) {
  return html
    .replace(/<span class="Apple-converted-space">\s*<\/span>/gi, ' ')
    .replace(/\u00a0/g, ' ');
}

function removeEmptyParagraphs(html) {
  return html
    .replace(/<p class="p1">[\s\S]*?<\/p>/gi, '')
    .replace(/<p class="p4"><br><\/p>/gi, '')
    .replace(/<p class="p8"><br><\/p>/gi, '')
    .replace(/<p class="p10"><br><\/p>/gi, '')
    .replace(/<p class="p12"><i><\/i><br><\/p>/gi, '')
    .replace(/<p class="p17"><br><\/p>/gi, '')
    .replace(/<p class="p18"><br><\/p>/gi, '')
    .replace(/<p class="p23"><br><\/p>/gi, '');
}

function removeContentsBlock(html) {
  return html.replace(
    /<p class="p5"><b>CONTENTS<\/b><\/p>[\s\S]*?(?=<p class="p5"><b>)/i,
    ''
  );
}

function extractTitleDeck(html) {
  let title = 'Document';
  let deck = '';
  let rest = html;

  const titleM = rest.match(/<p class="p2"><b>([\s\S]*?)<\/b><\/p>/i);
  if (titleM) {
    title = textFromHtml(titleM[1]);
    rest = rest.replace(titleM[0], '');
  }

  const deckM = rest.match(/<p class="p3">([\s\S]*?)<\/p>/i);
  if (deckM) {
    deck = textFromHtml(deckM[1]);
    rest = rest.replace(deckM[0], '');
  }

  return { title, deck, body: rest.trim() };
}

function isNumberedSection(text) {
  return /^\d+\s*[—–-]/.test(text);
}

function isChapterLabel(text) {
  const t = text.trim();
  if (isNumberedSection(t)) return false;
  if (/^CONTENTS$/i.test(t)) return false;
  return t.length > 0 && t.length < 80 && t === t.toUpperCase() && /[A-Z]/.test(t);
}

function collectSections(body) {
  const sections = [];
  const re = /<p class="p5"><b>([\s\S]*?)<\/b><\/p>/gi;
  let m;
  while ((m = re.exec(body)) !== null) {
    const text = textFromHtml(m[1]);
    if (/^CONTENTS$/i.test(text)) continue;
    const numbered = isNumberedSection(text);
    const chapter = !numbered && isChapterLabel(text);
    if (!numbered && !chapter) continue;
    const base = numbered ? text.replace(/^\d+\s*[—–-]\s*/i, '').trim() : text;
    const id = slugify((numbered ? text.match(/^(\d+)/)?.[1] + '-' : '') + base);
    sections.push({ text, id, numbered, chapter });
  }
  return sections;
}

function transformParagraphs(html) {
  let out = html;
  out = out.replace(/<p class="p13"><b>([\s\S]*?)<\/b><\/p>/gi, '<h3 class="doc-subsection__title">$1</h3>');
  out = out.replace(/<p class="p5"><b>([\s\S]*?)<\/b><\/p>/gi, (_, inner) => {
    const text = textFromHtml(inner);
    if (/^CONTENTS$/i.test(text)) return '';
    if (isNumberedSection(text)) {
      const id = slugify(text);
      return `<h2 class="doc-section__title" id="${id}">${inner}</h2>`;
    }
    if (isChapterLabel(text)) {
      const id = slugify(text);
      return `<h2 class="doc-chapter" id="${id}">${inner}</h2>`;
    }
    return `<p class="doc-prose"><b>${inner}</b></p>`;
  });
  const proseClasses = ['p9', 'p11', 'p15', 'p16', 'p19', 'p20', 'p21', 'p25', 'p26', 'p27', 'p28'];
  for (const cls of proseClasses) {
    out = out.replace(new RegExp(`<p class="${cls}">`, 'gi'), '<p class="doc-prose">');
  }
  out = out.replace(/<p class="p[^"]*">/gi, (tag) =>
    tag.includes('doc-') ? tag : '<p class="doc-prose">'
  );
  out = out.replace(/<p class="doc-prose">\s*<br\s*\/?>\s*<\/p>/gi, '');
  out = out.replace(/<ul class="doc-rows"><\/ul>/gi, '');
  out = out.replace(/<ul class="ul\d*">/gi, '<ul class="doc-list">');
  out = out.replace(/<ol class="ol\d*">/gi, '<ol class="doc-list doc-list--ordered">');
  return out;
}

function tableCellText(tdHtml) {
  return textFromHtml(tdHtml);
}

function normalizeCellHtml(cell) {
  return cell.replace(/<p class="[^"]*">/gi, '<p class="doc-prose">').trim();
}

function isPersonaTable(tableHtml) {
  return /<p class="p7"><b>/i.test(tableHtml);
}

function extractPersonaBlockLabel(cellHtml) {
  const m = cellHtml.match(/<p class="p9"><b>([\s\S]*?)<\/b>/i);
  return m ? textFromHtml(m[1]) : '';
}

function normalizePersonaCellBody(cellHtml) {
  let inner = cellHtml.replace(/<p class="p9"><b>[\s\S]*?<\/b><\/p>/gi, '');
  inner = inner.replace(/<ul class="ul\d*">/gi, '<ul class="doc-list">');
  inner = inner.replace(/<li class="li\d+">/gi, '<li>');
  inner = inner.replace(/<p class="p11">/gi, '<p class="doc-prose">');
  inner = inner.replace(/<p class="p12">/gi, '<p class="doc-persona__message-kicker">');
  inner = inner.replace(/<p class="p13">/gi, '<p class="doc-persona__quote">');
  return inner.trim();
}

function transformPersonaTable(table) {
  const rows = [...table.matchAll(/<tr>([\s\S]*?)<\/tr>/gi)].map((m) => m[1]);
  let head = '';
  let body = '';
  let message = '';

  for (const row of rows) {
    const cells = [...row.matchAll(/<td[^>]*>([\s\S]*?)<\/td>/gi)].map((m) => m[1]);
    if (cells.length === 1) {
      const cell = cells[0];
      if (/<p class="p7"><b>/i.test(cell)) {
        const titleM = cell.match(/<p class="p7"><b>([\s\S]*?)<\/b>/i);
        const roleM = cell.match(/<p class="p8"><i>([\s\S]*?)<\/i>/i);
        const titleText = titleM ? textFromHtml(titleM[1]) : 'Persona';
        const id = slugify(titleText);
        head =
          `<header class="doc-persona__head"><h2 class="doc-persona__title" id="${id}">` +
          (titleM ? titleM[1] : titleText) +
          '</h2>';
        if (roleM) head += `<p class="doc-persona__role">${roleM[1]}</p>`;
        head += '</header>';
      } else if (/MESSAGE THAT LANDS/i.test(cell)) {
        message = `<div class="doc-persona__message">${normalizePersonaCellBody(cell)}</div>`;
      }
    } else if (cells.length === 2) {
      body += '<div class="doc-persona__pair">';
      for (const cell of cells) {
        const label = extractPersonaBlockLabel(cell);
        const inner = normalizePersonaCellBody(cell);
        body +=
          `<section class="doc-persona__block"><h3 class="doc-persona__label">${label}</h3>${inner}</section>`;
      }
      body += '</div>';
    }
  }

  return `<article class="doc-persona">${head}${body}${message}</article>`;
}

function collectPersonaSections(html) {
  const sections = [];
  const re = /<h2 class="doc-persona__title" id="([^"]+)">([\s\S]*?)<\/h2>/gi;
  let m;
  while ((m = re.exec(html)) !== null) {
    sections.push({
      text: textFromHtml(m[2]),
      id: m[1],
      numbered: false,
      chapter: false,
    });
  }
  return sections;
}

function transformTables(html) {
  return html.replace(/<table[\s\S]*?<\/table>/gi, (table) => {
    if (isPersonaTable(table)) return transformPersonaTable(table);

    const rows = [...table.matchAll(/<tr>([\s\S]*?)<\/tr>/gi)].map((m) => m[1]);
    if (!rows.length) return '';

    const parsed = rows.map((row) => {
      const cells = [...row.matchAll(/<td[^>]*>([\s\S]*?)<\/td>/gi)].map((m) => m[1]);
      return cells;
    });

    if (parsed.every((row) => row.length === 1)) {
      return parsed
        .map((row) => {
          const inner = normalizeCellHtml(row[0]);
          const isKey = textFromHtml(row[0]).length > 80;
          const cls = isKey ? 'doc-callout doc-callout--key' : 'doc-callout';
          return `<aside class="${cls}">${inner}</aside>`;
        })
        .join('\n');
    }

    if (parsed.length === 1 && parsed[0].length === 1) {
      const cell = parsed[0][0];
      const inner = cell.replace(/<p class="[^"]*">/gi, '<p>').trim();
      const plain = textFromHtml(cell);
      const isKey = plain.length > 120 && /<b>0\d/i.test(cell);
      const cls = isKey ? 'doc-callout doc-callout--key' : 'doc-callout';
      return `<aside class="${cls}">${inner}</aside>`;
    }

    if (parsed.length === 1 && parsed[0].length === 2) {
      const left = parsed[0][0];
      const right = parsed[0][1];
      return (
        '<div class="doc-compare">' +
        `<div class="doc-compare__col">${left.replace(/<p class="[^"]*">/gi, '<p class="doc-prose">')}</div>` +
        `<div class="doc-compare__col">${right.replace(/<p class="[^"]*">/gi, '<p class="doc-prose">')}</div>` +
        '</div>'
      );
    }

    const headerRow = parsed[0];
    const hasHeader =
      headerRow.length >= 2 &&
      headerRow.every((c) => /<b>/i.test(c) && textFromHtml(c).length < 60);

    const dataRows = hasHeader ? parsed.slice(1) : parsed;

    const items = [];
    for (const cells of dataRows) {
      if (cells.length < 2) continue;
      const label = textFromHtml(cells[0]);
      const valueHtml = normalizeCellHtml(cells[1]);
      if (!label && !textFromHtml(cells[1])) continue;
      items.push(
        '<li><span class="doc-rows__label">' +
        label +
        '</span><span class="doc-rows__value">' +
        valueHtml +
        '</span></li>'
      );
    }
    if (!items.length) return '';
    return '<ul class="doc-rows">' + items.join('') + '</ul>';
  });
}

function wrapSections(html, sections) {
  if (!sections.length) return html;

  const parts = [];
  let cursor = 0;
  const markers = [...html.matchAll(/<h2 class="doc-(?:section__title|chapter)" id="([^"]+)">/gi)];

  if (!markers.length) return html;

  for (let i = 0; i < markers.length; i++) {
    const start = markers[i].index;
    const end = i + 1 < markers.length ? markers[i + 1].index : html.length;
    if (i === 0 && start > 0) {
      parts.push(html.slice(0, start));
    }
    const chunk = html.slice(start, end);
    parts.push(`<section class="doc-section">${chunk}</section>`);
    cursor = end;
  }
  if (cursor < html.length) parts.push(html.slice(cursor));
  return parts.join('');
}

function buildTocFromArticle(html, sections) {
  if (!sections.length) return '';
  let nav = '<nav aria-label="On this page"><ul class="resource__toc">';
  for (const s of sections) {
    nav += `<li><a href="#${s.id}">${s.text}</a></li>`;
    const sectionSlice = html.includes(`id="${s.id}"`)
      ? html.split(`id="${s.id}"`)[1]?.split(/<h2 class="doc-/)[0] || ''
      : '';
    const subRe = /<h3 class="doc-subsection__title" id="([^"]+)">([\s\S]*?)<\/h3>/gi;
    let sm;
    while ((sm = subRe.exec(sectionSlice)) !== null) {
      nav += `<li><a class="is-sub" href="#${sm[1]}">${textFromHtml(sm[2])}</a></li>`;
    }
  }
  nav += '</ul></nav>';
  return nav;
}

export function transformMessagingBody(rawBody) {
  let html = cleanAppleSpaces(rawBody);
  html = removeEmptyParagraphs(html);
  html = removeContentsBlock(html);

  const { title, deck, body } = extractTitleDeck(html);
  const sections = collectSections(body);

  html = transformTables(body);
  const allSections = [...sections, ...collectPersonaSections(html)];
  html = transformParagraphs(html);
  html = wrapSections(html, sections);

  html = html.replace(/<h3 class="doc-subsection__title">([\s\S]*?)<\/h3>/gi, (_, inner) => {
    const text = textFromHtml(inner);
    const id = slugify(text);
    return `<h3 class="doc-subsection__title" id="${id}">${inner}</h3>`;
  });

  const tocHtml = buildTocFromArticle(html, allSections);

  return { title, deck, bodyHtml: applyCanonicalMessagingCopy(html), tocHtml, sections };
}

export function buildLibraryNav(docs, currentId) {
  if (!docs?.length) return '';
  let html = '<ul class="resource__library">';
  for (const d of docs) {
    const href = d.url || `${d.id}.html`;
    const linkHref = href.replace(/^\//, '').replace(/^messaging\//, '');
    const cls = d.id === currentId ? ' class="is-current"' : '';
    html += `<li><a href="${linkHref}"${cls}>${d.title}</a>`;
    if (d.note) html += `<span>${d.note}</span>`;
    html += '</li>';
  }
  html += '</ul>';
  return html;
}

export function buildResourcePage({
  docId,
  title,
  deck,
  bodyHtml,
  tocHtml,
  libraryDocs,
  updatedIso,
}) {
  bodyHtml = applyCanonicalMessagingCopy(bodyHtml);
  const updatedLabel = new Date(updatedIso).toLocaleString('en-US', {
    month: 'short',
    day: 'numeric',
    year: 'numeric',
    hour: 'numeric',
    minute: '2-digit',
  });
  const library = buildLibraryNav(libraryDocs, docId);
  const pageTitle = title.includes('LUCI') ? title : `${title} · LUCI`;

  return `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="robots" content="noindex, nofollow">
  <title>${pageTitle}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Syncopate:wght@700&family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="${MESSAGING_CSS}">
</head>
<body>
  <div class="resource">
    <header class="resource__masthead">
      <div class="resource__masthead-row">
        <a href="https://lucisystems.com" class="resource__logo"><img src="${LOGO}" alt="LUCI Systems" width="120" height="24"></a>
        <span class="resource__badge">Brand resources</span>
      </div>
      <h1 class="resource__hero-title">${title}</h1>
      ${deck ? `<p class="resource__hero-deck">${deck}</p>` : ''}
      <p class="resource__meta">Synced ${updatedLabel}</p>
      <nav class="resource__crumbs" aria-label="Breadcrumb">
        <a href="../index.html">Review queue</a>
        <span>/</span>
        <span aria-current="page">${title}</span>
      </nav>
    </header>
    <div class="resource__layout">
      <aside class="resource__sidebar">
        <p class="resource__nav-kicker">Library</p>
        ${library}
        ${tocHtml ? `<p class="resource__nav-kicker">On this page</p>${tocHtml}` : ''}
      </aside>
      <main class="resource__article">
        ${bodyHtml}
      </main>
    </div>
  </div>
</body>
</html>
`;
}

export function extractStoredBody(html) {
  const article = html.match(/<main class="resource__article">([\s\S]*)<\/main>/i);
  if (article) return article[1].trim();
  const legacy = html.match(/<div class="doc__body">([\s\S]*)<\/div>/i);
  if (legacy) return legacy[1].trim();
  const body = html.match(/<body[^>]*>([\s\S]*)<\/body>/i);
  return body ? body[1].trim() : html;
}

export function buildMessagingIndex(docs) {
  const cards = (docs || [])
    .map(
      (d) =>
        `<li><a href="${d.url}"><strong>${d.title}</strong><span>${
          d.note || 'Canonical messaging document'
        }</span></a></li>`
    )
    .join('\n');

  return `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="robots" content="noindex, nofollow">
  <title>Messaging &amp; philosophy · LUCI</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Syncopate:wght@700&family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/messaging/messaging-docs.css">
</head>
<body>
  <div class="resource">
    <header class="resource__masthead">
      <div class="resource__masthead-row">
        <a href="https://lucisystems.com" class="resource__logo"><img src="${LOGO}" alt="LUCI Systems" width="120" height="24"></a>
        <span class="resource__badge">Brand resources</span>
      </div>
      <h1 class="resource__hero-title">Messaging &amp; philosophy</h1>
      <p class="resource__hero-deck">Canonical brand docs — synced from OneDrive and published on the review hub.</p>
      <nav class="resource__crumbs" aria-label="Breadcrumb">
        <a href="/">Review queue</a>
        <span>/</span>
        <span aria-current="page">Messaging library</span>
      </nav>
    </header>
    <div class="resource__layout">
      <aside class="resource__sidebar">
        <p class="resource__nav-kicker">Documents</p>
        <ul class="resource__library">
          ${cards}
        </ul>
      </aside>
      <main class="resource__article">
        <p class="doc-lead">Open a document from the library. These pages update when Word sources change and the site is rebuilt.</p>
        <section class="doc-section">
          <h2 class="doc-section__title">What lives here</h2>
          <p class="doc-prose">Brand philosophy, messaging guide, and personas — the finalized references for copy, positioning, and stakeholder review.</p>
        </section>
      </main>
    </div>
  </div>
</body>
</html>
`;
}

const isMain =
  process.argv[1] && fileURLToPath(import.meta.url) === path.resolve(process.argv[1]);

if (isMain) {
  const root = path.resolve(path.join(path.dirname(fileURLToPath(import.meta.url)), '..'));
  const messagingDir = path.join(root, 'ui_kits', 'review', 'messaging');
  const sourcesPath = path.join(root, 'ui_kits', 'review', 'messaging-sources.json');
  const manifestPath = path.join(root, 'ui_kits', 'review', 'messaging-manifest.json');

  const config = JSON.parse(fs.readFileSync(sourcesPath, 'utf8'));
  let manifest = { updated: new Date().toISOString().slice(0, 10), docs: [] };
  if (fs.existsSync(manifestPath)) {
    manifest = JSON.parse(fs.readFileSync(manifestPath, 'utf8'));
  }

  const libraryDocs = (config.docs || []).map((d) => {
    const m = (manifest.docs || []).find((x) => x.id === d.id);
    return {
      id: d.id,
      title: d.title,
      url: `/messaging/${d.id}.html`,
      note: m?.sourceModified
        ? 'Updated ' +
          new Date(m.sourceModified).toLocaleDateString('en-US', {
            month: 'short',
            day: 'numeric',
            year: 'numeric',
          })
        : '',
    };
  });

  for (const doc of config.docs || []) {
    const dest = path.join(messagingDir, `${doc.id}.html`);
    if (!fs.existsSync(dest)) {
      console.warn('Skip (missing):', dest);
      continue;
    }
    const rawFile = fs.readFileSync(dest, 'utf8');
    const stored = extractStoredBody(rawFile);
    const isLegacy = /<p class="p2">/i.test(stored);
    const updated =
      manifest.docs?.find((x) => x.id === doc.id)?.htmlModified || new Date().toISOString();

    if (isLegacy) {
      const { title, deck, bodyHtml, tocHtml } = transformMessagingBody(stored);
      const page = buildResourcePage({
        docId: doc.id,
        title,
        deck,
        bodyHtml,
        tocHtml,
        libraryDocs,
        updatedIso: updated,
      });
      fs.writeFileSync(dest, page);
      console.log('Transformed:', doc.id);
    } else {
      const page = buildResourcePage({
        docId: doc.id,
        title: doc.title,
        deck: '',
        bodyHtml: stored,
        tocHtml: '',
        libraryDocs,
        updatedIso: updated,
      });
      fs.writeFileSync(dest, page);
      console.log('Re-wrapped:', doc.id);
    }
  }

  fs.writeFileSync(path.join(messagingDir, 'index.html'), buildMessagingIndex(libraryDocs));
  console.log('Wrote messaging/index.html');
}
