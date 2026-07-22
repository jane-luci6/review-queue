/**
 * LUCI portal document edit mode.
 * Loaded on customization preview HTML only — click highlighted text to edit.
 */
(function () {
  'use strict';

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
      });
    }
  }

  function ensureEditableMarked() {
    document.querySelectorAll('.doc-edit, .deck-edit, [data-studio]').forEach(function (node) {
      if (node.closest('.luci-edit-locked')) return;
      if (node.tagName === 'IMG') return;
      if (!node.hasAttribute('contenteditable')) {
        node.setAttribute('contenteditable', 'true');
      }
    });
  }

  function mountToolbar(ctx) {
    if (document.querySelector('.luci-edit-bar')) return;

    var bar = document.createElement('div');
    bar.className = 'luci-edit-bar';
    bar.setAttribute('role', 'toolbar');
    bar.setAttribute('aria-label', 'Document edit mode');

    var hint =
      (ctx.editMode && ctx.editMode.hint) ||
      'Click highlighted text to edit. Locked pages stay read-only.';

    bar.innerHTML =
      '<span class="luci-edit-bar__label">Edit mode</span>' +
      '<p class="luci-edit-bar__hint">' + hint + '</p>' +
      '<div class="luci-edit-bar__actions">' +
      '<button type="button" class="luci-edit-bar__btn" data-action="copy-html">Copy updated HTML</button>' +
      '<button type="button" class="luci-edit-bar__btn" data-action="download-html">Download HTML</button>' +
      '</div>';

    document.body.prepend(bar);
    document.body.classList.add('luci-edit-active');

    bar.querySelector('[data-action="copy-html"]').addEventListener('click', function (btn) {
      var html = serializeHtml();
      function flashCopied() {
        var prev = btn.textContent;
        btn.textContent = 'Copied';
        btn.classList.add('is-copied');
        setTimeout(function () {
          btn.textContent = prev;
          btn.classList.remove('is-copied');
        }, 2000);
      }
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
        navigator.clipboard.writeText(html).then(flashCopied, function () {
          if (legacyCopy(html)) flashCopied();
          else window.prompt('Copy this HTML (Cmd+C):', html);
        });
        return;
      }
      if (legacyCopy(html)) flashCopied();
      else window.prompt('Copy this HTML (Cmd+C):', html);
    });

    bar.querySelector('[data-action="download-html"]').addEventListener('click', function () {
      var html = serializeHtml();
      var title = (ctx.title || 'luci-document').toLowerCase().replace(/\s+/g, '-');
      var blob = new Blob([html], { type: 'text/html;charset=utf-8' });
      var a = document.createElement('a');
      a.href = URL.createObjectURL(blob);
      a.download = title + '-edited.html';
      a.click();
      URL.revokeObjectURL(a.href);
    });
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
    ensureEditableMarked();
    mountToolbar(ctx);
    mountLogoTools();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
