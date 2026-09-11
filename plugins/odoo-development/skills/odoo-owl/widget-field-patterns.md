# Widget and Field Rendering Patterns

```
╔══════════════════════════════════════════════════════════════════════════════╗
║  WIDGET & FIELD RENDERING PATTERNS                                           ║
║  Field widgets, custom rendering, and UI components                          ║
║  Use for customizing field display in forms, trees, and kanban views         ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

## Common Widgets Reference

### Text and Selection Widgets
| Widget | Field Types | Description |
|
---

## Standard OWL 2 / OWL 3 Field Widgets Catalog (Odoo 16–19)

| Widget Name | Supported Field Types | Common Options / Usage |
|---|---|---|
| `monetary` | `Monetary`, `Float` | Currency symbol formatting (`options="{'currency_field': 'currency_id'}"`) |
| `badge` | `Selection`, `Char` | Displays text as color badge (`decoration-success="state == 'posted'"`) |
| `statusbar` | `Selection` | Standard header status bar (`statusbar_visible="draft,sent,sale"`) |
| `many2one_avatar` | `Many2one` (res.users/partner) | Shows avatar image circle next to user/partner name |
| `many2one_avatar_user` | `Many2one -> res.users` | User avatar with presence dot (online/offline/away) |
| `boolean_toggle` | `Boolean` | Renders a modern toggle switch instead of a checkbox |
| `handle` | `Integer` | Drag-and-drop reordering handle in tree/list views (`<field name="sequence" widget="handle"/>`) |
| `image` | `Binary` | Renders image thumbnail (`options="{'size': [90, 90]}"`) |
| `progressbar` | `Integer`, `Float` | Progress bar filled up to 100% |
| `priority` | `Selection` | Star rating widget (0, 1, 2, 3 stars) |
| `radio` | `Selection` | Radio buttons group layout |
