---
name: odoo-orchestrator
description: odoo task-routing and planning skill that decides which odoo skill to use, gathers context, and enforces mcp-first execution for odoo 18 and 19 community and enterprise work. use for broad odoo requests, ambiguous tasks, and initial planning.
---

# Odoo Orchestrator

## Core policy
- Detect target Odoo version first.
- Prefer repository patterns and MCP-backed facts over guesses.
- Start here for ambiguous Odoo work. Route to backend, security, migration, owl, testing, troubleshooting, or functional skills as needed. For Odoo 18/19 Community and Enterprise, consult MCP before selecting implementation patterns.

## MCP-first workflow
1. `health_check` when MCP reachability is uncertain.
2. `search_odoo_codebase` or `code_search` for similar patterns.
3. `read_odoo_file` or `get_file_snippet` for exact source context.
4. `get_odoo_model_schema` for fields, relations, inherited models, and edition-aware assumptions.
5. `get_odoo_xml_id_location` before using or inheriting XML IDs.
6. `get_model_dependencies` before changing manifests or cross-module integrations.
7. `get_odoo_development_guidelines` for Odoo 18/19 CE/EE framework guidance.

## Included knowledge files
- `agent-api-reference.md`
- `agent-quick-reference.md`
- `agent-quick-start.md`
- `autonomous-agent-guide.md`
- `workflow-orchestrator.md`

Read only the files relevant to the current task to keep context lean.
