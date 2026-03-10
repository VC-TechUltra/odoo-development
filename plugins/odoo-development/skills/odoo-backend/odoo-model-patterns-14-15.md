# Odoo 14 → 15 Migration Guide

## Breaking Changes

### 1. @api.multi REMOVED
```python
# v14 (DEPRECATED but works)
@api.multi
def my_method(self):
    for record in self:
        pass

# v15 (CORRECT)
def my_method(self):
    for record in self:
        pass
```

### 2. Tracking Changed
```python
# v14
stage_id = fields.Many2one('stage.model', track_visibility='onchange')

# v15
stage_id = fields.Many2one('stage.model', tracking=True)
```

### 3. View attrs - Still works in 15
```xml
<!-- Still works in v15, will break in v17 -->
<field name="discount" attrs="{'readonly': [('state', '=', 'done')]}"/>
```

## Checklist
- [ ] Remove all @api.multi decorators
- [ ] Replace track_visibility with tracking=True
- [ ] Test all methods work without @api.multi
- [ ] Update manifest version to 15.0.x.x.x

## Common Errors
- AttributeError: 'model' object has no attribute 'ensure_one' with multi-record
- Fix: Remove ensure_one() or loop over self
