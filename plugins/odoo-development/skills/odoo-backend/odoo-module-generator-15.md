# Odoo 15 Module Generator

## Manifest (__manifest__.py)
```python
{
    'name': 'My Custom Module',
    'version': '15.0.1.0.0',
    'category': 'Business Process',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'installable': True,
}
```

## models/my_model.py
```python
from odoo import fields, models

class MyModel(models.Model):
    _name = 'my.module'
    _description = 'My Model'
    
    name = fields.Char(required=True)
    state = fields.Selection([('draft', 'Draft'), ('done', 'Done')], default='draft', tracking=True)
    
    # NO @api.multi - methods are implicitly multi-record
    def action_confirm(self):
        for record in self:
            record.write({'state': 'done'})
```

## Key v15 Changes
- @api.multi REMOVED - will cause errors
- tracking=True instead of track_visibility
- All methods are implicitly multi-record
- OWL 1.x available (use legacy JS for compatibility)
