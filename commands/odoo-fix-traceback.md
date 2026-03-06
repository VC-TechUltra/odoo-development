---
name: odoo-fix-traceback
description: fix the provided odoo traceback with minimal guessing.
---

Fix the provided Odoo traceback with minimal guessing.

Workflow:
1. Locate the first meaningful application frame.
2. Classify the issue.
3. Use `read_odoo_file` or `get_file_snippet`.
4. Use `get_odoo_model_schema`, `get_odoo_xml_id_location`, and `get_model_dependencies` before proposing a fix.
5. For Odoo 18/19 Community and Enterprise, verify framework-specific fixes through MCP.

Output:
- Root cause
- Minimal fix
- Files to change
- Validation steps
