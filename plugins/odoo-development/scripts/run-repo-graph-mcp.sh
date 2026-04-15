#!/usr/bin/env bash
set -euo pipefail

CONFIG_DIR="${CURSOR_ODOO_CONFIG_DIR:-${HOME}/.cursor-odoo-development}"
CONFIG_FILE="${CONFIG_DIR}/config.env"

if [[ -f "$CONFIG_FILE" ]]; then
  # shellcheck disable=SC1090
  source "$CONFIG_FILE"
fi

PYTHON_BIN="${PYTHON_BIN:-python3}"

if command -v code-review-graph >/dev/null 2>&1; then
  exec code-review-graph serve --transport stdio
fi

exec "$PYTHON_BIN" -m code_review_graph serve --transport stdio
