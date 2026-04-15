#!/usr/bin/env bash
set -euo pipefail

CONFIG_DIR="${CURSOR_ODOO_CONFIG_DIR:-${HOME}/.cursor-odoo-development}"
CONFIG_FILE="${CONFIG_DIR}/config.env"

if [[ -f "$CONFIG_FILE" ]]; then
  # shellcheck disable=SC1090
  source "$CONFIG_FILE"
fi

PYTHON_BIN="${PYTHON_BIN:-python3}"
exec "$PYTHON_BIN" ./scripts/session_memory_mcp.py
