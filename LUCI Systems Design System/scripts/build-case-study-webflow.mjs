#!/usr/bin/env node
/**
 * Build Webflow embed files from ui_kits/case-studies/ameristar-council-bluffs.html
 * Scopes CSS under .luci-cs so Webflow site styles don't override the case study.
 */
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(__dirname, '..', 'ui_kits', 'case-studies');
const srcPath = path.join(root, 'ameristar-council-bluffs.html');

const DEMO_URL = 'https://www.lucisystems.com/#request-a-demo';
const PDF_URL = 'https://cdn.prod.website-files.com/62d7d68d14611c2a31d863cd/6a2c4a48af310cd38d35d17a_CS-Ameristar-Council-Bluffs-Final.pdf';
const LINK_NEW_TAB = ' target="_blank" rel="noopener noreferrer"';

const WEBFLOW_RESET = `
    /* Webflow embed: break out of page container + beat site styles */
    .luci-cs {
      width: 100vw;
      max-width: 100vw;
      margin-left: calc(50% - 50vw);
      margin-right: calc(50% - 50vw);
      position: relative;
      font-family: var(--body);
      background: var(--navy-deep);
      color: var(--body-ink);
      -webkit-font-smoothing: antialiased;
      font-size: 18px;
      line-height: 1.72;
    }

    .luci-cs *,
    .luci-cs *::before,
    .luci-cs *::after {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    .w-embed .luci-cs,
    .w-embed .luci-cs * {
      box-sizing: border-box;
    }

    .luci-cs img {
      max-width: none;
    }

    .luci-cs a {
      text-decoration: none;
    }

    .luci-cs blockquote {
      border: none;
      margin: 0;
      padding: 0;
    }

    .luci-cs ul,
    .luci-cs ol {
      list-style: none;
    }

    /* About LUCI — editorial block inside CTA, not a second footer */
    .luci-cs .cta__about {
      margin-top: 48px;
      padding-top: 32px;
      border-top: 1px solid rgba(255, 255, 255, 0.12);
      max-width: 62ch;
    }

    .luci-cs .cta__about-label {
      color: var(--mint);
      margin-bottom: 12px;
    }

    .luci-cs .cta__statement {
      color: rgba(235, 245, 248, 0.82);
      font-size: 17px;
      line-height: 1.65;
    }

    /* Footer bar only — no copyright row on Webflow */
    .luci-cs .footer__top {
      margin-bottom: 0;
      padding-bottom: 0;
      border-bottom: none;
    }
`;

function stripCssComments(css) {
  return css.replace(/\/\*[\s\S]*?\*\//g, '');
}

function prefixSelectorList(selectors) {
  return selectors
    .split(',')
    .map((sel) => {
      sel = sel.trim();
      if (!sel || sel.startsWith('.luci-cs')) return sel;
      return `.luci-cs ${sel}`;
    })
    .join(', ');
}

function scopeCss(raw) {
  const css = stripCssComments(raw)
    .replace(/\s*html\s*\{[^}]*\}/, '')
    .replace(/\s*body\s*\{[^}]*\}/, '')
    .replace(/\*, \*::before, \*::after \{[^}]*\}/, '');

  const out = [];
  let i = 0;

  while (i < css.length) {
    while (i < css.length && /\s/.test(css[i])) i++;
    if (i >= css.length) break;

    if (css[i] === '@') {
      const headerEnd = css.indexOf('{', i);
      const atRule = css.slice(i, headerEnd + 1);
      i = headerEnd + 1;
      let depth = 1;
      let inner = '';
      while (i < css.length && depth > 0) {
        const ch = css[i++];
        if (ch === '{') depth++;
        else if (ch === '}') depth--;
        if (depth > 0) inner += ch;
      }
      out.push(atRule + scopeCss(inner) + '}');
      continue;
    }

    const brace = css.indexOf('{', i);
    if (brace === -1) break;
    const selectors = css.slice(i, brace).trim();
    i = brace + 1;
    let depth = 1;
    let body = '';
    while (i < css.length && depth > 0) {
      const ch = css[i++];
      if (ch === '{') depth++;
      else if (ch === '}') depth--;
      if (depth > 0) body += ch;
    }

    if (selectors.startsWith(':root')) {
      out.push(`:root {${body}}`);
    } else {
      out.push(`${prefixSelectorList(selectors)} {${body}}`);
    }
  }

  return out.join('\n\n');
}

