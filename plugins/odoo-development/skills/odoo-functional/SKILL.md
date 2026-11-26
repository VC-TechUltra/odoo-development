---
name: odoo-functional
description: odoo functional domain patterns covering accounting, sales, crm, hr, purchase, stock, projects, product variants, pricing, taxes, uom, reports, mail, menus, actions, wizards, workflows, and business flows. use for domain-specific module work.
---

# Odoo Functional

## Router (token-first)
1. Pin version: `${ODOO_VERSION}` or nearest `__manifest__.py`.
2. Prefer repository patterns + `skills/odoo-invariants.md`; do not invent app XML IDs.
3. Prefer `odoo-codemode` → `codemode_search` → `codemode_execute` (`odoo.compact.implementation_brief` / `security`) for models/XML IDs/workflows.
4. If MCP unavailable: Read `skills/odoo-invariants.md`, then at most **one** matching file under `skills/odoo-functional/`.
