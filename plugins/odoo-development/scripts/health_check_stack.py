#!/usr/bin/env python3
"""Health check helper for local plugin stack."""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MCP_FILE = ROOT / "mcp.json"


def python_status() -> dict:
    major, minor = sys.version_info[:2]
    ok = major == 3 and 10 <= minor <= 12
    return {
        "name": "python",
        "status": "ok" if ok else "degraded",
        "detail": f"{major}.{minor}",
        "supported_range": "3.10-3.12",
    }


def binary_status(name: str) -> dict:
    path = shutil.which(name)
    return {
        "name": name,
        "status": "ok" if path else "degraded",
        "detail": path or "not-found",
    }


def session_memory_status() -> dict:
    cmd = [sys.executable, str(ROOT / "scripts" / "session_memory_store.py"), "health"]
    try:
        out = subprocess.check_output(cmd, stderr=subprocess.STDOUT, timeout=10)
        payload = json.loads(out.decode("utf-8"))
        detail = f"{payload.get('db', 'unknown')} (schema={payload.get('schema_version', 'unknown')})"
        return {"name": "session-memory-local", "status": "ok", "detail": detail}
    except Exception as exc:
        return {"name": "session-memory-local", "status": "degraded", "detail": str(exc)}


def parse_odoo_url() -> str | None:
    try:
        data = json.loads(MCP_FILE.read_text())
        return data.get("mcpServers", {}).get("odoo-knowledge", {}).get("url")
    except Exception:
        return None


def odoo_knowledge_status(offline: bool) -> dict:
    url = parse_odoo_url()
    if not url:
        return {"name": "odoo-knowledge", "status": "degraded", "detail": "missing-url"}
    if offline:
        return {"name": "odoo-knowledge", "status": "skipped", "detail": f"offline mode ({url})"}
    try:
        req = urllib.request.Request(url, method="GET")
        with urllib.request.urlopen(req, timeout=5) as resp:  # noqa: S310
            code = resp.getcode()
        return {"name": "odoo-knowledge", "status": "ok" if code < 500 else "degraded", "detail": f"http:{code}"}
    except urllib.error.URLError as exc:
        return {"name": "odoo-knowledge", "status": "degraded", "detail": str(exc)}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--offline", action="store_true", help="Skip remote odoo-knowledge network probe")
    args = parser.parse_args()

    checks = [
        python_status(),
        binary_status("code-review-graph"),
        session_memory_status(),
        odoo_knowledge_status(args.offline),
    ]

    failed = [c for c in checks if c["status"] == "degraded"]
    payload = {"status": "ok" if not failed else "degraded", "checks": checks}
    print(json.dumps(payload))
    return 0 if not failed else 2


if __name__ == "__main__":
    raise SystemExit(main())