function replaceAssets(html) {
  return html
    .replace(/\.\.\/\.\.\/assets\/logos\/luci-full-white\.png/g, 'https://content.app-us1.com/YzzLp9/2026/05/18/fa1f40ee-c6ac-4c7f-bd96-6a34971de1fa.png')
    .replace(/assets\/luci-case-study-ameristar-council-bluffs\.pdf/g, PDF_URL)
    .replace(/https:\/\/lucisystems\.com\/documents\/luci-case-study-ameristar-council-bluffs\.pdf/g, PDF_URL)
    .replace(/https:\/\/lucisystems\.com\/contact/g, DEMO_URL)
    .replace(/\.\.\/\.\.\/assets\/logos\/ameristar-council-bluffs\.svg/g, 'https://cdn.prod.website-files.com/62d7d68d14611c2a31d863cd/6a1e1c7089803edcc10a8491_ameristar-logo-cropped.png');
}

function addNewTabToExternalLinks(html) {
  return html
    .replace(
      /(<a class="(?:cta-btn|download-btn|cta-btn--secondary)" href="[^"]+")(?! target=)/g,
      `$1${LINK_NEW_TAB}`
    )
    .replace(/ download="[^"]*"/g, '');
}

/** Webflow pages already have a site footer — drop the case-study duplicate. */
function stripWebflowFooter(html) {
  return html.replace(/\s*<!-- FOOTER -->[\s\S]*?<footer class="footer">[\s\S]*?<\/footer>/, '');
}

/** About LUCI block reads like a second footer on Webflow pages that use the site footer. */
function stripWebflowCtaAbout(html) {
  return html.replace(/\s*<div class="cta__about">[\s\S]*?<\/div>/, '');
}

function stripFooterCss(css) {
  return css
    .replace(/\n\.luci-cs \.footer[^\n{]*\{[^}]*\}/g, '')
    .replace(/\n\.luci-cs \.footer__[^\n{]*\{[^}]*\}/g, '')
    .replace(/\n\.luci-cs \.cta__about[^\n{]*\{[^}]*\}/g, '')
    .replace(/\n\.luci-cs \.cta__about-label[^\n{]*\{[^}]*\}/g, '')
    .replace(/\n\.luci-cs \.cta__statement[^\n{]*\{[^}]*\}/g, '');
}

function fixFooterLogo(html) {
  return html.replace(
    /<a class="footer__logo"[\s\S]*?<img src="[^"]+" alt="LUCI Systems">/,
    '<a class="footer__logo" href="https://lucisystems.com">\n          <img src="https://content.app-us1.com/YzzLp9/2026/05/18/1bc8b968-9454-4813-a1b1-6477aaa143f2.png" alt="LUCI Systems">'
  );
}

/** Webflow: match live page bottom — no copyright row, single CTA button. PDF stays in hero. */
function trimWebflowPageBottom(html) {
  return html
    .replace(/\s*<a class="cta-btn cta-btn--secondary"[\s\S]*?<\/a>/, '')
    .replace(/\s*<p class="footer__legal">[\s\S]*?<\/p>/, '');
}

/** @param {{ includeFooter?: boolean, includeCtaAbout?: boolean }} opts */
function buildWebflowMarkup(markup, opts = {}) {
  let html = replaceAssets(markup);
  if (opts.includeFooter) html = fixFooterLogo(html);
  else html = stripWebflowFooter(html);
  if (!opts.includeCtaAbout) html = stripWebflowCtaAbout(html);
  html = trimWebflowPageBottom(html);
  html = addNewTabToExternalLinks(html);
  return html;
}

const src = fs.readFileSync(srcPath, 'utf8');
const styleMatch = src.match(/<style>([\s\S]*?)<\/style>/);
const markupMatch = src.match(/<div class="luci-cs">[\s\S]*<\/div>\s*(?=<\/body>)/);

if (!styleMatch || !markupMatch) {
  throw new Error('Could not parse ameristar-council-bluffs.html — expected .luci-cs wrapper');
}

const scopedCss = WEBFLOW_RESET + '\n' + scopeCss(styleMatch[1]);
const styleBlock = `<style>${scopedCss}\n</style>`;

const fonts = `<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Syncopate:wght@700&family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">
`;

let markup = buildWebflowMarkup(markupMatch[0], { includeFooter: true, includeCtaAbout: true });

fs.writeFileSync(path.join(root, 'ameristar-council-bluffs-webflow-head.html'), `${fonts}\n`);
fs.writeFileSync(path.join(root, 'ameristar-council-bluffs-webflow-body.html'), `${styleBlock}\n${markup}\n`);
fs.writeFileSync(path.join(root, 'ameristar-council-bluffs-webflow-embed.html'), `${fonts}${styleBlock}\n${markup}\n`);

console.log('Built Webflow embed files for Ameristar case study');
