---
name: odoo-review
description: review the selected odoo code for correctness, security, maintainability, and upgrade safety.
---

Review the selected Odoo code for correctness, security, maintainability, and upgrade safety.

**If odoo-knowledge MCP is unavailable:** Use built-in SemanticSearch, Grep, and Read tools. Proceed with the review—do not block.

Before reviewing:
- Detect version.
- Review against the patterns in the odoo-development skills.
- Escalate to MCP only to confirm a referenced field, XML ID, method override
  or access rule actually exists in the target version.

Output:
- Critical
- High
- Medium
- Low
- Suggested patch strategy
