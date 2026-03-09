# Odoo 16 Model Patterns

Odoo 16 was released in October 2022. Key features:
- Command class for x2many operations
- @api.model_create_multi recommended
- attrs deprecated (still works)
- OWL 2.x introduced

## Command Class (NEW in v16)
```python
from odoo import Command

# Instead of tuple syntax, use Command class
vals = {
    'line_ids': [
        Command.create({'name': 'Line 1', 'amount': 100}),
        Command.update(existing_id, {'name': 'Updated'}),
        Command.delete(line_id),
        Command.link(existing_id),
        Command.unlink(line_id),
        Command.clear(),
        Command.set([id1, id2]),
    ]
}
```

## @api.model_create_multi (Recommended)
```python
@api.model_create_multi
def create(self, vals_list):
    # vals_list is a list of dicts
    return super().create(vals_list)
```

## Tracking
```python
stage_id = fields.Many2one('stage.model', tracking=True)
state = fields.Selection([('draft', 'Draft')], tracking=True)
```

## Field Definitions
```python
name = fields.Char(required=True)
sequence = fields.Integer(default=10)
amount = fields.Monetary(currency_field='currency_id')
currency_id = fields.Many2one('res.currency')
```

## Computed Fields
```python
amount_total = fields.Float(compute='_compute_total', store=True)

@api.depends('line_ids.amount')
def _compute_total(self):
    for record in self:
        record.amount_total = sum(record.line_ids.mapped('amount'))
```

## View attrs - DEPRECATED (still works in 16)
```xml
<!-- Works but deprecated -->
<field name="discount" attrs="{'readonly': [('state', '=', 'done')]}"/>
```

## Manifest
```python
{
    'name': 'My Module',
    'version': '16.0.1.0.0',
    'depends': ['base'],
    'application': True,
}
```

## Migration Notes from v15 to v16

### Command Class
Replace tuple syntax with Command class:
```python
# v15 (tuple syntax - still works)
vals = {
    'line_ids': [(0, 0, {'name': 'Line 1'}),
                 (1, id, {'name': 'Updated'}),
                 (2, id, False),  # delete
                 (4, id),         # link
                 (5,),            # clear
                 (6, 0, [id1, id2])],  # set
}

# v16 (Command class - recommended)
vals = {
    'line_ids': [Command.create({'name': 'Line 1'}),
                 Command.update(id, {'name': 'Updated'}),
                 Command.delete(id),
                 Command.link(id),
                 Command.clear(),
                 Command.set([id1, id2])],
}
```

### @api.model_create_multi
Migration is optional but recommended:
```python
# v15 style
def create(self, vals):
    if isinstance(vals, dict):
        vals = [vals]
    return super().create(vals)

# v16 style (recommended)
@api.model_create_multi
def create(self, vals_list):
    return super().create(vals_list)
```

## Migration Notes from v16 to v17

### attrs Deprecated
Use `readonly` attribute with conditions instead:
```xml
<!-- v16 -->
<field name="discount" attrs="{'readonly': [('state', '=', 'done')]}"/>

<!-- v17+ -->
<field name="discount" readonly="state == 'done'"/>
```

### Tracking Changes
Tracking behavior is similar, but v17 has improved tracking UI.

### Computed Field Store
The pattern remains the same, but v17 improved recomputation efficiency.

### Field Definitions
Same patterns, v17 introduced `copy="0"` for non-copyable fields.
