# Odoo Development Cursor Plugin

Cursor marketplace-oriented Odoo plugin with focused skills, commands, rules, hooks, and MCP-first workflows.

## How to use

**Commands** (run in Agent Chat / Cmd+K):
- Type `/odoo-plan`, `/odoo-review`, `/odoo-module`, `/odoo-migrate`, `/odoo-fix-traceback`, `/odoo-security`, `/odoo-test`, `/odoo-owl`, `/odoo-optimize`, `/odoo-session-start`, `/odoo-session-summary`, `/odoo-session-clear`, `/odoo-repo-reindex`, or `/odoo-health-check` in chat
- Or press `Ctrl+Shift+P` (Cmd+Shift+P on Mac) and type `odoo` to see commands

**Skills** (apply automatically or invoke manually):
- Type `/` in chat and pick a skill (e.g. `odoo-orchestrator`, `odoo-backend`)
- Or mention Odoo in your request—the agent will use relevant skills

**Rules** (apply when editing matching files):
- Edit `.py`, `.xml`, `.js` files—rules apply automatically

## Included capabilities
- Skills for backend, security, migration, OWL, testing, troubleshooting, functional flows, and orchestration
- Commands for planning, review, module generation, migration, traceback fixing, security checks, testing guidance, OWL work, performance optimization, and session/repo lifecycle controls
- Rules for backend, XML/security, OWL, and upgrade safety
- Plugin-local MCP config for Odoo knowledge + local repo graph + session memory
- Plugin-local hooks config
- Agents for code review, migration analysis, context gathering, skill finding, and query optimization


## Documentation quality check

Validate that `Read:` references used in command docs resolve to real files:

```bash
./scripts/validate-command-read-paths.sh
```

## MCP configuration

The plugin connects to the `odoo-knowledge` MCP server for codebase search, schema inspection, and development guidelines. By default it uses `http://192.168.29.55:8099/mcp`.

**To change the URL:** Edit `mcp.json` in the plugin directory and update the `url` field under `mcpServers.odoo-knowledge`. For example, to use a remote server:

```json
"url": "http://your-server:8090/mcp"
```

**With MCP:** Commands and skills prefer `repo-graph-local` for local context minimization, verify with `odoo-knowledge`, and store session-scoped notes via `session-memory-local`. Run `health_check` when connectivity is uncertain.

**Without MCP:** The plugin works without the MCP server. Commands and skills fall back to built-in SemanticSearch, Grep, and Read tools. You can use all functionality immediately.

## MCP policy
This plugin is designed for an **MCP-first (preferred), fallback-capable** workflow. Prioritize MCP for:
- Odoo 18 Community
- Odoo 18 Enterprise
- Odoo 19 Community
- Odoo 19 Enterprise

If MCP is unavailable, continue with local file search/read tools and clearly state assumptions and verification gaps.

## Hooks

The plugin registers session bootstrap + safety hooks via `hooks/hooks.json`:

| Hook | Script | Purpose |
|------|--------|---------|
| `sessionStart` | `session-start-bootstrap.py` | Runs cross-platform bootstrap checks (Python range, local tool setup), emits local runtime status, and reminds the agent to use repo-graph-local first for local context before Odoo MCP verification. |
| `sessionStart` | `mcp-health-check.py` | Injects MCP-first workflow context at session start and advises health verification when connectivity is uncertain. |
| `beforeShellExecution` | `validate-odoo-paths.py` | Runs before shell commands; adds a note to prefer repository-local paths and Odoo MCP verification before destructive commands. Returns `permission: allow` so execution proceeds. |

Hook commands in `hooks/hooks.json` and local MCP stdio launchers in `mcp.json` now use Python entrypoints, so they no longer require `sh` to be available on Windows.



## Local bootstrap policy

- On first setup, the bootstrap flow asks for an install/cache base path and stores it under user-home config.
- Subsequent sessions run silent checks and auto-install/update for local tooling.
- Python runtime selection policy: choose the highest locally available version within **3.10 to 3.12**.
- For `code-review-graph`, the plugin prefers the latest version; if smoke test fails, it falls back to the last-known-good version and continues in degraded mode.
- Session memory intentionally refuses likely secret-bearing values (e.g., token/password/secret markers) and large payloads to reduce leakage risk.
- Automated tests now run via `python -m unittest discover -q tests` in local/CI check runners.
- Health checks now include session-memory schema version metadata for compatibility diagnostics.
- Branch-switch namespace rotation is now covered by an automated verifier (`scripts/verify_branch_rotation.py`).
- MCP stdio behavior is now validated with an end-to-end integration test (`tests/test_session_memory_mcp_integration.py`).
- Health check JSON now includes machine-readable remediation fields (`code`, `recommended_action`) per component.
- CI now exports per-matrix health JSON artifacts via `scripts/export_health_report.py` for easier post-failure diagnosis.


## Local memory validation

Run the session memory smoke test:

```bash
./scripts/test-session-memory-store.sh
```


Run the full local verification bundle:

```bash
./scripts/run-local-checks.sh
```

Quick stack health check:

```bash
python scripts/health_check_stack.py --offline --strict-local
```

On Windows/PowerShell:

```powershell
./scripts/run-local-checks.ps1
```

## Documentation strict-pass checklist

For a stricter third pass, run a file-by-file doc audit:
- `SKILL.md`: keep capability inventory synchronized with this README and include concrete review/migration/traceback flows
- `agents/odoo-code-reviewer.md`: use preference wording rather than hard-lock invocation language
- `agents/odoo-context-gatherer.md`: treat as preferred pre-work for multi-file/ambiguous tasks
- `commands/*.md`: verify listed commands still match shipped files

## Agents

The plugin includes:
- `odoo-code-reviewer`
- `odoo-upgrade-analyzer`
- `odoo-context-gatherer`
- `odoo-skill-finder`
- `odoo-query-optimizer`

## Agent tools

The plugin's agents use `Read`, `Glob`, `Grep`, and where needed `WebFetch`/`WebSearch`. These should map to Cursor's built-in capabilities (file read, glob, grep, web fetch, web search). If an agent fails to use web capabilities, verify the tool names against Cursor's current [agent tools documentation](https://cursor.com/docs/agent/tools).

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

- Implementation status: local session-memory MCP integration and rollout hardening are complete.

## Troubleshooting

For cross-platform failure diagnosis and remediation, see `docs/troubleshooting-matrix.md`.

## Performance and token efficiency

For practical ways to reduce agent/context token usage (including drop-in token budget clauses), see `docs/token-optimization.md`.
