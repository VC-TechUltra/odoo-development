---
name: odoo-functional
description: odoo functional domain patterns covering accounting, sales, crm, hr, purchase, stock, projects, product variants, pricing, taxes, uom, reports, mail, menus, actions, wizards, workflows, and business flows. use for domain-specific module work.
---

# Odoo Functional

## Core policy
- Detect target Odoo version first (check __manifest__.py or use ${ODOO_VERSION}).
- Prefer repository patterns and MCP-backed facts over guesses.
- For Odoo 18 and 19 Community and Enterprise, use MCP to verify app-specific models, XML IDs, dependencies, and workflows before generating domain-specific code.

## MCP-first workflow
When odoo-knowledge MCP is available: use it first. When MCP is unavailable: use built-in tools—proceed, do not block.

1. `health_check` when MCP reachability is uncertain.
2. `search_odoo_codebase` or `code_search` for similar patterns.
3. `read_odoo_file` or `get_file_snippet` for exact source context.
4. `get_odoo_model_schema` for fields, relations, inherited models, and edition-aware assumptions.
5. `get_odoo_xml_id_location` before using or inheriting XML IDs.
6. `get_model_dependencies` before changing manifests or cross-module integrations.
7. `get_odoo_development_guidelines` for Odoo 18/19 CE/EE framework guidance.

## Functional patterns
Load these as needed based on the app/domain:
- `skills/odoo-functional/accounting-patterns.md` - Account, invoice, payment flows
- `skills/odoo-functional/action-patterns.md` - Window actions, wizards, scheduled actions
- `skills/odoo-functional/config-settings-patterns.md` - Configuration settings
- `skills/odoo-functional/domain-filter-patterns.md` - Domain filtering
- `skills/odoo-functional/external-api-patterns.md` - External API integration
- `skills/odoo-functional/hr-employee-patterns.md` - HR and employee management
- `skills/odoo-functional/lot-serial-patterns.md` - Lot and serial tracking
- `skills/odoo-functional/mail-notification-patterns.md` - Mail and notification
- `skills/odoo-functional/menu-patterns.md` - Menu structures
- `skills/odoo-functional/multi-currency-patterns.md` - Multi-currency support
- `skills/odoo-functional/partner-contact-patterns.md` - Partner and contact management
- `skills/odoo-functional/pricing-patterns.md` - Pricing and pricelist
- `skills/odoo-functional/product-catalog-patterns.md` - Product catalog
- `skills/odoo-functional/product-variant-patterns.md` - Product variants
- `skills/odoo-functional/project-task-patterns.md` - Projects and tasks
- `skills/odoo-functional/purchase-patterns.md` - Purchase orders
- `skills/odoo-functional/reporting-patterns.md` - Reports and analysis
- `skills/odoo-functional/sale-order-patterns.md` - Sales orders
- `skills/odoo-functional/stock-movement-patterns.md` - Stock and warehouse
- `skills/odoo-functional/tax-computation-patterns.md` - Tax computation
- `skills/odoo-functional/uom-patterns.md` - Unit of measure
- `skills/odoo-functional/wizard-patterns.md` - Wizards and transient models
- `skills/odoo-functional/workflow-patterns.md` - State workflows

Read only the files relevant to the current task to keep context lean.
