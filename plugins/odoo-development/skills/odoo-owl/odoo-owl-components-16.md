# Odoo 16 - OWL 2.x

Odoo 16 introduces OWL 2.x with ES6 modules.

## Component (ES6 Modules)
```javascript
/** @odoo-module **/

import { Component, useState, onWillStart } from "@odoo/owl";
import { registry } from "@web/core/registry";

export class MyComponent extends Component {
    static template = "my_module.MyComponent";
    
    setup() {
        this.state = useState({ count: 0 });
        
        onWillStart(async () => {
            await this.loadData();
        });
    }

    async loadData() {
        // Load data
    }

    increment() {
        this.state.count++;
    }
}

registry.category("actions").add("my_action", MyComponent);
```

## Key Changes from OWL 1.x
- ES6 import/export
- /** @odoo-module **/ annotation
- Static template property
- useService for services

## Using Services
```javascript
import { useService } from "@web/core/utils/hooks";

setup() {
    this.orm = useService("orm");
    this.action = useService("action");
    
    async loadRecords() {
        const records = await this.orm.searchRead("my.model", [], ["name"]);
    }
}
```

## Template
```xml
<templates>
    <t t-name="my_module.MyComponent" owl="1">
        <div class="my-component">
            <span t-esc="state.count"/>
            <button t-on-click="increment">Increment</button>
        </div>
    </t>
</templates>
```

## Manifest
```python
'assets': {
    'web.assets_backend': [
        'my_module/static/src/js/my_component.js',
    ],
},
```

## File Structure (v16+)
```
static/
└── src/
    ├── components/
    │   └── my_component/
    │       ├── my_component.js
    │       ├── my_component.xml
    │       └── my_component.scss
    └── js/
        └── main.js
```
