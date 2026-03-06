# TechUltra Cursor Marketplace Source

This repository is a build-oriented source layout for Cursor plugin packaging.

## Layout
- `plugins/.cursor-plugin/marketplace.json`
- `plugins/odoo-development/.cursor-plugin/plugin.json`
- `plugins/odoo-development/skills/`
- `plugins/odoo-development/commands/`
- `plugins/odoo-development/rules/`
- `plugins/odoo-development/agents/`
- `plugins/odoo-development/hooks/hooks.json`
- `plugins/odoo-development/mcp.json`

## Notes
- The plugin uses a streamable-http MCP server at `http://192.168.29.55:8090/mcp`.
- The plugin is tuned for Odoo 18 and 19 Community and Enterprise.
