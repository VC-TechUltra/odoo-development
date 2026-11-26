# Odoo Project Instructions

- Detect target Odoo version before generating code (`${ODOO_VERSION}` or nearest `__manifest__.py`).
- Prefer slim local rules/skills for stable syntax (cheaper than an MCP roundtrip).
- For schema, XML IDs, dependencies, and multi-fact research on Odoo 18/19 CE/EE: use `odoo-codemode` (`codemode_search` → `codemode_execute`).
- Reuse repository patterns before introducing new abstractions.
- Keep changes minimal, upgrade-safe, and security-aware.
- Do not invent fields, XML IDs, groups, or dependencies when MCP can confirm them.
