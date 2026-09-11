# Input Validation Patterns

## Field-Level Validation
```python
# Required field
name = fields.Char(required=True)

# Size constraints
code = fields.Char(size=10)

# Selection enum
state = fields.Selection([('draft','Draft'),('done','Done')])
```

## Python Constraints
```python
from odoo.exceptions import ValidationError

@api.constrains('field1', 'field2')
def _check_values(self):
    for r in self:
        if r.field1 > r.field2:
            raise ValidationError("field1 must be <= field2")
```

## SQL Constraints
```python
_sql_constraints = [
    ('name_uniq', 'UNIQUE(name)', 'Name must be unique!'),
    ('amount_positive', 'CHECK(amount >= 0)', 'Amount must be positive!'),
]
```

## Onchange Validation
```python
@api.onchange('partner_id')
def _onchange_partner(self):
    if self.partner_id and not self.partner_id.email:
        return {'warning': {'title': 'Warning', 'message': 'No email!'}}
```

## Version Notes
- v14-16: Standard patterns
- v17+: Same patterns, attrs replaced with inline expressions
