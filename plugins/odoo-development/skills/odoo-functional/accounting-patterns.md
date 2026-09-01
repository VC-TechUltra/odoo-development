# Accounting Integration Patterns

```
╔══════════════════════════════════════════════════════════════════════════════╗
║  ACCOUNTING INTEGRATION PATTERNS                                             ║
║  Journal entries, invoicing, and financial operations                        ║
║  Use for ERP integrations, financial reporting, and accounting automation    ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

## Module Setup

### Manifest Dependencies
```python
{
    'name': 'My Accounting Module',
    'version': '18.0.1.0.0',
    'depends': ['account'],
    'data': [
        'security/ir.model.access.csv',
        'data/account_data.xml',
        'views/account_views.xml',
    ],
}
```

---

## Journal Entries

### Create Journal Entry
```python
from odoo import api, fields, models
from odoo.exceptions import UserError


class AccountingMixin(models.AbstractModel):
    _name = 'accounting.mixin'
    _description = 'Accounting Mixin'

    def _create_journal_entry(self, lines, journal=None, ref=None, date=None):
        """Create a journal entry with multiple lines.

        Args:
            lines: List of dicts with account_id, debit, credit, partner_id
            journal: account.journal record (optional)
            ref: Reference string
            date: Entry date (defaults to today)

        Returns:
            account.move record
        """
        if not journal:
            journal = self.env['account.journal'].search([
                ('type', '=', 'general'),
                ('company_id', '=', self.env.company.id),
            ], limit=1)

        move_vals = {
            'journal_id': journal.id,
            'date': date or fields.Date.today(),
            'ref': ref or self.name,
            'line_ids': [(0, 0, {
                'account_id': line['account_id'],
                'partner_id': line.get('partner_id'),
                'name': line.get('name', ref or '/'),
                'debit': line.get('debit', 0.0),
                'credit': line.get('credit', 0.0),
            }) for line in lines],
        }

        move = self.env['account.move'].create(move_vals)
        return move

    def _post_journal_entry(self, lines, **kwargs):
        """Create and post journal entry."""
        move = self._create_journal_entry(lines, **kwargs)
        move.action_post()
        return move
```

### Balanced Entry Example
```python
def _create_expense_entry(self, amount, expense_account, description):
    """Create expense journal entry."""
    bank_account = self.env['account.account'].search([
        ('account_type', '=', 'asset_cash'),
        ('company_id', '=', self.env.company.id),
    ], limit=1)

    lines = [
        {
            'account_id': expense_account.id,
            'name': description,
            'debit': amount,
            'credit': 0.0,
        },
        {
            'account_id': bank_account.id,
            'name': description,
            'debit': 0.0,
            'credit': amount,
        },
    ]

    return self._post_journal_entry(lines, ref=description)
```

---

## Invoice Creation

### Customer Invoice
```python
def _create_customer_invoice(self, partner, lines, date=None):
    """Create customer invoice.

    Args:
        partner: res.partner record
        lines: List of dicts with product_id, quantity, price_unit
        date: Invoice date

    Returns:
        account.move record (invoice)
    """
    invoice_vals = {
        'move_type': 'out_invoice',
        'partner_id': partner.id,
        'invoice_date': date or fields.Date.today(),
        'invoice_line_ids': [(0, 0, {
            'product_id': line.get('product_id'),
            'name': line.get('name', line.get('product_id') and
                           self.env['product.product'].browse(line['product_id']).name),
            'quantity': line.get('quantity', 1),
            'price_unit': line['price_unit'],
            'tax_ids': line.get('tax_ids', [(6, 0, [])]),
        }) for line in lines],
    }

    invoice = self.env['account.move'].create(invoice_vals)
    return invoice


def _create_and_post_invoice(self, partner, lines, **kwargs):
    """Create and post customer invoice."""
    invoice = self._create_customer_invoice(partner, lines, **kwargs)
    invoice.action_post()
    return invoice
```

### Vendor Bill
```python
def _create_vendor_bill(self, partner, lines, date=None, ref=None):
    """Create vendor bill.

    Args:
        partner: res.partner (vendor)
        lines: List of dicts with product_id, quantity, price_unit
        date: Bill date
        ref: Vendor reference

    Returns:
        account.move record (bill)
    """
    bill_vals = {
        'move_type': 'in_invoice',
        'partner_id': partner.id,
        'invoice_date': date or fields.Date.today(),
        'ref': ref,
        'invoice_line_ids': [(0, 0, {
            'product_id': line.get('product_id'),
            'name': line.get('name', ''),
            'quantity': line.get('quantity', 1),
            'price_unit': line['price_unit'],
        }) for line in lines],
    }

    bill = self.env['account.move'].create(bill_vals)
    return bill
