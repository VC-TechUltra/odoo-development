---
name: odoo-migration
description: odoo migration and version-routing guidance for version-specific model, module, security, and frontend changes across odoo 14 to 19. use for upgrades, deprecated pattern replacement, target-version planning, and release-specific implementation choices.
---

# Odoo Migration

## Core policy
- Detect source and target Odoo versions first.
- Prefer repository patterns and MCP-backed facts over guesses.
- For Odoo 18 and 19 Community and Enterprise, treat MCP guidance as the source of truth for version-sensitive replacements and edition-aware behavior.

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
After detecting the source and target Odoo versions, load the appropriate version file:

**Version knowledge:** `skills/odoo-migration/odoo-version-knowledge-{version}.md`
- Available: 14, 15, 16, 17, 18, 19, 14-15, 15-16, 17-18, 18-19

Use transition files (e.g., 17-18, 18-19) when migrating between adjacent versions.

## General patterns (version-agnostic)
Load these as needed:
- `skills/odoo-migration/data-migration-patterns.md`
- `skills/odoo-migration/odoo-editions.md`

Read only the files relevant to the current task to keep context lean.
