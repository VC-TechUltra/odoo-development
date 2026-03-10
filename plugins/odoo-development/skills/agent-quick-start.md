# Odoo Development Quick Start

## 1. Detect Version FIRST
Always ask: "What Odoo version?" or check __manifest__.py

## 2. Use Commands
- `/odoo-module` - Create new module
- `/odoo-owl` - Create frontend component  
- `/odoo-security` - Add access rights
- `/odoo-test` - Write tests
- `/odoo-review` - Review code

## 3. Version Patterns
| Version | Key Pattern |
|---------|-------------|
| 14 | @api.multi (deprecated), track_visibility |
| 15 | tracking=True, @api.multi removed |
| 16 | Command class, @api.model_create_multi |
| 17 | attrs removed, inline expressions |
| 18 | _check_company_auto, type hints rec |
| 19 | Type hints mandatory |

## 4. MCP Workflow
1. health_check - Verify MCP connection
2. search_odoo_codebase - Find similar code
3. get_odoo_model_schema - Get model fields

## 5. Common Tasks
- New model: Use odoo-module generator
- Add field: Update model + view XML
- Security: ACL CSV + record rules XML
- Test: tests/test_model.py with TransactionCase
