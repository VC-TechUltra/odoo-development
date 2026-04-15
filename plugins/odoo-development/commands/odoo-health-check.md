---
name: odoo-health-check
description: verify odoo-knowledge MCP, repo-graph-local MCP, and local bootstrap runtime.
---

Run a comprehensive health check.

Checks:
- Python runtime in supported range (3.10-3.12)
- code-review-graph availability (latest preferred, LKG fallback)
- `repo-graph-local` availability
- `odoo-knowledge` connectivity

Return:
- Pass/degraded/fail per component
- Auto-remediation actions already attempted
- Suggested next step without blocking development
