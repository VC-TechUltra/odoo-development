# Odoo 14 → 15 OWL Migration

## Key Change
- Odoo 15 introduces OWL 1.x
- Legacy JavaScript still works but deprecated

## Legacy to OWL Conversion

### Old (v14)
```javascript
odoo.define('my.widget', function (require) {
    var Widget = require('web.Widget');
    var MyWidget = Widget.extend({
        template: 'MyTemplate',
        events: { 'click': 'onClick' },
        onClick: function () { /* ... */ },
    });
    return MyWidget;
});
```

### New (v15)
```javascript
odoo.define('my_module.MyComponent', function (require) {
    const { Component } = owl;
    const { useState } = owl.hooks;
    
    class MyComponent extends Component {
        static template = "my_module.MyComponent";
        setup() {
            this.state = useState({ clicked: false });
        }
        onClick() {
            this.state.clicked = true;
        }
    }
    return MyComponent;
});
```

## Checklist
- [ ] Start migrating to OWL
- [ ] Use owl="1" in templates
- [ ] Replace Widget.extend with Component class
