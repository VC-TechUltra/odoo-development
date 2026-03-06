---
name: odoo-migrate
description: migrate the selected odoo code to the target version with mcp-backed verification.
---

Migrate the selected Odoo code to the target version with MCP-backed verification.

**If odoo-knowledge MCP is unavailable:** Use built-in SemanticSearch, Grep, and Read tools to find patterns. Proceed with migration—do not block.

Workflow:
1. Confirm source and target version.
2. Identify version-sensitive Python, XML, security, manifest, and OWL areas.
3. Use `search_odoo_codebase`, `read_odoo_file`, `get_model_dependencies`, and `get_odoo_development_guidelines`.
4. For Odoo 18/19 Community and Enterprise, verify replacement patterns through MCP before proposing code.
5. Provide minimal migration patches.
