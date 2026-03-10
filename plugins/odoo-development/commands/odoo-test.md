---
name: odoo-test
description: Create and run Odoo tests. Use when user asks to "write tests", "create unit tests", "run tests".
---

# Odoo Test Command

Create and manage tests for Odoo modules.

## Execution Flow

### Step 1: Determine Test Type

- Unit tests: Testing individual methods
- Integration tests: Testing model interactions
- HTTP tests: Testing controllers

### Step 2: Load Testing Patterns

```
Read: odoo-development/skills/odoo-test-patterns.md
```

### Step 3: Generate Test Files

## Test File Structure

```python
from odoo.tests.common import TransactionCase

class TestMyModel(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # Setup test data

    def test_create_record(self):
        record = self.env['my.model'].create({'name': 'Test'})
        self.assertEqual(record.name, 'Test')

    def test_compute_field(self):
        record = self.env['my.model'].create({
            'line_ids': [(0, 0, {'amount': 100})]
        })
        self.assertEqual(record.total, 100)
```

## Test Types

### TransactionCase
For standard model testing.

### HttpCase
For HTTP controller testing.

```python
from odoo.tests import HttpCase

class TestController(HttpCase):
    def test_my_endpoint(self):
        response = self.url_open('/my/module/endpoint')
        self.assertEqual(response.status_code, 200)
```

## Running Tests

### Command Line
```bash
# Run specific test
odoo-bin test -d my_db -m my_module --test-tags=test_model

# Run all tests in module
odoo-bin test -d my_db -m my_module

# With coverage
coverage run --source=my_module odoo-bin test -d my_db -m my_module
```

### Python
```bash
# Using odoo instance
./odoo-bin test -d db_name -i my_module
```

## Version-Specific

### Odoo 14-16
- Standard test patterns
- CommonTransactionCase available

### Odoo 17+
- Enhanced assert methods
- Record CRUD helpers

## Instructions
1. Determine test type needed
2. Load testing patterns
3. Generate test file in tests/
4. Include setup and teardown
5. Add assertions for expected behavior
6. Document how to run tests
