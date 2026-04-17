# Cursor Plugin Improvement Ideas (Focus: Token Usage)

## High-impact token reductions

1. **Compress agent prompts**
   - Keep role + workflow + output contract only.
   - Move large examples/version tables to skill docs and reference them by file.

2. **Use two-phase retrieval by default**
   - Phase 1: `odoo-skill-finder` returns path + lines.
   - Phase 2: main agent reads only that excerpt if needed.

3. **Enforce output budgets in prompts**
   - Add explicit limits like:
     - max 5 bullets for notes
     - max 2 code snippets unless user asks for more
     - no repeated summaries

4. **Version-aware file routing**
   - Resolve version first, then load only matching version docs.
   - Avoid opening cross-version “all versions” docs unless version is unknown.

5. **Short command scaffolds**
   - In command markdown files, replace long policy repetition with links to one canonical policy file.

## Drop-in prompt upgrades

Use these as standard clauses in agent prompts:

- **Context budget:** “Read at most 3 files in first pass; fetch more only if blocked.”
- **Response budget:** “Keep first response under 220 tokens unless user requests detail.”
- **Snippet budget:** “Provide max 2 snippets; prefer smallest runnable examples.”
- **Retry policy:** “If answer confidence is low, ask one clarifying question instead of expanding context.”

## Quality improvements (non-token)

1. **Add consistency checks in hooks**
   - Warn when generated answers omit target version.
   - Warn when response includes patterns from mixed major versions.

2. **Add lightweight tests for prompt contracts**
   - Validate required sections exist in agent outputs (version, risks, files consulted).

3. **Create shared “response templates” folder**
   - Reuse compact templates across agents and commands.

## Suggested metrics to track

- Average prompt tokens per Odoo task
- Average completion tokens per command
- % of runs loading more than 3 skill files
- % outputs missing version line
- % responses exceeding first-pass budget

## 30/60/90 rollout

- **Day 30:** Apply token budgets to top 2 agents, measure baseline delta.
- **Day 60:** Add hook warnings and contract tests.
- **Day 90:** Tune budgets by command type and publish defaults.
