# Odoo Development Cursor Plugin

Cursor marketplace-oriented Odoo plugin with focused skills, commands, rules, hooks, and MCP-first workflows.

## Included capabilities
- Skills for backend, security, migration, OWL, testing, troubleshooting, functional flows, and orchestration
- Commands for module generation, review, migration, traceback fixing, and planning
- Rules for backend, XML/security, OWL, and upgrade safety
- Plugin-local MCP config for Odoo code knowledge
- Plugin-local hooks config

## MCP policy
This plugin is designed to use the `odoo-knowledge` MCP first for:
- Odoo 18 Community
- Odoo 18 Enterprise
- Odoo 19 Community
- Odoo 19 Enterprise

## Plugin structure
- `.cursor-plugin/plugin.json`
- `skills/`
- `commands/`
- `rules/`
- `agents/`
- `hooks/hooks.json`
- `mcp.json`
- `assets/logo.svg`

## Marketplace repo layout
This zip is structured as a marketplace source repo:
- `plugins/.cursor-plugin/marketplace.json`
- `plugins/odoo-development/...`
