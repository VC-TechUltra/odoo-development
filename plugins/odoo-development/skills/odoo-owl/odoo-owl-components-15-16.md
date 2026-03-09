# Odoo 15 → 16 OWL Migration

## Key Changes
- OWL 1.x to OWL 2.x
- Legacy JS deprecated (removed in v17)
- ES6 modules introduced

## OWL 1.x to 2.x

### Old (v15 - OWL 1.x)
```javascript
odoo.define('my_module.Component', function (require) {
    const { Component } = owl;
    const { useState } = owl.hooks;
    
    class MyComponent extends Component {
        setup() {
            this.state = useState({ value: 0 });
        }
    }
    MyComponent.template = "module.Component";
    return MyComponent;
});
```

### New (v16 - OWL 2.x)
```javascript
/** @odoo-module **/

import { Component, useState } from "@odoo/owl";
import { registry } from "@web/core/registry";

export class MyComponent extends Component {
    static template = "module.MyComponent";
    
    setup() {
        this.state = useState({ value: 0 });
    }
}

registry.category("actions").add("my_action", MyComponent);
```

## Changes Summary
- /** @odoo-module **/ annotation
- import/export syntax
- useService for services
- Static template property

## Checklist
- [ ] Add /** @odoo-module **/
- [ ] Convert to import syntax
- [ ] Use useService for services
