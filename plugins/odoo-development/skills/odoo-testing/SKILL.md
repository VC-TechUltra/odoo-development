---
name: odoo-testing
description: odoo testing, verification, and performance patterns for unit tests, integration tests, functional checks, debugging, and optimization. use for test design, regression protection, performance review, and release validation.
---

# Odoo Testing

## Core policy
- Detect target Odoo version first.
- Answer from this skill first; escalate to MCP only for existence checks.
- For Odoo 18 and 19 Community and Enterprise, confirm with MCP that a referenced field, XML ID, dependency or access rule exists before relying on it.

## Answering order
**1. Answer from this skill.** Syntax, patterns, file shapes, conventions and
documented version differences are covered here. Do not call MCP for these.

**2. Escalate to MCP only for existence questions** - a claim about what is
actually present in a given Odoo version:

| Question | Tool |
|---|---|
| Does model X have field/method Y? | `get_odoo_model` |
| Where is this XML ID, what inherits it? | `resolve_odoo_xml_id` |
| What overrides this method? | `trace_odoo_method` |
| What ACLs or record rules apply? | `get_odoo_security` |
| Exact source of a known file range | `read_odoo_source_range` |
| What changed between two versions? | `compare_odoo_versions` |

When you know the file, prefer `read_odoo_source_range` over `get_odoo_model`
(~50k tokens). Always pass `start_line`/`end_line`: a 20-line read is ~180
tokens, but the default range is 200 lines (~2k).

## Included knowledge files
- `odoo-test-patterns.md`
- `odoo-performance-guide.md`
- `end-to-end-examples.md`
- `quick-patterns.md`
- `github-verification-guide.md`
- `github-fetch-patterns.md`

Read only the files relevant to the current task to keep context lean.
