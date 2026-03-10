# Odoo 14 Module Generator

## Manifest (__manifest__.py)
```python
{
    'name': 'My Custom Module',
    'version': '14.0.1.0.0',
    'category': 'Business Process',
    'summary': 'Module summary',
    'description': """
        Module description
    """,
    'author': 'Author Name',
    'website': 'https://example.com',
    'license': 'LGPL-3',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
}
```

## __init__.py
```python
from . import models
```

## models/__init__.py
```python
from . import my_model
```

## models/my_model.py
```python
from odoo import api, fields, models

class MyModel(models.Model):
    _name = 'my.module'
    _description = 'My Model'
    
    name = fields.Char(required=True)
    active = fields.Boolean(default=True)
    state = fields.Selection([('draft', 'Draft'), ('done', 'Done')], default='draft')
    
    @api.multi
    def action_confirm(self):
        for record in self:
            record.write({'state': 'done'})
```

## security/ir.model.access.csv
```
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_my_module_user,my.module.user,model_my_module,base.group_user,1,0,0,0
```

## views/views.xml
```xml
<odoo>
    <record id="view_my_module_form" model="ir.ui.view">
        <field name="name">my.module.form</field>
        <field name="model">my.module</field>
        <field name="arch" type="xml">
            <form string="My Module">
                <header>
                    <button name="action_confirm" string="Confirm" type="object"/>
                </header>
                <sheet>
                    <group>
                        <field name="name"/>
                        <field name="state"/>
                    </group>
                </sheet>
            </form>
        </field>
    </record>
</odoo>
```

## Key v14 Notes
- Use @api.multi (deprecated but works)
- track_visibility='onchange' for field tracking
- Tuple syntax for x2many
- attrs in views still works
