---
name: odoo-owl
description: odoo frontend and owl patterns for components, assets, qweb, widgets, website integration, and javascript behavior. use for web client, owl, qweb, frontend assets, dashboards, and user-interface development across supported odoo versions.
---

# Odoo Owl

## Core policy
- Detect target Odoo version first.
- Prefer repository patterns and MCP-backed facts over guesses.
- For Odoo 18 and 19 Community and Enterprise, use MCP development guidance before proposing OWL, registry, or asset-bundle patterns.

## MCP-first workflow
1. `health_check` when MCP reachability is uncertain.
2. `search_odoo_codebase` or `code_search` for similar patterns.
3. `read_odoo_file` or `get_file_snippet` for exact source context.
4. `get_odoo_model_schema` for fields, relations, inherited models, and edition-aware assumptions.
5. `get_odoo_xml_id_location` before using or inheriting XML IDs.
6. `get_model_dependencies` before changing manifests or cross-module integrations.
7. `get_odoo_development_guidelines` for Odoo 18/19 CE/EE framework guidance.

## Included knowledge files
- `odoo-owl-components.md`
- `odoo-owl-components-all.md`
- `odoo-owl-components-17.md`
- `odoo-owl-components-18.md`
- `odoo-owl-components-19.md`
- `odoo-owl-components-17-18.md`
- `odoo-owl-components-18-19.md`
- `assets-bundling-patterns.md`
- `qweb-template-patterns.md`
- `widget-field-patterns.md`
- `website-integration-patterns.md`
- `dashboard-kpi-patterns.md`

Read only the files relevant to the current task to keep context lean.
