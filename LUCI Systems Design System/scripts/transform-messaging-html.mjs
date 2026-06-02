/**
 * Post-process Word/textutil HTML → LUCI resource reader markup.
 */
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const LOGO = '../assets/logos/luci-full-white.png';
const MESSAGING_CSS = 'messaging-docs.css';

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

function transformTables(html) {
  return html.replace(/<table[\s\S]*?<\/table>/gi, (table) => {
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
  html = transformParagraphs(html);
  html = wrapSections(html, sections);

  html = html.replace(/<h3 class="doc-subsection__title">([\s\S]*?)<\/h3>/gi, (_, inner) => {
    const text = textFromHtml(inner);
    const id = slugify(text);
    return `<h3 class="doc-subsection__title" id="${id}">${inner}</h3>`;
  });

  const tocHtml = buildTocFromArticle(html, sections);

  return { title, deck, bodyHtml: html, tocHtml, sections };
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
