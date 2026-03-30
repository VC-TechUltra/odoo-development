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

Ask user or detect from project:
- 14.0 (Legacy JS, no OWL)
- 15.0 (OWL 1.x)
- 16.0-18.0 (OWL 2.x)
- 19.0 (OWL 3.x)

### Step 2: Load Version-Specific Skill

Read: skills/odoo-owl/odoo-owl-components-{version}.md

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

## Version-Specific Templates

### OWL 1.x (Odoo 15)
```javascript
odoo.define('{module_name}.{ComponentName}', function (require) {
    const { Component } = owl;
    const { useState } = owl.hooks;
    const { registry } = require("@web/core/registry");

    class {ComponentName} extends Component {
        setup() {
            this.state = useState({ value: 0 });
        }
    }
    {ComponentName}.template = "{module_name}.{ComponentName}";
    registry.category("actions").add("{action_name}", {ComponentName});
    return {ComponentName};
});
```

### OWL 2.x (Odoo 16-18)
```javascript
/** @odoo-module **/
import { Component, useState, onWillStart } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";
import { registry } from "@web/core/registry";

export class {ComponentName} extends Component {
    static template = "{module_name}.{ComponentName}";
    static props = { // Optional in OWL 2.x };

    setup() {
        this.orm = useService("orm");
        this.state = useState({ loading: true, data: [] });
        onWillStart(async () => { await this.loadData(); });
    }
}
registry.category("actions").add("{action_name}", {ComponentName});
```

### OWL 3.x (Odoo 19)
```javascript
/** @odoo-module **/
import { Component, useState, onWillStart } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";
import { registry } from "@web/core/registry";

export class {ComponentName} extends Component {
    static template = "{module_name}.{ComponentName}";
    static props = { // REQUIRED in OWL 3.x
        recordId: { type: Number, optional: true },
    };
    setup() {
        this.orm = useService("orm");
        this.state = useState({ loading: true, data: [] });
    }
}
registry.category("actions").add("{action_name}", {ComponentName});
```

## Legacy JavaScript (Odoo 14)

```javascript
odoo.define('my_module.my_widget', function (require) {
    var Widget = require('web.Widget');
    var MyWidget = Widget.extend({
        template: 'MyModule.MyWidget',
        events: { 'click .my-button': '_onClick' },
        start: function () { this.$el.text('Hello'); },
        _onClick: function (ev) { this.do_notify('Clicked', 'Button was clicked!'); },
    });
    return MyWidget;
});
```

## Manifest Assets

### Odoo 15+
'assets': {
    'web.assets_backend': [
        '{module_name}/static/src/**/*.js',
    ],
},

### Odoo 14
'js': ['static/src/js/my_widget.js'],

## Common Services
- orm: Database operations
- action: Navigation
- notification: User notifications
- dialog: Modal dialogs
- user: Current user info

## Instructions
1. Determine Odoo version first
2. Load version-specific OWL skill
3. Verify OWL version matches Odoo version
4. Generate version-appropriate component code
5. Include template XML and SCSS
6. Update manifest assets section
