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

  function init() {
    var ctx = readContext();
    if (ctx.editMode && ctx.editMode.enabled === false) return;
    enforceLocked(ctx);
    ensureEditableMarked();
    mountToolbar(ctx);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
