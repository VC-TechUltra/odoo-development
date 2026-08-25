---
name: odoo-owl
description: Generate OWL components for Odoo frontend. Use when user asks to "create owl component", "add widget", "frontend component", "client action".
---

# Odoo OWL Command

Generate OWL components for Odoo frontend development.

## CRITICAL: OWL VERSION REQUIREMENT

```
╔══════════════════════════════════════════════════════════════════════════════╗
║  OWL versions are COMPLETELY DIFFERENT between Odoo versions!              ║
║                                                                              ║
║  - Odoo 14: NO OWL (use legacy JavaScript)                                 ║
║  - Odoo 15: OWL 1.x (odoo.define syntax)                                   ║
║  - Odoo 16-18: OWL 2.x (ES modules)                                        ║
║  - Odoo 19+: OWL 3.x (ES modules, strict props)                             ║
║                                                                              ║
║  Using wrong OWL version WILL cause JavaScript errors.                       ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

## Execution Flow

### Step 1: Determine Version

Detect from project (check __manifest__.py) or use ${ODOO_VERSION}:
- 14.0 (Legacy JS, no OWL)
- 15.0 (OWL 1.x)
- 16.0-18.0 (OWL 2.x)
- 19.0+ (OWL 3.x)

### Step 2: Load Version-Specific Skill

Read: skills/odoo-owl/odoo-owl-components-{version}.md

Example: For Odoo 18, read `skills/odoo-owl/odoo-owl-components-18.md`

### Step 3: Gather Component Information

- Component type (widget, action, systray, dialog, field)
- Component name
- Required services
- State requirements

## Component Types

- Widget: Custom UI element embedded in views
- Client Action: Full-page components registered in action registry
- Systray Item: Icons in the top-right system tray
- Dialog: Modal dialog components
- Field Widget: Custom field rendering in forms/lists

## Instructions
1. Determine Odoo version first
2. Load version-specific OWL skill using the path template above
3. Verify OWL version matches Odoo version
4. Generate version-appropriate component code
5. Include template XML and SCSS
6. Update manifest assets section
