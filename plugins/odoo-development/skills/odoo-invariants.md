# Odoo stable invariants (token-cheap) — v16–v19

Verified via `odoo-codemode` against Community snapshots for **v16, v17, v18, and v19**. Use these instead of an MCP roundtrip for common syntax. For schema/XML IDs/source, still use `codemode_search` → `codemode_execute`.

## Version pin
- Prefer `${ODOO_VERSION}` or nearest `__manifest__.py` (`16.0.x`→16 … `19.0.x`→19). Plugin default: `18`.
- This cheat-sheet targets **16–19**. Treat 14–15 as limited/unsupported stubs elsewhere.

## Matrix (what changes by series)

| Topic | v16 | v17 | v18 | v19 |
|-------|-----|-----|-----|-----|
| `Command` x2many | yes (prefer) | yes | yes | yes |
| `@api.model_create_multi` | recommended | required for create | required | required |
| View `attrs` / `states` | allowed | **removed** | removed | removed |
| List markup | `<tree>` common | prefer `<list>` | prefer `<list>` | prefer `<list>` |
| `view_mode` | `tree,form` OK | prefer `list,form` | prefer `list,form` | prefer `list,form` |
| `ir.rule` company domain | `company_ids` | `company_ids` | `company_ids` | `company_ids` |
| `useService` import | `@web/core/utils/hooks` | same | same | same |
| `SQL()` builder (`odoo.tools.SQL`) | **no** (not this class) | available | recommended | recommended |
| `_check_company_auto` | rare/manual | emerging | common / prefer | prefer |
| OWL | 2.x | 2.x | 2.x | 3.x (stricter static props) |

## Backend
- v16+: `from odoo.fields import Command` for x2many (tuples still work)
- v16+: `@api.model_create_multi` exists; treat as mandatory from **v17+**
- v15+ field chatter: `tracking=True` (not `track_visibility`)
- v18+: `_check_company_auto = True`; `check_company=True` on company-scoped relations
- Raw SQL: `from odoo.tools import SQL` from **v17+** (`odoo/tools/sql.py`). On **v16** do not assume this API. Still recommended—not mandatory—for every custom module on 18/19
- Prefer batch ORM; avoid unnecessary `sudo()`

## Views / actions
- **v16:** `attrs` / `states` OK; `<tree>` and `view_mode` `tree,form` are normal
- **v17–v19:** no `attrs` / `states` — use `invisible="..."`, `readonly="..."`, `required="..."`; prefer `<list>` and `view_mode` `list,form`

## Security / ir.rule (v16–v19)
Confirmed identical pattern on `sale.sale_order_comp_rule` for v16/v17/v18/v19:

```text
[('company_id', 'in', company_ids)]
```

Shareable:

```text
['|', ('company_id', '=', False), ('company_id', 'in', company_ids)]
```

- Magic var is **`company_ids`** (not `allowed_company_ids`)
- `allowed_company_ids` is a **context** key only: `self.env.context.get('allowed_company_ids')`
- ACL CSV: `id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink`
- Do not grant write/create/unlink to `base.group_user` by default

## OWL / JS (v16–v19)
- `/** @odoo-module **/`
- `import { Component, useState } from "@odoo/owl"`
- `import { useService } from "@web/core/utils/hooks"` — confirmed in `web/static/src/core/utils/hooks.js` on **v16, v17, v18, v19**
- `import { registry } from "@web/core/registry"` for actions / systray / services
- Typical backend assets: `web.assets_backend`
- v16–v18: OWL 2.x; v19: OWL 3.x (stricter `static props`) — do not invent hooks (`useVisible`, `useIntersectionObserver`, …)

## When to call MCP-code anyway
- Model fields / relations / method overrides
- Exact XML IDs, inherit targets, groups
- Edition (CE/EE) or cross-version diffs → `odoo.compact.compare_versions` / `implementation_brief` (pin `version` to v16|v17|v18|v19)
