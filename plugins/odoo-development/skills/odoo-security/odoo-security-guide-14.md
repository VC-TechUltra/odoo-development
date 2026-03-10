# Odoo 14 Security Guide

## Access Control List (ACL)
```
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_my_model_user,my.model.user,model_my_model,base.group_user,1,0,0,0
access_my_model_manager,my.model.manager,model_my_model,base.group_system,1,1,1,1
```

## Record Rules
```xml
<record id="my_model_rule" model="ir.rule">
    <field name="name">my.model: multi-company</field>
    <field name="model_id" ref="model_my_model"/>
    <field name="domain_force">[('company_id', 'in', company_ids)]</field>
</record>
```

## Security Groups
```xml
<record id="group_my_model_user" model="res.groups">
    <field name="name">My Model User</field>
    <field name="category_id" ref="module_category_my"/>
</record>
```

## Multi-Company
- Use company_ids in domain
- Standard record rules

## Best Practices
- Define ACL for each model
- Use record rules for row-level security
- Avoid sudo() where possible
