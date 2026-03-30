# Codebase Issue Triage (2026-03-30)

## 1) Typo Fix Task
**Issue:** The Odoo 18 quick-start guidance appears truncated: `type hints rec`.

- **Location:** `skills/agent-quick-start.md` (Version Patterns table, row for 18).
- **Why it matters:** Truncated wording reduces clarity for contributors using this cheat sheet.
- **Proposed task:** Replace `type hints rec` with a complete phrase such as `type hints recommended`.
- **Suggested acceptance criteria:**
  - The row reads clearly and consistently with the rest of the table.
  - No partial or truncated abbreviations remain in that section.

## 2) Bug Fix Task
**Issue:** The `/odoo-test` command points to a non-existent path: `Read: odoo-development/skills/odoo-test-patterns.md`.

- **Location:** `commands/odoo-test.md` (Step 2: Load Testing Patterns).
- **Why it matters:** The agent following this instruction will fail to load the intended testing reference because the actual file is under `skills/odoo-testing/odoo-test-patterns.md`.
- **Proposed task:** Update the referenced path to the existing file path under `skills/odoo-testing/`.
- **Suggested acceptance criteria:**
  - The command references an existing file.
  - A quick `test -f` check passes for the documented path.

## 3) Documentation Discrepancy Task
**Issue:** README command list is incomplete vs. actual commands present in `commands/`.

- **Location:** `README.md` (“How to use” → Commands section).
- **Why it matters:** Users may not discover available commands such as `/odoo-security`, `/odoo-owl`, and `/odoo-test` from the top-level docs.
- **Proposed task:** Align README command list with the current `commands/*.md` inventory.
- **Suggested acceptance criteria:**
  - README command bullets match all shipped command files.
  - Any intentionally hidden/deprecated commands are explicitly labeled.

## 4) Test Improvement Task
**Issue:** No lightweight automated check currently verifies that referenced skill paths in command docs actually exist.

- **Location:** `commands/*.md` (cross-file quality gap).
- **Why it matters:** Broken internal references can silently regress command quality.
- **Proposed task:** Add a CI-friendly script/test that validates file paths referenced after `Read:` in command docs.
- **Suggested acceptance criteria:**
  - Test fails if a referenced file path does not exist.
  - Test can run locally in a single command and is documented.
