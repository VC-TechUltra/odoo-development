---
name: odoo-orchestrator
description: odoo task-routing and planning skill. decides which odoo skill to use and enforces mcp-code-first execution for odoo 18 and 19 community and enterprise work. use ONLY for broad odoo requests where the domain is ambiguous and you need to decide between backend, functional, owl, migration, security, testing, or troubleshooting skills.
---

# Odoo Orchestrator

## Router (token-first)
1. Pin version: `${ODOO_VERSION}` or nearest `__manifest__.py`.
2. Route to one specialized skill (backend / functional / owl / migration / security / testing / troubleshooting).
3. Prefer slim local rules for stable syntax; use `odoo-codemode` for research.
4. Do not load overlapping playbooks; keep planning short.
