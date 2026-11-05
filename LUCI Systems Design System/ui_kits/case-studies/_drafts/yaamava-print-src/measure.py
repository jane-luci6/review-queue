import subprocess,re,os
d="/Users/janehaynie/Documents/Cursor Projects/luci-design/LUCI Systems Design System/ui_kits/case-studies/_drafts"
h=open(d+"/yaamava-partnership-print.html").read()
js='''<script>window.addEventListener('load',()=>{setTimeout(()=>{const o=[];document.querySelectorAll('.pg').forEach((p,i)=>{const parts=[];let c=0;for(const e of p.children){const n=e.scrollHeight;c+=n;parts.push((e.className||e.tagName).toString().split(' ').pop()+'='+n);}o.push('P'+(i+1)+' total '+c+' ['+parts.join(', ')+']');});document.body.setAttribute('data-m',o.join(' || '));},1500)});</script>'''
open(d+"/_measure.html","w").write(h.replace("</head>",js+"</head>"))
CH="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
out=subprocess.run([CH,"--headless=new","--disable-gpu","--window-size=900,1200","--virtual-time-budget=10000","--dump-dom","file://"+d+"/_measure.html"],capture_output=True,text=True).stdout
m=re.search(r'data-m="([^"]*)"',out)
print(m.group(1).replace(" || ","\n") if m else "no data")
os.remove(d+"/_measure.html")
