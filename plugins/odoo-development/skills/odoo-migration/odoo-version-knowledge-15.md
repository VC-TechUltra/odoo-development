# Odoo 15 Version Knowledge

Release: October 2021

## Breaking Changes
- @api.multi REMOVED - will cause errors
- track_visibility replaced by tracking=True

## Python API
```python
# NO decorator needed - all methods are multi-record by default
def my_method(self):
    for record in self:
        pass
```

## Field Tracking
```python
# tracking=True replaces track_visibility
stage_id = fields.Many2one('stage.model', tracking=True)
```

## XML Views
- attrs still works
- states still works

## Frontend
- OWL 1.x introduced
- Legacy JavaScript still supported

## Manifest Version
```
'version': '15.0.1.0.0'
```

## Migration from v14
1. Remove all @api.multi decorators
2. Replace track_visibility with tracking=True

## Next Version (16)
- Command class for x2many
- @api.model_create_multi recommended
- attrs deprecated
