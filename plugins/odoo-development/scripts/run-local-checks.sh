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

python3 -m unittest -q tests/test_session_memory_store.py
./scripts/test-session-memory-store.sh
./scripts/validate-command-read-paths.sh
