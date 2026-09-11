---
name: odoo-module
description: create or extend an odoo module using repository patterns, with existence confirmed against the odoo index.
---

Create or extend an Odoo module using repository patterns, confirming against the index that anything you depend on exists.

**If odoo-knowledge MCP is unavailable:** Use built-in SemanticSearch, Grep, and Read tools to find patterns. Proceed with implementation—do not block.

Workflow:
1. Detect Odoo version.
2. Take module structure, field and view patterns from the odoo-development skills.
3. Escalate to MCP only to confirm existence before depending on it:
   - a model's fields or methods -> `get_odoo_model`
   - an XML ID you inherit -> `resolve_odoo_xml_id`
   - a module dependency -> `explain_odoo_dependencies`
4. Do not assert that a field, XML ID or dependency exists without that confirmation.
5. Produce the smallest complete patch set.

Output:
- Goal
- Confirmed facts
- Files to change
- Patch plan
- Security impact
- Upgrade impact
- Assumptions
