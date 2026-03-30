---
name: odoo-security
description: Implement Odoo security (ACL, record rules, groups). Use when user asks to "add security", "create access rights", "configure permissions".
---

# Odoo Security Command

Implement security for Odoo modules including ACLs, record rules, groups, and multi-company rules.

## Execution Flow

### Step 1: Identify Target Models

- List all models in the module
- Identify which need access control

### Step 2: Load Version-Specific Security Guide

```
Read: skills/odoo-security/odoo-security-guide-{version}.md
```

### Step 3: Generate Security Files

## Access Control List (ACL) - ir.model.access.csv

```
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_my_model_user,my.model.user,model_my_model,base.group_user,1,0,0,0
access_my_model_manager,my.model.manager,model_my_model,base.group_system,1,1,1,1
```

## Record Rules

### Single Company
```xml
<record id="my_model_comp_rule" model="ir.rule">
    <field name="name">my.model: multi-company</field>
    <field name="model_id" ref="model_my_model"/>
    <field name="domain_force">[('company_id', 'in', company_ids)]</field>
</record>
```

### Multi-company (v18+)
```xml
<record id="my_model_comp_rule" model="ir.rule">
    <field name="name">my.model: multi-company</field>
    <field name="model_id" ref="model_my_model"/>
    <field name="domain_force">[('company_id', 'in', allowed_company_ids)]</field>
</record>
```

## Security Groups

```xml
<record id="group_my_model_user" model="res.groups">
    <field name="name">My Model User</field>
    <field name="category_id" ref="module_category_my"/>
</record>
```

## Version-Specific Notes

### Odoo 14-16
- Use `company_id` in domain_force
- Standard ACL patterns

### Odoo 17+
- Enhanced multi-company support
- allowed_company_ids in context

### Odoo 18+
- _check_company_auto = True
- check_company=True on fields

## Instructions
1. Identify all models requiring security
2. Load version-specific security guide
3. Generate ACL CSV file
4. Generate record rules XML
5. Generate group definitions if needed
6. Verify multi-company compatibility
