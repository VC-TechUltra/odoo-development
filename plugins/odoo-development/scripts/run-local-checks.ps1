$ErrorActionPreference = 'Stop'

python -m py_compile scripts/session_memory_store.py scripts/session_memory_mcp.py

python -m unittest discover -q tests

# shell scripts may not be executable on Windows runners; validate via bash if available
$bash = Get-Command bash -ErrorAction SilentlyContinue
if ($bash) {
    bash -n scripts/bootstrap-env.sh scripts/run-repo-graph-mcp.sh scripts/run-session-memory-mcp.sh scripts/test-session-memory-store.sh hooks/session-start-bootstrap.sh
    bash ./scripts/test-session-memory-store.sh
    bash ./scripts/validate-command-read-paths.sh
}

pwsh -NoProfile -ExecutionPolicy Bypass -File ./scripts/test-session-memory-store.ps1
python ./scripts/health_check_stack.py --offline --strict-local
