# Action Patterns

```
╔══════════════════════════════════════════════════════════════════════════════╗
║  ACTION PATTERNS                                                             ║
║  Window actions, server actions, client actions, and URL actions             ║
║  Use for navigation, automation, and user interface interactions             ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

## Action Types Overview

| Type | Model | Use Case |
|
---

## Standard Window Actions & XML IDs Catalog (Index Ground-Truth)

| Business Domain | Action XML ID | Target Model | Default View Mode |
|---|---|---|---|
| **Sales Orders** | `sale.action_orders` | `sale.order` | `list,kanban,form,calendar,pivot,graph` |
| **Quotations** | `sale.action_quotations_with_onboarding` | `sale.order` | `list,kanban,form,calendar,pivot,graph` |
| **Customer Invoices** | `account.action_move_out_invoice_type` | `account.move` | `list,kanban,form` |
| **Vendor Bills** | `account.action_move_in_invoice_type` | `account.move` | `list,kanban,form` |
| **Transfers / Pickings** | `stock.action_picking_tree_all` | `stock.picking` | `list,kanban,form,calendar` |
| **Purchase Orders** | `purchase.purchase_form_action` | `purchase.order` | `list,kanban,form,pivot,graph` |
| **Contacts / Partners** | `base.action_partner_form` | `res.partner` | `kanban,list,form` |
| **CRM Leads / Pipeline**| `crm.crm_lead_action_pipeline` | `crm.lead` | `kanban,list,form,calendar,pivot,graph` |
| **Products** | `product.product_template_action` | `product.template` | `kanban,list,form` |
| **Employees** | `hr.open_view_employee_list_my` | `hr.employee` | `kanban,list,form,activity` |
