#!/usr/bin/env bash
set -euo pipefail

PLUGIN_NAME="odoo-development"
CONFIG_DIR_DEFAULT="${HOME}/.cursor-${PLUGIN_NAME}"
CONFIG_DIR="${CURSOR_ODOO_CONFIG_DIR:-$CONFIG_DIR_DEFAULT}"
CONFIG_FILE="${CONFIG_DIR}/config.env"
LKG_FILE="${CONFIG_DIR}/lkg.env"

mkdir -p "$CONFIG_DIR"

load_config() {
  if [[ -f "$CONFIG_FILE" ]]; then
    # shellcheck disable=SC1090
    source "$CONFIG_FILE"
  fi
}

save_config() {
  cat > "$CONFIG_FILE" <<CFG
INSTALL_BASE=${INSTALL_BASE}
PYTHON_BIN=${PYTHON_BIN}
CFG
}

select_install_base() {
  if [[ -n "${INSTALL_BASE:-}" ]]; then
    return
  fi

  local default_base="${HOME}/.local/share/${PLUGIN_NAME}"
  if [[ -t 0 ]]; then
    printf "[odoo-development] Enter install/cache base path [%s]: " "$default_base" >&2
    read -r input_base || true
    INSTALL_BASE="${input_base:-$default_base}"
  else
    INSTALL_BASE="$default_base"
  fi

  mkdir -p "$INSTALL_BASE"
}

version_in_range() {
  local v="$1"
  local major minor patch
  IFS='.' read -r major minor patch <<<"$v"
  major=${major:-0}
  minor=${minor:-0}
  patch=${patch:-0}

  if [[ "$major" -ne 3 ]]; then
    return 1
  fi

  if [[ "$minor" -lt 10 || "$minor" -gt 12 ]]; then
    return 1
  fi

  return 0
}

version_gt() {
  local a="$1"
  local b="$2"
  python3 - "$a" "$b" <<'PY'
import sys

def parse(v: str):
    p = [int(x) for x in v.split('.')]
    while len(p) < 3:
        p.append(0)
    return tuple(p)

print("1" if parse(sys.argv[1]) > parse(sys.argv[2]) else "0")
PY
}

pick_python() {
  if [[ -n "${PYTHON_BIN:-}" && -x "${PYTHON_BIN}" ]]; then
    local existing_ver
    existing_ver="$($PYTHON_BIN -c 'import sys; print(".".join(map(str, sys.version_info[:3])))' 2>/dev/null || true)"
    if [[ -n "$existing_ver" ]] && version_in_range "$existing_ver"; then
      return
    fi
  fi

  local candidates=(python3.12 python3.11 python3.10 python3 py)
  local best_bin=""
  local best_ver=""

  for bin in "${candidates[@]}"; do
    if ! command -v "$bin" >/dev/null 2>&1; then
      continue
    fi

    local ver
    ver="$($bin -c 'import sys; print(".".join(map(str, sys.version_info[:3])))' 2>/dev/null || true)"
    [[ -n "$ver" ]] || continue

    version_in_range "$ver" || continue

    if [[ -z "$best_ver" || "$(version_gt "$ver" "$best_ver")" == "1" ]]; then
      best_bin="$(command -v "$bin")"
      best_ver="$ver"
    fi
  done

  if [[ -z "$best_bin" ]]; then
    echo "No local Python in supported range [3.10, 3.12]." >&2
    echo "Please install Python 3.10-3.12 and re-run setup." >&2
    exit 1
  fi

  PYTHON_BIN="$best_bin"
}

install_or_upgrade_crg() {
  "$PYTHON_BIN" -m pip install --user --upgrade code-review-graph >/dev/null 2>&1 || {
    echo "Failed to install/upgrade code-review-graph." >&2
    return 1
  }
}

resolve_crg_version() {
  "$PYTHON_BIN" - <<'PY'
import importlib.metadata as md
try:
    print(md.version("code-review-graph"))
except Exception:
    print("")
PY
}

smoke_test_crg() {
  if command -v code-review-graph >/dev/null 2>&1; then
    code-review-graph --help >/dev/null 2>&1
    return $?
  fi

  "$PYTHON_BIN" -m code_review_graph --help >/dev/null 2>&1
}

load_lkg() {
  if [[ -f "$LKG_FILE" ]]; then
    # shellcheck disable=SC1090
    source "$LKG_FILE"
  fi
}

save_lkg() {
  cat > "$LKG_FILE" <<LKG
CRG_LKG_VERSION=${CRG_LKG_VERSION}
LKG
}

main() {
  load_config
  select_install_base
  pick_python

  save_config

  install_or_upgrade_crg || true

  local current_version
  current_version="$(resolve_crg_version)"

  if smoke_test_crg; then
    if [[ -n "$current_version" ]]; then
      CRG_LKG_VERSION="$current_version"
      save_lkg
    fi
    cat <<JSON
{"status":"ok","python":"$PYTHON_BIN","codeReviewGraphVersion":"${current_version}","installBase":"$INSTALL_BASE"}
JSON
    exit 0
  fi

  load_lkg
  if [[ -n "${CRG_LKG_VERSION:-}" ]]; then
    "$PYTHON_BIN" -m pip install --user --upgrade "code-review-graph==${CRG_LKG_VERSION}" >/dev/null 2>&1 || true
    if smoke_test_crg; then
      cat <<JSON
{"status":"degraded","reason":"latest_failed_using_lkg","python":"$PYTHON_BIN","codeReviewGraphVersion":"${CRG_LKG_VERSION}","installBase":"$INSTALL_BASE"}
JSON
      exit 0
    fi
  fi

  cat <<JSON
{"status":"degraded","reason":"code_review_graph_unavailable","python":"$PYTHON_BIN","installBase":"$INSTALL_BASE"}
JSON
}

main "$@"
