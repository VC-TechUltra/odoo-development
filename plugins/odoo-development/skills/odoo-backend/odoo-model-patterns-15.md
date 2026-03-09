# Odoo 15 Model Patterns

Odoo 15 was released in October 2021. Key features:
- @api.multi is REMOVED - will cause errors if used
- tracking=True replaces track_visibility
- All methods are implicitly multi-record
- OWL 1.x introduced

## API Changes - @api.multi REMOVED
```python
# WRONG - will cause error in v15
@api.multi
def my_method(self):
    pass

# CORRECT - no decorator needed
def my_method(self):
    for record in self:
        pass
```

## Tracking
```python
# Old v14
stage_id = fields.Many2one('stage.model', track_visibility='onchange')

# New v15
stage_id = fields.Many2one('stage.model', tracking=True)
state = fields.Selection([('draft', 'Draft')], tracking=True)
```

## Field Definitions
```python
name = fields.Char(required=True)
active = fields.Boolean(default=True)
amount = fields.Float(digits=(16, 2))
```

## x2many - Still tuple syntax
```python
line_ids = fields.One2many('my.line', 'parent_id')
vals = {'line_ids': [(0, 0, {'name': 'Line'})]}
```

## Computed Fields
```python
amount_total = fields.Float(compute='_compute_total', store=True)

@api.depends('line_ids.amount')
def _compute_total(self):
    for record in self:
        record.amount_total = sum(record.line_ids.mapped('amount'))
```

## View attrs still works (deprecated in 16, removed in 17)
```xml
<field name="discount" attrs="{'readonly': [('state', '=', 'done')]}"/>
```

## Manifest
```python
{
    'name': 'My Module',
    'version': '15.0.1.0.0',
    'depends': ['base'],
}
```

## Migration Notes from v14 to v15

### Remove @api.multi
All methods now implicitly work on recordset. Remove the decorator:
```python
# Before v15
@api.multi
def process(self):
    for rec in self:
        rec.write({'state': 'done'})

# v15+
def process(self):
    for rec in self:
        rec.write({'state': 'done'})
```

### Replace track_visibility with tracking
```python
# v14
name = fields.Char(track_visibility='onchange')

# v15+
name = fields.Char(tracking=True)
```

### model_attribute vs @api.model
```python
# v14 - @api.model for single record
@api.model
def create(self, vals):
    return super().create(vals)

# v15+ - still the same
@api.model
def create(self, vals):
    return super().create(vals)
```

## Migration Notes from v15 to v16

### tracking=True still works
The tracking parameter is still supported in v16.

### attrs still works (deprecated)
View attrs still works but is deprecated in v16.

### compute_sudo still available
```python
amount = fields.Float(compute='_compute_amount', compute_sudo=True)
```

### New in v16
- WebP support for images
- Excel export improvements
- kanban view improvements
