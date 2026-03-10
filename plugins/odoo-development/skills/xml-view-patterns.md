# XML View Patterns Reference

```
╔══════════════════════════════════════════════════════════════════════════════╗
║  XML VIEW PATTERNS                                                           ║
║  Complete reference for Odoo view definitions with version-specific syntax   ║
║  Critical: visibility syntax differs between versions                        ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

## View Types Overview

| View Type | Purpose | Key Attributes |
|-----------|---------|----------------|
| **Form** | Single record editing | `string`, `create`, `edit` |
| **Tree/List** | Multiple records list | `string`, `decoration-*`, `default_order` |
| **Kanban** | Card-based visualization | `default_group_by`, `kanban_draggable` |
| **Search** | Filter and group records | `string`, `model` |
| **Graph** | Bar/line/pie charts | `type` (bar,line,pie) |
| **Pivot** | Matrix/OLAP view | `expand`, `order` |
| **Calendar** | Date-based events | `date_start`, `date_stop`, `color` |
| **Gantt** | Project timeline | `date_start`, `date_stop`, `default_group_by` |

---

## Form View - Basic Structure

```xml
<record id="my_model_view_form" model="ir.ui.view">
    <field name="name">my.model.form</field>
    <field name="model">my.model</field>
    <field name="arch" type="xml">
        <form string="My Model">
            <header>
                <!-- Status bar and buttons -->
                <button name="action_confirm" string="Confirm" type="object" class="oe_highlight"/>
                <field name="state" widget="statusbar" statusbar_visible="draft,confirmed,done"/>
            </header>
            <sheet>
                <!-- Main content area -->
                <group>
                    <group>
                        <field name="name"/>
                        <field name="partner_id"/>
                    </group>
                    <group>
                        <field name="amount" widget="monetary"/>
                        <field name="date"/>
                    </group>
                </group>
                <group string="Notes">
                    <field name="description" nolabel="1"/>
                </group>
                <notebook>
                    <page string="Details" name="details">
                        <field name="line_ids">
                            <tree>
                                <field name="product_id"/>
                                <field name="quantity"/>
                                <field name="price_unit"/>
                            </tree>
                        </field>
                    </page>
                </notebook>
            </sheet>
            <div class="oe_chatter">
                <field name="message_follower_ids" widget="mail_followers"/>
                <field name="message_ids" widget="mail_thread"/>
            </div>
        </form>
    </field>
</record>
```

---

## Visibility Syntax by Version

### v14-v16: attrs Syntax (DEPRECATED in v16, REMOVED in v17)

```xml
<field name="partner_id"
       attrs="{
           'invisible': [('state', '=', 'draft')],
           'readonly': [('state', '!=', 'draft')],
           'required': [('state', '=', 'confirmed')]
       }"/>
```

### v17+: Inline Expression Syntax (REQUIRED)

```xml
<field name="partner_id"
       invisible="state == 'draft'"
       readonly="state != 'draft'"
       required="state == 'confirmed'"/>
```

### v17+: Column Invisible (NEW in v17)

```xml
<field name="internal_note" column_invisible="True"/>
<!-- or -->
<field name="internal_note" column_invisible="not is_admin"/>
```

---

## Expression Conversion Table

| attrs Domain (v14-v16) | v17+ Expression | Description |
|------------------------|-----------------|-------------|
| `[('field', '=', 'value')]` | `field == 'value'` | Equals |
| `[('field', '!=', 'value')]` | `field != 'value'` | Not equals |
| `[('field', '=', False)]` | `not field` or `field == False` | Is False/Empty |
| `[('field', '!=', False)]` | `field` | Is set |
| `[('field', 'in', ['a','b'])]` | `field in ('a', 'b')` | In list |
| `[('field', 'not in', ['a','b'])]` | `field not in ('a', 'b')` | Not in list |
| `['&', A, B]` | `A and B` | AND condition |
| `['|', A, B]` | `A or B` | OR condition |
| `['!', A]` | `not A` | NOT condition |
| `[('field', '>', 100)]` | `field > 100` | Greater than |
| `[('field', '&lt;', 100)]` | `field < 100` | Less than |
| `[('field', 'like', 'test')]` | `field Like 'test%'` | Like pattern |
| `[('field', 'ilike', 'test')]` | `field Ilike 'test%'` | Case-insensitive like |

### Multiple Conditions

```xml
<!-- v14-v16 -->
attrs="{'invisible': ['&', ('state', '=', 'draft'), ('amount', '>', 100)]}"

