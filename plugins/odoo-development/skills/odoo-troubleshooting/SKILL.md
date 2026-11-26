---
name: odoo-troubleshooting
description: odoo troubleshooting patterns for tracebacks, runtime failures, xml issues, data-load problems, dependency mistakes, and debugging workflows. use for pasted exceptions, broken upgrades, load-order issues, and root-cause analysis.
---

# Odoo Troubleshooting

## Router (token-first)
1. Pin version: `${ODOO_VERSION}` or nearest `__manifest__.py`.
2. Identify failing model / XML ID / dependency from the traceback first.
3. Prefer `odoo-codemode` → `codemode_search` → `codemode_execute` to confirm source/schema before fixing.
4. If MCP unavailable: Read `skills/odoo-troubleshooting/odoo-troubleshooting-guide.md` only.
