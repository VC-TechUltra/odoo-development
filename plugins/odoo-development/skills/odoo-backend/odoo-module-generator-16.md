# Odoo 16 Module Generator

## Manifest (__manifest__.py)
```python
{
    'name': 'My Custom Module',
    'version': '16.0.1.0.0',
    'category': 'Business Process',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'installable': True,
    'application': True,
}
```

## models/my_model.py
```python
from odoo import api, fields, models
from odoo import Command

class MyModel(models.Model):
    _name = 'my.module'
    _description = 'My Model'
    
    name = fields.Char(required=True)
    state = fields.Selection([('draft', 'Draft'), ('done', 'Done')], default='draft', tracking=True)
    line_ids = fields.One2many('my.module.line', 'parent_id')
    
    # Use @api.model_create_multi recommended
    @api.model_create_multi
    def create(self, vals_list):
        return super().create(vals_list)
    
    def action_confirm(self):
        for record in self:
            record.write({'state': 'done'})
            # Use Command class for x2many
            record.write({'line_ids': [Command.create({'name': 'New Line'})]})
```

## Using Command Class
```python
from odoo import Command

# Create new lines
vals = {'line_ids': [Command.create({'name': 'Line 1'})]}

# Update existing
vals = {'line_ids': [Command.update(line_id, {'name': 'Updated'})]}

# Delete
vals = {'line_ids': [Command.delete(line_id)]}

# Link
vals = {'line_ids': [Command.link(existing_id)]}

# Clear and set
vals = {'line_ids': [Command.clear(), Command.set([id1, id2])]}
```

## Key v16 Changes
- Command class for x2many operations
- @api.model_create_multi recommended
- attrs deprecated (still works, removed in v17)
- OWL 2.x introduced
