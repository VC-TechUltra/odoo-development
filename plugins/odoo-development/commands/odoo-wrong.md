---
name: odoo-wrong
description: report that Odoo guidance was wrong, missing or outdated so the skill files can be corrected.
---

Report that the guidance you just received was wrong, missing or outdated.

Gather the report from the user, then call `report_odoo_feedback`. Ask only for
what is missing — do not interrogate. If the problem is obvious from the
conversation above, fill it in and confirm rather than asking.

Required:
- `kind` — one of:
  - `wrong_answer` — the guidance was incorrect
  - `missing` — nothing covered this
  - `outdated` — correct for an older version, wrong for this one
- `severity` — one of:
  - `broke_code` — following it produced code that failed
  - `wrong_guidance` — incorrect, but caught before it caused damage
  - `incomplete` — right as far as it went
  - `cosmetic` — unclear or badly worded
- `topic` — a short phrase naming the subject, e.g. "record rule multi-company"
- `version` and `scope` — the Odoo target in play

Optional:
- `detail` — what was said versus what is actually correct

Do not paste client source, credentials, or customer data into `detail`. A
description of the problem is enough.

After reporting, confirm the id returned and continue with the task. A report is
a note for later review, not a blocker.

Use `feedback_summary` to see what has already been reported.
