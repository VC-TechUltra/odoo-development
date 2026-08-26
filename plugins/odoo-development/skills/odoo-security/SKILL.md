---
name: odoo-security
description: odoo security patterns for acl, record rules, groups, portal access, validation, multi-company, and secure implementation review. use for access control, record rules, permissions, portal exposure, secure coding, and edition-aware security checks.
---

# Odoo Security

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
- `odoo-security-guide.md`
- `odoo-security-guide-all.md`
- `odoo-security-guide-17.md`
- `odoo-security-guide-18.md`
- `odoo-security-guide-19.md`
- `odoo-security-guide-17-18.md`
- `odoo-security-guide-18-19.md`
- `multi-company-patterns.md`
- `portal-access-patterns.md`
- `input-validation-schema.md`

Legacy versions (Odoo 14-16). Odoo 14 and 15 predate the odoo-knowledge index (v16-v19) and are unverified; prefer MCP for anything current:
- `odoo-security-guide-14.md`
- `odoo-security-guide-14-15.md`
- `odoo-security-guide-15.md`
- `odoo-security-guide-15-16.md`
- `odoo-security-guide-16.md`
- `odoo-security-guide-16-17.md`

Read only the files relevant to the current task to keep context lean.
