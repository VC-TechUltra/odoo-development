---
name: odoo-module
description: create or extend an odoo module using repository patterns and mcp verification.
---

Create or extend an Odoo module using repository patterns and MCP verification.

**If odoo-knowledge MCP is unavailable:** Use built-in SemanticSearch, Grep, and Read tools to find patterns. Proceed with implementation—do not block.

Workflow:
1. Detect Odoo version.
2. Use `search_odoo_codebase` or `code_search`.
3. Use `get_odoo_model_schema`, `get_model_dependencies`, and `get_odoo_development_guidelines`.
4. For Odoo 18/19 Community and Enterprise, verify version-specific behavior through MCP before writing code.
5. Produce the smallest complete patch set.

Output:
- Goal
- Confirmed facts
- Files to change
- Patch plan
- Security impact
- Upgrade impact
- Assumptions
