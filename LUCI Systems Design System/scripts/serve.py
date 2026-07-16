#!/usr/bin/env python3
"""No-cache dev server for the LUCI Design System preview hub.

Serves the design-system root on http://localhost:8765 with headers that force
the browser to refetch on every reload — so HTML/CSS/JS edits always show up
without hard-refreshing or manually bumping ?v= cache-busters.

Usage:
    python3 scripts/serve.py          # serves on 8765
    python3 scripts/serve.py 9000     # custom port
    npm run serve                     # via package.json
"""
import os
import sys
import functools
import http.server

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8765
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class NoCacheHandler(http.server.SimpleHTTPRequestHandler):
    """SimpleHTTPRequestHandler that sends no-cache headers on every response."""

    def end_headers(self):
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate")
        self.send_header("Expires", "0")
        self.send_header("Pragma", "no-cache")
        super().end_headers()

    def log_message(self, fmt, *args):
        # Keep the default access log but prefix so it's easy to spot.
        sys.stderr.write("  %s - %s\n" % (self.address_string(), fmt % args))


def main():
    handler = functools.partial(NoCacheHandler, directory=ROOT)
    server = http.server.ThreadingHTTPServer(("", PORT), handler)
    print(f"Serving {ROOT} on http://localhost:{PORT} (no-cache) — Ctrl-C to stop")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping.")
        server.shutdown()


if __name__ == "__main__":
    main()
