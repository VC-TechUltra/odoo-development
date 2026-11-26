---
name: odoo-security
description: odoo security patterns for acl, record rules, groups, portal access, validation, multi-company, and secure implementation review. use for access control, record rules, permissions, portal exposure, secure coding, and edition-aware security checks.
---

# Odoo Security

## Router (token-first)
1. Pin version **16–19**: `${ODOO_VERSION}` or nearest `__manifest__.py` (codemode `version`: `v16`|`v17`|`v18`|`v19`).
2. Prefer slim rules + `skills/odoo-invariants.md` — `ir.rule` uses `company_ids` on **all of 16–19** (not `allowed_company_ids`).
3. If need groups/XML IDs/schema: `odoo-codemode` → `codemode_search` → `codemode_execute` (`odoo.compact.security`).
4. If MCP unavailable: Read `skills/odoo-invariants.md`, then at most **one** `skills/odoo-security/odoo-security-guide-{version}.md` (never `-all`).
5. Never invent groups, ACLs, or XML IDs.

## Optional offline patterns (Read only if needed)
- `skills/odoo-security/multi-company-patterns.md`
- `skills/odoo-security/portal-access-patterns.md`
