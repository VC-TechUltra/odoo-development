---
name: odoo-testing
description: odoo testing, verification, and performance patterns for unit tests, integration tests, functional checks, debugging, and optimization. use for test design, regression protection, performance review, and release validation.
---

# Odoo Testing

## Core policy
- Detect target Odoo version first.
- Prefer repository patterns and MCP-backed facts over guesses.
- For Odoo 18 and 19 Community and Enterprise, verify target-version APIs and edition-specific flows with MCP before finalizing tests.

## MCP-first workflow
1. `health_check` when MCP reachability is uncertain.
2. `search_odoo_codebase` or `code_search` for similar patterns.
3. `read_odoo_file` or `get_file_snippet` for exact source context.
4. `get_odoo_model_schema` for fields, relations, inherited models, and edition-aware assumptions.
5. `get_odoo_xml_id_location` before using or inheriting XML IDs.
6. `get_model_dependencies` before changing manifests or cross-module integrations.
7. `get_odoo_development_guidelines` for Odoo 18/19 CE/EE framework guidance.

## Included knowledge files
- `odoo-test-patterns.md`
- `odoo-performance-guide.md`
- `end-to-end-examples.md`
- `quick-patterns.md`
- `github-verification-guide.md`
- `github-fetch-patterns.md`

Read only the files relevant to the current task to keep context lean.