```

### Credit Note
```python
def _create_credit_note(self, invoice, reason=None):
    """Create credit note for an invoice.

    Args:
        invoice: Original account.move record
        reason: Reason for credit

    Returns:
        account.move record (credit note)
    """
    # Use the reversal wizard approach
    reversal_wizard = self.env['account.move.reversal'].with_context(
        active_model='account.move',
        active_ids=invoice.ids,
    ).create({
        'reason': reason or 'Credit Note',
        'refund_method': 'refund',  # 'refund', 'cancel', 'modify'
        'journal_id': invoice.journal_id.id,
    })

    result = reversal_wizard.reverse_moves()
    credit_note = self.env['account.move'].browse(result['res_id'])

    return credit_note
```

---

## Payment Processing

### Register Payment
```python
def _register_payment(self, invoice, amount=None, date=None, journal=None):
    """Register payment for an invoice.

    Args:
        invoice: account.move record
        amount: Payment amount (defaults to invoice amount)
        date: Payment date
        journal: Payment journal

    Returns:
        account.payment record
    """
    if not journal:
        journal = self.env['account.journal'].search([
            ('type', 'in', ['bank', 'cash']),
            ('company_id', '=', self.env.company.id),
        ], limit=1)

    payment_vals = {
        'payment_type': 'inbound' if invoice.move_type == 'out_invoice' else 'outbound',
        'partner_type': 'customer' if invoice.move_type in ['out_invoice', 'out_refund'] else 'supplier',
        'partner_id': invoice.partner_id.id,
        'amount': amount or invoice.amount_residual,
        'date': date or fields.Date.today(),
        'journal_id': journal.id,
        'ref': invoice.name,
    }

    payment = self.env['account.payment'].create(payment_vals)
    payment.action_post()

    # Reconcile with invoice
    lines_to_reconcile = (payment.move_id.line_ids + invoice.line_ids).filtered(
        lambda l: l.account_id.reconcile and not l.reconciled
    )
    lines_to_reconcile.reconcile()

    return payment
```

### Bulk Payment
```python
def _create_batch_payment(self, invoices, journal=None):
    """Create batch payment for multiple invoices.

    Args:
        invoices: account.move recordset

    Returns:
        account.payment record
    """
    if not invoices:
        raise UserError("No invoices to pay")

    # Group by partner
    partner = invoices[0].partner_id
    if any(inv.partner_id != partner for inv in invoices):
        raise UserError("All invoices must be for the same partner")

    total_amount = sum(invoices.mapped('amount_residual'))

    payment = self._register_payment(
        invoices[0],
        amount=total_amount,
        journal=journal,
    )

    # Reconcile all invoices
    for invoice in invoices[1:]:
        lines_to_reconcile = (payment.move_id.line_ids + invoice.line_ids).filtered(
            lambda l: l.account_id.reconcile and not l.reconciled
        )
        lines_to_reconcile.reconcile()

    return payment
```

---

## Account Queries

### Get Account by Type
```python
def _get_account(self, account_type, company=None):
    """Get account by type.

    Args:
        account_type: e.g., 'asset_receivable', 'liability_payable',
                     'expense', 'income', 'asset_cash'
    """
    company = company or self.env.company
    return self.env['account.account'].search([
        ('account_type', '=', account_type),
        ('company_id', '=', company.id),
    ], limit=1)


def _get_receivable_account(self):
    return self._get_account('asset_receivable')


def _get_payable_account(self):
    return self._get_account('liability_payable')


def _get_expense_account(self, product=None):
    if product and product.property_account_expense_id:
        return product.property_account_expense_id
    return self._get_account('expense')


def _get_income_account(self, product=None):
    if product and product.property_account_income_id:
        return product.property_account_income_id
    return self._get_account('income')
```

### Get Journal by Type
```python
def _get_journal(self, journal_type, company=None):
    """Get journal by type.

    Args:
        journal_type: 'sale', 'purchase', 'cash', 'bank', 'general'
    """
    company = company or self.env.company
    return self.env['account.journal'].search([
        ('type', '=', journal_type),
        ('company_id', '=', company.id),
    ], limit=1)
