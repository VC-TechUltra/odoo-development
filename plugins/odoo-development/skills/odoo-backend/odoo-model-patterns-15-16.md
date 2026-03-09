# Odoo 15 → 16 Migration Guide

## New Features

### 1. Command Class for x2many
```python
# v15 - Tuple syntax
vals = {'line_ids': [(0, 0, {'name': 'Line'})]}

# v16 - Command class (RECOMMENDED)
from odoo import Command
vals = {'line_ids': [Command.create({'name': 'Line'})]}
```

### 2. @api.model_create_multi Recommended
```python
# Recommended for v16+
@api.model_create_multi
def create(self, vals_list):
    return super().create(vals_list)
```

### 3. attrs DEPRECATED (still works)
```xml
<!-- Still works but deprecated in v16 -->
<field name="discount" attrs="{'readonly': [('state', '=', 'done')]}"/>

<!-- v17+ style (works in v16) -->
<field name="discount" readonly="state == 'done'"/>
```

## Checklist
- [ ] Adopt Command class for x2many
- [ ] Add @api.model_create_multi to create methods
- [ ] Start migrating attrs to inline expressions
- [ ] Update manifest version to 16.0.x.x.x

## OWL Note
v16 introduces OWL 2.x. Legacy JS still works but deprecated.
