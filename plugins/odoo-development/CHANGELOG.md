# Changelog

## Unreleased
- Added cross-platform troubleshooting matrix doc for local MCP/session-memory failures (`docs/troubleshooting-matrix.md`).
- Linked troubleshooting guidance in README and marked troubleshooting matrix milestone complete in phase plan.
- Added `--strict-local` mode to `health_check_stack.py` so local/CI checks fail only on core local components.
- Updated check runners and docs to use strict-local health gating by default.
- Added health-check test coverage for strict-local behavior.
- Added MCP adapter tests for successful `tools/call` content shape and initialized-notification handling.
- Updated implementation phase doc: Phase 2 completed, Phase 3 in progress.
- Added session memory schema metadata (`schema_version`) in the local SQLite store and surfaced it in health reporting.
- Added unittest coverage for oversized-memory rejection and health schema detail assertions.
- Added unit tests for MCP adapter request handling (`tests/test_session_memory_mcp.py`).
- Added unit test for consolidated health checker JSON output (`tests/test_health_check_stack.py`).
- Updated local check runners to execute full unittest discovery in `tests/`.
- Added `scripts/health_check_stack.py` for consolidated stack health reporting (Python/tool/session-memory/odoo-knowledge).
- Updated local check runners and `/odoo-health-check` command guidance to use the new health checker.
- Added session memory guardrails to reject likely secret-bearing entries and oversized values.
- Added `.gitignore` for Python cache artifacts and local runtime/session DB files.
- Added unittest coverage for sensitive-content rejection in session memory writes.
- Expanded CI matrix to Ubuntu + Windows and Python 3.10/3.11/3.12 for plugin checks.
- Added Windows local verification runner (`scripts/run-local-checks.ps1`) and PowerShell smoke test (`scripts/test-session-memory-store.ps1`).
- Updated tests to use `sys.executable` for cross-platform interpreter compatibility.
- Added automated unittest coverage for session memory namespace lifecycle and branch isolation (`tests/test_session_memory_store.py`).
- Added consolidated local verification runner (`scripts/run-local-checks.sh`).
- Added GitHub Actions workflow for plugin checks (`.github/workflows/odoo-plugin-checks.yml`).
- Added `namespace_info` session-memory tool and CLI command for branch/workspace/session namespace inspection.
- Added `scripts/test-session-memory-store.sh` smoke test to validate init/list/namespace-info/clear lifecycle.
- Added automatic expired-namespace GC on memory store startup.
- Added local `session-memory-local` MCP server wiring with stdio wrapper and minimal MCP tool surface (`session_init`, `memory_put`, `memory_list`, `memory_summary`, `memory_clear`).
- Added file-backed session memory store (`scripts/session_memory_store.py`) with workspace+branch+session namespace scoping and 48h TTL initialization support.
- Extended session start hook to initialize session memory namespace automatically at startup.
- Added bootstrap scripts for silent local tool setup with first-run path selection and Python 3.10-3.12 auto-selection.
- Added `repo-graph-local` MCP wiring and launcher wrapper for code-review-graph stdio mode.
- Added session lifecycle commands (`/odoo-session-start`, `/odoo-session-summary`, `/odoo-session-clear`, `/odoo-repo-reindex`, `/odoo-health-check`).
- Added `hooks/session-start-bootstrap.sh` and updated hook configs to run bootstrap at session start.
- Updated README MCP URL default and documented bootstrap/fallback policy.
- Added `agents/odoo-query-optimizer.md` for Odoo ORM/query performance diagnostics.
- Added `/odoo-optimize` command for performance-oriented analysis workflows.
- Synced command and agent inventory documentation in `README.md` and `SKILL.md`.
- Added explicit MCP tool-sequencing guidance to optimization agent/command flows.

## 1.0.0
- First Cursor marketplace-oriented build
- Added `.cursor-plugin/plugin.json`
- Added plugin-local `hooks/hooks.json`
- Added marketplace manifest at `plugins/.cursor-plugin/marketplace.json`
- Added command frontmatter
- Embedded MCP-first policy for Odoo 18/19 Community and Enterprise
