---
name: odoo-orchestrator
description: odoo task-routing and planning skill. decides which odoo skill to use and enforces mcp-first execution for odoo 18 and 19 community and enterprise work. use ONLY for broad odoo requests where the domain is ambiguous and you need to decide between backend, functional, owl, migration, security, testing, or troubleshooting skills.
---

# Odoo Orchestrator

## Core policy
- Detect target Odoo version first (check __manifest__.py or use ${ODOO_VERSION}).
- Prefer repository patterns and MCP-backed facts over guesses.
- Route to the appropriate specialized skill based on task domain.
- For Odoo 18/19 Community and Enterprise, consult MCP before selecting implementation patterns.

## MCP-first workflow
When odoo-knowledge MCP is available: use it first. When MCP is unavailable: use built-in SemanticSearch, Grep, and Read tools—proceed, do not block.

1. `health_check` when MCP reachability is uncertain.
2. `search_odoo_codebase` or `code_search` for similar patterns.
3. `read_odoo_file` or `get_file_snippet` for exact source context.
4. `get_odoo_model_schema` for fields, relations, inherited models, and edition-aware assumptions.
5. `get_odoo_xml_id_location` before using or inheriting XML IDs.
6. `get_model_dependencies` before changing manifests or cross-module integrations.
7. `get_odoo_development_guidelines` for Odoo 18/19 CE/EE framework guidance.

## Skill routing
Use this skill to decide which specialized skill to invoke:

- **odoo-backend** - Python models, ORM, manifests, controllers, cron, module structure
- **odoo-functional** - Named app domains (sale, purchase, stock, accounting, hr, etc.)
- **odoo-owl** - Frontend JavaScript/OWL components, widgets, assets, QWeb templates
- **odoo-migration** - Version upgrades, deprecated pattern replacement
- **odoo-security** - ACL, record rules, groups, portal access, multi-company
- **odoo-testing** - Unit tests, integration tests, performance, debugging
- **odoo-troubleshooting** - Tracebacks, runtime errors, data-load issues, debugging

## Quick reference
For general agent guidance, see:
- `skills/odoo-orchestrator/agent-quick-start.md` - Getting started with Odoo tasks

Read only the files relevant to the current task to keep context lean.
