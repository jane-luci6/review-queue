#!/usr/bin/env python3
"""Annotate the base photo with a coordinate grid to read off the laptop-screen corners."""
from PIL import Image, ImageDraw

BASE = '/Users/janehaynie/.cursor/projects/Users-janehaynie-Documents-Cursor-Projects-luci-design/assets/platform-hero-tech-base.png'
OUT = '/tmp/platform-hero-annotated.png'

im = Image.open(BASE).convert('RGB')
d = ImageDraw.Draw(im)
w, h = im.size
for x in range(0, w, 100):
    d.line([(x, 0), (x, h)], fill=(255, 0, 0, 80), width=1)
    d.text((x + 2, 2), str(x), fill=(255, 80, 80))
for y in range(0, h, 100):
    d.line([(0, y), (w, y)], fill=(0, 255, 0, 80), width=1)
    d.text((2, y + 2), str(y), fill=(80, 255, 80))
im.save(OUT)
print('saved', OUT, im.size)
