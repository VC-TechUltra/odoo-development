# Odoo 16 → 17 Migration

## Breaking Changes

### attrs REMOVED
```xml
<!-- v16 - DEPRECATED but works -->
<field name="discount" attrs="{'readonly': [('state', '=', 'done')]}"/>

<!-- v17 - REQUIRED inline -->
<field name="discount" readonly="state == 'done'"/>
```

### states REMOVED
```xml
<!-- v16 -->
<field name="date" states="draft,confirmed"/>

<!-- v17 -->
<field name="date" invisible="state in ('draft', 'confirmed')"/>
```

### @api.model_create_multi Mandatory
```python
# MUST add this decorator to create() override
@api.model_create_multi
def create(self, vals_list):
    return super().create(vals_list)
```

## Expression Conversion
| v16 attrs | v17 inline |
|-----------|-----------|
| [('state','=','draft')] | state == 'draft' |
| [('field','!=',False)] | not field |

## Migration Checklist
- [ ] Replace ALL attrs with inline expressions
- [ ] Remove ALL states attributes
- [ ] Add @api.model_create_multi to create methods
- [ ] Update manifest version to 17.0.x.x.x
