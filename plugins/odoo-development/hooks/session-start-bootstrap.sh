#!/usr/bin/env sh
set -eu

SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
PLUGIN_ROOT=$(CDPATH= cd -- "${SCRIPT_DIR}/.." && pwd)

BOOTSTRAP_JSON=''
MEMORY_JSON=''
WORKSPACE_PATH="${CURSOR_WORKSPACE_PATH:-$(pwd)}"
SESSION_ID="${CURSOR_SESSION_ID:-session-$(date +%s)}"
BRANCH="${CURSOR_GIT_BRANCH:-}"

if [ -z "$BRANCH" ]; then
  BRANCH=$(git -C "$WORKSPACE_PATH" rev-parse --abbrev-ref HEAD 2>/dev/null || echo unknown)
fi

case "$(uname -s 2>/dev/null || echo unknown)" in
  MINGW*|MSYS*|CYGWIN*)
    if command -v pwsh >/dev/null 2>&1; then
      BOOTSTRAP_JSON=$(pwsh -NoProfile -ExecutionPolicy Bypass -File "${PLUGIN_ROOT}/scripts/bootstrap-env.ps1" 2>/dev/null || true)
    elif command -v powershell >/dev/null 2>&1; then
      BOOTSTRAP_JSON=$(powershell -NoProfile -ExecutionPolicy Bypass -File "${PLUGIN_ROOT}/scripts/bootstrap-env.ps1" 2>/dev/null || true)
    fi
    ;;
  *)
    BOOTSTRAP_JSON=$("${PLUGIN_ROOT}/scripts/bootstrap-env.sh" 2>/dev/null || true)
    ;;
esac

if [ -x "${PLUGIN_ROOT}/scripts/session_memory_store.py" ]; then
  MEMORY_JSON=$("${PLUGIN_ROOT}/scripts/session_memory_store.py" init --workspace "$WORKSPACE_PATH" --branch "$BRANCH" --session-id "$SESSION_ID" --ttl-hours 48 2>/dev/null || true)
fi

if [ -n "$BOOTSTRAP_JSON" ] || [ -n "$MEMORY_JSON" ]; then
  if [ -z "$BOOTSTRAP_JSON" ]; then
    BOOTSTRAP_JSON='{"status":"degraded","reason":"bootstrap_not_available"}'
  fi
  if [ -z "$MEMORY_JSON" ]; then
    MEMORY_JSON='{"status":"degraded","reason":"session_memory_init_failed"}'
  fi
  printf '{"additional_context":"Session bootstrap complete. Prefer repo-graph-local for local context minimization, then verify with odoo-knowledge MCP. Session memory is scoped to workspace+branch+session with 48h TTL.","hookSpecificOutput":{"hookEventName":"sessionStart","bootstrap":%s,"sessionMemory":%s}}\n' "$BOOTSTRAP_JSON" "$MEMORY_JSON"
else
  printf '{"additional_context":"Bootstrap unavailable. Continue with available MCP tools and pure Cursor fallback if needed.","hookSpecificOutput":{"hookEventName":"sessionStart","bootstrap":{"status":"degraded","reason":"bootstrap_not_available"},"sessionMemory":{"status":"degraded","reason":"session_memory_unavailable"}}}\n'
fi
