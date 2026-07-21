#!/usr/bin/env node
// Derives field-activation-guide-web-published.html from the detailed
// field-activation-guide-web.html: swaps each "How to do it" accordion for
// a per-use-case "Learn more in the support portal" link (or a portal
// fallback where no KB article exists), and adds a per-section
// "Need a hand? Contact your FDE / browse the support portal" line.
// Re-run after any change to the detailed page or the links JSON.

import fs from 'node:fs';
import path from 'node:path';

const dir = 'LUCI Systems Design System/ui_kits/sales';
const htmlPath = path.join(dir, 'field-activation-guide-web.html');
const linksPath = path.join(dir, 'field-activation-links.json');
const outPath = path.join(dir, 'field-activation-guide-web-published.html');

const html = fs.readFileSync(htmlPath, 'utf8');
const links = JSON.parse(fs.readFileSync(linksPath, 'utf8'));
const portal = links.supportPortal;
const bySlug = Object.fromEntries(links.links.map(l => [l.slug, l]));

// panel-id prefix (e.g. "m1") -> use-case slug
const panelToSlug = {
  m1: 'marketing-push-message', m2: 'marketing-daypart-promotions', m3: 'marketing-zone-content', m4: 'marketing-event-campaign',
  g1: 'gaming-floor-audio', g2: 'gaming-jackpot-event', g3: 'gaming-reconfigure-property', g4: 'gaming-new-game-launch',
  a1: 'av-property-schedule', a2: 'av-service-requests', a3: 'av-find-problems', a4: 'av-private-event',
  i1: 'it-add-endpoint', i2: 'it-config-docs', i3: 'it-permissions', i4: 'it-kiosk',
  gm1: 'gm-walk-floor-ipad', gm2: 'gm-morning-reset', gm4: 'gm-team-adoption',
};

// Return index just past the </div> that closes the <div class="fag-acc"> at startIdx.
function blockEnd(h, startIdx) {
  let i = h.indexOf('>', startIdx) + 1;
  let depth = 1;
  while (i < h.length && depth > 0) {
    const o = h.indexOf('<div', i);
    const c = h.indexOf('</div>', i);
    if (c === -1) return -1;
    if (o !== -1 && o < c) { depth++; i = o + 4; }
    else { depth--; i = c + 6; }
  }
  return i;
}

const chev = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 6 15 12 9 18"/></svg>';

// Per-section "LUCI features" highlight block: lists the capabilities the
// section's use cases rely on, each linked to its how-to article, and closes
// with the FDE / support-portal help line.
function featuresBlock(sf) {
  const helpFooter = `      <p class="fag-feats__help"><strong>Need a hand?</strong> Your FDE can walk you through any of this &mdash; or <a href="${portal}" target="_blank" rel="noopener">browse the support portal</a> for the step-by-step guides.</p>`;
  let inner;
  if (sf.features.length === 0) {
    inner = `      <p class="fag-feats__note">These are business-process moves, not software steps. Your FDE can help you build each case &mdash; or <a href="${portal}" target="_blank" rel="noopener">browse the support portal</a> for the platform guides.</p>`;
  } else {
    const items = sf.features.map(f => {
      const link = bySlug[f.fromSlug];
      const url = link && link.url ? link.url : portal;
      const article = link ? link.article.replace(/&/g, '&amp;') : 'Support portal';
      return `        <li class="fag-feat"><span class="fag-feat__name">${f.feature}</span><a class="fag-feat__link" href="${url}" target="_blank" rel="noopener">How-to guide ${chev}</a><span class="fag-feat__article">${article}</span></li>`;
    }).join('\n');
    inner = `      <p class="fag-feats__label">LUCI features in this section</p>\n      <p class="fag-feats__intro">These use cases rely on a few capabilities &mdash; here&rsquo;s where to learn each one.</p>\n      <ul class="fag-feats__list">\n${items}\n      </ul>`;
  }
  return `    <div class="fag-feats">\n${inner}\n${helpFooter}\n    </div>\n`;
}

// 1) Strip each "How to do it" accordion — the how-to links move to the
// per-section features highlight at the end of each section.
let out = '';
let cursor = 0;
let accStart = html.indexOf('<div class="fag-acc">', cursor);
const report = [];
while (accStart !== -1) {
  out += html.slice(cursor, accStart);
  const end = blockEnd(html, accStart);
  report.push('stripped accordion');
  cursor = end;
  accStart = html.indexOf('<div class="fag-acc">', cursor);
}
out += html.slice(cursor);

// 2) Insert a per-section "LUCI features" highlight block before each
// fag-sec </section> (after the fag-spot aside). The conclusion section has
// no aside, so it's skipped.
for (const sf of links.sectionFeatures) {
  const secStart = out.indexOf(`id="${sf.section}"`);
  if (secStart === -1) continue;
  const secClose = out.indexOf('</section>', secStart);
  if (secClose === -1) continue;
  out = out.slice(0, secClose) + featuresBlock(sf) + out.slice(secClose);
}

