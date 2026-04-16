---
name: odoo-session-start
description: bootstrap local tooling, start/recheck repo graph, and initialize workspace+branch session memory scope.
---

Initialize the current workspace session.

Workflow:
1. Run bootstrap checks (Python 3.10-3.12, code-review-graph install/upgrade).
2. Confirm `repo-graph-local` health.
3. Record session scope key using workspace + branch + session id.
4. Continue in degraded mode if any subsystem is unavailable.

Output:
- Bootstrap status
- Active Python/runtime details
- Repo graph status
- Session namespace details
- Degraded-mode notes (if any)
