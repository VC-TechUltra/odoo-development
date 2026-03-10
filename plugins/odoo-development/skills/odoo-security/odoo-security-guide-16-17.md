# Odoo 16 → 17 Security Migration

## Changes
- Enhanced multi-company support
- allowed_company_ids in context
- Same ACL patterns

## New in v17+
```python
# Use allowed_company_ids in v17+
domain = [('company_id', 'in', allowed_company_ids)]
```

## Checklist
- [ ] Update multi-company rules to use allowed_company_ids
- [ ] Test ACL permissions
