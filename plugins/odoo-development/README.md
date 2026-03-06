# Odoo Development Cursor Plugin

Cursor marketplace-oriented Odoo plugin with focused skills, commands, rules, hooks, and MCP-first workflows.

## How to use

**Commands** (run in Agent Chat / Cmd+K):
- Type `/odoo-plan`, `/odoo-review`, `/odoo-module`, `/odoo-migrate`, or `/odoo-fix-traceback` in chat
- Or press `Ctrl+Shift+P` (Cmd+Shift+P on Mac) and type `odoo` to see commands

**Skills** (apply automatically or invoke manually):
- Type `/` in chat and pick a skill (e.g. `odoo-orchestrator`, `odoo-backend`)
- Or mention Odoo in your request—the agent will use relevant skills

**Rules** (apply when editing matching files):
- Edit `.py`, `.xml`, `.js` files—rules apply automatically

## Included capabilities
- Skills for backend, security, migration, OWL, testing, troubleshooting, functional flows, and orchestration
- Commands for module generation, review, migration, traceback fixing, and planning
- Rules for backend, XML/security, OWL, and upgrade safety
- Plugin-local MCP config for Odoo code knowledge
- Plugin-local hooks config

## MCP configuration

The plugin connects to the `odoo-knowledge` MCP server for codebase search, schema inspection, and development guidelines. By default it uses `http://127.0.0.1:8090/mcp`.

**To change the URL:** Edit `mcp.json` in the plugin directory and update the `url` field under `mcpServers.odoo-knowledge`. For example, to use a remote server:

```json
"url": "http://your-server:8090/mcp"
```

**With MCP:** Commands and skills use odoo-knowledge MCP for best results. Run `health_check` via MCP when connectivity is uncertain.

**Without MCP:** The plugin works without the MCP server. Commands and skills fall back to built-in SemanticSearch, Grep, and Read tools. You can use all functionality immediately.

## MCP policy
This plugin is designed to use the `odoo-knowledge` MCP first for:
- Odoo 18 Community
- Odoo 18 Enterprise
- Odoo 19 Community
- Odoo 19 Enterprise

## Hooks

The plugin registers two hooks via `hooks/hooks.json`:

| Hook | Script | Purpose |
|------|--------|---------|
| `sessionStart` | `mcp-health-check.sh` | Injects MCP-first workflow context at session start, reminding the agent to use odoo-knowledge MCP first and run `health_check` when connectivity is uncertain. |
| `beforeShellExecution` | `validate-odoo-paths.sh` | Runs before shell commands; adds a note to prefer repository-local paths and Odoo MCP verification before destructive commands. Returns `permission: allow` so execution proceeds. |

**Windows:** The hook scripts use `sh` (POSIX shell). On Windows, ensure Git Bash or WSL is available in your PATH so the `sh` command resolves. Otherwise hooks may fail to run.

## Agent tools

The plugin's agents (odoo-code-reviewer, odoo-upgrade-analyzer) use `Read`, `Glob`, `Grep`, `WebFetch`, and `WebSearch`. These should map to Cursor's built-in capabilities (file read, glob, grep, web fetch, web search). If an agent fails to use web capabilities, verify the tool names against Cursor's current [agent tools documentation](https://cursor.com/docs/agent/tools).

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
This repo is structured as a Cursor marketplace source. The marketplace manifest must be at the **repository root**:

```
<repo-root>/
├── .cursor-plugin/
│   └── marketplace.json       # Required: at repo root
├── plugins/
│   └── odoo-development/      # This plugin
│       ├── .cursor-plugin/
│       │   └── plugin.json
│       ├── skills/
│       ├── commands/
│       ├── rules/
│       ├── agents/
│       ├── hooks/
│       ├── mcp.json
│       └── assets/
```

With `pluginRoot: "plugins"` and `source: "odoo-development"`, Cursor discovers the plugin at `plugins/odoo-development/`.