```

---

## Financial Reports

### Partner Balance
```python
def _get_partner_balance(self, partner, account_type='asset_receivable'):
    """Get partner balance for specific account type."""
    account = self._get_account(account_type)

    self.env.cr.execute("""
        SELECT COALESCE(SUM(debit - credit), 0)
        FROM account_move_line
        WHERE partner_id = %s
        AND account_id = %s
        AND parent_state = 'posted'
    """, (partner.id, account.id))

    return self.env.cr.fetchone()[0]


def _get_customer_receivable(self, partner):
    """Get customer receivable balance."""
    return self._get_partner_balance(partner, 'asset_receivable')


def _get_vendor_payable(self, partner):
    """Get vendor payable balance."""
    return self._get_partner_balance(partner, 'liability_payable')
```

### Account Balance
```python
def _get_account_balance(self, account, date_from=None, date_to=None):
    """Get account balance for date range."""
    domain = [
        ('account_id', '=', account.id),
        ('parent_state', '=', 'posted'),
    ]

    if date_from:
        domain.append(('date', '>=', date_from))
    if date_to:
        domain.append(('date', '<=', date_to))

    lines = self.env['account.move.line'].search(domain)
    return sum(lines.mapped('balance'))
```

### Aged Receivables
```python
def _get_aged_receivables(self, partner=None):
    """Get aged receivables report data."""
    today = fields.Date.today()
    periods = [
        ('0-30', 0, 30),
        ('31-60', 31, 60),
        ('61-90', 61, 90),
        ('90+', 91, 9999),
    ]

    domain = [
        ('account_id.account_type', '=', 'asset_receivable'),
        ('parent_state', '=', 'posted'),
        ('reconciled', '=', False),
    ]

    if partner:
        domain.append(('partner_id', '=', partner.id))

    lines = self.env['account.move.line'].search(domain)

    result = {period[0]: 0.0 for period in periods}

    for line in lines:
        days = (today - line.date_maturity).days if line.date_maturity else 0
        for period_name, min_days, max_days in periods:
            if min_days <= days <= max_days:
                result[period_name] += line.amount_residual
                break

    return result
```

---

## Tax Handling

### Get Taxes
```python
def _get_sale_taxes(self, product=None):
    """Get applicable sale taxes."""
    if product:
        return product.taxes_id
    return self.env['account.tax'].search([
        ('type_tax_use', '=', 'sale'),
        ('company_id', '=', self.env.company.id),
    ])


def _get_purchase_taxes(self, product=None):
    """Get applicable purchase taxes."""
    if product:
        return product.supplier_taxes_id
    return self.env['account.tax'].search([
        ('type_tax_use', '=', 'purchase'),
        ('company_id', '=', self.env.company.id),
    ])
```

### Calculate Tax
```python
def _compute_tax_amount(self, amount, taxes, price_include=False):
    """Compute tax amount for given amount and taxes.

    Args:
        amount: Base amount
        taxes: account.tax recordset
        price_include: Whether amount includes tax

    Returns:
        dict with total, taxes breakdown
    """
    tax_results = taxes.compute_all(
        amount,
        currency=self.env.company.currency_id,
        quantity=1.0,
        product=None,
        partner=None,
        is_refund=False,
    )

    return {
        'total_included': tax_results['total_included'],
        'total_excluded': tax_results['total_excluded'],
        'taxes': tax_results['taxes'],
    }
```

---

## Reconciliation

### Auto Reconcile
```python
def _auto_reconcile_partner(self, partner):
    """Auto-reconcile partner's open items."""
    receivable_account = self._get_receivable_account()

    lines = self.env['account.move.line'].search([
        ('partner_id', '=', partner.id),
        ('account_id', '=', receivable_account.id),
        ('reconciled', '=', False),
        ('parent_state', '=', 'posted'),
    ])

    # Group by exact amount match
    by_amount = {}
    for line in lines:
        amount = abs(line.balance)
        if amount not in by_amount:
            by_amount[amount] = {'debit': [], 'credit': []}

        if line.balance > 0:
            by_amount[amount]['debit'].append(line)
        else:
            by_amount[amount]['credit'].append(line)

    # Reconcile matching amounts
    for amount, grouped in by_amount.items():
        if grouped['debit'] and grouped['credit']:
            to_reconcile = grouped['debit'][0] + grouped['credit'][0]
            to_reconcile.reconcile()
