---
name: odoo-development
description: Odoo development plugin for backend, migration, security, testing, troubleshooting, OWL, functional flows, and orchestration. Use version detection with MCP-preferred verification.
---

# Odoo Development

## Core Policy
- Detect target Odoo version first.
- Prefer MCP verification over guessing.
- For Odoo 18/19 CE/EE, prioritize MCP for schema, XML IDs, dependencies, and framework guidance.
- If MCP is unavailable, fall back to repository search/read workflows and explicitly note assumptions.

## Capability Alignment (Synced with `README.md`)
This skill reflects the plugin capability set documented in `plugins/odoo-development/README.md`:
- **Commands:** `/odoo-plan`, `/odoo-review`, `/odoo-module`, `/odoo-migrate`, `/odoo-fix-traceback`, `/odoo-security`, `/odoo-test`, `/odoo-owl`, `/odoo-optimize`, `/odoo-session-start`, `/odoo-session-summary`, `/odoo-session-clear`, `/odoo-repo-reindex`, `/odoo-health-check`
- **Skills:** backend, migration, security, testing, troubleshooting, OWL, functional, orchestrator
- **Rules:** core backend, XML/security, OWL, upgrade safety
- **Hooks + MCP:** session health checks, path safety reminders, MCP-first guidance with fallback support

## MCP-Preferred Workflow
1. `health_check` - MCP reachability
2. `search_odoo_codebase` / `code_search` - locate repository patterns
3. `read_odoo_file` / `get_file_snippet` - gather concrete context
4. `get_odoo_model_schema` - verify fields/relations (edition-aware)
5. `get_odoo_xml_id_location` - resolve XML inheritance and references
6. `get_model_dependencies` - validate dependency/module impact
7. `get_odoo_development_guidelines` - framework guidance (especially Odoo 18/19)

If steps 1-7 are partially unavailable, continue with local repository evidence and call out risk areas.

## Skills Index
- `skills/odoo-backend/SKILL.md` - Models, fields, computed/onchange, inheritance, controllers, cron, module generation (v14-19)
- `skills/odoo-migration/SKILL.md` - Version routing, upgrade patterns, deprecated replacements (v14-19)
- `skills/odoo-security/SKILL.md` - ACLs, record rules, groups, portal access, validation, multi-company
- `skills/odoo-testing/SKILL.md` - Unit/integration tests, performance, debugging, release checks
- `skills/odoo-troubleshooting/SKILL.md` - Tracebacks, runtime failures, XML/load issues, debugging workflows
- `skills/odoo-owl/SKILL.md` - OWL component patterns, assets, widgets, templates
- `skills/odoo-functional/SKILL.md` - Business workflow and functional customization patterns
- `skills/odoo-orchestrator/SKILL.md` - Multi-step execution and context orchestration

## Agent Selection (Preference Logic, Not Hard Lock)
- Prefer `agents/odoo-code-reviewer.md` for broad or high-risk code reviews.
- Prefer `agents/odoo-upgrade-analyzer.md` for cross-version migration analysis.
- Prefer `agents/odoo-context-gatherer.md` when implementation needs concise version-scoped context.
- Prefer `agents/odoo-skill-finder.md` when only a minimal excerpt is needed.
- Prefer `agents/odoo-query-optimizer.md` for ORM/query performance diagnosis and batching strategy.
- For small, single-file tasks, direct execution is acceptable if version and risk checks are still enforced.

## End-to-End Examples

### 1) Real Odoo Code Review Workflow
**Scenario:** User asks: “Review my custom sale workflow module for security/perf on Odoo 18.”

1. Detect version from `__manifest__.py` (`18.0.x`).
2. Prefer `odoo-code-reviewer` for systematic review.
3. Use MCP/local checks for model schema, XML IDs, dependencies, and risky patterns.
4. Audit manifest, models, security, views, and performance hotspots.
5. Produce prioritized findings (Critical/Warning/Suggestion) with file:line evidence and concrete fixes.

### 2) Real Migration + Traceback Workflow
**Scenario:** User asks: “Migrate 16.0 module to 18.0 and fix ParseError during upgrade.”

1. Confirm source/target versions and migration path (16 -> 17 -> 18 concerns).
2. Prefer `odoo-upgrade-analyzer` to enumerate breaking changes (`attrs` removal, create signatures, company vars).
3. Apply migration edits in Python/XML/security with ordered data file checks.
4. When traceback appears, switch to troubleshooting flow:
   - Parse traceback root cause (file, XML ID, line, failing model/field)
   - Verify referenced records are defined before use
   - Re-run validation and provide minimal corrective patch
5. Return a final migration checklist, regression tests, and residual risks.

## Third Pass: Stricter File-by-File Audit Plan
Use this audit when a user asks for a strict documentation or migration hardening pass.

1. **`SKILL.md` (this file)**
   - Ensure listed capabilities exactly match `README.md` (commands, skills, rules, hooks, MCP fallback).
   - Replace absolute “must use exact agent” language with preference-based routing.
   - Keep at least one full review and one migration+traceback workflow example.

2. **`README.md` (plugin README)**
   - Keep “Included capabilities” synchronized with skill and command inventory.
   - Ensure MCP policy clearly says “MCP-first/preferred” and documents fallback behavior.
   - Confirm command list matches actual command files in `commands/`.

3. **`agents/odoo-code-reviewer.md`**
   - Convert “always/must invoke this agent” wording to “preferred for broad/high-risk reviews”.
   - Preserve strict version detection and structured review categories.

4. **`agents/odoo-context-gatherer.md`**
   - Change “required before every generation task” to “preferred default for multi-file or uncertain tasks”.
   - Keep compact-output and version-purity constraints.

5. **Validation checks after edits**
   - Verify all referenced commands, skills, rules, and agents exist on disk.
   - Verify no contradictory policy text between `SKILL.md` and `README.md`.
