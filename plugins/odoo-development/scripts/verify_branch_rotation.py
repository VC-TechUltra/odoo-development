#!/usr/bin/env python3
"""Verify branch-scoped namespace rotation semantics for session memory."""

from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STORE = ROOT / "scripts" / "session_memory_store.py"


def run(env: dict[str, str], *args: str) -> dict:
    out = subprocess.check_output([sys.executable, str(STORE), *args], env=env)
    return json.loads(out.decode("utf-8"))


def main() -> int:
    with tempfile.TemporaryDirectory() as tmp:
        env = os.environ.copy()
        env["CURSOR_ODOO_CONFIG_DIR"] = tmp
        workspace = str(Path(tmp) / "repo")
        Path(workspace).mkdir(parents=True, exist_ok=True)

        ns_main = run(env, "init", "--workspace", workspace, "--branch", "main", "--session-id", "s1")
        ns_feat = run(env, "init", "--workspace", workspace, "--branch", "feature-x", "--session-id", "s1")

        if ns_main["namespace_key"] == ns_feat["namespace_key"]:
            print(json.dumps({"status": "error", "reason": "namespace_key_collision"}))
            return 2

        run(env, "put", "--workspace", workspace, "--branch", "main", "--session-id", "s1", "--key", "k", "--value", "main-v")
        run(env, "put", "--workspace", workspace, "--branch", "feature-x", "--session-id", "s1", "--key", "k", "--value", "feature-v")

        sum_main = run(env, "summary", "--workspace", workspace, "--branch", "main", "--session-id", "s1")
        sum_feat = run(env, "summary", "--workspace", workspace, "--branch", "feature-x", "--session-id", "s1")

        if "main-v" not in sum_main["summary"] or "feature-v" in sum_main["summary"]:
            print(json.dumps({"status": "error", "reason": "main_branch_isolation_failed"}))
            return 2

        if "feature-v" not in sum_feat["summary"] or "main-v" in sum_feat["summary"]:
            print(json.dumps({"status": "error", "reason": "feature_branch_isolation_failed"}))
            return 2

        print(json.dumps({"status": "ok", "checked": ["namespace_rotation", "branch_isolation"]}))
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
