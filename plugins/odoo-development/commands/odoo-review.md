---
name: odoo-review
description: review the selected odoo code for correctness, security, maintainability, and upgrade safety.
---

Review the selected Odoo code for correctness, security, maintainability, and upgrade safety.

**If odoo-codemode is unavailable:** Use Grep/Read. Proceed—do not block.

Before reviewing:
- Detect version.
- Prefer slim local rules for stable syntax (`attrs`, `company_ids`, `useService`, `Command`).
- For schema/XML IDs/dependencies: `codemode_search` → `codemode_execute`.

Output:
- Critical
- High
- Medium
- Low
- Suggested patch strategy
