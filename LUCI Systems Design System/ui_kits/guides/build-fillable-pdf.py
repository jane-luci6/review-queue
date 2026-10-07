#!/usr/bin/env python3
"""Export the Belterra STB guide as a PDF with every IP address as an editable form field.

Usage:
  python3 build-fillable-pdf.py [output.pdf]

Two headless-Chrome passes: one measures each IP element's box, one prints the page
with those values hidden. PyMuPDF then drops a pre-filled text field over each box.
"""
import html, json, pathlib, re, subprocess, sys, tempfile
import fitz

HERE = pathlib.Path(__file__).resolve().parent
SRC = HERE / 'belterra-park-lg-stb-setup-guide.html'
OUT = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else pathlib.Path.home() / 'Desktop' / 'LUCI - Belterra Park LG STB-6500 Setup Guide.pdf'
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
PX_TO_PT = 0.75

TAG_JS = r"""
<script>
(() => {
  const ip = /^\d{1,3}\.\d{1,3}\.\d{1,3}\.(\d{1,3}|\[label\])$/;
  const port = /^\d{4}$/;
  const isAddr = t => ip.test(t) || port.test(t);
  const targets = [];
  document.querySelectorAll('.guide-settings__v:not(.guide-settings__v--note), .guide-step__enter, .guide-code, .guide-log__ip').forEach(el => {
    if (isAddr(el.textContent.trim())) targets.push(el);
  });
  document.querySelectorAll('.guide-log__row').forEach(row => {
    if (!row.querySelector('.guide-log__ip')) targets.push(row.children[1]);
  });
  targets.forEach((el, i) => el.setAttribute('data-f', i));
  const st = document.createElement('style');
  st.textContent = '[data-f]{color:transparent!important}';
  document.head.appendChild(st);
  window.__targets = targets;
})();
</script>
"""

PROBE_JS = r"""
<script>
window.addEventListener('load', () => setTimeout(() => {
  const pages = [...document.querySelectorAll('.doc-page')];
  const out = window.__targets.map((el, i) => {
    const page = el.closest('.doc-page');
    const pr = page.getBoundingClientRect();
    const r = el.getBoundingClientRect();
    const cs = getComputedStyle(el);
    const pad = parseFloat(cs.paddingLeft) || 0;
    el.style.color = '';
    const color = getComputedStyle(el).color;
    return {i, page: pages.indexOf(page), x: r.left - pr.left + pad, y: r.top - pr.top,
            w: r.width - pad * 2, h: r.height, fs: parseFloat(cs.fontSize),
            color, value: el.textContent.trim(), log: !!el.closest('.guide-log')};
  });
  const pre = document.createElement('pre'); pre.id = 'FIELDS';
  pre.textContent = JSON.stringify(out); document.body.appendChild(pre);
}, 1500));
</script>
"""


def chrome(args, html_text):
    with tempfile.NamedTemporaryFile('w', suffix='.html', dir=HERE, delete=False) as f:
        f.write(html_text)
        tmp = pathlib.Path(f.name)
    try:
        return subprocess.run([CHROME, '--headless', '--disable-gpu', '--virtual-time-budget=8000', *args, tmp.as_uri()],
                              capture_output=True, text=True).stdout
    finally:
        tmp.unlink()


def rgb(css):
    r, g, b = [int(v) for v in re.findall(r'\d+', css)[:3]]
    return (r / 255, g / 255, b / 255)


def main():
    src = SRC.read_text()
    tagged = src.replace('</body>', TAG_JS + '</body>')

    dom = chrome(['--window-size=1200,1400', '--dump-dom'], tagged.replace('</body>', PROBE_JS + '</body>'))
    fields = json.loads(html.unescape(re.search(r'<pre id="FIELDS">(.*?)</pre>', dom, re.S).group(1)))

    tmp_pdf = HERE / '_fillable_tmp.pdf'
    chrome(['--no-pdf-header-footer', f'--print-to-pdf={tmp_pdf}'], tagged)

    doc = fitz.open(tmp_pdf)
    for f in fields:
        page = doc[f['page']]
        x0, y0 = f['x'] * PX_TO_PT, f['y'] * PX_TO_PT
        w = max(f['w'], 90 if f['log'] else 0) * PX_TO_PT
        rect = fitz.Rect(x0 - 1, y0, x0 + w + 2, y0 + f['h'] * PX_TO_PT)
        wd = fitz.Widget()
        wd.field_type = fitz.PDF_WIDGET_TYPE_TEXT
        wd.field_name = f"ip_{f['i']:02d}"
        wd.field_value = f['value']
        wd.rect = rect
        wd.text_font = 'Cour'
        wd.text_fontsize = round(f['fs'] * PX_TO_PT, 1)
        wd.text_color = rgb(f['color'])
        wd.border_width = 0
        wd.border_color = None
        wd.fill_color = None
        page.add_widget(wd)
    # PyMuPDF widgets only offer regular Courier; Courier-Bold shares its metrics.
    for xref in range(1, doc.xref_length()):
        if doc.xref_get_key(xref, 'BaseFont') == ('name', '/Courier'):
            doc.xref_set_key(xref, 'BaseFont', '/Courier-Bold')
    doc.save(OUT, garbage=3, deflate=True)
    tmp_pdf.unlink()
    print(f'{len(fields)} editable fields -> {OUT}')


if __name__ == '__main__':
    main()
