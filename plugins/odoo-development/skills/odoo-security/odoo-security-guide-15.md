# Odoo 15 Security Guide

## Access Control List (ACL)
Same as v14:
```
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_my_model_user,my.model.user,model_my_model,base.group_user,1,0,0,0
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
- Same as v14
- company_ids in domain_force

## Security Improvements
- Enhanced validation
- Better SQL injection protection
