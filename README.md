# TechUltra Cursor Marketplace Source

This repository is a Cursor marketplace source layout for plugin packaging.

## Layout

The marketplace manifest **must** be at the repository root for Cursor to discover plugins:

```
<repo-root>/
├── .cursor-plugin/
│   └── marketplace.json       # At repo root (required)
├── plugins/
│   └── odoo-development/
│       ├── .cursor-plugin/plugin.json
│       ├── skills/
│       ├── commands/
│       ├── rules/
│       ├── agents/
│       ├── hooks/hooks.json
│       ├── mcp.json
│       └── assets/
```

## Notes
- The plugin uses a streamable-http MCP server (default: `http://127.0.0.1:8090/mcp`). Edit `plugins/odoo-development/mcp.json` to change the URL.
- The plugin is tuned for Odoo 18 and 19 Community and Enterprise.