```

---

## Best Practices

1. **Always balance entries** - Debits must equal credits
2. **Use correct account types** - Receivable, payable, income, expense
3. **Post entries** - Draft entries don't affect financials
4. **Handle multi-currency** - Use currency conversion methods
5. **Respect fiscal year** - Check date restrictions
6. **Use proper journals** - Sales, purchase, bank, cash, general
7. **Reconcile regularly** - Match payments to invoices
8. **Multi-company aware** - Always filter by company
9. **Tax compliance** - Use correct tax accounts
10. **Audit trail** - Don't delete, use reversals

---

## Core Model Reference Catalog (Index Ground-Truth)

> Ground-truth structural catalog extracted from Odoo knowledge database. Use these exact field names and mixins without tool calls.

### Model: `account.move`
- **Inherited Mixins**: `['portal.mixin', 'mail.thread.main.attachment', 'mail.activity.mixin', 'sequence.mixin', 'product.catalog.mixin', 'account.document.import.mixin']`, `"account.move"`, `'account.move'`

| Field Name | Type | Definition / Key Arguments |
|---|---|---|
| `statement_line_ids` | `One2many` | `'account.bank.statement.line', 'move_id', string='Statements'` |
| `name` | `Char` | ` string='Number', compute='_compute_name', inverse='_inverse_name` |
| `name_placeholder` | `Char` | `compute='_compute_name_placeholder'` |
| `ref` | `Char` | ` string='Reference', copy=False, tracking=True, index='trigram', ` |
| `date` | `Date` | ` string='Date', index=True, compute='_compute_date', store=True, ` |
| `state` | `Selection` | ` selection=[ ('draft', 'Draft'` |
| `move_type` | `Selection` | ` selection=[ ('entry', 'Journal Entry'` |
| `is_storno` | `Boolean` | `compute='_compute_is_storno'` |
| `journal_id` | `Many2one` | ` 'account.journal', string='Journal', compute='_compute_journal_i` |
| `journal_group_id` | `Many2one` | ` 'account.journal.group', string='Ledger', store=False, search='_` |
| `company_id` | `Many2one` | ` comodel_name='res.company', string='Company', compute='_compute_` |
| `line_ids` | `One2many` | ` 'account.move.line', 'move_id', string='Journal Items', copy=Tru` |
| `journal_line_ids` | `One2many` | ` comodel_name='account.move.line', inverse_name='move_id', string` |
| `exchange_diff_partial_ids` | `One2many` | ` comodel_name='account.partial.reconcile', inverse_name='exchange` |
| `origin_payment_id` | `Many2one` | ` # the payment this is the journal entry of comodel_name='account` |
| `matched_payment_ids` | `Many2many` | ` # the payments linked to this invoice string="Matched Payments",` |
| `reconciled_payment_ids` | `Many2many` | `'account.payment', string="Reconciled Payments", compute='_comput` |
| `payment_count` | `Integer` | `compute='_compute_payment_count', compute_sudo=True` |
| `statement_line_id` | `Many2one` | ` comodel_name='account.bank.statement.line', string="Statement Li` |
| `statement_id` | `Many2one` | ` related="statement_line_id.statement_id" ` |
| `adjusting_entry_origin_move_ids` | `Many2many` | ` comodel_name='account.move', relation='adjusting_entries__accoun` |
| `adjusting_entry_origin_label` | `Char` | `compute="_compute_adjusting_entry_origin_label"` |
| `adjusting_entry_origin_moves_count` | `Integer` | ` string="Adjusting Entry Origin Moves Count", compute='_compute_a` |
| `adjusting_entries_move_ids` | `Many2many` | ` comodel_name='account.move', relation='adjusting_entries__accoun` |
| `adjusting_entries_count` | `Integer` | ` string="Adjusting Entries Count", compute='_compute_adjusting_en` |

### Model: `account.move.line`
- **Inherited Mixins**: `["analytic.mixin"]`, `'account.move.line'`, `"account.move.line"`

