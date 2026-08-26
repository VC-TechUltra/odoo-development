---
name: odoo-fix-traceback
description: fix the provided odoo traceback with minimal guessing.
---

Fix the provided Odoo traceback with minimal guessing.

**If odoo-knowledge MCP is unavailable:** Use built-in Read and Grep tools to inspect files. Proceed with the fix—do not block.

Workflow:
1. Locate the first meaningful application frame.
2. Classify the issue against `skills/odoo-troubleshooting/`.
3. Read the failing source with `read_odoo_source_range`, passing explicit
   `start_line`/`end_line` around the frame (the default range is 200 lines).
4. Escalate further only to confirm existence: `get_odoo_model`,
   `resolve_odoo_xml_id`, `explain_odoo_dependencies`.
5. Propose the minimal fix.

Output:
- Root cause
- Minimal fix
- Files to change
- Validation steps
