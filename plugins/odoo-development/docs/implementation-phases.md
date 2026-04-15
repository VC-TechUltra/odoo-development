# Local Repo Graph + Session Memory Implementation Phases

## Phase 0 — Decisions and contracts
- Freeze bootstrap/runtime policy
- Freeze Python version range (3.10-3.12)
- Freeze user-home config/data location
- Freeze fallback behavior (latest -> LKG -> degraded continuation)

## Phase 1 — Foundation (completed)
- Add cross-platform bootstrap scripts
- Add session start bootstrap hook
- Add repo graph MCP launcher wrapper
- Add session/repo lifecycle commands
- Update docs for setup and runtime behavior

## Phase 2 — Session memory MCP integration (in progress)
- Add `session-memory-local` MCP server process and tool contract
- Namespace by workspace + branch + session id
- Persist across restart with TTL 48h and manual clear

## Phase 3 — Hardening and rollout
- Add diagnostics and richer health checks
- Add branch switch auto-rotation verification
- Add cross-platform acceptance checks and troubleshooting matrix
