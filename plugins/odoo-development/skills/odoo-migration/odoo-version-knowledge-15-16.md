# Odoo 15 → 16 Migration

## New Features

### Command Class (Recommended)
```python
# v15 - Tuple syntax
vals = {'line_ids': [(0, 0, {'name': 'Line'})]}

# v16 - Command class
from odoo import Command
vals = {'line_ids': [Command.create({'name': 'Line'})]}
```

### @api.model_create_multi Recommended
```python
@api.model_create_multi
def create(self, vals_list):
    return super().create(vals_list)
```

### attrs Deprecated
```xml
<!-- Still works but deprecated -->
<field name="x" attrs="{'readonly': [('state', '=', 'done')]}"/>
```

## Migration Checklist
- [ ] Adopt Command class for x2many
- [ ] Add @api.model_create_multi to create methods
- [ ] Update manifest version to 16.0.x.x.x
