---
name: odoo-security
description: odoo security patterns for acl, record rules, groups, portal access, validation, multi-company, and secure implementation review. use for access control, record rules, permissions, portal exposure, secure coding, and edition-aware security checks.
---

# Odoo Security

## Core policy
- Detect target Odoo version first.
- Prefer repository patterns and MCP-backed facts over guesses.
- For Odoo 18 and 19 Community and Enterprise, use MCP to verify XML IDs, model schema, dependencies, and multi-company assumptions before changing security.

## MCP-first workflow
1. `health_check` when MCP reachability is uncertain.
2. `search_odoo_codebase` or `code_search` for similar patterns.
3. `read_odoo_file` or `get_file_snippet` for exact source context.
4. `get_odoo_model_schema` for fields, relations, inherited models, and edition-aware assumptions.
5. `get_odoo_xml_id_location` before using or inheriting XML IDs.
6. `get_model_dependencies` before changing manifests or cross-module integrations.
7. `get_odoo_development_guidelines` for Odoo 18/19 CE/EE framework guidance.

## Included knowledge files
- `odoo-security-guide.md`
- `odoo-security-guide-all.md`
- `odoo-security-guide-17.md`
- `odoo-security-guide-18.md`
- `odoo-security-guide-19.md`
- `odoo-security-guide-17-18.md`
- `odoo-security-guide-18-19.md`
- `multi-company-patterns.md`
- `portal-access-patterns.md`
- `input-validation-schema.md`

Read only the files relevant to the current task to keep context lean.
