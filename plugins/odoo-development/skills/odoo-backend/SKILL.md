---
name: odoo-backend
description: odoo backend patterns for models, fields, computed logic, onchange, inheritance, controllers, imports, automation, xml views, and module generation. use for python, manifests, orm logic, data models, api, cron, form/tree/kanban/search view definitions, view inheritance and xpath, and backend architecture tasks across odoo versions, especially when generating or extending modules.
---

# Odoo Backend

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
- `field-type-reference.md`
- `computed-field-patterns.md`
- `constraint-patterns.md`
- `onchange-dynamic-patterns.md`
- `inheritance-patterns.md`
- `context-environment-patterns.md`
- `controller-api-patterns.md`
- `cron-automation-patterns.md`
- `error-handling-patterns.md`
- `odoo-model-patterns.md`
- `odoo-model-patterns-all.md`
- `odoo-model-patterns-17.md`
- `odoo-model-patterns-18.md`
- `odoo-model-patterns-19.md`
- `odoo-model-patterns-17-18.md`
- `odoo-model-patterns-18-19.md`
- `odoo-module-generator.md`
- `odoo-module-generator-all.md`
- `odoo-module-generator-17.md`
- `odoo-module-generator-18.md`
- `odoo-module-generator-19.md`
- `odoo-module-generator-17-18.md`
- `odoo-module-generator-18-19.md`
- `xml-view-patterns.md`
- `field-validation-patterns.md`
- `odoo-syntax-cheatsheet.md`
- `odoo-getting-started.md`
- `common-module-templates.md`
- `module-generation-example.md`
- `attachment-binary-patterns.md`
- `import-export-patterns.md`
- `logging-debugging-patterns.md`
- `workflow-orchestrator.md`

Legacy versions (Odoo 14-16). Odoo 14 and 15 predate the odoo-knowledge index (v16-v19) and are unverified; prefer MCP for anything current:
- `odoo-model-patterns-14.md`
- `odoo-module-generator-14.md`
- `odoo-model-patterns-14-15.md`
- `odoo-model-patterns-15.md`
- `odoo-module-generator-15.md`
- `odoo-model-patterns-15-16.md`
- `odoo-model-patterns-16.md`
- `odoo-module-generator-16.md`
- `odoo-model-patterns-16-17.md`

Read only the files relevant to the current task to keep context lean.
