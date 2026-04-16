#!/usr/bin/env bash
set -euo pipefail

python3 -m py_compile \
  scripts/session_memory_store.py \
  scripts/session_memory_mcp.py

bash -n \
  scripts/bootstrap-env.sh \
  scripts/run-repo-graph-mcp.sh \
  scripts/run-session-memory-mcp.sh \
  scripts/test-session-memory-store.sh \
  hooks/session-start-bootstrap.sh

python3 -m unittest discover -q tests
./scripts/test-session-memory-store.sh
python3 scripts/verify_branch_rotation.py
./scripts/validate-command-read-paths.sh
python3 scripts/health_check_stack.py --offline --strict-local
