---
name: odoo-security
description: odoo security patterns for acl, record rules, groups, portal access, validation, multi-company, and secure implementation review. use for access control, record rules, permissions, portal exposure, secure coding, and edition-aware security checks.
---

# Odoo Security

## Router (token-first)
1. Pin version: `${ODOO_VERSION}` or nearest `__manifest__.py`.
2. Prefer slim `rules/odoo-views-security.mdc` — `ir.rule` uses `company_ids` (not `allowed_company_ids`).
3. If need groups/XML IDs/schema: `odoo-codemode` → `codemode_search` → `codemode_execute`.
4. If MCP unavailable: Read **one** `skills/odoo-security/odoo-security-guide-{version}.md` (never `-all`).
5. Never invent groups, ACLs, or XML IDs.

## Optional offline patterns (Read only if needed)
- `skills/odoo-security/multi-company-patterns.md`
- `skills/odoo-security/portal-access-patterns.md`
