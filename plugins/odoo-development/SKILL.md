---
name: odoo-development
description: Odoo development plugin for backend, migration, security, testing, and troubleshooting. Skill-first workflow with version detection; MCP confirms what exists in a version.
---

# Odoo Development

## Core Policy
- Detect target Odoo version first
- Answer from the skills; they cover syntax, patterns and version differences
- Escalate to MCP only to confirm a field, method, XML ID, dependency or access
  rule actually exists in the target version

## Answering order
1. Answer from the relevant skill - syntax, patterns, conventions, version differences.
2. Escalate to MCP only to confirm what EXISTS in a version:
   - field/method on a model -> `get_odoo_model`
   - XML ID and its inheritors -> `resolve_odoo_xml_id`
   - method overrides -> `trace_odoo_method`
   - ACLs and record rules -> `get_odoo_security`
   - known file range -> `read_odoo_source_range`
   - cross-version diff -> `compare_odoo_versions`

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
