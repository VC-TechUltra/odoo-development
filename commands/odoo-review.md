---
name: odoo-review
description: review the selected odoo code for correctness, security, maintainability, and upgrade safety.
---

Review the selected Odoo code for correctness, security, maintainability, and upgrade safety.

Before reviewing:
- Detect version.
- Use `search_odoo_codebase` or `code_search`.
- Use `get_odoo_model_schema`, `get_odoo_xml_id_location`, and `get_model_dependencies` where relevant.
- For Odoo 18/19 Community and Enterprise, validate version-specific concerns through MCP.

Output:
- Critical
- High
- Medium
- Low
- Suggested patch strategy
