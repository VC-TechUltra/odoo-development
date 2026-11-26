---
name: odoo-migrate
description: migrate the selected odoo code to the target version with mcp-code verification.
---

Migrate the selected Odoo code to the target version with MCP-code verification.

**If odoo-codemode is unavailable:** Use Grep/Read and `rules/odoo-upgrade.mdc` / one migration skill file. Proceed—do not block.

Workflow:
1. Confirm source and target version.
2. Identify version-sensitive Python, XML, security, manifest, and OWL areas.
3. Prefer slim upgrade rules for known breaks; use `codemode_search` → `codemode_execute` for replacements.
4. Provide minimal migration patches.
