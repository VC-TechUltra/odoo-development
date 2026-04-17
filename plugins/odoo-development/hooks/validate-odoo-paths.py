#!/usr/bin/env python3
import json

print(
    json.dumps(
        {
            "permission": "allow",
            "hookSpecificOutput": {
                "hookEventName": "beforeShellExecution",
                "note": "Prefer repository-local paths and Odoo MCP verification before destructive commands.",
            },
        }
    )
)
