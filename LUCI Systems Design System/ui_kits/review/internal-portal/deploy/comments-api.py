#!/usr/bin/env python3
"""Internal Marketing Portal — comment/approval sync API.

A zero-dependency (Python stdlib) HTTP service that stores review comments and
approvals in a JSON file so Jane can see Mike/Mark's feedback from any browser.

Restores the contract of the old Netlify function (netlify/functions/comments.mjs):

  GET  /api/comments
    -> { "comments": [ { assetId, author, text, at } ... ],
         "approvals": { "<assetId>": { "<reviewer>": "<iso8601>" } } }

  POST /api/comments   { "assetId", "author", "text" }
    -> appends { assetId, author, text, at: <now> }
    -> { "ok": true, "comment": { ... } }

  POST /api/comments   { "action": "approval", "assetId", "reviewer" }
    -> toggles approvals[assetId][reviewer]
    -> { "ok": true, "approvals": {...byAsset}, "assetId", "reviewer", "approved": bool }

  OPTIONS /api/comments -> 204 (CORS preflight)

Storage: a single JSON file (default /data/comments.json), written through on
every POST and atomically (tmp + rename). State is held in memory under a lock
so concurrent writes are safe.

Run:
  python3 comments-api.py
  PORT=8090 DATA_FILE=/data/comments.json python3 comments-api.py
"""

import json
import os
import threading
from datetime import datetime, timezone
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

PORT = int(os.environ.get("PORT", "8090"))
DATA_FILE = os.environ.get("DATA_FILE", "/data/comments.json")

CORS_HEADERS = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type",
    "Access-Control-Max-Age": "86400",
}

_lock = threading.Lock()
_state = {"comments": [], "approvals": {"byAsset": {}}}


def _now_iso():
    return datetime.now(timezone.utc).isoformat()


def _load():
    global _state
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as fh:
            data = json.load(fh)
        _state = {
            "comments": list(data.get("comments", [])),
            "approvals": {"byAsset": dict(data.get("approvals", {}).get("byAsset", {}))},
        }
    except (FileNotFoundError, json.JSONDecodeError):
        _state = {"comments": [], "approvals": {"byAsset": {}}}


def _persist():
    os.makedirs(os.path.dirname(DATA_FILE) or ".", exist_ok=True)
    tmp = DATA_FILE + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(_state, fh, indent=2)
    os.replace(tmp, DATA_FILE)


def _add_comment(asset_id, author, text):
    entry = {"assetId": asset_id, "author": author, "text": text, "at": _now_iso()}
    _state["comments"].append(entry)
    _persist()
    return entry


def _toggle_approval(asset_id, reviewer):
    by_asset = _state["approvals"]["byAsset"]
    row = dict(by_asset.get(asset_id, {}))
    was_approved = bool(row.get(reviewer))
    if was_approved:
        del row[reviewer]
    else:
        row[reviewer] = _now_iso()
    if row:
        by_asset[asset_id] = row
    else:
        by_asset.pop(asset_id, None)
    _persist()
    return by_asset, bool(row.get(reviewer))


class Handler(BaseHTTPRequestHandler):
    server_version = "LUCIComments/1.0"

    def _send(self, status, payload=None, extra=None):
        body = b"" if payload is None else json.dumps(payload).encode("utf-8")
        self.send_response(status)
        if payload is not None:
            self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        for k, v in CORS_HEADERS.items():
            self.send_header(k, v)
        if extra:
            for k, v in extra.items():
                self.send_header(k, v)
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        if body:
            self.wfile.write(body)

    def _err(self, status, message):
        self._send(status, {"error": message})

    def do_OPTIONS(self):  # noqa: N802
        self._send(HTTPStatus.NO_CONTENT)

    def do_GET(self):  # noqa: N802
        if self.path.split("?", 1)[0].rstrip("/") not in ("/api/comments", "/api/comments/"):
            return self._err(HTTPStatus.NOT_FOUND, "not found")
        with _lock:
            payload = {
                "comments": list(_state["comments"]),
                "approvals": dict(_state["approvals"]["byAsset"]),
            }
        self._send(HTTPStatus.OK, payload)

    def do_POST(self):  # noqa: N802
        if self.path.split("?", 1)[0].rstrip("/") not in ("/api/comments", "/api/comments/"):
            return self._err(HTTPStatus.NOT_FOUND, "not found")
        length = int(self.headers.get("Content-Length") or 0)
        try:
            body = json.loads(self.rfile.read(length) or b"{}")
        except (json.JSONDecodeError, ValueError):
            return self._err(HTTPStatus.BAD_REQUEST, "invalid JSON")

        asset_id = (body.get("assetId") or "").strip()
        if not asset_id:
            return self._err(HTTPStatus.BAD_REQUEST, "assetId required")

        with _lock:
            if body.get("action") == "approval":
                reviewer = (body.get("reviewer") or "").strip()
                if not reviewer:
                    return self._err(HTTPStatus.BAD_REQUEST, "reviewer required for approval")
                by_asset, approved = _toggle_approval(asset_id, reviewer)
                return self._send(HTTPStatus.OK, {
                    "ok": True,
                    "approvals": by_asset,
                    "assetId": asset_id,
                    "reviewer": reviewer,
                    "approved": approved,
                })

            author = (body.get("author") or "").strip()
            text = (body.get("text") or "").strip()
            if not author or not text:
                return self._err(HTTPStatus.BAD_REQUEST, "assetId, author, and text required")
            entry = _add_comment(asset_id, author, text)
            self._send(HTTPStatus.OK, {"ok": True, "comment": entry})

    def log_message(self, fmt, *args):
        # Keep the container log concise: one line per request.
        print("%s - %s" % (self.address_string(), fmt % args), flush=True)


def main():
    _load()
    server = ThreadingHTTPServer(("0.0.0.0", PORT), Handler)
    print(f"comments-api listening on :{PORT}, data={DATA_FILE}", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
