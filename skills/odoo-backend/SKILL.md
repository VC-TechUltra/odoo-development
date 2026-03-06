---
name: odoo-backend
description: odoo backend patterns for models, fields, computed logic, onchange, inheritance, controllers, imports, automation, and module generation. use for python, manifests, orm logic, data models, api, cron, and backend architecture tasks across odoo versions, especially when generating or extending modules.
---

# Odoo Backend

## Core policy
- Detect target Odoo version first.
- Prefer repository patterns and MCP-backed facts over guesses.
- For Odoo 18 and 19 Community and Enterprise, always verify schema, dependencies, and version guidance with MCP before suggesting framework-specific backend code.

## MCP-first workflow
1. `health_check` when MCP reachability is uncertain.
2. `search_odoo_codebase` or `code_search` for similar patterns.
3. `read_odoo_file` or `get_file_snippet` for exact source context.
4. `get_odoo_model_schema` for fields, relations, inherited models, and edition-aware assumptions.
5. `get_odoo_xml_id_location` before using or inheriting XML IDs.
6. `get_model_dependencies` before changing manifests or cross-module integrations.
7. `get_odoo_development_guidelines` for Odoo 18/19 CE/EE framework guidance.

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
- `common-module-templates.md`
- `module-generation-example.md`
- `attachment-binary-patterns.md`
- `import-export-patterns.md`
- `logging-debugging-patterns.md`
- `workflow-orchestrator.md`

Read only the files relevant to the current task to keep context lean.
