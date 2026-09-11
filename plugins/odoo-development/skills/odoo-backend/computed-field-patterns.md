# Computed Field Patterns

```
╔══════════════════════════════════════════════════════════════════════════════╗
║  COMPUTED FIELD PATTERNS                                                     ║
║  @api.depends, compute methods, inverse, and search                          ║
║  Use for derived values, aggregations, and dynamic data                      ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

## Basic Computed Fields

### Simple Computation
```python
from odoo import api, fields, models


class MyModel(models.Model):
    _name = 'my.model'

    first_name = fields.Char()
    last_name = fields.Char()

    # Basic computed field
    full_name = fields.Char(
        string='Full Name',
        compute='_compute_full_name',
    )

    @api.depends('first_name', 'last_name')
    def _compute_full_name(self):
        for record in self:
            parts = filter(None, [record.first_name, record.last_name])
            record.full_name = ' '.join(parts)
```

### Stored Computed Field
```python
class MyModel(models.Model):
    _name = 'my.model'

    quantity = fields.Float()
    price = fields.Float()

    # Stored - saved to database, recomputed on dependency change
    subtotal = fields.Float(
        string='Subtotal',
        compute='_compute_subtotal',
        store=True,
    )

    @api.depends('quantity', 'price')
    def _compute_subtotal(self):
        for record in self:
            record.subtotal = record.quantity * record.price
```

### Readonly vs Editable
```python
class MyModel(models.Model):
    _name = 'my.model'

    # Non-stored are always readonly
    calculated_value = fields.Float(compute='_compute_value')

    # Stored computed can be readonly (default) or editable
    total = fields.Float(
        compute='_compute_total',
        store=True,
        readonly=True,  # Default
    )

    # Editable stored computed (rare)
    adjustable_total = fields.Float(
        compute='_compute_adjustable_total',
        store=True,
        readonly=False,
    )
```
---

## Standard Computed Field & Dependency Map (Index Ground-Truth)

| Model | Computed Field | `@api.depends` Dependencies | Store / Searchable |
|---|---|---|---|
| `sale.order` | `amount_untaxed`, `amount_tax`, `amount_total` | `'order_line.price_subtotal'`, `'order_line.price_tax'` | `store=True` |
| `sale.order` | `invoice_status` | `'order_line.invoice_status'`, `'state'` | `store=True` |
| `sale.order.line` | `price_subtotal` | `'price_unit'`, `'tax_id'`, `'discount'`, `'product_uom_qty'` | `store=True` |
| `account.move` | `amount_untaxed`, `amount_total` | `'line_ids.balance'`, `'line_ids.amount_currency'` | `store=True` |
| `account.move` | `payment_state` | `'line_ids.matched_debit_ids'`, `'line_ids.matched_credit_ids'` | `store=True` |
| `stock.picking` | `state` | `'move_ids.state'`, `'move_ids.picking_id'` | `store=True` |
| `product.template`| `qty_available`, `virtual_available` | Context-dependent (`'product_variant_ids'`) | `store=False`, `search='_search_...'` |
