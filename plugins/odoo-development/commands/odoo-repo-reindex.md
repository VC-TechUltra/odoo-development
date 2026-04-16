---
name: odoo-repo-reindex
description: trigger incremental local repository graph reindex for current branch/workspace.
---

Run incremental reindex for `repo-graph-local`.

Workflow:
1. Confirm repo graph tool availability.
2. Trigger incremental update for current workspace and branch.
3. Return index status + changed files summary.
4. If unavailable, continue with SemanticSearch/Grep/Read fallback.
