---
name: odoo-functional
description: odoo functional domain patterns covering accounting, sales, crm, hr, purchase, stock, projects, product variants, pricing, taxes, uom, reports, mail, menus, actions, wizards, workflows, and business flows. use for domain-specific module work.
---

# Odoo Functional

## Core policy
- Detect target Odoo version first.
- Prefer repository patterns and MCP-backed facts over guesses.
- For Odoo 18 and 19 Community and Enterprise, use MCP to verify upstream model and XML structures before extending functional apps.

## MCP-first workflow
1. `health_check` when MCP reachability is uncertain.
2. `search_odoo_codebase` or `code_search` for similar patterns.
3. `read_odoo_file` or `get_file_snippet` for exact source context.
4. `get_odoo_model_schema` for fields, relations, inherited models, and edition-aware assumptions.
5. `get_odoo_xml_id_location` before using or inheriting XML IDs.
6. `get_model_dependencies` before changing manifests or cross-module integrations.
7. `get_odoo_development_guidelines` for Odoo 18/19 CE/EE framework guidance.

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
