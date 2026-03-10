# Odoo 14 Frontend - Legacy JavaScript

**Note: Odoo 14 does NOT have OWL. Use legacy JavaScript.**

## Widget Definition
```javascript
odoo.define('my_module.my_widget', function (require) {
    "use strict";

    var Widget = require('web.Widget');
    var core = require('web.core');
    var QWeb = core.qweb;

    var MyWidget = Widget.extend({
        template: 'MyModule.MyWidget',
        
        events: {
            'click .my-button': '_onButtonClick',
            'change .my-input': '_onInputChange',
        },

        init: function (parent, data) {
            this._super(parent, data);
            this.someData = data;
        },

        start: function () {
            this._super.apply(this, arguments);
            this.$el.find('.my-element').text('Hello World');
        },

        _onButtonClick: function (ev) {
            this.do_notify('Title', 'Button clicked!');
        },

        _onInputChange: function (ev) {
            var value = this.$el.find('.my-input').val();
            console.log('Input changed:', value);
        },
    });

    return MyWidget;
});
```

## Widget Extension
```javascript
odoo.define('my_module.widget_extension', function (require) {
    var MyWidget = require('my_module.my_widget');

    MyWidget.include({
        start: function () {
            this._super.apply(this, arguments);
            this.$el.addClass('my-custom-class');
        },
    });

    return MyWidget;
});
```

## Common Requires
- web.Widget
- web.Model
- web.FormWidget
- web.ListView
- web.FormView

## Manifest (v14)
```python
'js': [
    'static/src/js/my_widget.js',
],
'css': [
    'static/src/css/my_widget.scss',
],
'xml': [
    'static/src/xml/my_widget.xml',
],
```

## Template (QWeb)
```xml
<t t-name="MyModule.MyWidget">
    <div class="my-widget">
        <button class="my-button">Click Me</button>
        <input type="text" class="my-input"/>
    </div>
</t>
```

## Key Points
- Use odoo.define()
- Widget.extend() for inheritance
- this._super() for parent methods
- Events dict for DOM events