| Field Name | Type | Definition / Key Arguments |
|---|---|---|
| `move_id` | `Many2one` | ` comodel_name='account.move', string='Journal Entry', required=Tr` |
| `journal_id` | `Many2one` | ` related='move_id.journal_id', store=True, precompute=True, index` |
| `journal_group_id` | `Many2one` | ` string='Ledger', comodel_name='account.journal.group', store=Fal` |
| `company_id` | `Many2one` | ` related='move_id.company_id', store=True, readonly=True, precomp` |
| `company_currency_id` | `Many2one` | ` string='Company Currency', related='move_id.company_currency_id'` |
| `move_name` | `Char` | ` string='Number', related='move_id.name', store=True, index='btre` |
| `parent_state` | `Selection` | `related='move_id.state', store=True` |
| `date` | `Date` | `{ string: "Date" }` |
| `invoice_date` | `Date` | ` related='move_id.invoice_date', store=True, copy=False, aggregat` |
| `ref` | `Char` | ` related='move_id.ref', store=True, copy=False, index='trigram', ` |
| `is_storno` | `Boolean` | ` string="Company Storno Accounting", compute='_compute_is_storno'` |
| `sequence` | `Integer` | `compute='_compute_sequence', store=True, readonly=False, precompu` |
| `move_type` | `Selection` | `related='move_id.move_type'` |
| `account_id` | `Many2one` | `{ relation: "account.account" }` |
| `account_name` | `Char` | `related='account_id.name'` |
| `account_code` | `Char` | `related='account_id.code'` |
| `search_account_id` | `Many2one` | `'account.account', search='_search_account_id', store=False` |
| `name` | `Char` | `` |
| `translated_product_name` | `Text` | `compute='_compute_translated_product_name'` |
| `debit` | `Monetary` | ` string='Debit', compute='_compute_debit_credit', inverse='_inver` |
| `credit` | `Monetary` | ` string='Credit', compute='_compute_debit_credit', inverse='_inve` |
| `balance` | `Monetary` | ` string='Balance', compute='_compute_balance', store=True, readon` |
| `cumulated_balance` | `Monetary` | ` string='Cumulated Balance', compute='_compute_cumulated_balance'` |
| `currency_rate` | `Float` | ` compute='_compute_currency_rate', help="Currency rate from compa` |
| `amount_currency` | `Monetary` | ` string='Amount in Currency', compute='_compute_amount_currency',` |

### Model: `account.payment`
- **Inherited Mixins**: `['mail.thread.main.attachment', 'mail.activity.mixin']`, `'account.payment'`, `"account.payment"`

| Field Name | Type | Definition / Key Arguments |
|---|---|---|
| `name` | `Char` | `string="Number", compute='_compute_name', store=True` |
| `date` | `Date` | `default=fields.Date.context_today, required=True, tracking=True` |
| `is_sent` | `Boolean` | `string="Is Sent", readonly=True, copy=False` |
| `amount` | `Monetary` | `currency_field='currency_id'` |
| `memo` | `Char` | `string="Memo", tracking=True, inverse='_inverse_memo'` |
| `company_currency_id` | `Many2one` | `string="Company Currency", related='company_id.currency_id'` |
| `need_cancel_request` | `Boolean` | `related='move_id.need_cancel_request'` |
| `country_code` | `Char` | `related='company_id.account_fiscal_country_id.code'` |
| `duplicate_payment_ids` | `Many2many` | `comodel_name='account.payment', compute='_compute_duplicate_payme` |
| `attachment_ids` | `One2many` | `'ir.attachment', 'res_id', string='Attachments'` |
| `check_manual_sequencing` | `Boolean` | `related='journal_id.check_manual_sequencing'` |
| `payment_method_line_id` | `Many2one` | `index=True` |
| `show_check_number` | `Boolean` | `compute='_compute_show_check_number'` |
| `amount_available_for_refund` | `Monetary` | `compute='_compute_amount_available_for_refund'` |
| `refunds_count` | `Integer` | `string="Refunds Count", compute='_compute_refunds_count'` |
| `expense_ids` | `One2many` | `related='move_id.expense_ids'` |
| `display_withholding` | `Boolean` | `compute='_compute_display_withholding'` |
| `withholding_payment_account_id` | `Many2one` | `related="payment_method_line_id.payment_account_id"` |
| `outstanding_account_id` | `Many2one` | `readonly=False` |
| `withholding_hide_tax_base_account` | `Boolean` | `compute='_compute_withholding_hide_tax_base_account'` |
| `payment_ids` | `One2many` | `'account.payment', 'move_id', string='Payments'` |

### Model: `account.journal`
- **Inherited Mixins**: `"account.journal"`, `['portal.mixin',
                'mail.alias.mixin.optional',
                'mail.thread',
                'mail.activity.mixin',
               ]`, `'account.journal'`

