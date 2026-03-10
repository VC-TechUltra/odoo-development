# Odoo 14 Model Patterns

Odoo 14 was released in October 2020. Key features:
- @api.multi is DEPRECATED but still works
- track_visibility='onchange' is the standard tracking
- Last version where @api.multi works

## API Decorators
```python
@api.multi  # DEPRECATED - still works
def my_method(self):
    for record in self:
        pass

@api.model
def create(self, vals):
    return super().create(vals)

@api.depends('field1', 'field2')
def _compute_field(self):
    for record in self:
        record.field3 = record.field1 + record.field2
```

## Field Definitions
```python
name = fields.Char(string='Name', required=True)
stage_id = fields.Many2one('stage.model', string='Stage', track_visibility='onchange')
state = fields.Selection([('draft', 'Draft'), ('done', 'Done')], tracking=True)
```

## x2many - Tuple Syntax (v14)
```python
line_ids = fields.One2many('my.line', 'parent_id', string='Lines')
# Using tuple syntax
vals = {'line_ids': [(0, 0, {'name': 'Line 1'}), (4, existing_id)]}
```

## Constraints
```python
_sql_constraints = [
    ('name_uniq', 'UNIQUE(name)', 'Name must be unique!'),
]
@api.constrains('date', 'end_date')
def _check_dates(self):
    # validation
    pass
```

## Computed Fields
```python
amount_total = fields.Float(compute='_compute_amount', store=True)
```

## Onchange
```python
@api.onchange('partner_id')
def _onchange_partner(self):
    if self.partner_id:
        self.address = self.partner_id.address
```

## View attrs (v14)
```xml
<field name="discount" attrs="{'readonly': [('state', '=', 'done')]}"/>
<field name="date" states="draft,confirmed"/>
```

## Migration Notes to Odoo 15

### Key Changes
- @api.multi is REMOVED - use @api.depends or @api.model instead
- `track_visibility='onchange'` replaced by `tracking=True`
- `states` attribute in XML views is DEPRECATED (use attrs)
- Many2one fields require explicit `ondelete='cascade'` for proper cascade delete
- `company_dependent` field attribute replaced by `global_company_dependent`

### Code Migration Example
```python
# Odoo 14
@api.multi
def action_done(self):
    for record in self:
        record.state = 'done'

# Odoo 15+ - @api.multi is removed
def action_done(self):
    for record in self:
        record.state = 'done'
    # Or use @api.depends for computed logic
```

### View Migration
```xml
<!-- Odoo 14 -->
<field name="date" states="draft,confirmed"/>

<!-- Odoo 15+ -->
<field name="date" attrs="{'readonly': [('state', 'not in', ('draft', 'confirmed'))]}"/>
```

### Tracking Migration
```python
# Odoo 14
stage_id = fields.Many2one('stage.model', track_visibility='onchange')

# Odoo 15+
stage_id = fields.Many2one('stage.model', tracking=True)
```
