---
name: odoo-orchestrator
description: odoo task-routing and planning skill that decides which odoo skill to use, gathers context, and enforces mcp-first execution for odoo 18 and 19 community and enterprise work. use for broad odoo requests, ambiguous tasks, and initial planning.
---

# Odoo Orchestrator

## Core policy
- Detect target Odoo version first.
- Answer from this skill first; escalate to MCP only for existence checks.
- Start here for ambiguous Odoo work. Route to backend, security, migration, owl, testing, troubleshooting, or functional skills as needed. For Odoo 18/19 Community and Enterprise, consult MCP before selecting implementation patterns.

## Answering order
**1. Answer from the routed skill.** Syntax, patterns, file shapes, conventions
and documented version differences are covered by the skills. Do not call MCP
for these. When MCP is unavailable, built-in SemanticSearch, Grep and Read are
sufficient—proceed, do not block.

**2. Escalate to MCP only for existence questions** - a claim about what is
actually present in a given Odoo version:

| Question | Tool |
|---|---|
| Does model X have field/method Y? | `get_odoo_model` |
| Where is this XML ID, what inherits it? | `resolve_odoo_xml_id` |
| What overrides this method? | `trace_odoo_method` |
| What ACLs or record rules apply? | `get_odoo_security` |
| Exact source of a known file range | `read_odoo_source_range` |
| What changed between two versions? | `compare_odoo_versions` |

When you know the file, prefer `read_odoo_source_range` over `get_odoo_model`
(~50k tokens). Always pass `start_line`/`end_line`: a 20-line read is ~180
tokens, but the default range is 200 lines (~2k).

## Included knowledge files
- `agent-api-reference.md`
- `agent-quick-reference.md`
- `agent-quick-start.md`
- `autonomous-agent-guide.md`
- `workflow-orchestrator.md`

Read only the files relevant to the current task to keep context lean.
