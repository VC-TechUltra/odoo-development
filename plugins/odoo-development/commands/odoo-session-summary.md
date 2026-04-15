---
name: odoo-session-summary
description: return compact summary of current session memory and unresolved items for this workspace/branch.
---

Return a compact summary for the active session namespace.

Include:
- Current scope (workspace, branch, session)
- Confirmed decisions
- Open items
- Next recommended actions

If session memory is unavailable, infer summary from current chat + repository context and mark as fallback.
