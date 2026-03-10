---
name: odoo-development
description: Odoo development plugin for backend, migration, security, testing, and troubleshooting. Use MCP-first workflow with version detection.
---

# Odoo Development

## Core Policy
- Detect target Odoo version first
- Prefer MCP verification over guessing
- For Odoo 18/19 CE/EE, use MCP to verify schema, XML IDs, dependencies, framework guidance

## MCP-First Workflow
1. `health_check` - MCP reachability
2. `search_odoo_codebase` / `code_search` - find patterns
3. `read_odoo_file` / `get_file_snippet` - source context
4. `get_odoo_model_schema` - fields, relations, edition-aware assumptions
5. `get_odoo_xml_id_location` - XML ID inheritance
6. `get_model_dependencies` - manifest/cross-module changes
7. `get_odoo_development_guidelines` - Odoo 18/19 CE/EE guidance

## Skills Index

### odoo-backend
`skills/odoo-backend/SKILL.md` - Models, fields, computed, onchange, inheritance, controllers, cron, module generation (v14-19)

### odoo-migration
`skills/odoo-migration/SKILL.md` - Version routing, upgrade patterns, deprecated replacements (v14-19)

### odoo-security
`skills/odoo-security/SKILL.md` - ACL, record rules, groups, portal access, validation, multi-company

### odoo-testing
`skills/odoo-testing/SKILL.md` - Unit/integration tests, performance, debugging, release validation

### odoo-troubleshooting
`skills/odoo-troubleshooting/SKILL.md` - Tracebacks, runtime failures, XML issues, debugging workflows

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
