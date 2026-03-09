# Odoo 14 Version Knowledge

Release: October 2020

## Key Features
- @api.multi is DEPRECATED but works
- track_visibility for field tracking
- Last version with @api.multi support

## Python API
```python
# @api.multi works (deprecated)
@api.multi
def my_method(self):
    for record in self:
        pass
```

## Field Tracking
```python
stage_id = fields.Many2one('stage.model', track_visibility='onchange')
```

## XML Views
- attrs fully supported
- states fully supported

## Frontend
- Legacy JavaScript
- No OWL support

## Manifest Version
```
'version': '14.0.1.0.0'
```

## Next Version (15)
- @api.multi will be REMOVED
- track_visibility replaced by tracking=True
