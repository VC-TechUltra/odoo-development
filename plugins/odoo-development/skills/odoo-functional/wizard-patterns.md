# Wizard and Transient Model Patterns

```
╔══════════════════════════════════════════════════════════════════════════════╗
║  WIZARD PATTERNS                                                             ║
║  Complete reference for transient models and wizard implementation           ║
║  Use for user interactions, batch operations, and confirmation dialogs       ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

## Overview

Wizards (TransientModel) are temporary records that:
- Auto-delete after a period (vacuum)
- Don't persist permanently in database
- Perfect for user dialogs and batch operations
- Support multi-record operations
---

## Core Standard TransientModel Wizards Catalog

| Wizard Model | Table Name | Purpose / Trigger Point |
|---|---|---|
| `account.payment.register` | `account_payment_register` | Triggered by `account.move.action_register_payment()` to record payment |
| `sale.advance.payment.inv` | `sale_advance_payment_inv` | Triggered from sale order to create regular/down-payment invoice |
| `stock.immediate.transfer` | `stock_immediate_transfer` | Validates picking when quantities are processed without reservations |
| `stock.backorder.confirmation`| `stock_backorder_confirmation`| Prompted when partial picking quantity is processed |
| `stock.return.picking` | `stock_return_picking` | Generates reverse picking / returns for stock transfers |
