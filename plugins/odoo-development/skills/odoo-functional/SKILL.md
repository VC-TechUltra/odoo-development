---
name: odoo-functional
description: odoo functional domain patterns covering accounting, sales, crm, hr, purchase, stock, projects, product variants, pricing, taxes, uom, reports, mail, menus, actions, wizards, workflows, and business flows. use for domain-specific module work.
---

# Odoo Functional

## Core policy
- Detect target Odoo version first.
- Answer from this skill first; escalate to MCP only for existence checks.
- For Odoo 18 and 19 Community and Enterprise, confirm with MCP that a referenced field, XML ID, dependency or access rule exists before relying on it.

## Answering order
**1. Answer from this skill.** Syntax, patterns, file shapes, conventions and
documented version differences are covered here. Do not call MCP for these.

**2. Escalate to MCP only for existence questions** - a claim about what is
actually present in a given Odoo version:

| Question | Tool |
|---|---|
| Does model X have field/method Y? | `get_odoo_model` |
| Where is this XML ID, what inherits it? | `resolve_odoo_xml_id` |
| What overrides this method? | `trace_odoo_method` |
| What ACLs or record rules apply? | `get_odoo_security` |
| Exact source of a known file range | `read_odoo_source_range` |
| What changed between two versions? | `compare_odoo_versions` |

When you know the file, prefer `read_odoo_source_range` over `get_odoo_model`
(~50k tokens). Always pass `start_line`/`end_line`: a 20-line read is ~180
tokens, but the default range is 200 lines (~2k).

## Included knowledge files
- `accounting-patterns.md`
- `action-patterns.md`
- `hr-employee-patterns.md`
- `mail-notification-patterns.md`
- `menu-navigation-patterns.md`
- `lot-serial-patterns.md`
- `pricelist-pricing-patterns.md`
- `product-variant-patterns.md`
- `project-task-patterns.md`
- `purchase-procurement-patterns.md`
- `report-patterns.md`
- `sale-crm-patterns.md`
- `sequence-numbering-patterns.md`
- `stock-inventory-patterns.md`
- `tax-fiscal-patterns.md`
- `translation-i18n-patterns.md`
- `uom-patterns.md`
- `wizard-patterns.md`
- `workflow-state-patterns.md`
- `config-settings-patterns.md`
- `domain-filter-patterns.md`
- `external-api-patterns.md`

Read only the files relevant to the current task to keep context lean.
