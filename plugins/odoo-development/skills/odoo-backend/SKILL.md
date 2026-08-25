---
name: odoo-backend
description: odoo backend patterns for models, fields, computed logic, onchange, inheritance, controllers, imports, automation, and module generation. use for python, manifests, orm logic, data models, api, cron, and backend architecture tasks across odoo versions, especially when generating or extending modules.
---

# Odoo Backend

## Core policy
- Detect target Odoo version first (check __manifest__.py or use ${ODOO_VERSION}).
- Prefer repository patterns and MCP-backed facts over guesses.
- For Odoo 18 and 19 Community and Enterprise, always verify schema, dependencies, and version guidance with MCP before suggesting framework-specific backend code.

## MCP-first workflow
When odoo-knowledge MCP is available: use it first. When MCP is unavailable: use built-in tools—proceed, do not block.

1. `health_check` when MCP reachability is uncertain.
2. `search_odoo_codebase` or `code_search` for similar patterns.
3. `read_odoo_file` or `get_file_snippet` for exact source context.
4. `get_odoo_model_schema` for fields, relations, inherited models, and edition-aware assumptions.
5. `get_odoo_xml_id_location` before using or inheriting XML IDs.
6. `get_model_dependencies` before changing manifests or cross-module integrations.
7. `get_odoo_development_guidelines` for Odoo 18/19 CE/EE framework guidance.

## Version-specific knowledge
After detecting the target Odoo version, load the appropriate version file:

**Model patterns:** `skills/odoo-backend/odoo-model-patterns-{version}.md`
- Available: 14, 15, 16, 17, 18, 19, 14-15, 15-16, 16-17, 17-18, 18-19

**Module generator:** `skills/odoo-backend/odoo-module-generator-{version}.md`
- Available: 14, 15, 16, 17, 18, 19, 17-18, 18-19

Use transition files (e.g., 17-18, 18-19) when working on upgrades between adjacent versions.

## General patterns (version-agnostic)
Load these as needed without version suffixes:
- `skills/odoo-backend/field-type-reference.md`
- `skills/odoo-backend/computed-field-patterns.md`
- `skills/odoo-backend/constraint-patterns.md`
- `skills/odoo-backend/onchange-dynamic-patterns.md`
- `skills/odoo-backend/inheritance-patterns.md`
- `skills/odoo-backend/controller-api-patterns.md`
- `skills/odoo-backend/cron-automation-patterns.md`
- `skills/odoo-backend/common-module-templates.md`
- `skills/odoo-backend/module-generation-example.md`
- `skills/odoo-backend/attachment-binary-patterns.md`
- `skills/odoo-backend/import-export-patterns.md`

## Troubleshooting patterns
For error handling, logging, and context management, see:
- `skills/odoo-troubleshooting/error-handling-patterns.md`
- `skills/odoo-troubleshooting/logging-debugging-patterns.md`
- `skills/odoo-troubleshooting/context-environment-patterns.md`

Read only the files relevant to the current task to keep context lean.
