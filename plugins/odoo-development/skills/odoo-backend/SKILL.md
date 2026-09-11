---
name: odoo-backend
description: odoo backend patterns for models, fields, computed logic, onchange, inheritance, controllers, imports, automation, xml views, and module generation. use for python, manifests, orm logic, data models, api, cron, form/tree/kanban/search view definitions, view inheritance and xpath, and backend architecture tasks across odoo versions, especially when generating or extending modules.
---

# Odoo Backend

## Strict 3-Tier Retrieval Hierarchy

1. **Tier 1: Answer from this Skill (Default / Fast)**
   - Always check local patterns, conventions, model catalogs, and version matrices first.
   - Zero tool overhead, zero latency.

2. **Tier 2: Odoo Knowledge MCP Database (First Fallback)**
   - If a specific field, method override chain, or XML ID is **not** in this skill's catalog, call MCP tools (`get_odoo_model`, `resolve_odoo_xml_id`, `trace_odoo_method`, `search_odoo_code`, `read_odoo_source_range`).
   - **Negative Knowledge Rule**: DO NOT GUESS or hallucinate missing fields/methods. If not in the skill catalog, escalate to MCP.

3. **Tier 3: Internet / Web Search (Absolute Last Resort)**
   - If and only if the knowledge is absent from BOTH the local skills AND the Odoo MCP database (e.g. unindexed 3rd-party modules, external APIs, non-standard libraries), use web search.
   - Always constrain queries to the specific Odoo version (e.g. `"Odoo 18" OR "Odoo 19"`) and official domains (`github.com/odoo/odoo`, `odoo.com`).

## Universal Core Model Index (Tier-1 Ground-Truth)

> **LOCAL RETRIEVAL RULE**: For detailed field catalogs, mixins, and relational targets, consult this table or read the corresponding local pattern file in `skills/odoo-functional/` BEFORE making any MCP tool calls.

| Model | Inherited Mixins | Key Relational Fields | Standard States | Local Detail File |
|---|---|---|---|---|
| `account.move` | `portal.mixin`, `mail.thread.main.attachment`, `mail.activity.mixin`, `sequence.mixin`, `product.catalog.mixin`, `account.document.import.mixin` | `partner_id`, `journal_id`, `line_ids`, `invoice_line_ids`, `statement_line_ids`, `company_id` | `draft`, `posted`, `cancel` | `skills/odoo-functional/accounting-patterns.md` |
| `account.move.line` | N/A | `move_id`, `account_id`, `partner_id`, `currency_id`, `tax_ids` | `draft`, `posted`, `cancel` | `skills/odoo-functional/accounting-patterns.md` |
| `sale.order` | `portal.mixin`, `mail.thread.main.attachment`, `mail.activity.mixin`, `utm.mixin` | `partner_id`, `order_line`, `company_id`, `pricelist_id`, `currency_id` | `draft`, `sent`, `sale`, `cancel` | `skills/odoo-functional/sale-crm-patterns.md` |
| `sale.order.line` | N/A | `order_id`, `product_id`, `product_uom`, `tax_id` | `draft`, `sale`, `cancel` | `skills/odoo-functional/sale-crm-patterns.md` |
| `stock.picking` | `mail.thread.main.attachment`, `mail.activity.mixin` | `partner_id`, `picking_type_id`, `location_id`, `location_dest_id`, `move_ids` | `draft`, `waiting`, `confirmed`, `assigned`, `done`, `cancel` | `skills/odoo-functional/stock-inventory-patterns.md` |
| `stock.move` | N/A | `picking_id`, `product_id`, `location_id`, `location_dest_id` | `draft`, `waiting`, `confirmed`, `assigned`, `done`, `cancel` | `skills/odoo-functional/stock-inventory-patterns.md` |
| `purchase.order` | `portal.mixin`, `mail.thread.main.attachment`, `mail.activity.mixin` | `partner_id`, `order_line`, `company_id`, `currency_id` | `draft`, `sent`, `to approve`, `purchase`, `done`, `cancel` | `skills/odoo-functional/purchase-procurement-patterns.md` |
| `purchase.order.line`| N/A | `order_id`, `product_id`, `product_uom`, `taxes_id` | `draft`, `sent`, `to approve`, `purchase`, `done`, `cancel` | `skills/odoo-functional/purchase-procurement-patterns.md` |
| `product.template` | `mail.thread.main.attachment`, `mail.activity.mixin`, `image.mixin` | `categ_id`, `uom_id`, `uom_po_id`, `company_id`, `product_variant_ids` | N/A | `skills/odoo-functional/product-variant-patterns.md` |
| `product.product` | `image.mixin` | `product_tmpl_id`, `product_template_attribute_value_ids` | N/A | `skills/odoo-functional/product-variant-patterns.md` |
| `crm.lead` | `mail.thread.main.attachment`, `mail.activity.mixin`, `utm.mixin` | `partner_id`, `user_id`, `team_id`, `stage_id`, `company_id` | `draft`, `assigned`, `won`, `lost` | `skills/odoo-functional/sale-crm-patterns.md` |
| `hr.employee` | `mail.thread.main.attachment`, `mail.activity.mixin`, `resource.mixin`, `avatar.mixin` | `user_id`, `department_id`, `job_id`, `parent_id`, `coach_id`, `company_id` | N/A | `skills/odoo-functional/hr-employee-patterns.md` |
| `res.partner` | `avatar.mixin`, `image.mixin` | `parent_id`, `company_id`, `user_id`, `country_id` | N/A | `skills/odoo-functional/sale-crm-patterns.md` |
| `res.users` | `resource.mixin` | `partner_id`, `company_id`, `company_ids` | N/A | `skills/odoo-security/odoo-security-guide-all.md` |

## Included knowledge files
- `field-type-reference.md`
- `computed-field-patterns.md`
- `constraint-patterns.md`
- `onchange-dynamic-patterns.md`
- `inheritance-patterns.md`
- `context-environment-patterns.md`
- `controller-api-patterns.md`
- `cron-automation-patterns.md`
- `error-handling-patterns.md`
- `odoo-model-patterns.md`
- `odoo-model-patterns-all.md`
- `odoo-model-patterns-17.md`
- `odoo-model-patterns-18.md`
- `odoo-model-patterns-19.md`
- `odoo-model-patterns-17-18.md`
- `odoo-model-patterns-18-19.md`
- `odoo-module-generator.md`
- `odoo-module-generator-all.md`
- `odoo-module-generator-17.md`
- `odoo-module-generator-18.md`
- `odoo-module-generator-19.md`
- `odoo-module-generator-17-18.md`
- `odoo-module-generator-18-19.md`
- `xml-view-patterns.md`
- `field-validation-patterns.md`
- `odoo-syntax-cheatsheet.md`
- `odoo-getting-started.md`
- `common-module-templates.md`
- `module-generation-example.md`
- `attachment-binary-patterns.md`
- `import-export-patterns.md`
- `logging-debugging-patterns.md`
- `workflow-orchestrator.md`

Legacy versions (Odoo 14-16). Odoo 14 and 15 predate the odoo-knowledge index (v16-v19) and are unverified; prefer MCP for anything current:
- `odoo-model-patterns-14.md`
- `odoo-module-generator-14.md`
- `odoo-model-patterns-14-15.md`
- `odoo-model-patterns-15.md`
- `odoo-module-generator-15.md`
- `odoo-model-patterns-15-16.md`
- `odoo-model-patterns-16.md`
- `odoo-module-generator-16.md`
- `odoo-model-patterns-16-17.md`

Read only the files relevant to the current task to keep context lean.
