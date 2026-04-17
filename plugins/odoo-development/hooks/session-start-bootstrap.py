#!/usr/bin/env python3
"""Cross-platform sessionStart hook for bootstrap + memory initialization."""

from __future__ import annotations

import json
import os
import pathlib
import platform
import subprocess
import sys
import time

SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
PLUGIN_ROOT = SCRIPT_DIR.parent
sys.path.insert(0, str(PLUGIN_ROOT / "scripts"))

from workspace_scope import detect_branch, resolve_effective_root


def _run_json_command(cmd: list[str]) -> dict | None:
    try:
        completed = subprocess.run(
            cmd,
            check=False,
            capture_output=True,
            text=True,
            timeout=60,
        )
    except (FileNotFoundError, subprocess.TimeoutExpired, OSError):
        return None

    output = (completed.stdout or "").strip()
    if not output:
        return None

    for line in reversed(output.splitlines()):
        line = line.strip()
        if not line:
            continue
        try:
            value = json.loads(line)
        except json.JSONDecodeError:
            continue
        if isinstance(value, dict):
            return value
    return None


def _bootstrap_status(plugin_root: pathlib.Path) -> dict | None:
    scripts_dir = plugin_root / "scripts"
    is_windows = platform.system().lower().startswith("win")

    if is_windows:
        for shell in ("pwsh", "powershell"):
            result = _run_json_command(
                [
                    shell,
                    "-NoProfile",
                    "-ExecutionPolicy",
                    "Bypass",
                    "-File",
                    str(scripts_dir / "bootstrap-env.ps1"),
                ]
            )
            if result:
                return result
        return None

    return _run_json_command([str(scripts_dir / "bootstrap-env.sh")])


def _memory_status(plugin_root: pathlib.Path, workspace_path: str, branch: str, session_id: str) -> dict | None:
    store = plugin_root / "scripts" / "session_memory_store.py"
    if not store.is_file():
        return None
    return _run_json_command(
        [
            str(store),
            "init",
            "--workspace",
            workspace_path,
            "--branch",
            branch,
            "--session-id",
            session_id,
            "--ttl-hours",
            "48",
        ]
    )


def main() -> int:
    plugin_root = PLUGIN_ROOT
    effective_root = resolve_effective_root()
    workspace_path = str(effective_root)
    session_id = os.environ.get("CURSOR_SESSION_ID") or f"session-{int(time.time())}"
    branch = detect_branch(effective_root)

    bootstrap = _bootstrap_status(plugin_root) or {
        "status": "degraded",
        "reason": "bootstrap_not_available",
    }
    memory = _memory_status(plugin_root, workspace_path, branch, session_id) or {
        "status": "degraded",
        "reason": "session_memory_init_failed",
    }

    if bootstrap.get("status") == "degraded" and memory.get("status") == "degraded":
        additional_context = "Bootstrap unavailable. Continue with available MCP tools and pure Cursor fallback if needed."
    else:
        additional_context = (
            "Session bootstrap complete. Prefer repo-graph-local for local context minimization, "
            "then verify with odoo-knowledge MCP. Session memory is scoped to workspace+branch+session with 48h TTL."
        )

    payload = {
        "additional_context": additional_context,
        "hookSpecificOutput": {
            "hookEventName": "sessionStart",
            "bootstrap": bootstrap,
            "sessionMemory": memory,
            "effectiveScope": {
                "workspace": workspace_path,
                "branch": branch,
            },
        },
    }
    print(json.dumps(payload))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
