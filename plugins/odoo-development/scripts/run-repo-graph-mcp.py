#!/usr/bin/env python3
"""Cross-platform launcher for repo-graph MCP stdio server."""

from __future__ import annotations

import os
import shlex
import shutil
import sys

from workspace_scope import resolve_effective_root


def _load_config_env() -> None:
    import pathlib

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


def main() -> int:
    _load_config_env()
    graph_root = resolve_effective_root()
    os.environ.setdefault("CURSOR_REPO_GRAPH_EFFECTIVE_ROOT", str(graph_root))
    os.chdir(graph_root)

    crg_binary = shutil.which("code-review-graph")
    if crg_binary:
        os.execvp(crg_binary, [crg_binary, "serve", "--transport", "stdio"])

    python_bin = os.environ.get("PYTHON_BIN") or sys.executable or "python"
    os.execvp(python_bin, [python_bin, "-m", "code_review_graph", "serve", "--transport", "stdio"])


if __name__ == "__main__":
    raise SystemExit(main())
