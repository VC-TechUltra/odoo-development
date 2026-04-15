# Changelog

## Unreleased
- Added bootstrap scripts for silent local tool setup with first-run path selection and Python 3.10-3.12 auto-selection.
- Added `repo-graph-local` MCP wiring and launcher wrapper for code-review-graph stdio mode.
- Added session lifecycle commands (`/odoo-session-start`, `/odoo-session-summary`, `/odoo-session-clear`, `/odoo-repo-reindex`, `/odoo-health-check`).
- Added `hooks/session-start-bootstrap.sh` and updated hook configs to run bootstrap at session start.
- Updated README MCP URL default and documented bootstrap/fallback policy.
- Added `agents/odoo-query-optimizer.md` for Odoo ORM/query performance diagnostics.
- Added `/odoo-optimize` command for performance-oriented analysis workflows.
- Synced command and agent inventory documentation in `README.md` and `SKILL.md`.
- Added explicit MCP tool-sequencing guidance to optimization agent/command flows.

## 1.0.0
- First Cursor marketplace-oriented build
- Added `.cursor-plugin/plugin.json`
- Added plugin-local `hooks/hooks.json`
- Added marketplace manifest at `plugins/.cursor-plugin/marketplace.json`
- Added command frontmatter
- Embedded MCP-first policy for Odoo 18/19 Community and Enterprise
