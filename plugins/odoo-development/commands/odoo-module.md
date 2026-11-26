---
name: odoo-module
description: create or extend an odoo module using repository patterns and mcp-code verification.
---

Create or extend an Odoo module using repository patterns and MCP-code verification.

**If odoo-codemode is unavailable:** Use Grep/Read and at most one versioned skill file. Proceed—do not block.

Workflow:
1. Detect Odoo version (`${ODOO_VERSION}` or nearest `__manifest__.py`).
2. Prefer slim local rules for stable syntax.
3. For schema/XML IDs/dependencies: `codemode_search` → `codemode_execute`.
4. Produce the smallest complete patch set.

Output:
- Goal
- Confirmed facts
- Files to change
- Patch plan
- Security impact
- Upgrade impact
- Assumptions
