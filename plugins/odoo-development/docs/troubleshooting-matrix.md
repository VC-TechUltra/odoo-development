# Troubleshooting Matrix (Local MCP + Session Memory)

## Quick diagnosis flow
1. Run `python scripts/health_check_stack.py --offline --strict-local`.
2. If degraded, run `./scripts/run-local-checks.sh` (or `./scripts/run-local-checks.ps1`).
3. Apply the fix for the first failing component from the matrix below.

Each health check now includes a machine-readable `code` and `recommended_action` field to support deterministic remediation automation.

## Matrix

| Symptom | Likely cause | Verification | Resolution |
|---|---|---|---|
| `python` degraded | Unsupported Python version | `python --version` and health checker output | Install/use Python 3.10-3.12 and rerun bootstrap |
| `code-review-graph` not found | Local binary not installed/visible on PATH | `which code-review-graph` / `Get-Command code-review-graph` | Re-run bootstrap scripts to install latest and refresh PATH |
| `session-memory-local` degraded | DB path permissions or runtime errors | `python scripts/session_memory_store.py health` | Ensure writable user-home config path and rerun init |
| Session memory write returns `status:error` | Sensitive marker or oversize payload blocked | `python scripts/session_memory_store.py put ...` response | Store only non-secret compact notes (<=2000 chars) |
| Hook bootstrap degraded | Missing shell/runtime on host | inspect `hooks/session-start-bootstrap.sh` output | Install Git Bash/WSL on Windows or use PowerShell runners |
| `odoo-knowledge` unreachable | Remote MCP URL unavailable/network issue | Run health without `--offline` | Continue in degraded mode and use local tools until endpoint recovers |
| CI Windows failures only | Bash-specific checks unavailable | Review Windows job logs and PowerShell runner | Use `scripts/run-local-checks.ps1` and ensure `pwsh` script dependencies are met |

## Branch/session isolation sanity checks
- Validate namespace metadata:
  - `python scripts/session_memory_store.py namespace-info --workspace <path> --branch <branch> --session-id <id>`
- Clear namespace explicitly:
  - `python scripts/session_memory_store.py clear --workspace <path> --branch <branch> --session-id <id>`

## Safe fallback policy
When one component fails:
- Keep remaining local components active.
- Skip only failing subsystems.
- Continue work with Cursor native tools (`Read`, `Grep`, `Glob`) plus reachable MCPs.