// 2b) Drop the floating "Need a hand?" pill — the per-section help line + the
// conclusion's FDE line already cover contact; the pill is now redundant.
out = out.replace(/<a class="fag-fab"[\s\S]*?<\/a>/, '');

// 2c) Replace the whole <script> block: drop the dead accordion JS and the
// FAB-visibility JS (no .fag-acc__btn or .fag-fab remain); keep the scroll-spy
// that highlights the active persona in the sticky nav.
const cleanScript = `<script>
  (function () {
    // Scroll-spy: highlight the active persona link in the sticky nav
    var links = Array.prototype.slice.call(document.querySelectorAll('.fag-nav__link'));
    var sections = links.map(function (l) { return document.querySelector(l.getAttribute('href')); }).filter(Boolean);
    if ('IntersectionObserver' in window && sections.length) {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) {
          if (e.isIntersecting) {
            var id = e.target.id;
            links.forEach(function (l) { l.classList.toggle('is-active', l.getAttribute('href') === '#' + id); });
          }
        });
      }, { rootMargin: '-45% 0px -50% 0px', threshold: 0 });
      sections.forEach(function (s) { io.observe(s); });
    }
  })();
</script>`;
out = out.replace(/<script>[\s\S]*?<\/script>/, cleanScript);

// 2d) Normalize to LF for a clean generated artifact.
out = out.replace(/\r\n/g, '\n');

// 3) Inject CSS for the new classes (after the first <style> open).
const css = `
    /* published-variant: per-section LUCI features highlight */
    .fag-feats{margin-top:32px;padding:20px 0 0;border-top:1px solid rgba(104,227,190,.18);}
    .fag-feats__label{font-family:var(--font-head);font-weight:700;font-size:10.5px;letter-spacing:.18em;text-transform:uppercase;color:var(--mint);margin:0 0 8px;}
    .fag-feats__intro,.fag-feats__note{font-family:var(--font-body);font-size:14px;line-height:1.6;color:rgba(235,245,248,0.72);margin:0 0 16px;max-width:62ch;}
    .fag-feats__list{list-style:none;margin:0;padding:0;}
    .fag-feat{display:flex;flex-wrap:wrap;align-items:baseline;gap:6px 14px;padding:12px 0;border-bottom:1px solid rgba(104,227,190,.10);}
    .fag-feat:last-child{border-bottom:0;}
    .fag-feat__name{font-family:var(--font-head);font-weight:700;font-size:15px;color:var(--off-white);letter-spacing:-.01em;flex:0 0 auto;}
    .fag-feat__link{display:inline-flex;align-items:center;gap:6px;font-family:var(--font-head);font-weight:700;font-size:11px;letter-spacing:.06em;text-transform:uppercase;color:var(--mint);text-decoration:none;margin-left:auto;white-space:nowrap;}
    .fag-feat__link:hover{text-decoration:underline;}
    .fag-feat__link svg{width:13px;height:13px;}
    .fag-feat__article{flex:0 0 100%;font-family:var(--font-body);font-size:13px;color:rgba(235,245,248,0.60);line-height:1.5;}
    .fag-feats__help{margin:18px 0 0;font-family:var(--font-body);font-size:14px;color:rgba(235,245,248,0.72);line-height:1.6;}
    .fag-feats__help strong{color:var(--off-white);font-weight:600;}
    .fag-feats__help a{color:var(--mint);font-weight:600;text-decoration:none;}
    .fag-feats__help a:hover{text-decoration:underline;}
    .fag-sec--light .fag-feats{border-top-color:var(--rule-light);}
    .fag-sec--light .fag-feats__label{color:var(--accent-light);}
    .fag-sec--light .fag-feats__intro,.fag-sec--light .fag-feats__note{color:var(--ink-muted);}
    .fag-sec--light .fag-feat{border-bottom-color:var(--rule-light);}
    .fag-sec--light .fag-feat__name{color:var(--ink-strong);}
    .fag-sec--light .fag-feat__link{color:var(--accent-light);}
    .fag-sec--light .fag-feat__article{color:var(--ink-muted);}
    .fag-sec--light .fag-feats__help{color:var(--ink-muted);}
    .fag-sec--light .fag-feats__help strong{color:var(--ink-strong);}
    .fag-sec--light .fag-feats__help a{color:var(--accent-light);}
`;
out = out.replace(/(<style[^>]*>)/, `$1${css}`);

fs.writeFileSync(outPath, out);
console.log(`wrote ${outPath}`);
console.log(`replaced ${report.length} accordions:`);
report.forEach(r => console.log('  ' + r));
