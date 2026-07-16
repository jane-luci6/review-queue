import re

p = "ameristar-council-bluffs-webflow-body.html"
s = open(p).read()

topbar_cdn = "https://cdn.prod.website-files.com/62d7d68d14611c2a31d863cd/6a569df17c388a8f5ec49728_LUCI%20logo%20white%20%26%20mint.png"
footer_cdn = "https://cdn.prod.website-files.com/62d7d68d14611c2a31d863cd/6a569df95ad5aa594c4202c5_LUCI%20logo%20Mint.png"

# Split keeping the data-URI tokens; replace 1st (topbar) and 2nd (footer) with CDN URLs.
parts = re.split(r'(data:image/png;base64,[A-Za-z0-9+/=]+)', s)
idxs = [i for i, t in enumerate(parts) if t.startswith("data:image/png;base64,")]
print("data-URI count:", len(idxs))
parts[idxs[0]] = topbar_cdn
parts[idxs[1]] = footer_cdn
s2 = "".join(parts)
open(p, "w").write(s2)
print("new size:", len(s2))
