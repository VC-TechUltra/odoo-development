#!/usr/bin/env python3
"""Workspace/repository scope resolution helpers for MCP launchers and hooks."""

from __future__ import annotations

import os
import pathlib
import subprocess


def find_git_toplevel(path: pathlib.Path) -> pathlib.Path | None:
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


def detect_workspace() -> pathlib.Path:
    workspace = pathlib.Path(os.environ.get("CURSOR_WORKSPACE_PATH") or os.getcwd()).expanduser()
    if workspace.exists():
        return workspace.resolve()
    return pathlib.Path(os.getcwd()).resolve()


def resolve_effective_root() -> pathlib.Path:
    for env_key in ("CURSOR_ACTIVE_REPO_PATH", "CURSOR_REPO_GRAPH_ROOT"):
        override = os.environ.get(env_key)
        if not override:
            continue
        override_path = pathlib.Path(override).expanduser()
        if override_path.is_dir():
            return override_path.resolve()

    workspace = detect_workspace()
    git_toplevel = find_git_toplevel(workspace)
    if git_toplevel:
        return git_toplevel
    return workspace


def detect_branch(path: pathlib.Path) -> str:
    branch = os.environ.get("CURSOR_GIT_BRANCH")
    if branch:
        return branch

    try:
        completed = subprocess.run(
            ["git", "-C", str(path), "rev-parse", "--abbrev-ref", "HEAD"],
            check=False,
            capture_output=True,
            text=True,
            timeout=10,
        )
    except (FileNotFoundError, OSError, subprocess.TimeoutExpired):
        return "workspace"

    candidate = (completed.stdout or "").strip()
    return candidate or "workspace"
