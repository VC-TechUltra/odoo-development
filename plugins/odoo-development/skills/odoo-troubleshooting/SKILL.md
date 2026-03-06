---
name: odoo-troubleshooting
description: odoo troubleshooting patterns for tracebacks, runtime failures, xml issues, data-load problems, dependency mistakes, and debugging workflows. use for pasted exceptions, broken upgrades, load-order issues, and root-cause analysis.
---

# Odoo Troubleshooting

## Core policy
- Detect target Odoo version first.
- Prefer repository patterns and MCP-backed facts over guesses.
- For Odoo 18 and 19 Community and Enterprise, verify the failing model, XML ID, dependency, or framework behavior through MCP before suggesting a fix.

## MCP-first workflow
1. `health_check` when MCP reachability is uncertain.
2. `search_odoo_codebase` or `code_search` for similar patterns.
3. `read_odoo_file` or `get_file_snippet` for exact source context.
4. `get_odoo_model_schema` for fields, relations, inherited models, and edition-aware assumptions.
5. `get_odoo_xml_id_location` before using or inheriting XML IDs.
6. `get_model_dependencies` before changing manifests or cross-module integrations.
7. `get_odoo_development_guidelines` for Odoo 18/19 CE/EE framework guidance.

## Included knowledge files
- `odoo-troubleshooting-guide.md`
- `logging-debugging-patterns.md`
- `error-handling-patterns.md`
- `context-environment-patterns.md`

Read only the files relevant to the current task to keep context lean.
