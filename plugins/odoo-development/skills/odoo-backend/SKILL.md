---
name: odoo-backend
description: odoo backend patterns for models, fields, computed logic, onchange, inheritance, controllers, imports, automation, and module generation. use for python, manifests, orm logic, data models, api, cron, and backend architecture tasks across odoo versions, especially when generating or extending modules.
---

# Odoo Backend

## Router (token-first)
1. Pin version: `${ODOO_VERSION}` or nearest `__manifest__.py`.
2. Prefer slim local rules for stable syntax (`Command`, create-multi, tracking, `_check_company_auto`).
3. If need schema/XML ID/source: `odoo-codemode` → `codemode_search` → `codemode_execute`.
4. If MCP unavailable: Read **one** `skills/odoo-backend/odoo-model-patterns-{version}.md` or `skills/odoo-backend/odoo-module-generator-{version}.md` (never `-all`).
5. Never invent fields, comodels, XML IDs, or dependencies.

## Optional offline patterns (Read only if needed)
- `skills/odoo-backend/field-type-reference.md`
- `skills/odoo-backend/computed-field-patterns.md`
- `skills/odoo-backend/constraint-patterns.md`
- `skills/odoo-backend/onchange-dynamic-patterns.md`
- `skills/odoo-backend/inheritance-patterns.md`
- `skills/odoo-backend/controller-api-patterns.md`
- `skills/odoo-backend/cron-automation-patterns.md`
