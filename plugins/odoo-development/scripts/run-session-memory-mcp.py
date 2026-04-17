#!/usr/bin/env python3
"""Cross-platform launcher for session-memory MCP stdio server."""

from __future__ import annotations

import os
import pathlib
import shlex
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


def main() -> int:
    _load_config_env()
    plugin_root = pathlib.Path(__file__).resolve().parents[1]
    python_bin = os.environ.get("PYTHON_BIN") or sys.executable or "python"
    target = plugin_root / "scripts" / "session_memory_mcp.py"
    os.execvp(python_bin, [python_bin, str(target)])


if __name__ == "__main__":
    raise SystemExit(main())
