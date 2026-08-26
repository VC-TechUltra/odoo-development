# Odoo 16 → 17 Security Migration

## Changes
- Enhanced multi-company support
- allowed_company_ids in context
- Same ACL patterns

## New in v17+
```python
# Rule domains use company_ids (all versions)
domain = [('company_id', 'in', company_ids)]
```

## Checklist
- [ ] Confirm multi-company rules use company_ids
- [ ] Test ACL permissions
