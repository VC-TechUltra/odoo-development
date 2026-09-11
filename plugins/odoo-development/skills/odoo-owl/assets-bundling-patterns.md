# Assets Bundling Patterns

```
╔══════════════════════════════════════════════════════════════════════════════╗
║  ASSETS BUNDLING PATTERNS                                                    ║
║  JavaScript, CSS, and SCSS asset management                                  ║
║  Use for frontend customization and OWL component registration               ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

## Asset Bundles Overview

### Main Bundles
| Bundle | Used In | Purpose |
|
---

## Standard Asset Bundle Registry (Manifest Assets Key)

```python
# __manifest__.py asset declarations across Odoo 16, 17, 18, 19:
'assets': {
    'web.assets_backend': [
        'my_module/static/src/components/**/*.js',
        'my_module/static/src/components/**/*.xml',
        'my_module/static/src/scss/**/*.scss',
    ],
    'web.assets_frontend': [
        'my_module/static/src/portal/**/*.js',
        'my_module/static/src/portal/**/*.xml',
    ],
    'web._assets_primary_variables': [
        'my_module/static/src/scss/primary_variables.scss',
    ],
    'web.assets_unit_tests': [
        'my_module/static/tests/**/*.js',
    ],
}
```
