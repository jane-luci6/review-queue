# LUCI See How Outro

A HyperFrames video composition. Plain HTML + GSAP; rendered to MP4 by the `hyperframes` CLI.

## Requirements

- **Node.js 22+** — [nodejs.org](https://nodejs.org/)
- **FFmpeg** — `brew install ffmpeg` (macOS) · `sudo apt install ffmpeg` (Debian/Ubuntu) · [ffmpeg.org/download](https://ffmpeg.org/) (Windows)

Chrome is downloaded automatically on first preview/render. Verify the environment with:

```bash
npx hyperframes doctor
```

`npx` downloads the `hyperframes` CLI from npm on first use — no global install required.

## Preview in your browser

```bash
npx hyperframes preview
```

Opens the HyperFrames Studio at `http://localhost:3002`.

## Render to MP4

```bash
npx hyperframes render index.html -o output.mp4
```

Produces `output.mp4` at 1920×1080 / 30fps by default. Roughly 1–3× real-time on a modern laptop. Use `--fps 60` or `--resolution 3840x2160` to override.

## Troubleshooting

- **"FFmpeg not found"** — install FFmpeg per Requirements.
- **"Node version too old"** — install Node 22+.
- **Full docs** — [hyperframes.heygen.com](https://hyperframes.heygen.com/).
