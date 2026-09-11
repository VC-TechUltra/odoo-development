# Odoo Project Instructions

- Answer from the odoo-development skills first.
- Detect target Odoo version before generating code.
- Call MCP only to confirm version-specific existence: does this field, method,
  XML ID or dependency exist, what inherits it, what access rules apply.
- Never assert that a field, XML ID, group or dependency exists without MCP
  confirmation. Skills describe patterns; only MCP knows what is in the tree.
- Reuse repository patterns before introducing new abstractions.
- Keep changes minimal, upgrade-safe, and security-aware.
- Do not invent fields, XML IDs, groups, or dependencies when MCP can confirm them.
