# Odoo 16 Version Knowledge

Release: October 2022

## New Features
- Command class for x2many operations
- @api.model_create_multi recommended

## Python API
```python
from odoo import Command

# Use Command class
vals = {'line_ids': [Command.create({'name': 'Line'})]}

# model_create_multi recommended
@api.model_create_multi
def create(self, vals_list):
    return super().create(vals_list)
```

## XML Views
- attrs DEPRECATED (still works, removed in v17)
- states still works

## Frontend
- OWL 2.x introduced
- Legacy JavaScript deprecated

## Manifest Version
```
'version': '16.0.1.0.0'
```

## Migration from v15
1. Adopt Command class for x2many
2. Add @api.model_create_multi

## Next Version (17)
- attrs REMOVED
- states REMOVED
- @api.model_create_multi mandatory
