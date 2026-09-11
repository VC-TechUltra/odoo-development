---
name: odoo-migrate
description: migrate the selected odoo code to the target version, with replacements confirmed against the odoo index.
---

Migrate the selected Odoo code to the target version, confirming each replacement against the index.

**If odoo-knowledge MCP is unavailable:** Use built-in SemanticSearch, Grep, and Read tools to find patterns. Proceed with migration—do not block.

Workflow:
1. Confirm source and target version.
2. Identify version-sensitive Python, XML, security, manifest, and OWL areas.
3. Take the version-hop deltas from `skills/odoo-migration/`.
4. Escalate to MCP only to confirm a replacement symbol exists in the target
   version (`compare_odoo_versions`, `get_odoo_model`).
5. Provide minimal migration patches.
