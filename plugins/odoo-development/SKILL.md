---
name: odoo-development
description: Odoo development plugin for backend, functional, migration, owl, security, testing, troubleshooting, and workflow orchestration across Odoo 14-19. Strict 3-tier retrieval hierarchy (Local Skills First -> MCP Fallback Only -> Internet Last Resort).
---

# Odoo Development

## Core Policy
- **Zero-Tool Policy for Ground-Truth Catalogs**: The skill files and Universal Core Model Index ALREADY contain verified ground truth. DO NOT call MCP tools to "confirm" or "re-verify" models, mixins, or fields that are already listed.
- **Strict 3-Tier Retrieval**:
  1. **Tier 1 (Skills First - 0 Tool Calls)**: Answer syntax, core models, mixins, relational fields, selection states, OWL widgets, and migration rules directly from local skill catalogs without tool calls.
  2. **Tier 2 (Odoo MCP Database - Fallback Only)**: Escalate to MCP ONLY when reading exact file source lines (`read_odoo_source_range`), tracing multi-module method override graphs (`trace_odoo_method`), or when a model is completely unlisted.
  3. **Tier 3 (Internet as Last Resort)**: For unindexed 3rd-party modules with version constraints.
- **Negative Knowledge Guard**: NEVER guess or hallucinate unlisted fields or methods.
- **Automatic Version Detection**: Inspect `__manifest__.py` to determine target version (v14-v19).

## Universal Core Model Index (Tier-1 Ground-Truth)

> **LOCAL RETRIEVAL MANDATE**: Answer directly from this table or local files in `skills/odoo-functional/`. DO NOT call MCP tools to re-check these facts.

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

## Skills Directory Index
1. `skills/odoo-backend/SKILL.md` - ORM, fields, compute dependencies, inheritance, SQL builder (v14-19)
2. `skills/odoo-functional/SKILL.md` - Core business catalogs (sale, account, stock, purchase, product, hr, crm), actions, menus, wizards
3. `skills/odoo-migration/SKILL.md` - Version routing, attrs removal, upgrade patterns (v14-19)
4. `skills/odoo-owl/SKILL.md` - OWL 2/3 widgets, registries, asset bundles
5. `skills/odoo-security/SKILL.md` - Groups, ACLs, record rules, _check_company_auto
6. `skills/odoo-testing/SKILL.md` - TransactionCase, test fixtures
7. `skills/odoo-troubleshooting/SKILL.md` - Tracebacks, runtime fixes
8. `skills/odoo-orchestrator/SKILL.md` - Multi-step business workflow orchestration

## Rules
- `rules/odoo-core.mdc`
- `rules/odoo-views-security.mdc`
- `rules/odoo-owl.mdc`
- `rules/odoo-upgrade.mdc`

## Agents
- `agents/odoo-upgrade-analyzer.md`
- `agents/odoo-code-reviewer.md`
- `agents/odoo-context-gatherer.md`
- `agents/odoo-skill-finder.md`
