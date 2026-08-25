---
name: odoo-owl
description: odoo frontend and owl patterns for components, assets, qweb, widgets, website integration, and javascript behavior. use for web client, owl, qweb, frontend assets, dashboards, and user-interface development across supported odoo versions.
---

# Odoo Owl

## Core policy
- Detect target Odoo version first (check __manifest__.py or use ${ODOO_VERSION}).
- OWL versions differ significantly: v14 (no OWL), v15 (OWL 1.x), v16-18 (OWL 2.x), v19+ (OWL 3.x).
- Prefer repository patterns and MCP-backed facts over guesses.
- For Odoo 18 and 19 Community and Enterprise, use MCP development guidance before proposing OWL, registry, or asset-bundle patterns.

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

**OWL components:** `skills/odoo-owl/odoo-owl-components-{version}.md`
- Available: 14, 15, 16, 17, 18, 19, 14-15, 15-16, 17-18, 18-19

Use transition files (e.g., 17-18, 18-19) when working on upgrades between adjacent versions.

## General patterns (version-agnostic)
Load these as needed:
- `skills/odoo-owl/assets-bundling-patterns.md`
- `skills/odoo-owl/qweb-template-patterns.md`
- `skills/odoo-owl/widget-field-patterns.md`
- `skills/odoo-owl/website-integration-patterns.md`
- `skills/odoo-owl/dashboard-kpi-patterns.md`

Read only the files relevant to the current task to keep context lean.
