---
name: odoo-migration
description: odoo migration and version-routing guidance for version-specific model, module, security, and frontend changes across odoo 14 to 19. use for upgrades, deprecated pattern replacement, target-version planning, and release-specific implementation choices.
---

# Odoo Migration

## Router (token-first)
1. Pin source and target versions among **16–19** (codemode `v16`|`v17`|`v18`|`v19`).
2. Prefer slim `rules/odoo-upgrade.mdc` + `skills/odoo-invariants.md` matrix for stable break-change / syntax bullets.
3. If need edition/source proof: `odoo-codemode` → `codemode_search` → `codemode_execute` (`odoo.compact.compare_versions`).
4. If MCP unavailable: Read **one** `skills/odoo-migration/odoo-version-knowledge-{version}.md` (never `-all`).
5. Preserve external IDs; migrate incrementally.