<!-- v17+ -->
invisible="state == 'draft' and amount > 100"
```

---

## Tree/List View

### Basic List View

```xml
<record id="my_model_view_tree" model="ir.ui.view">
    <field name="name">my.model.tree</field>
    <field name="model">my.model</field>
    <field name="arch" type="xml">
        <tree string="My Models" decoration-danger="state == 'cancel'" 
              decoration-success="state == 'done'" decoration-warning="state == 'pending'"
              default_order="date desc, name asc">
            <field name="name"/>
            <field name="partner_id"/>
            <field name="amount" sum="Total"/>
            <field name="state"/>
            <field name="date"/>
        </tree>
    </field>
</record>
```

### v17+ List View with Column Control

```xml
<tree string="My Models">
    <field name="sequence" widget="handle"/>
    <field name="name"/>
    <field name="amount" sum="Total" column_invisible="not is_admin"/>
    <field name="internal_ref" invisible="True"/>
</tree>
```

---

## Search View

```xml
<record id="my_model_view_search" model="ir.ui.view">
    <field name="name">my.model.search</field>
    <field name="model">my.model</field>
    <field name="arch" type="xml">
        <search string="Search My Model">
            <field name="name" string="Name" filter_domain="['|', ('name', 'ilike', self), ('ref', 'ilike', self)]"/>
            <field name="partner_id"/>
            <field name="user_id"/>
            
            <filter name="draft" string="Draft" domain="[('state', '=', 'draft')]"/>
            <filter name="confirmed" string="Confirmed" domain="[('state', '=', 'confirmed')]"/>
            <filter name="done" string="Done" domain="[('state', '=', 'done')]"/>
            
            <separator/>
            <filter name="today" string="Today" domain="[('date', '=', context_today().strftime('%Y-%m-%d'))]"/>
            
            <group expand="0" string="Group By">
                <filter string="Partner" context="{'group_by': 'partner_id'}"/>
                <filter string="State" context="{'group_by': 'state'}"/>
                <filter string="Month" context="{'group_by': 'date:month'}"/>
            </group>
            
            <searchpanel>
                <field name="partner_id" select="1" icon="oi-arrow-right"/>
            </searchpanel>
        </search>
    </field>
</record>
```

---

## Kanban View

```xml
<record id="my_model_view_kanban" model="ir.ui.view">
    <field name="name">my.model.kanban</field>
    <field name="model">my.model</field>
    <field name="arch" type="xml">
        <kanban default_group_by="state" 
                class="o_kanban_mobile" 
                kanban_draggable="1"
                kanban_color="state"
                group_create="0" group_delete="0" group_edit="0">
            <field name="name"/>
            <field name="partner_id"/>
            <field name="amount"/>
            <field name="state"/>
            <field name="color"/>
            <templates>
                <t t-name="kanban-box">
                    <div t-attf-class="oe_kanban_card #{record.color.raw_value == 1 ? 'oe_kanban_color_1' : ''}">
                        <div class="o_kanban_record_top">
                            <div class="o_kanban_record_headings">
                                <strong class="o_kanban_record_title">
                                    <field name="name"/>
                                </strong>
                            </div>
                            <button name="action_open" type="object" icon="oi-arrow-right" class="oe_link"/>
                        </div>
                        <div class="o_kanban_record_body">
                            <field name="partner_id" widget="res_partner"/>
                            <div t-if="record.amount.raw_value">
                                <strong>
                                    <field name="amount" widget="monetary"/>
                                </strong>
                            </div>
                        </div>
                        <div class="o_kanban_record_bottom">
                            <div class="oe_kanban_bottom_left">
                                <field name="date"/>
                            </div>
                        </div>
                    </div>
                </t>
            </templates>
        </kanban>
    </field>
</record>
```

---

## View Inheritance

### Basic Inheritance with XPath

```xml
<record id="view_inherit" model="ir.ui.view">
    <field name="name">my.model.inherit</field>
    <field name="model">my.model</field>
    <field name="inherit_id" ref="my_module.my_model_view_form"/>
    <field name="arch" type="xml">
        <xpath expr="//field[@name='name']" position="after">
            <field name="code"/>
        </xpath>
    </field>
</record>
```

### Position Values

| Position | Description |
|----------|-------------|
| `before` | Insert before the matched element |
| `after` | Insert after the matched element |
| `inside` | Insert inside the matched element (as last child) |
| `replace` | Replace the matched element entirely |
| `attributes` | Modify attributes of the matched element |

### Inherit Inside a Group

```xml
<xpath expr="//group[@name='left_group']" position="inside">
    <field name="new_field"/>
