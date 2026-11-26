# Odoo stable invariants (token-cheap)

Verified for Odoo 19 Community via `odoo-codemode`. Use these instead of an MCP roundtrip for common syntax. For schema/XML IDs/source, still use `codemode_search` → `codemode_execute`.

## Version pin
- Prefer `${ODOO_VERSION}` or nearest `__manifest__.py` (`18.0.x` → 18). Default plugin var: `18`.

## Backend
- v15+: `tracking=True` (not `track_visibility`)
- v16+: `from odoo.fields import Command` for x2many (tuples still work)
- v17+: `@api.model_create_multi` on `create`
- v18+: `_check_company_auto = True`; `check_company=True` on company-scoped relations
- Raw SQL: prefer `from odoo.tools import SQL` (class in `odoo/tools/sql.py`); recommended, not mandatory for every custom module
- Prefer batch ORM; avoid unnecessary `sudo()`

## Views / actions (v17+)
- No `attrs` / `states` — use `invisible="..."`, `readonly="..."`, `required="..."`
- Prefer `<list>` over `<tree>`
- Prefer `view_mode`: `list,form` (not `tree,form`)

## Security / ir.rule
- Multi-company domain magic var is `company_ids` (confirmed e.g. `sale.sale_order_comp_rule`):
  - `[('company_id', 'in', company_ids)]`
  - Shareable: `['|', ('company_id', '=', False), ('company_id', 'in', company_ids)]`
- `allowed_company_ids` is a **context** key for business logic only: `self.env.context.get('allowed_company_ids')`
- ACL CSV: `id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink`
- Do not grant write/create/unlink to `base.group_user` by default

## OWL / JS (v16+)
- `/** @odoo-module **/`
- `import { Component, useState } from "@odoo/owl"`
- `import { useService } from "@web/core/utils/hooks"` (file: `web/static/src/core/utils/hooks.js`)
- `import { registry } from "@web/core/registry"` for actions/systray/services
- Typical backend assets: `web.assets_backend`
- Do not invent hooks (`useVisible`, `useIntersectionObserver`, etc.)

## When to call MCP-code anyway
- Model fields / relations / method overrides
- Exact XML IDs, inherit targets, groups
- Edition (CE/EE) or cross-version diffs → `odoo.compact.compare_versions` / `implementation_brief`
