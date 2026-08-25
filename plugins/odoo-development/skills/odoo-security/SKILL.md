---
name: odoo-security
description: odoo security patterns for acl, record rules, groups, portal access, validation, multi-company, and secure implementation review. use for access control, record rules, permissions, portal exposure, secure coding, and edition-aware security checks.
---

# Odoo Security

## Core policy
- Detect target Odoo version first (check __manifest__.py or use ${ODOO_VERSION}).
- Prefer repository patterns and MCP-backed facts over guesses.
- For Odoo 18 and 19 Community and Enterprise, use MCP to verify XML IDs, model schema, dependencies, and multi-company assumptions before changing security.

## MCP-first workflow
When odoo-knowledge MCP is available: use it first. When MCP is unavailable: use built-in tools—proceed, do not block.

1. `health_check` when MCP reachability is uncertain.
2. `search_odoo_codebase` or `code_search` for similar patterns.
3. `read_odoo_file` or `get_file_snippet` for exact source context.
4. `get_odoo_model_schema` for fields, relations, inherited models, and edition-aware assumptions.
5. `get_odoo_xml_id_location` before using or inheriting XML IDs.
6. `get_model_dependencies` before changing manifests or cross-module integrations.
7. `get_odoo_development_guidelines` for Odoo 18/19 CE/EE framework guidance.

## Version-specific knowledge
After detecting the target Odoo version, load the appropriate version file:

**Security guide:** `skills/odoo-security/odoo-security-guide-{version}.md`
- Available: 14, 15, 16, 17, 18, 19, 14-15, 15-16, 17-18, 18-19

Use transition files (e.g., 17-18, 18-19) when working on upgrades between adjacent versions.

## General patterns (version-agnostic)
Load these as needed:
- `skills/odoo-security/multi-company-patterns.md`
- `skills/odoo-security/portal-access-patterns.md`
- `skills/odoo-security/input-validation-schema.md`

Read only the files relevant to the current task to keep context lean.
