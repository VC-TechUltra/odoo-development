---
name: odoo-health-check
description: verify odoo-knowledge MCP, repo-graph-local MCP, and local bootstrap runtime.
---

Run a comprehensive health check.

Primary flow:
1. Execute `python scripts/health_check_stack.py` (or `--offline` for local-only checks, `--strict-local` for CI gating on core local components).
2. Report status for:
   - Python runtime (3.10-3.12 policy)
   - `code-review-graph` availability
   - `session-memory-local` store health
   - `odoo-knowledge` reachability
3. If degraded, continue with available components and clearly list what is skipped.

Checks:
- Python runtime in supported range (3.10-3.12)
- code-review-graph availability (latest preferred, LKG fallback)
- `repo-graph-local` availability
- `odoo-knowledge` connectivity

Return:
- Pass/degraded/fail per component
- Auto-remediation actions already attempted
- Suggested next step without blocking development
