/**
 * LUCI portal document edit mode.
 * Loaded on customization preview HTML only — click text to edit.
 * Fonts/colors/layout stay on CSS classes; only text nodes change.
 */
(function () {
  'use strict';

  var fileHandle = null;

  function readContext() {
    var el = document.getElementById('luci-cursor-context');
    if (!el) return {};
    try {
      return JSON.parse(el.textContent || '{}');
    } catch (e) {
      return {};
    }
  }

  function serializeHtml() {
    var clone = document.documentElement.cloneNode(true);
    clone.querySelectorAll('.luci-edit-bar').forEach(function (n) {
      n.remove();
    });
    clone.querySelectorAll('.luci-logo-file-input').forEach(function (n) { n.remove(); });
    clone.querySelectorAll('.doc-cover__client.is-drop-target').forEach(function (n) {
      n.classList.remove('is-drop-target');
    });
    clone.querySelector('body').classList.remove('luci-edit-active');
    var barLink = clone.querySelector('link[href*="luci-doc-edit.css"]');
    if (barLink) barLink.remove();
    var barScript = clone.querySelector('script[src*="luci-doc-edit.js"]');
    if (barScript) barScript.remove();
    return '<!DOCTYPE html>\n' + clone.outerHTML;
  }

  function suggestedFileName(ctx) {
    var title = (ctx.title || 'luci-document').toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
    return title + '.html';
  }

  function enforceLocked(ctx) {
    var lockedPages = (ctx.editMode && ctx.editMode.lockedPages) || '';
    if (lockedPages) {
      document.querySelectorAll(lockedPages).forEach(function (page) {
        page.classList.add('luci-edit-locked');
        page.querySelectorAll('[contenteditable="true"]').forEach(function (node) {
          node.removeAttribute('contenteditable');
        });
      });
    }
    var lockedElements = (ctx.editMode && ctx.editMode.lockedElements) || '';
    if (lockedElements) {
      document.querySelectorAll(lockedElements).forEach(function (node) {
        node.classList.add('luci-edit-locked');
        node.removeAttribute('contenteditable');
        node.querySelectorAll('[contenteditable="true"]').forEach(function (child) {
          child.removeAttribute('contenteditable');
        });
      });
    }
  }

  /** Mark every text-bearing leaf inside .doc so Mike can click anywhere. */
  function ensureAllTextEditable() {
    var root = document.querySelector('.doc') || document.body;
    var EDIT_TAGS = {
      P: 1, LI: 1, H1: 1, H2: 1, H3: 1, H4: 1, H5: 1, H6: 1,
      DT: 1, DD: 1, SPAN: 1, FIGCAPTION: 1, BLOCKQUOTE: 1, TD: 1, TH: 1
    };
    var SKIP_CLASS = /doc-hub-link|doc-cover__logo|led-signoff-band__logo|luci-edit/;

    root.querySelectorAll('*').forEach(function (node) {
      if (!EDIT_TAGS[node.tagName]) return;
      if (node.closest('.luci-edit-locked')) return;
      if (node.tagName === 'IMG') return;
      if (SKIP_CLASS.test(node.className || '')) return;
      if (node.closest('[contenteditable="true"]') && node.getAttribute('contenteditable') !== 'true') {
        /* Nested inside an already-editable ancestor — leave alone. */
        return;
      }
      if (node.getAttribute('contenteditable') === 'true') {
        if (!/\bdoc-edit\b/.test(node.className || '')) node.classList.add('doc-edit');
        return;
      }
      /* Only mark if this node (or a direct text child) has visible text. */
      var text = (node.textContent || '').replace(/\s+/g, ' ').trim();
      if (!text) return;
      node.classList.add('doc-edit');
      node.setAttribute('contenteditable', 'true');
    });
  }

  function flashButton(btn, label) {
    var prev = btn.textContent;
    btn.textContent = label;
    btn.classList.add('is-copied');
    setTimeout(function () {
      btn.textContent = prev;
      btn.classList.remove('is-copied');
    }, 2000);
  }

  function downloadBlob(filename, blob) {
    var a = document.createElement('a');
    a.href = URL.createObjectURL(blob);
    a.download = filename;
    a.click();
    URL.revokeObjectURL(a.href);
  }

  /** True when the page is served from the LUCI dev server on localhost. */
  function onDevServer() {
    try {
      var loc = window.location;
      return loc.protocol === 'http:' && loc.hostname === '127.0.0.1' && loc.port === '8771';
    } catch (e) { return false; }
  }

  async function saveViaDevServer(html, btn) {
    var res = await fetch('/__save', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ path: window.location.pathname, html: html })
    });
    if (!res.ok) {
      var detail = '';
      try { detail = (await res.json()).error || ''; } catch (e) {}
      throw new Error('Save failed (' + res.status + (detail ? ': ' + detail : '') + ')');
    }
    flashButton(btn, 'Saved');
  }

  async function saveHtml(ctx, btn) {
    var html = serializeHtml();
    var name = suggestedFileName(ctx);
    var blob = new Blob([html], { type: 'text/html;charset=utf-8' });

    /* 1. LUCI dev server (most reliable — no picker, no Downloads artifact).
       The agent starts this server as part of the customization setup, so
       Mike just clicks Save and the working file on disk is overwritten. */
    if (onDevServer()) {
      try {
        await saveViaDevServer(html, btn);
        return;
      } catch (err) {
        /* Server died or not running — fall through to the picker / download. */
        console.warn('Dev server save failed:', err && err.message);
      }
    }

    /* 2. File System Access API — overwrite the same working file via a
       user-granted handle. Needs browser support (often missing in Cursor's
       in-editor browser) and Mike must pick the file the first time. */
    if (window.showSaveFilePicker) {
      try {
        if (!fileHandle) {
          fileHandle = await window.showSaveFilePicker({
            suggestedName: name,
            types: [{ description: 'HTML', accept: { 'text/html': ['.html'] } }]
          });
        }
        var writable = await fileHandle.createWritable();
        await writable.write(blob);
        await writable.close();
        flashButton(btn, 'Saved');
        return;
      } catch (err) {
        if (err && err.name === 'AbortError') return;
        fileHandle = null;
      }
    }

    /* 3. Last resort — download a *-edited.html and tell Mike to paste it
       over the working file. This is the path that loses typed edits, so
       the hint nudges Mike to ask Cursor to restart the dev server. */
    downloadBlob(name, blob);
    flashButton(btn, 'Downloaded');
    window.alert('Could not save directly to the working file (the LUCI dev server is not running and the browser file API is unavailable).\n\nAsk Cursor to reopen the project so it starts the dev server, then click Save again.');
  }

  function copyHtml(btn) {
    var html = serializeHtml();
    function legacyCopy(text) {
      var ta = document.createElement('textarea');
      ta.value = text;
      ta.setAttribute('readonly', '');
      ta.style.cssText = 'position:fixed;left:-9999px;top:0;opacity:0';
      document.body.appendChild(ta);
      ta.focus();
      ta.select();
      var ok = false;
      try { ok = document.execCommand('copy'); } catch (e) { ok = false; }
      document.body.removeChild(ta);
      return ok;
    }
    if (navigator.clipboard && window.isSecureContext) {
      navigator.clipboard.writeText(html).then(function () {
        flashButton(btn, 'Copied');
      }, function () {
        if (legacyCopy(html)) flashButton(btn, 'Copied');
        else window.prompt('Copy this HTML (Cmd+C), then paste over your working .html file:', html);
      });
      return;
    }
    if (legacyCopy(html)) flashButton(btn, 'Copied');
    else window.prompt('Copy this HTML (Cmd+C), then paste over your working .html file:', html);
  }

  async function downloadPdf(btn) {
    // Never call window.print() — it crashes Cursor's in-editor browser.
    // On the LUCI dev server, render via POST /__pdf (headless Chrome pipeline).
    if (!onDevServer()) {
      if (btn) flashButton(btn, 'Need local preview');
      window.alert('Download PDF needs the LUCI local preview server (http://127.0.0.1:8771).\n\nAsk Cursor to restart the server and open the preview, then click Download PDF again.');
      return;
    }

    var prev = btn ? btn.textContent : 'Download PDF';
    if (btn) {
      btn.textContent = 'Rendering…';
      btn.disabled = true;
    }

    try {
      // Persist click-to-edit changes first so the PDF matches what you see.
      try {
        await fetch('/__save', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ path: window.location.pathname, html: serializeHtml() })
        });
      } catch (saveErr) {
        console.warn('Pre-PDF save skipped:', saveErr && saveErr.message);
      }

      var res = await fetch('/__pdf', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ path: window.location.pathname })
      });

      if (!res.ok) {
        var detail = '';
        var ct = res.headers.get('Content-Type') || '';
        if (ct.indexOf('application/json') !== -1) {
          try { detail = (await res.json()).error || ''; } catch (e) {}
        } else {
          try { detail = await res.text(); } catch (e) {}
        }
        if (res.status === 404) {
          throw new Error('Preview server is outdated (no PDF endpoint). Ask Cursor to refresh luci-dev-server.py and restart the preview.');
        }
        throw new Error(detail || ('PDF failed (' + res.status + ')'));
      }

      var blob = await res.blob();
      var base = (window.location.pathname.split('/').pop() || 'document.html').replace(/\.html$/i, '');
      downloadBlob(base + '.pdf', blob);
      if (btn) {
        btn.textContent = prev;
        flashButton(btn, 'Downloaded');
      }
    } catch (err) {
      console.error('PDF render failed:', err);
      if (btn) {
        btn.textContent = prev;
        flashButton(btn, 'Failed');
      }
      window.alert('Could not generate the PDF.\n\n' + ((err && err.message) || err) + '\n\nYou can also ask Cursor: make a PDF.');
    } finally {
      if (btn) btn.disabled = false;
    }
  }

  function mountToolbar(ctx) {
    if (document.querySelector('.luci-edit-bar')) return;

    var bar = document.createElement('div');
    bar.className = 'luci-edit-bar';
    bar.setAttribute('role', 'toolbar');
    bar.setAttribute('aria-label', 'Document edit mode');

    var hint =
      (ctx.editMode && ctx.editMode.hint) ||
      'Click any text to edit. Fonts and colors stay locked to the design. Click Save when finished.';

    bar.innerHTML =
      '<span class="luci-edit-bar__label">Edit mode</span>' +
      '<p class="luci-edit-bar__hint">' + hint + '</p>' +
      '<div class="luci-edit-bar__actions">' +
      '<button type="button" class="luci-edit-bar__btn luci-edit-bar__btn--primary" data-action="save-html">Save</button>' +
      '<button type="button" class="luci-edit-bar__btn" data-action="copy-html">Copy HTML</button>' +
      '<button type="button" class="luci-edit-bar__btn" data-action="download-pdf">Download PDF</button>' +
      '</div>';

    document.body.prepend(bar);
    document.body.classList.add('luci-edit-active');

    bar.querySelector('[data-action="save-html"]').addEventListener('click', function (e) {
      saveHtml(ctx, e.currentTarget);
    });
    bar.querySelector('[data-action="copy-html"]').addEventListener('click', function (e) {
      copyHtml(e.currentTarget);
    });
    bar.querySelector('[data-action="download-pdf"]').addEventListener('click', function (e) {
      downloadPdf(e.currentTarget);
    });

    // Detect an outdated luci-dev-server.py (pre-PDF). Agent must always
    // overwrite that file before starting the server — this is the safety net.
    ensurePdfCapableServer(bar);
  }

  function ensurePdfCapableServer(bar) {
    if (!onDevServer()) return;
    var pdfBtn = bar.querySelector('[data-action="download-pdf"]');
    fetch('/__health')
      .then(function (res) {
        if (!res.ok) throw new Error('no health');
        return res.json();
      })
      .then(function (info) {
        if (info && info.pdf && Number(info.version) >= 2) return;
        markPdfServerStale(pdfBtn);
      })
      .catch(function () {
        markPdfServerStale(pdfBtn);
      });
  }

  function markPdfServerStale(pdfBtn) {
    if (!pdfBtn) return;
    pdfBtn.title = 'Preview server is outdated. Ask Cursor to refresh luci-dev-server.py and restart the preview.';
  }

  /* Client-logo placement picker + drag-and-drop image swap. Only mounts when a
     cover logo (.doc-cover__client) exists, so docs without one are unaffected.
     The chip group is appended to the edit bar (already print-hidden); the
     drop/click affordance is screen/edit-mode only. */
  function mountLogoTools() {
    var cover = document.querySelector('.doc-page--cover');
    if (!cover) return;
    if (cover.classList.contains('luci-edit-locked')) return;
    var logo = cover.querySelector('.doc-cover__client');
    if (!logo) return;
    var prepared = cover.querySelector('.doc-cover__prepared');
    var hero = cover.querySelector('.doc-cover__hero');
    if (!prepared || !hero) return;
    var originalParent = prepared.parentNode; /* the cover section */

    var POSITIONS = ['bottom-left', 'band', 'band-right', 'bottom-right'];
    var LABELS = { 'bottom-left': 'Bottom-left', 'band': 'Band', 'band-right': 'Band-right', 'bottom-right': 'Bottom-right' };
    var BAND_POSITIONS = ['band', 'band-right'];
    var chips = [];

    function applyPos(pos) {
      POSITIONS.forEach(function (p) { cover.classList.remove('logo-pos--' + p); });
      cover.classList.add('logo-pos--' + pos);
      /* Compare direct parentNode (not .contains) — hero is a descendant of
         cover, so .contains would always be true and the move-back would fail. */
      if (BAND_POSITIONS.indexOf(pos) !== -1) {
        if (prepared.parentNode !== hero) hero.appendChild(prepared);
      } else {
        if (prepared.parentNode !== originalParent) originalParent.appendChild(prepared);
      }
      chips.forEach(function (c) { c.classList.toggle('is-active', c.dataset.pos === pos); });
    }

    /* Build the chip group into the edit bar, before the Copy/Download actions. */
    var bar = document.querySelector('.luci-edit-bar');
    if (bar) {
      var group = document.createElement('div');
      group.className = 'luci-edit-bar__group';
      group.setAttribute('role', 'group');
      group.setAttribute('aria-label', 'Client logo placement');
      group.innerHTML = '<span class="luci-edit-bar__label">Logo spot</span>' +
        POSITIONS.map(function (p) {
          return '<button type="button" class="luci-edit-bar__chip" data-pos="' + p + '">' + LABELS[p] + '</button>';
        }).join('');
      var actions = bar.querySelector('.luci-edit-bar__actions');
      if (actions) bar.insertBefore(group, actions); else bar.appendChild(group);
      chips = Array.prototype.slice.call(group.querySelectorAll('.luci-edit-bar__chip'));
      chips.forEach(function (c) {
        c.addEventListener('click', function () { applyPos(c.dataset.pos); });
      });
      var current = 'bottom-left';
      POSITIONS.forEach(function (p) { if (cover.classList.contains('logo-pos--' + p)) current = p; });
      chips.forEach(function (c) { c.classList.toggle('is-active', c.dataset.pos === current); });
    }

    /* Image swap: click → file picker; drag-and-drop → base64 data URL (survives save). */
    var fileInput = document.createElement('input');
    fileInput.type = 'file';
    fileInput.accept = 'image/*';
    fileInput.hidden = true;
    fileInput.className = 'luci-logo-file-input';
    document.body.appendChild(fileInput);

    function setLogoFromFile(file) {
      if (!file || !file.type || !/^image\//.test(file.type)) return;
      var reader = new FileReader();
      reader.onload = function () {
        logo.src = reader.result;
        logo.alt = (file.name || 'Client logo').replace(/\.[^.]+$/, '');
        logo.removeAttribute('width');
        logo.removeAttribute('height');
        logo.dataset.swapped = '1';
        detectLight();
      };
      reader.readAsDataURL(file);
    }

    logo.addEventListener('click', function () { fileInput.click(); });
    fileInput.addEventListener('change', function () {
      if (fileInput.files && fileInput.files[0]) setLogoFromFile(fileInput.files[0]);
      fileInput.value = '';
    });
    ['dragenter', 'dragover'].forEach(function (ev) {
      logo.addEventListener(ev, function (e) { e.preventDefault(); e.stopPropagation(); logo.classList.add('is-drop-target'); });
    });
    ['dragleave', 'drop'].forEach(function (ev) {
      logo.addEventListener(ev, function (e) { e.preventDefault(); e.stopPropagation(); logo.classList.remove('is-drop-target'); });
    });
    logo.addEventListener('drop', function (e) {
      var dt = e.dataTransfer;
      if (dt && dt.files && dt.files[0]) setLogoFromFile(dt.files[0]);
    });

    /* Light-logo detection: on a band spot a dark logo is inverted to white, but an
       already-light/white logo would invert to black. Sample average luminance
       (skipping transparent pixels); if bright, mark data-logo-light so the CSS
       skips the invert. Best-effort — a tainted canvas just leaves the invert. */
    function detectLight() {
      try {
        var canvas = document.createElement('canvas');
        var w = canvas.width = 32, h = canvas.height = 16;
        var c2d = canvas.getContext('2d');
        c2d.drawImage(logo, 0, 0, w, h);
        var data = c2d.getImageData(0, 0, w, h).data;
        var sum = 0, n = 0;
        for (var i = 0; i < data.length; i += 4) {
          if (data[i + 3] < 16) continue;
          sum += 0.299 * data[i] + 0.587 * data[i + 1] + 0.114 * data[i + 2];
          n++;
        }
        var avg = n ? sum / n : 0;
        if (avg > 200) logo.dataset.logoLight = '1'; else logo.removeAttribute('data-logo-light');
      } catch (e) { /* tainted canvas (cross-origin src) — leave invert as-is */ }
    }
    if (logo.complete && logo.naturalWidth) detectLight();
    else logo.addEventListener('load', detectLight, { once: true });
  }

  function init() {
    var ctx = readContext();
    if (ctx.editMode && ctx.editMode.enabled === false) return;
    enforceLocked(ctx);
    ensureAllTextEditable();
    mountToolbar(ctx);
    mountLogoTools();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
