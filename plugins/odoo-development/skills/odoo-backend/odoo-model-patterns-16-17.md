# Odoo 16 → 17 Migration Guide

## Breaking Changes

### 1. attrs REMOVED
```xml
<!-- v16 - DEPRECATED but works -->
<field name="discount" attrs="{'readonly': [('state', '=', 'done')]}"/>

<!-- v17 - REQUIRED -->
<field name="discount" readonly="state == 'done'"/>
```

### 2. states REMOVED
```xml
<!-- v16 -->
<field name="date" states="draft,confirmed"/>

<!-- v17 -->
<field name="date" invisible="state not in ('draft', 'confirmed')"/>
```

### 3. @api.model_create_multi MANDATORY
```python
# v16 - recommended
# v17 - mandatory for create() override
@api.model_create_multi
def create(self, vals_list):
    return super().create(vals_list)
```

## Expression Conversion
| v16 attrs | v17 inline |
|-----------|-----------|
| [('state', '=', 'draft')] | state == 'draft' |
| [('state', '!=', 'draft')] | state != 'draft' |
| [('field', '=', False)] | not field |
| ['&', A, B] | A and B |
| ['|', A, B] | A or B |

## Checklist
- [ ] Replace ALL attrs with inline expressions
- [ ] Remove ALL states attributes
- [ ] Add @api.model_create_multi to create methods
- [ ] Update manifest version to 17.0.x.x.x

## Common Errors
- Error: "attrs is not a valid attribute"
- Fix: Convert to inline invisible/readonly/required
