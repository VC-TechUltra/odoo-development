# Odoo Development Quick Reference

## Version Detection
- Check __manifest__.py for version
- @api.multi = v14, tracking=True = v15+, Command = v16+

## Field Quick Ref
```python
# Basic
name = fields.Char(required=True)
active = fields.Boolean(default=True)

# Relational  
partner_id = fields.Many2one('res.partner')
line_ids = fields.One2many('model.line', 'parent_id')

# Computed
total = fields.Float(compute='_compute', store=True)
@api.depends('amount') def _compute(self):
    for r in self: r.total = r.amount
```

## XML View Quick Ref
```xml
<!-- v14-16 -->
<field name="x" attrs="{'readonly': [('state','=','done')]}"/>

<!-- v17+ -->
<field name="x" readonly="state == 'done'"/>
```

## OWL Quick Ref
- v14: Legacy JS (Widget.extend)
- v15: OWL 1.x (Component)
- v16+: OWL 2.x (ES6 modules)

## Common Commands
- /odoo-module - Generate module
- /odoo-owl - OWL component
- /odoo-test - Tests
- /odoo-security - Security
