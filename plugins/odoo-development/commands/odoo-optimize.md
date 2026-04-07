---
name: odoo-optimize
description: analyze odoo orm/query performance and suggest safe optimization strategies.
---

Analyze the selected Odoo code for ORM/query performance bottlenecks and provide upgrade-safe optimizations.

Before optimizing:
- Detect Odoo version.
- Prefer `odoo-query-optimizer` for deep analysis.
- Use MCP verification first when available:
  - `health_check`
  - `search_odoo_codebase` / `code_search`
  - `read_odoo_file` / `get_file_snippet`
  - `get_odoo_model_schema`
  - `get_model_dependencies`
  - `get_odoo_development_guidelines`
- Use targeted MCP helpers as needed:
  - `find_model_file`, `find_method_definition`
  - `find_view_arch`, `find_inherited_views`
  - `find_xml_record`, `resolve_customization_target`

If MCP is unavailable, continue with local repository tools and explicitly call out assumptions.

Focus areas:
- N+1 query patterns
- Batch create/write/read strategies
- `_read_group` opportunities
- Compute/onchange performance hotspots
- Report/cron throughput bottlenecks

Output:
- Hotspots with file:line evidence
- Critical/High/Medium optimization items
- Proposed patch strategy with risk notes
- Validation checklist (tests + benchmark approach)
