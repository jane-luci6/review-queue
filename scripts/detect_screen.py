#!/usr/bin/env python3
"""Detect the laptop screen in the base photo as the largest cool-dark blob; report + draw its quad."""
from PIL import Image, ImageDraw

BASE = '/Users/janehaynie/.cursor/projects/Users-janehaynie-Documents-Cursor-Projects-luci-design/assets/platform-hero-tech-base-v2.png'
OUT = '/tmp/platform-hero-detected.png'

im = Image.open(BASE).convert('RGB')
px = im.load()
w, h = im.size

# "Cool dark" mask: screen pixels are dark and cool-tinted (green or blue >= red), unlike warm wood/desk/lamp.
def cool_dark(r, g, b):
    return (max(r, g, b) < 150) and (g > r + 6 or b > r + 6)

mask = bytearray(w * h)
for y in range(h):
    for x in range(w):
        r, g, b = px[x, y][:3]
        if cool_dark(r, g, b):
            mask[y * w + x] = 1

# Largest connected component (4-conn), iterative flood with a visited array.
visited = bytearray(w * h)
best = (0, None)  # (size, bbox)
stack_cap = w * h
for sy in range(h):
    for sx in range(w):
        idx = sy * w + sx
        if not mask[idx] or visited[idx]:
            continue
        # BFS
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
        if size > best[0]:
            best = (size, (minx, miny, maxx, maxy))

print('largest cool-dark blob size=', best[0])
print('bbox=', best[1])

d = ImageDraw.Draw(im)
if best[1]:
    minx, miny, maxx, maxy = best[1]
    d.rectangle([minx, miny, maxx, maxy], outline=(255, 60, 255), width=4)
    d.text((minx + 4, miny + 4), f'{minx},{miny}  {maxx},{maxy}', fill=(255, 60, 255))
im.save(OUT)
print('saved', OUT)
