# Model and View Inheritance Patterns

```
╔══════════════════════════════════════════════════════════════════════════════╗
║  INHERITANCE PATTERNS                                                        ║
║  Extending models, views, and controllers without modifying core code        ║
║  Use for customizations, extensions, and module integrations                 ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

## Inheritance Types Overview

| Type | `_name` | `_inherit` | Use Case |
|
---

## Core Method Override & Extension Catalog (Index Ground-Truth)

| Model | Target Method | Typical Return | Common Extension Purpose |
|---|---|---|---|
| `sale.order` | `action_confirm()` | `True` or super() | Create delivery pickings, trigger invoice generation |
| `sale.order` | `_prepare_invoice()` | `dict` (move vals) | Pass custom sale order fields to `account.move` |
| `sale.order.line` | `_prepare_invoice_line(**optional_values)` | `dict` (line vals) | Pass custom line fields/taxes to `account.move.line` |
| `account.move` | `action_post()` | `True` or super() | Post journal entry, lock lines, generate tax audit records |
| `account.move` | `button_draft()` | `True` or super() | Reset posted/cancelled entry back to draft |
| `account.move` | `_compute_name()` | `None` (sets `name`) | Compute sequence numbering on posting |
| `stock.picking` | `button_validate()` | `True` or dict (wizard)| Validate stock transfer, move quants, trigger backorders |
| `stock.move` | `_action_done(cancel_backorder=False)` | `stock.move` recordset | Finish stock move and update on-hand quantities |
| `purchase.order` | `button_confirm()` | `True` or super() | Confirm RFQ into Purchase Order, generate incoming shipment |
| `purchase.order` | `_prepare_invoice()` | `dict` (move vals) | Generate vendor bill from purchase order |
| `res.partner` | `_compute_display_name()` | `None` (sets display) | Format commercial partner or contact display name |
