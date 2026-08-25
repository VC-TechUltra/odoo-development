---
name: odoo-testing
description: odoo testing, verification, and performance patterns for unit tests, integration tests, functional checks, debugging, and optimization. use for test design, regression protection, performance review, and release validation.
---

# Odoo Testing

## Core policy
- Detect target Odoo version first (check __manifest__.py or use ${ODOO_VERSION}).
- Prefer repository patterns and MCP-backed facts over guesses.
- For Odoo 18 and 19 Community and Enterprise, verify target-version APIs and edition-specific flows with MCP before finalizing tests.

## MCP-first workflow
When odoo-knowledge MCP is available: use it first. When MCP is unavailable: use built-in tools—proceed, do not block.

1. `health_check` when MCP reachability is uncertain.
2. `search_odoo_codebase` or `code_search` for similar patterns.
3. `read_odoo_file` or `get_file_snippet` for exact source context.
4. `get_odoo_model_schema` for fields, relations, inherited models, and edition-aware assumptions.
5. `get_odoo_xml_id_location` before using or inheriting XML IDs.
6. `get_model_dependencies` before changing manifests or cross-module integrations.
7. `get_odoo_development_guidelines` for Odoo 18/19 CE/EE framework guidance.

## Testing patterns
Load these as needed:
- `skills/odoo-testing/odoo-test-patterns.md` - Core testing patterns (TransactionCase, etc.)
- `skills/odoo-testing/odoo-performance-guide.md` - Performance testing and optimization
- `skills/odoo-testing/end-to-end-examples.md` - Complete test examples
- `skills/odoo-testing/quick-patterns.md` - Quick test patterns
- `skills/odoo-testing/github-verification-guide.md` - GitHub CI/CD verification
- `skills/odoo-testing/github-fetch-patterns.md` - Fetching and analyzing GitHub data

Read only the files relevant to the current task to keep context lean.
