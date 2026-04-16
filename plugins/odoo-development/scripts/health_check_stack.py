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


def mk_check(name: str, status: str, detail: str, code: str, action: str) -> dict:
    return {
        "name": name,
        "status": status,
        "detail": detail,
        "code": code,
        "recommended_action": action,
    }


def python_status() -> dict:
    major, minor = sys.version_info[:2]
    ok = major == 3 and 10 <= minor <= 12
    if ok:
        return mk_check("python", "ok", f"{major}.{minor}", "PYTHON_OK", "No action needed")
    return mk_check(
        "python",
        "degraded",
        f"{major}.{minor}",
        "PYTHON_UNSUPPORTED",
        "Install/use Python 3.10-3.12 and rerun bootstrap",
    )


def binary_status(name: str) -> dict:
    path = shutil.which(name)
    if path:
        return mk_check(name, "ok", path, "BINARY_OK", "No action needed")
    return mk_check(name, "degraded", "not-found", "BINARY_NOT_FOUND", f"Install {name} or rerun bootstrap")


def session_memory_status() -> dict:
    cmd = [sys.executable, str(ROOT / "scripts" / "session_memory_store.py"), "health"]
    try:
        out = subprocess.check_output(cmd, stderr=subprocess.STDOUT, timeout=10)
        payload = json.loads(out.decode("utf-8"))
        detail = f"{payload.get('db', 'unknown')} (schema={payload.get('schema_version', 'unknown')})"
        return mk_check("session-memory-local", "ok", detail, "SESSION_MEMORY_OK", "No action needed")
    except Exception as exc:
        return mk_check(
            "session-memory-local",
            "degraded",
            str(exc),
            "SESSION_MEMORY_UNAVAILABLE",
            "Check writable user-home config path and rerun session init",
        )


def parse_odoo_url() -> str | None:
    try:
        data = json.loads(MCP_FILE.read_text())
        return data.get("mcpServers", {}).get("odoo-knowledge", {}).get("url")
    except Exception:
        return None


def odoo_knowledge_status(offline: bool) -> dict:
    url = parse_odoo_url()
    if not url:
        return mk_check("odoo-knowledge", "degraded", "missing-url", "ODOO_URL_MISSING", "Set mcpServers.odoo-knowledge.url")
    if offline:
        return mk_check("odoo-knowledge", "skipped", f"offline mode ({url})", "ODOO_OFFLINE_SKIPPED", "Run without --offline when network is available")
    try:
        req = urllib.request.Request(url, method="GET")
        with urllib.request.urlopen(req, timeout=5) as resp:  # noqa: S310
            code = resp.getcode()
        status = "ok" if code < 500 else "degraded"
        return mk_check(
            "odoo-knowledge",
            status,
            f"http:{code}",
            "ODOO_HTTP_OK" if status == "ok" else "ODOO_HTTP_5XX",
            "Check endpoint health and network route" if status != "ok" else "No action needed",
        )
    except urllib.error.URLError as exc:
        return mk_check(
            "odoo-knowledge",
            "degraded",
            str(exc),
            "ODOO_UNREACHABLE",
            "Continue in degraded mode and retry when endpoint/network is available",
        )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--offline", action="store_true", help="Skip remote odoo-knowledge network probe")
    parser.add_argument("--strict-local", action="store_true", help="Fail only on core local components (python + session-memory-local)")
    args = parser.parse_args()

    checks = [
        python_status(),
        binary_status("code-review-graph"),
        session_memory_status(),
        odoo_knowledge_status(args.offline),
    ]

    if args.strict_local:
        failed = [c for c in checks if c["status"] == "degraded" and c["name"] in {"python", "session-memory-local"}]
    else:
        failed = [c for c in checks if c["status"] == "degraded"]

    payload = {
        "status": "ok" if not failed else "degraded",
        "mode": "strict-local" if args.strict_local else "full",
        "checks": checks,
        "failed_count": len(failed),
    }
    print(json.dumps(payload))
    return 0 if not failed else 2


if __name__ == "__main__":
    raise SystemExit(main())
