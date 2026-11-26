---
name: odoo-testing
description: odoo testing, verification, and performance patterns for unit tests, integration tests, functional checks, debugging, and optimization. use for test design, regression protection, performance review, and release validation.
---

# Odoo Testing

## Router (token-first)
1. Pin version: `${ODOO_VERSION}` or nearest `__manifest__.py`.
2. Prefer local `TransactionCase` / `HttpCase` patterns; use Command/tuples per version rules.
3. If need target APIs/edition flows: `odoo-codemode` → `codemode_search` → `codemode_execute`.
4. If MCP unavailable: Read `skills/odoo-testing/odoo-test-patterns.md` only.
