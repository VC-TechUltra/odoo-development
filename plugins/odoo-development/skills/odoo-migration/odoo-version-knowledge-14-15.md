# Odoo 14 → 15 Migration

## Breaking Changes

### @api.multi Removed
```python
# v14 - WORKS but deprecated
@api.multi
def my_method(self):
    for record in self:
        record.do_something()

# v15 - REMOVE decorator
def my_method(self):
    for record in self:
        record.do_something()
```

### track_visibility Changed
```python
# v14
stage_id = fields.Many2one('stage.model', track_visibility='onchange')

# v15
stage_id = fields.Many2one('stage.model', tracking=True)
```

## Migration Checklist
- [ ] Remove all @api.multi decorators
- [ ] Replace track_visibility='onchange' with tracking=True
- [ ] Update manifest version to 15.0.x.x.x

## Common Errors
- AttributeError: 'model' object has no attribute 'ensure_one'
- Fix: Remove ensure_one() calls or loop properly
