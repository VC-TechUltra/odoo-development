# Odoo Development Cursor Plugin

Cursor marketplace-oriented Odoo plugin with focused skills, commands, rules, hooks, and a skill-first workflow.

## How to use

**Commands** (run in Agent Chat / Cmd+K):
- Type `/odoo-plan`, `/odoo-review`, `/odoo-module`, `/odoo-migrate`, `/odoo-fix-traceback`, `/odoo-owl`, `/odoo-security`, or `/odoo-test` in chat
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


## Documentation quality check

Validate that `Read:` references used in command docs resolve to real files:

```bash
./scripts/validate-command-read-paths.sh
```

## MCP configuration

The plugin connects to the `odoo-knowledge` MCP server for codebase search and schema inspection. It ships pointing at `http://127.0.0.1:8099/mcp/`, which assumes the server runs on your own machine.

**To change the URL:** Edit `mcp.json` in the plugin directory and update the `url` field under `mcpServers.odoo-knowledge`. For a shared server on your network:

```json
"url": "http://your-server:8099/mcp/"
```

Keep the trailing slash — requests to `/mcp` are answered with a 307 redirect to `/mcp/`.

If the server was started with `GREEN_MCP_API_KEY` set, it requires a bearer token; add one alongside the URL:

```json
"headers": { "Authorization": "Bearer your-key" }
```

**With MCP:** Commands and skills use odoo-knowledge MCP for best results. Run `knowledge_status` via MCP when connectivity is uncertain.

**Without MCP:** The plugin works without the MCP server. Commands and skills fall back to built-in SemanticSearch, Grep, and Read tools. You can use all functionality immediately.

## MCP policy
The skills answer syntax, patterns, conventions and version differences.
MCP is called only to confirm what actually exists in a version - a field,
method, XML ID, inheritance chain or access rule. Supported targets:
- Odoo 18 Community
- Odoo 18 Enterprise
- Odoo 19 Community
- Odoo 19 Enterprise

## Hooks

The plugin registers two hooks via `hooks/hooks.json`:

| Hook | Script | Purpose |
|------|--------|---------|
| `sessionStart` | `mcp-health-check.sh` | Injects skill-first workflow context at session start: answer from the skills, and call odoo-knowledge MCP only to confirm version-specific existence. |
| `beforeShellExecution` | `validate-odoo-paths.sh` | Runs before shell commands; adds a note to prefer repository-local paths and to confirm Odoo facts before destructive commands. Returns `permission: allow` so execution proceeds. |

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