| Field Name | Type | Definition / Key Arguments |
|---|---|---|
| `kanban_dashboard` | `Text` | `compute='_kanban_dashboard'` |
| `kanban_dashboard_graph` | `Text` | `compute='_kanban_dashboard_graph'` |
| `json_activity_data` | `Text` | `compute='_get_json_activity_data'` |
| `show_on_dashboard` | `Boolean` | `string='Show journal on dashboard', help="Whether this journal sh` |
| `color` | `Integer` | `"Color Index", default=0` |
| `current_statement_balance` | `Monetary` | `compute='_compute_current_statement_balance'` |
| `has_statement_lines` | `Boolean` | `compute='_compute_current_statement_balance'` |
| `entries_count` | `Integer` | `compute='_compute_entries_count'` |
| `has_posted_entries` | `Boolean` | `compute='_compute_has_entries'` |
| `has_entries` | `Boolean` | `compute='_compute_has_entries'` |
| `has_sequence_holes` | `Boolean` | `compute='_compute_has_sequence_holes'` |
| `has_unhashed_entries` | `Boolean` | `string='Unhashed Entries', compute='_compute_has_unhashed_entries` |
| `last_statement_id` | `Many2one` | `comodel_name='account.bank.statement', compute='_compute_last_ban` |
| `name` | `Char` | `string='Journal Name', required=True, translate=True` |
| `name_placeholder` | `Char` | `compute='_compute_name_placeholder'` |
| `code` | `Char` | ` string='Sequence Prefix', size=5, compute='_compute_code', reado` |
| `active` | `Boolean` | `default=True, help="Set active to false to hide the Journal witho` |
| `type` | `Selection` | `[ ('sale', 'Sales'` |
| `is_self_billing` | `Boolean` | ` string='Self Billing', help="This journal is for self-billing in` |
| `default_account_type` | `Char` | `string='Default Account Type', compute="_compute_default_account_` |
| `default_account_id` | `Many2one` | ` comodel_name='account.account', check_company=True, copy=False, ` |
| `suspense_account_id` | `Many2one` | ` comodel_name='account.account', check_company=True, ondelete='re` |
| `non_deductible_account_id` | `Many2one` | ` comodel_name='account.account', check_company=True, string='Priv` |
| `restrict_mode_hash_table` | `Boolean` | `string="Secure Posted Entries with Hash", help="If ticked, when a` |
| `sequence` | `Integer` | `help='Used to order Journals in the dashboard view', default=10` |

### Model: `account.tax`
- **Inherited Mixins**: `"account.tax"`, `['mail.thread']`, `'account.tax'`

| Field Name | Type | Definition / Key Arguments |
|---|---|---|
| `name` | `Char` | `string='Tax Name', required=True, translate=True, tracking=True` |
| `tax_scope` | `Selection` | `[('service', 'Services'` |
| `display_alternative_taxes_field` | `Boolean` | `compute='_compute_display_alternative_taxes_field'` |
| `is_domestic` | `Boolean` | `compute='_compute_is_domestic', store=True, precompute=True` |
| `active` | `Boolean` | `default=True, help="Set active to false to hide the tax without r` |
| `company_id` | `Many2one` | `'res.company', string='Company', required=True, readonly=True, de` |
| `amount` | `Float` | `required=True, digits=(16, 4` |
| `description` | `Html` | `string='Description', translate=html_translate` |
| `invoice_label` | `Char` | `string='Label on Invoices', translate=True` |
| `tax_label` | `Char` | `compute='_compute_tax_label'` |
| `company_price_include` | `Selection` | `related="company_id.account_price_include"` |
| `analytic` | `Boolean` | `string="Include in Analytic Cost", help="If set, the amount compu` |
| `hide_tax_exigibility` | `Boolean` | `string='Hide Use Cash Basis Option', related='company_id.tax_exig` |
| `country_code` | `Char` | `related='country_id.code', readonly=True` |
| `is_used` | `Boolean` | `string="Tax used", compute='_compute_is_used'` |
| `repartition_lines_str` | `Char` | `string="Repartition Lines", tracking=True, compute='_compute_repa` |
| `invoice_legal_notes` | `Html` | `string="Legal Notes", translate=True, help="Legal mentions that h` |
| `has_negative_factor` | `Boolean` | `compute='_compute_has_negative_factor'` |
| `ubl_cii_tax_category_code` | `Selection` | ` help="The VAT category code used for electronic invoicing purpos` |
| `ubl_cii_tax_exemption_reason_code` | `Selection` | ` help="The reason why the amount is exempted from VAT or why no V` |
| `ubl_cii_requires_exemption_reason` | `Boolean` | `compute='_compute_ubl_cii_requires_exemption_reason'` |
| `formula_decoded_info` | `Json` | `compute='_compute_formula_decoded_info'` |
