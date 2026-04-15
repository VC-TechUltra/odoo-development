#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
STORE="$ROOT_DIR/scripts/session_memory_store.py"

WORKSPACE="/tmp/odoo-mem-test"
BRANCH="feature-test"
SESSION_ID="sess-123"

INIT_JSON=$($STORE init --workspace "$WORKSPACE" --branch "$BRANCH" --session-id "$SESSION_ID" --ttl-hours 48)
python3 - "$INIT_JSON" <<'PY'
import json, sys
obj=json.loads(sys.argv[1])
assert obj["status"] == "ok"
assert obj["workspace"] == "/tmp/odoo-mem-test"
assert obj["branch"] == "feature-test"
PY

$STORE put --workspace "$WORKSPACE" --branch "$BRANCH" --session-id "$SESSION_ID" --key decision --value "phase3-test" --kind note >/dev/null
LIST_JSON=$($STORE list --workspace "$WORKSPACE" --branch "$BRANCH" --session-id "$SESSION_ID" --limit 5)
python3 - "$LIST_JSON" <<'PY'
import json, sys
obj=json.loads(sys.argv[1])
assert obj["status"] == "ok"
assert len(obj["items"]) >= 1
assert obj["items"][0]["key"] == "decision"
PY

NS_JSON=$($STORE namespace-info --workspace "$WORKSPACE" --branch "$BRANCH" --session-id "$SESSION_ID")
python3 - "$NS_JSON" <<'PY'
import json, sys
obj=json.loads(sys.argv[1])
assert obj["status"] == "ok"
assert obj["branch"] == "feature-test"
PY

$STORE clear --workspace "$WORKSPACE" --branch "$BRANCH" --session-id "$SESSION_ID" >/dev/null
