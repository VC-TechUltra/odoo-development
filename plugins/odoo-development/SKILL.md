---
name: odoo-development
description: Odoo development plugin for backend, frontend, migration, security, testing, functional, and troubleshooting. Use MCP-first workflow with version detection.
---

# Odoo Development

## Core Policy
- Detect target Odoo version first (check __manifest__.py or use ${ODOO_VERSION})
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

## Available Skills

### odoo-backend
`skills/odoo-backend/SKILL.md` - Models, fields, computed, onchange, inheritance, controllers, cron, module generation (v14-19)

### odoo-functional
`skills/odoo-functional/SKILL.md` - Domain-specific patterns for accounting, sales, stock, HR, purchase, projects, and other Odoo apps

### odoo-owl
`skills/odoo-owl/SKILL.md` - Frontend JavaScript/OWL components, assets, QWeb templates, widgets, website integration

### odoo-migration
`skills/odoo-migration/SKILL.md` - Version routing, upgrade patterns, deprecated replacements (v14-19)

### odoo-security
`skills/odoo-security/SKILL.md` - ACL, record rules, groups, portal access, validation, multi-company

### odoo-testing
`skills/odoo-testing/SKILL.md` - Unit/integration tests, performance, debugging, release validation

### odoo-troubleshooting
`skills/odoo-troubleshooting/SKILL.md` - Tracebacks, runtime failures, XML issues, debugging workflows

### odoo-orchestrator
`skills/odoo-orchestrator/SKILL.md` - Task routing and planning. Use only when the domain is ambiguous and you need to decide which skill to invoke.

## Rules
- `rules/odoo-core.mdc` - Backend implementation standards
- `rules/odoo-views-security.mdc` - XML views and security standards
- `rules/odoo-owl.mdc` - Frontend and OWL standards
- `rules/odoo-upgrade.mdc` - Migration and upgrade guardrails

## Agents
- `agents/odoo-upgrade-analyzer.md` - Analyze upgrade compatibility
- `agents/odoo-code-reviewer.md` - Review Odoo code quality
- `agents/odoo-context-gatherer.md` - Gather context before code generation
- `agents/odoo-skill-finder.md` - Find specific pattern excerpts
