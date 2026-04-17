#!/usr/bin/env python3
"""Cross-platform launcher for repo-graph MCP stdio server."""

from __future__ import annotations

import os
import pathlib
import shlex
import shutil
import subprocess
import sys


def _load_config_env() -> None:
    config_dir = pathlib.Path(
        os.environ.get("CURSOR_ODOO_CONFIG_DIR", pathlib.Path.home() / ".cursor-odoo-development")
    )
    config_file = config_dir / "config.env"
    if not config_file.is_file():
        return

    for raw_line in config_file.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("export "):
            line = line[len("export ") :].strip()
        if "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip()
        if not key:
            continue
        if value:
            try:
                parsed = shlex.split(value, posix=True)
                if parsed:
                    value = parsed[0]
            except ValueError:
                value = value.strip('"\'')
        os.environ.setdefault(key, value)


def _find_git_toplevel(path: pathlib.Path) -> pathlib.Path | None:
    try:
        completed = subprocess.run(
            ["git", "-C", str(path), "rev-parse", "--show-toplevel"],
            check=False,
            capture_output=True,
            text=True,
            timeout=10,
        )
    except (FileNotFoundError, OSError, subprocess.TimeoutExpired):
        return None

    if completed.returncode != 0:
        return None

    top = (completed.stdout or "").strip()
    if not top:
        return None

    candidate = pathlib.Path(top).expanduser()
    if candidate.is_dir():
        return candidate.resolve()
    return None


def _detect_workspace() -> pathlib.Path:
    workspace = pathlib.Path(os.environ.get("CURSOR_WORKSPACE_PATH") or os.getcwd()).expanduser()
    if workspace.exists():
        return workspace.resolve()
    return pathlib.Path(os.getcwd()).resolve()


def _resolve_repo_graph_root() -> pathlib.Path:
    override = os.environ.get("CURSOR_REPO_GRAPH_ROOT")
    if override:
        override_path = pathlib.Path(override).expanduser()
        if override_path.is_dir():
            return override_path.resolve()

    workspace = _detect_workspace()
    git_toplevel = _find_git_toplevel(workspace)
    if git_toplevel:
        return git_toplevel
    return workspace


def main() -> int:
    _load_config_env()
    graph_root = _resolve_repo_graph_root()
    os.environ.setdefault("CURSOR_REPO_GRAPH_EFFECTIVE_ROOT", str(graph_root))
    os.chdir(graph_root)

    crg_binary = shutil.which("code-review-graph")
    if crg_binary:
        os.execvp(crg_binary, [crg_binary, "serve", "--transport", "stdio"])

    python_bin = os.environ.get("PYTHON_BIN") or sys.executable or "python"
    os.execvp(python_bin, [python_bin, "-m", "code_review_graph", "serve", "--transport", "stdio"])


if __name__ == "__main__":
    raise SystemExit(main())