</xpath>
```

### Replace Element

```xml
<xpath expr="//field[@name='old_field']" position="replace">
    <field name="new_field"/>
</xpath>
```

### Modify Attributes

```xml
<xpath expr="//field[@name='partner_id']" position="attributes">
    <attribute name="invisible">True</attribute>
    <attribute name="domain">[('customer', '=', True)]</attribute>
</xpath>
```

---

## XPath Expressions Reference

| XPath Expression | Matches |
|-----------------|---------|
| `//field[@name='x']` | Field with name='x' |
| `//group[@name='x']` | Group with name='x' |
| `//page[@name='x']` | Page with name='x' |
| `//div[@class='x']` | Div with class='x' |
| `//sheet` | First sheet element |
| `//header` | First header element |
| `//notebook` | First notebook element |
| `//group[2]` | Second group element |
| `//field[@name='partner_id'][1]` | First partner_id field |
| `//tree//field` | Any field inside tree |
| `//group/field` | Field that is direct child of group |

---

## Common Widgets

### Status & Progress

```xml
<field name="state" widget="statusbar" statusbar_visible="draft,confirmed"/>
<field name="progress" widget="progressbar"/>
<field name="priority" widget="priority"/>
```

### Selection & Reference

```xml
<field name="state" widget="selection"/>
<field name="partner_id" widget="res_partner"/>
<field name="user_id" widget="many2one_avatar_user"/>
<field name="category_ids" widget="many2many_tags" options="{'color_field': 'color'}"/>
<field name="image" widget="image" options="{'size': [100, 100]}"/>
```

### Numeric & Data

```xml
<field name="amount" widget="monetary" options="{'currency_field': 'currency_id'}"/>
<field name="date" widget="date"/>
<field name="datetime" widget="datetime"/>
<field name="qty" widget="float_factor" options="{'factor': 2}"/>
<field name="sequence" widget="handle"/>
```

### Boolean & Toggle

```xml
<field name="is_active" widget="boolean_toggle"/>
<field name="is_approved" widget="boolean_favorite"/>
<field name="type" widget="badge"/>
```

### Special

```xml
<field name="note" widget="html" options="{'wet': '0'}"/>
<field name="phone" widget="phone"/>
<field name="email" widget="email"/>
<field name="url" widget="url"/>
<field name="binary" widget="binary"/>
<field name="file" widget="binary" filename="filename"/>
```

---

## Version-Specific Summary

| Feature | v14-v16 | v17+ |
|---------|---------|------|
| **Visibility** | `attrs="{'invisible': [...]}"` | `invisible="condition"` |
| **Readonly** | `attrs="{'readonly': [...]}"` | `readonly="condition"` |
| **Required** | `attrs="{'required': [...]}"` | `required="condition"` |
| **Column Hide** | N/A | `column_invisible="True/condition"` |
| **List Decoration** | `decoration-danger` | `decoration-danger` (still supported) |

### Quick Migration Checklist

- [ ] Replace `attrs` dict with inline attributes
- [ ] Convert domain tuples to Python expressions
- [ ] Remove `type="xml"` from arch field
- [ ] Check `column_invisible` for list views
- [ ] Test all visibility conditions

---

## Additional Patterns

### Conditional Required (v17+)

```xml
<field name="end_date" required="date_type == 'fixed'"/>
```

### Conditional Styling

```xml
<field name="state" class="text-danger" invisible="state != 'cancel'"/>
```

### Dynamic Placeholder

```xml
<field name="name" placeholder="Enter name..." options="{'placeholder': 'Dynamic'}"/>
```

### Group-Based Permissions in Views

```xml
<field name="admin_only_field" invisible="not user.has_group('base.group_system')"/>
```

### Form with Edit Mode Control

```xml
<form string="My Model" create="1" edit="1" delete="1" import="1">
```

### Button Types

```xml
<button name="%(action_wizard)d" string="Run Wizard" type="action"/>
<button name="method_name" string="Process" type="object" class="oe_highlight"/>
<button name="method_name" string="Delete" type="object" icon="trash" confirm="Are you sure?"/>
```

---

## Common Errors & Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| `AttributeError: 'str' object has no attribute 'get'` | Using old attrs syntax in v17 | Convert to inline syntax |
| `Invalid view` | XPath not matching | Verify XPath with field name |
| `Field not found` | Field not in model | Add field to model or check visibility |
| `Arch error` | Malformed XML | Validate XML syntax |
