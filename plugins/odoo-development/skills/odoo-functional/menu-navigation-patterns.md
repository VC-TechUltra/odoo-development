# Menu and Navigation Patterns

```
╔══════════════════════════════════════════════════════════════════════════════╗
║  MENU & NAVIGATION PATTERNS                                                  ║
║  Menu structure, navigation, and application organization                    ║
║  Use for module UI organization and user navigation                          ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

## Menu Structure Overview

```
Root Menu (App)
├── Category Menu 1
│   ├── Submenu 1.1 → Action
│   └── Submenu 1.2 → Action
├── Category Menu 2
│   ├── Submenu 2.1 → Action
│   └── Submenu 2.2 → Action
└── Configuration
    ├── Settings → Action
    └── Data → Action
```
---

## Standard Root & Parent Menu XML IDs Catalog

| App / Domain | Root Menu XML ID | Primary Category / Parent Menu ID |
|---|---|---|
| **Sales** | `sale.sale_menu_root` | `sale.sale_order_menu` (Orders), `sale.menu_sale_config` (Configuration) |
| **Invoicing / Accounting**| `account.menu_finance` | `account.menu_finance_receivables` (Customers), `account.menu_finance_payables` (Vendors) |
| **Inventory** | `stock.menu_stock_root` | `stock.menu_stock_warehouse_mgmt` (Operations), `stock.menu_stock_config_settings` |
| **Purchase** | `purchase.menu_purchase_root` | `purchase.menu_procurement_management` (Orders), `purchase.menu_purchase_config` |
| **CRM** | `crm.crm_menu_root` | `crm.crm_menu_sales` (Sales), `crm.crm_menu_leads` (Leads) |
| **Employees** | `hr.menu_hr_root` | `hr.menu_hr_employee_payroll` (Employees), `hr.menu_human_resources_configuration` |
| **Settings** | `base.menu_administration` | `base.menu_custom` (Technical), `base.menu_users` (Users & Companies) |
