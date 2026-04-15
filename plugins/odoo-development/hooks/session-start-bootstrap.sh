#!/usr/bin/env sh
set -eu

BOOTSTRAP_JSON=''

case "$(uname -s 2>/dev/null || echo unknown)" in
  MINGW*|MSYS*|CYGWIN*)
    if command -v pwsh >/dev/null 2>&1; then
      BOOTSTRAP_JSON=$(pwsh -NoProfile -ExecutionPolicy Bypass -File ./scripts/bootstrap-env.ps1 2>/dev/null || true)
    elif command -v powershell >/dev/null 2>&1; then
      BOOTSTRAP_JSON=$(powershell -NoProfile -ExecutionPolicy Bypass -File ./scripts/bootstrap-env.ps1 2>/dev/null || true)
    fi
    ;;
  *)
    BOOTSTRAP_JSON=$(./scripts/bootstrap-env.sh 2>/dev/null || true)
    ;;
esac

if [ -n "$BOOTSTRAP_JSON" ]; then
  printf '{"additional_context":"Session bootstrap complete. Prefer repo-graph-local for local context minimization, then verify with odoo-knowledge MCP.","hookSpecificOutput":{"hookEventName":"sessionStart","bootstrap":%s}}\n' "$BOOTSTRAP_JSON"
else
  printf '{"additional_context":"Bootstrap unavailable. Continue with available MCP tools and pure Cursor fallback if needed.","hookSpecificOutput":{"hookEventName":"sessionStart","bootstrap":{"status":"degraded","reason":"bootstrap_not_available"}}}\n'
fi
