#!/usr/bin/env python3
"""Find the laptop screen as the darkest large rectangle in the upper region of the base photo."""
from PIL import Image, ImageDraw

BASE = '/Users/janehaynie/.cursor/projects/Users-janehaynie-Documents-Cursor-Projects-luci-design/assets/platform-hero-tech-base-v2.png'
OUT = '/tmp/platform-hero-detected2.png'

im = Image.open(BASE).convert('RGB')
px = im.load()
w, h = im.size

# Very-dark mask, upper region only (screen sits above the keyboard ~y540).
def very_dark(r, g, b):
    return max(r, g, b) < 55

mask = bytearray(w * h)
for y in range(0, 560):
    for x in range(w):
        r, g, b = px[x, y][:3]
        if very_dark(r, g, b):
            mask[y * w + x] = 1

visited = bytearray(w * h)
blobs = []
for sy in range(0, 560):
    for sx in range(w):
        idx = sy * w + sx
        if not mask[idx] or visited[idx]:
            continue
        stack = [(sx, sy)]
        visited[idx] = 1
        size = 0
        minx, maxx, miny, maxy = sx, sx, sy, sy
        while stack:
            x, y = stack.pop()
            size += 1
            if x < minx: minx = x
            if x > maxx: maxx = x
            if y < miny: miny = y
            if y > maxy: maxy = y
            for nx, ny in ((x-1, y), (x+1, y), (x, y-1), (x, y+1)):
                if 0 <= nx < w and 0 <= ny < h:
                    ni = ny * w + nx
                    if mask[ni] and not visited[ni]:
                        visited[ni] = 1
                        stack.append((nx, ny))
        blobs.append((size, (minx, miny, maxx, maxy)))

blobs.sort(reverse=True)
print('top 5 very-dark blobs (size, bbox):')
for size, bb in blobs[:5]:
    print(' ', size, bb)

# Pick the blob whose aspect is landscape-ish and large.
best = None
for size, bb in blobs:
    minx, miny, maxx, maxy = bb
    bw, bh = maxx - minx, maxy - miny
    if size > 8000 and bw > 200 and bh > 100:
        best = bb
        break
print('chosen screen bbox=', best)

d = ImageDraw.Draw(im)
if best:
    minx, miny, maxx, maxy = best
    d.rectangle([minx, miny, maxx, maxy], outline=(80, 255, 80), width=4)
    d.text((minx + 4, miny + 4), f'{minx},{miny} {maxx},{maxy}', fill=(80, 255, 80))
im.save(OUT)
print('saved', OUT)
