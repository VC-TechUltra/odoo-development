---
name: odoo-backend
description: odoo backend patterns for models, fields, computed logic, onchange, inheritance, controllers, imports, automation, and module generation. use for python, manifests, orm logic, data models, api, cron, and backend architecture tasks across odoo versions, especially when generating or extending modules.
---

# Odoo Backend

## Router (token-first)
1. Pin version **16–19**: `${ODOO_VERSION}` or nearest `__manifest__.py` (codemode `version`: `v16`|`v17`|`v18`|`v19`).
2. Prefer slim rules + `skills/odoo-invariants.md` (`Command`, create-multi, tracking, `_check_company_auto`, `SQL` from v17+).
3. If need schema/XML ID/source: `odoo-codemode` → `codemode_search` → `codemode_execute` (`odoo.compact.implementation_brief` / `field`).
4. If MCP unavailable: Read `skills/odoo-invariants.md`, then at most **one** `skills/odoo-backend/odoo-model-patterns-{version}.md` or `odoo-module-generator-{version}.md` (never `-all`).
5. Never invent fields, comodels, XML IDs, or dependencies.

## Optional offline patterns (Read only if needed)
- `skills/odoo-backend/field-type-reference.md`
- `skills/odoo-backend/computed-field-patterns.md`
- `skills/odoo-backend/constraint-patterns.md`
- `skills/odoo-backend/onchange-dynamic-patterns.md`
- `skills/odoo-backend/inheritance-patterns.md`
- `skills/odoo-backend/controller-api-patterns.md`
- `skills/odoo-backend/cron-automation-patterns.md`
