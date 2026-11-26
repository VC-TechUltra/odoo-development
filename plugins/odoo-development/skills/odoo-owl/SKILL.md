---
name: odoo-owl
description: odoo frontend and owl patterns for components, assets, qweb, widgets, website integration, and javascript behavior. use for web client, owl, qweb, frontend assets, dashboards, and user-interface development across supported odoo versions.
---

# Odoo Owl

## Router (token-first)
1. Pin version **16–19**: `${ODOO_VERSION}` or nearest `__manifest__.py` (OWL 2.x on 16–18, OWL 3.x on 19).
2. Prefer slim rules + `skills/odoo-invariants.md` (`useService` / `registry` imports verified on v16–v19).
3. If need registries/services/templates: `odoo-codemode` → `codemode_search` → `codemode_execute` (`odoo.compact.frontend_brief` / `owl_components`).
4. If MCP unavailable: Read `skills/odoo-invariants.md`, then at most **one** `skills/odoo-owl/odoo-owl-components-{version}.md` (never `-all`).
5. Never invent OWL hooks or service names.

## Optional offline patterns (Read only if needed)
- `skills/odoo-owl/assets-bundling-patterns.md`
- `skills/odoo-owl/qweb-template-patterns.md`
- `skills/odoo-owl/widget-field-patterns.md`
