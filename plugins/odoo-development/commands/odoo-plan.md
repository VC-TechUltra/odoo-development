---
name: odoo-plan
description: plan an odoo implementation before coding.
---

Plan an Odoo implementation before coding.

**If odoo-knowledge MCP is unavailable:** Use built-in SemanticSearch, Grep, and Read tools to inspect the codebase. Proceed with the plan—do not block.

Workflow:
1. Confirm target version and edition.
2. Take patterns and version differences from the odoo-development skills.
3. Escalate to MCP only to confirm what exists: model fields (`get_odoo_model`),
   XML IDs (`resolve_odoo_xml_id`), dependencies (`explain_odoo_dependencies`).
4. Produce a phased implementation plan.

Output:
- Scope
- Confirmed facts
- Open assumptions
- Files/components affected
- Risks
- Step-by-step plan
