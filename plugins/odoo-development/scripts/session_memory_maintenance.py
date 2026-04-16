#!/usr/bin/env python3
"""Maintenance utility for local session memory store."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STORE = ROOT / "scripts" / "session_memory_store.py"


def run(command: str) -> dict:
    try:
        proc = subprocess.run(
            [sys.executable, str(STORE), command],
            capture_output=True,
            text=True,
            check=False,
        )
    except OSError as exc:
        return {
            "status": "error",
            "command": command,
            "error": f"unable to execute store script: {exc}",
        }

    output = (proc.stdout or proc.stderr or "").strip()
    if not output:
        return {
            "status": "error",
            "command": command,
            "error": "store script returned no output",
            "exit_code": proc.returncode,
        }

    try:
        payload = json.loads(output)
    except json.JSONDecodeError:
        return {
            "status": "error",
            "command": command,
            "error": "store script returned invalid JSON",
            "raw_output": output,
            "exit_code": proc.returncode,
        }

    if proc.returncode != 0:
        payload = {
            "status": "error",
            "command": command,
            "exit_code": proc.returncode,
            "result": payload,
        }
    return payload


def main() -> int:
    gc_result = run("gc")
    health_result = run("health")
    status = "ok"
    if gc_result.get("status") != "ok" or health_result.get("status") != "ok":
        status = "error"
    payload = {
        "status": status,
        "gc": gc_result,
        "health": health_result,
    }
    print(json.dumps(payload))
    return 0 if status == "ok" else 1


if __name__ == "__main__":
    raise SystemExit(main())
