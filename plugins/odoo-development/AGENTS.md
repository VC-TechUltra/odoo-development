# Odoo Project Instructions

- Detect target Odoo version before generating code (`${ODOO_VERSION}` or nearest `__manifest__.py`). Primary support: **16–19**.
- Prefer slim local rules + `skills/odoo-invariants.md` (verified on v16–v19) for stable syntax (cheaper than an MCP roundtrip).
- For schema, XML IDs, dependencies, and multi-fact research: use `odoo-codemode` with pinned `version` (`v16`|`v17`|`v18`|`v19`) — `codemode_search` → `codemode_execute`, prefer `odoo.compact.*` helpers.
- Reuse repository patterns before introducing new abstractions.
- Keep changes minimal, upgrade-safe, and security-aware.
- Do not invent fields, XML IDs, groups, or dependencies when MCP can confirm them.
