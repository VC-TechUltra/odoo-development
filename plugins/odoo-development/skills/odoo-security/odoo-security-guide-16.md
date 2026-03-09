# Odoo 16 Security Guide

## Access Control List (ACL)
Same pattern as v14/v15:
```
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
```

## Record Rules
```xml
<record id="my_model_rule" model="ir.rule">
    <field name="name">my.model: multi-company</field>
    <field name="model_id" ref="model_my_model"/>
    <field name="domain_force">[('company_id', 'in', company_ids)]</field>
</record>
```

## Multi-Company
- company_ids still used
- Enhanced support in v17+

## New in v16
- Better input validation
- Enhanced XSS protection
