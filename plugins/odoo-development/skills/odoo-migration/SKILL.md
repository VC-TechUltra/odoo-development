---
name: odoo-migration
description: odoo migration and version-routing guidance for version-specific model, module, security, and frontend changes across odoo 14 to 19. use for upgrades, deprecated pattern replacement, target-version planning, and release-specific implementation choices.
---

# Odoo Migration

## Router (token-first)
1. Pin source and target versions.
2. Prefer slim `rules/odoo-upgrade.mdc` for stable break-change bullets.
3. If need edition/source proof: `odoo-codemode` → `codemode_search` → `codemode_execute` (or `compare_versions` helpers).
4. If MCP unavailable: Read **one** `skills/odoo-migration/odoo-version-knowledge-{version}.md` (never `-all`).
5. Preserve external IDs; migrate incrementally.
