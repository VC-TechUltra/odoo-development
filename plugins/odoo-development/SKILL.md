---
name: odoo-development
description: Odoo development plugin for backend, frontend, migration, security, testing, functional, and troubleshooting. Prefer slim local rules plus odoo-codemode for research.
---

# Odoo Development

## Router (token-first)
1. Pin version: `${ODOO_VERSION}` or nearest `__manifest__.py`.
2. Prefer slim rules + `skills/odoo-invariants.md` for stable syntax (cheaper than MCP).
3. For schema / XML IDs / source / multi-fact research: `odoo-codemode` → `codemode_search` → `codemode_execute` (compact helpers).
4. If MCP unavailable: Read `skills/odoo-invariants.md`, then at most **one** versioned skill file; never `-all`.
5. Never invent fields, XML IDs, groups, or dependencies when MCP can confirm them.

## Skills
- `skills/odoo-backend/SKILL.md` — Python/ORM/manifests/controllers
- `skills/odoo-functional/SKILL.md` — named apps (sale, stock, accounting, …)
- `skills/odoo-owl/SKILL.md` — OWL/JS/assets/QWeb
- `skills/odoo-migration/SKILL.md` — upgrades / deprecations
- `skills/odoo-security/SKILL.md` — ACL / rules / multi-company
- `skills/odoo-testing/SKILL.md` — tests / performance
- `skills/odoo-troubleshooting/SKILL.md` — tracebacks / load errors
- `skills/odoo-orchestrator/SKILL.md` — only when domain is ambiguous

## Rules
- `rules/odoo-core.mdc`, `rules/odoo-views-security.mdc`, `rules/odoo-owl.mdc`, `rules/odoo-upgrade.mdc`
