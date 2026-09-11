---
name: odoo-migration
description: odoo migration and version-routing guidance for version-specific model, module, security, and frontend changes across odoo 14 to 19. use for upgrades, deprecated pattern replacement, target-version planning, and release-specific implementation choices.
---

# Odoo Migration

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
- `data-migration-patterns.md`
- `odoo-version-knowledge.md`
- `odoo-version-knowledge-all.md`
- `odoo-version-knowledge-17.md`
- `odoo-version-knowledge-18.md`
- `odoo-version-knowledge-19.md`
- `odoo-version-knowledge-17-18.md`
- `odoo-version-knowledge-18-19.md`
- `odoo-editions.md`

Legacy versions (Odoo 14-16). Odoo 14 and 15 predate the odoo-knowledge index (v16-v19) and are unverified; prefer MCP for anything current:
- `odoo-version-knowledge-14.md`
- `odoo-version-knowledge-14-15.md`
- `odoo-version-knowledge-15.md`
- `odoo-version-knowledge-15-16.md`
- `odoo-version-knowledge-16.md`
- `odoo-version-knowledge-16-17.md`

Read only the files relevant to the current task to keep context lean.
