---
name: odoo-owl
description: odoo frontend and owl patterns for components, assets, qweb, widgets, website integration, and javascript behavior. use for web client, owl, qweb, frontend assets, dashboards, and user-interface development across supported odoo versions.
---

# Odoo Owl

## Router (token-first)
1. Pin version: `${ODOO_VERSION}` or nearest `__manifest__.py` (OWL differs sharply by series).
2. Prefer slim rules + `skills/odoo-invariants.md` (`useService` / `registry` imports).
3. If need registries/services/templates: `odoo-codemode` → `codemode_search` → `codemode_execute` (`odoo.compact.frontend_brief` / `owl_components`).
4. If MCP unavailable: Read `skills/odoo-invariants.md`, then at most **one** `skills/odoo-owl/odoo-owl-components-{version}.md` (never `-all`).
5. Never invent OWL hooks or service names.

## Optional offline patterns (Read only if needed)
- `skills/odoo-owl/assets-bundling-patterns.md`
- `skills/odoo-owl/qweb-template-patterns.md`
- `skills/odoo-owl/widget-field-patterns.md`
