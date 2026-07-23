#!/usr/bin/env node
// Splits the FAG pages into Webflow custom-code embeds:
//   <page>-webflow-head.html  -> Webflow Page Settings > "Before </head>" tag
//   <page>-webflow-body.html  -> Webflow Page Settings > "Before </body>" tag (or an Embed widget)
//   <page>-webflow-preview.html -> combined render for local review
// Processes BOTH pages: the persona-picker hub and the published content page.
//
// Minimal-viable scoping: the .fag-* classnames are unique and won't clash with the
// Webflow site, so we only neutralize the rules that WOULD leak globally — :root vars,
// the universal *, html, and body — by re-homing them under a .luci-fag wrapper that
// also wraps the body markup. Fonts load via Google Fonts <link> (lightweight).

import { readFileSync, writeFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';

const here = dirname(fileURLToPath(import.meta.url));
const sales = join(here, '..', 'ui_kits', 'sales');

const pages = [
  'field-activation-guide-hub.html',
  'field-activation-guide-web-published.html',
];

const fontsLink = `<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;700&family=Inter:wght@400;600;700&family=Syncopate:wght@400;700&display=swap">`;

// Conservative HTML minify for the body markup only (keeps the <script> block
// readable). Collapses inter-tag whitespace + runs of whitespace to a single
// space — identical rendering, just small enough to fit Webflow's 50k-char
// custom-code field. No <pre>/<textarea>/<code> exist in the FAG body, so
// whitespace is never semantically significant here.
function minifyHtml(s) {
  const stash = [];
  s = s.replace(/<(pre|textarea|script|style)\b[\s\S]*?<\/\1>/gi, (m) => {
    stash.push(m); return `\u0000${stash.length - 1}\u0000`;
  });
  s = s.replace(/>\s+</g, '><');
  s = s.replace(/\s{2,}/g, ' ');
  s = s.trim();
  // Break at top-level <section> boundaries so the embed isn't one giant
  // line (Webflow's custom-code editor can choke/truncate a 40k+ char line).
  s = s.replace(/<section /g, '\n<section ');
  s = s.replace(/\u0000(\d+)\u0000/g, (_, i) => stash[i]);
  return s;
}

// Minify CSS for the head embed so the <style> block stays small enough for
// Webflow's "Inside <head>" field (a too-large <style> gets truncated and the
// </style> closing tag can be dropped, which eats the rest of the page as CSS
// -> blank page). Drops comments + collapses whitespace; no value semantics
// changed.
function minifyCss(c) {
  return c
    .replace(/\/\*[\s\S]*?\*\//g, '')
    .replace(/\s+/g, ' ')
    .replace(/\s*([{};,:>])\s*/g, '$1')
    .replace(/;}/g, '}')
    .trim();
}

for (const file of pages) {
  const src = join(sales, file);
  const base = file.replace(/\.html$/, '');
  const html = readFileSync(src, 'utf8');

  // 1. extract <style id="fag-...-css"> ... </style>
  const styleMatch = html.match(/<style id="fag-[^"]*">([\s\S]*?)<\/style>/);
  if (!styleMatch) throw new Error(`no fag-* style block found in ${file}`);
  let css = styleMatch[1];

  // 2. scope the leaking rules under .luci-fag
  css = css.replace(/^  :root \{/gm, '  .luci-fag {');            // :root blocks -> .luci-fag
  css = css.replace(/^  \* \{ box-sizing: border-box; \}/m, '  .luci-fag * { box-sizing: border-box; }');
  css = css.replace(/^  html \{ scroll-behavior: smooth; \}\n/m, ''); // drop global html rule
  css = css.replace(/ html \{ scroll-behavior: auto; \}/m, '');      // drop html inside @media
  css = css.replace(/^  body \{/m, '  .luci-fag {');                // body styles -> wrapper

  // 3. extract <body> ... </body> inner
  const bodyMatch = html.match(/<body>([\s\S]*?)<\/body>/);
  if (!bodyMatch) throw new Error(`no body found in ${file}`);
  let bodyInner = bodyMatch[1];

  // pull any <script> out so it can follow the markup in the body embed
  let script = '';
  const scriptMatch = bodyInner.match(/(\s*)(<script>[\s\S]*?<\/script>)/);
  if (scriptMatch) {
    script = scriptMatch[2];
    bodyInner = bodyInner.replace(scriptMatch[2], '').replace(/\s+$/, '');
  }

  // inline persona SVGs as base64 data URIs so they render on Webflow with no
  // uploads (the source keeps clean relative paths that work locally).
  bodyInner = bodyInner.replace(/src="assets\/personas\/([^"]+\.svg)(\?v=\d+)?"/g, (m, file) => {
    try {
      const svg = readFileSync(join(sales, 'assets', 'personas', file));
      return `src="data:image/svg+xml;base64,${svg.toString('base64')}"`;
    } catch (e) {
      console.warn(`persona svg not found, leaving relative: ${file}`);
      return m;
    }
  });

  const wrappedBody = `<div class="luci-fag">${minifyHtml(bodyInner.trim())}</div>`;

  // 4. write head + body embeds
  const headEmbed = `<!-- LUCI Field Activation Guide (${base}) — Webflow "Before </head>" embed.
     Paste into: Webflow Page Settings > Custom Code > "Before </head>" tag.
     Self-contained: scoped CSS + Google Fonts. No global body/html styles leak. -->
${fontsLink}
<style>
${minifyCss(css)}
</style>`;

  const bodyEmbed = `<!-- LUCI Field Activation Guide (${base}) — Webflow "Before </body>" embed.
     Paste into: Webflow Page Settings > Custom Code > "Before </body>" tag (or an Embed widget).
     Everything is wrapped in .luci-fag so the scoped CSS above applies only here. -->
${wrappedBody}${script ? '\n' + script : ''}
`;

  writeFileSync(join(sales, `${base}-webflow-head.html`), headEmbed, 'utf8');
  writeFileSync(join(sales, `${base}-webflow-body.html`), bodyEmbed, 'utf8');

  // 5. combined preview for local review
  const preview = `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="robots" content="noindex, nofollow">
<title>LUCI — Field Activation Guide (${base} preview)</title>
${fontsLink}
<style>
${minifyCss(css)}
</style>
</head>
<body>
${wrappedBody}${script ? '\n' + script : ''}
</body>
</html>
`;
  writeFileSync(join(sales, `${base}-webflow-preview.html`), preview, 'utf8');

  console.log(`wrote ${base}-webflow-{head,body,preview}.html`);
}
