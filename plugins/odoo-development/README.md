# Odoo Development Cursor Plugin

Cursor marketplace-oriented Odoo plugin with focused skills, commands, rules, hooks, and MCP-code-first workflows.

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

**Active (default):** `odoo-codemode` at `${ODOO_MCP_CODE_URL}` → `http://127.0.0.1:8090/mcp-code`

Use `codemode_search` then `codemode_execute` for compact multi-step research (schema, XML IDs, source, overrides). Prefer slim local rules/skills for stable syntax so common edits skip an MCP roundtrip.

**Disabled by default:** full `odoo-knowledge` at `${ODOO_MCP_URL}` → `http://127.0.0.1:8090/mcp`

To re-enable the full Knowledge tool catalog, copy entries from `mcp.knowledge.disabled.json.example` into `mcp.json` (or merge both servers). Prefer keeping only codemode active to reduce tool-schema token tax.

**Plugin variables** (in `.cursor-plugin/plugin.json`):
- `ODOO_VERSION` — target series (default `18`)
- `ODOO_MCP_CODE_URL` — primary codemode endpoint
- `ODOO_MCP_URL` — optional full Knowledge endpoint

**Without MCP:** The plugin works offline. Commands and skills fall back to one versioned skill file plus built-in Grep/Read. Do not load `-all` or every version file.

## MCP policy
Prefer `odoo-codemode` for Odoo 18/19 Community and Enterprise research. Use slim rules for edit-time invariants (`attrs` removal, `company_ids` in `ir.rule`, `useService` import path, etc.).

## Hooks

The plugin registers two hooks via `hooks/hooks.json`:

| Hook | Script | Purpose |
|------|--------|---------|
| `sessionStart` | `mcp-health-check.sh` | Injects MCP-code-first session context (codemode_search → codemode_execute; slim local rules for stable syntax). |
| `beforeShellExecution` | `validate-odoo-paths.sh` | Prefers repository-local paths and MCP verification before destructive commands. Returns `permission: allow`. |

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
- `mcp.json` (active codemode)
- `mcp.knowledge.disabled.json.example` (optional full Knowledge)
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
