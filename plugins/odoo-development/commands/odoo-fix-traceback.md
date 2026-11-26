---
name: odoo-fix-traceback
description: fix the provided odoo traceback with minimal guessing.
---

Fix the provided Odoo traceback with minimal guessing.

**If odoo-codemode is unavailable:** Use Read/Grep. Proceed—do not block.

Workflow:
1. Locate the first meaningful application frame.
2. Classify the issue.
3. Prefer `codemode_search` → `codemode_execute` for schema/XML IDs/source before proposing a fix.
4. Apply the minimal fix.

Output:
- Root cause
- Minimal fix
- Files to change
- Validation steps
