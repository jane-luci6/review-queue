#!/usr/bin/env python3
"""Detect the solid-blue laptop screen, fit a quad to its corners, composite the real screenshot onto it."""
from PIL import Image, ImageDraw

BASE = '/Users/janehaynie/.cursor/projects/Users-janehaynie-Documents-Cursor-Projects-luci-design/assets/platform-hero-tech-base-v3.png'
SHOT = '/Users/janehaynie/.cursor/projects/Users-janehaynie-Documents-Cursor-Projects-luci-design/assets/Screenshot_2026-08-12_at_2.20.13_PM-3ee8cdbf-2b25-4558-92f0-7d971f711412.png'
OUT = '/Users/janehaynie/Documents/Cursor Projects/luci-website/public/images/hero-platform-employee.png'
PREVIEW = '/tmp/platform-hero-v3-preview.png'


def solve_persp(src_pts, dst_pts):
    A = [[0.0] * 8 for _ in range(8)]
    b = [0.0] * 8
    for i in range(4):
        x, y = src_pts[i]
        u, v = dst_pts[i]
        r = 2 * i
        A[r] = [x, y, 1, 0, 0, 0, -u * x, -u * y]; b[r] = u
        A[r + 1] = [0, 0, 0, x, y, 1, -v * x, -v * y]; b[r + 1] = v
    n = 8
    for col in range(n):
        piv = max(range(col, n), key=lambda r: abs(A[r][col]))
        A[col], A[piv] = A[piv], A[col]
        b[col], b[piv] = b[piv], b[col]
        pv = A[col][col]
        for j in range(col, n):
            A[col][j] /= pv
        b[col] /= pv
        for r in range(n):
            if r == col:
                continue
            f = A[r][col]
            for j in range(col, n):
                A[r][j] -= f * A[col][j]
            b[r] -= f * b[col]
    return tuple(b)


def main():
    im = Image.open(BASE).convert('RGB')
    px = im.load()
    w, h = im.size

    # Saturated blue mask (screen only, not the dim glow spill on hands/desk).
    def blue(r, g, b):
        return b > 175 and r < 110 and g < 140

    mask = bytearray(w * h)
    for y in range(h):
        for x in range(w):
            r, g, b = px[x, y][:3]
            if blue(r, g, b):
                mask[y * w + x] = 1

    # Largest connected component (4-conn).
    visited = bytearray(w * h)
    best = (0, [])
    for sy in range(h):
        for sx in range(w):
            idx = sy * w + sx
            if not mask[idx] or visited[idx]:
                continue
            stack = [(sx, sy)]
            visited[idx] = 1
            comp_pts = []
            while stack:
                x, y = stack.pop()
                comp_pts.append((x, y))
                for nx, ny in ((x-1, y), (x+1, y), (x, y-1), (x, y+1)):
                    if 0 <= nx < w and 0 <= ny < h:
                        ni = ny * w + nx
                        if mask[ni] and not visited[ni]:
                            visited[ni] = 1
                            stack.append((nx, ny))
            if len(comp_pts) > best[0]:
                best = (len(comp_pts), comp_pts)
    pts = best[1]
    print('screen blob pixel count=', len(pts))
    if len(pts) < 5000:
        raise SystemExit('screen blob too small')

    # Quad corners via extreme sums/diffs (captures tilt).
    tl = min(pts, key=lambda p: p[0] + p[1])
    tr = max(pts, key=lambda p: p[0] - p[1])
    br = max(pts, key=lambda p: p[0] + p[1])
    bl = min(pts, key=lambda p: p[0] - p[1])
    quad = [tl, tr, br, bl]
    print('quad=', quad)

    # Composite.
    base = Image.open(BASE).convert('RGBA')
    shot = Image.open(SHOT).convert('RGBA')
    sw, sh = shot.size
    xs = [p[0] for p in quad]
    ys = [p[1] for p in quad]
    minx, maxx = min(xs), max(xs)
    miny, maxy = min(ys), max(ys)
    bw, bh = maxx - minx, maxy - miny
    src_pts = [(p[0] - minx, p[1] - miny) for p in quad]
    dst_pts = [(0, 0), (sw, 0), (sw, sh), (0, sh)]
    coeffs = solve_persp(src_pts, dst_pts)
    warped = shot.transform((bw, bh), Image.PERSPECTIVE, coeffs, Image.BICUBIC)
    wmask = Image.new('L', (sw, sh), 255).transform((bw, bh), Image.PERSPECTIVE, coeffs, Image.BICUBIC)
    comp = base.copy()
    comp.paste(warped, (minx, miny), wmask)
    comp.convert('RGB').save(OUT)
    print('saved', OUT, comp.size)

    # Preview with quad drawn on the base.
    pv = base.convert('RGB').copy()
    d = ImageDraw.Draw(pv)
    d.line(quad + [quad[0]], fill=(255, 255, 0), width=3)
    for (x, y) in quad:
        d.ellipse([x - 6, y - 6, x + 6, y + 6], outline=(255, 0, 0), width=2)
    pv.save(PREVIEW)
    print('preview', PREVIEW)


if __name__ == '__main__':
    main()
