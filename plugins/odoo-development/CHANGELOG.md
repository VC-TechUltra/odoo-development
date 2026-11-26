# Changelog

## 1.1.0
- MCP-code-first: active `odoo-codemode` (`/mcp-code`); full `odoo-knowledge` (`/mcp`) disabled by default
- Slim rules/skills routers; stable invariants verified via codemode (company_ids, useService import)
- Added `skills/odoo-invariants.md` micro cheat-sheet verified on **v16–v19** (company_ids, useService, SQL from v17+, list/attrs matrix)
- Plugin vars: `ODOO_VERSION`, `ODOO_MCP_CODE_URL`, `ODOO_MCP_URL`

## 1.0.0
- First Cursor marketplace-oriented build
- Added `.cursor-plugin/plugin.json`
- Added plugin-local `hooks/hooks.json`
- Added marketplace manifest at `plugins/.cursor-plugin/marketplace.json`
- Added command frontmatter
- Embedded MCP-first policy for Odoo 18/19 Community and Enterprise
