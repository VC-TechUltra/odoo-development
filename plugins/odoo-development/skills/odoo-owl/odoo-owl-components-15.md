# Odoo 15 - OWL 1.x

Odoo 15 introduces OWL 1.x. Legacy JS still works but deprecated.

## OWL Component
```javascript
odoo.define('my_module.MyComponent', function (require) {
    "use strict";

    const { Component } = owl;
    const { useState, useEffect } = owl.hooks;
    const { registry } = require("@web/core/registry");

    class MyComponent extends Component {
        setup() {
            this.state = useState({ count: 0, loading: false });
            
            useEffect(() => {
                console.log('Component mounted');
                return () => console.log('Component unmounted');
            }, () => []);
        }

        increment() {
            this.state.count++;
        }
    }
    MyComponent.template = "my_module.MyComponent";

    registry.category("actions").add("my_action", MyComponent);

    return MyComponent;
});
```

## Template
```xml
<t t-name="my_module.MyComponent" owl="1">
    <div class="my-component">
        <span t-esc="state.count"/>
        <button t-on-click="increment">Increment</button>
    </div>
</t>
```

## Manifest
```python
'assets': {
    'web.assets_backend': [
        'my_module/static/src/js/my_component.js',
        'my_module/static/src/xml/my_component.xml',
    ],
},
```

## Key Differences from Legacy
- Component-based (like React/Vue)
- useState for reactive state
- t-on-click instead of events dict
- t-esc for rendering

## Services
- require("web/core/registry")
- require("web/core/orm_service")
