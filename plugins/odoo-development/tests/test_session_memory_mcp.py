import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MCP_PATH = ROOT / "scripts" / "session_memory_mcp.py"

spec = importlib.util.spec_from_file_location("session_memory_mcp", MCP_PATH)
module = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(module)


class SessionMemoryMcpTests(unittest.TestCase):
    def test_tools_list_contains_expected_tools(self):
        response = module.handle_request({"jsonrpc": "2.0", "id": 1, "method": "tools/list"})
        self.assertIn("result", response)
        tools = {t["name"] for t in response["result"]["tools"]}
        self.assertIn("session_init", tools)
        self.assertIn("memory_put", tools)
        self.assertIn("namespace_info", tools)

    def test_unknown_tool_returns_error(self):
        response = module.handle_request(
            {
                "jsonrpc": "2.0",
                "id": 2,
                "method": "tools/call",
                "params": {"name": "missing_tool", "arguments": {}},
            }
        )
        self.assertIn("error", response)
        self.assertIn("Unknown tool", response["error"]["message"])

    def test_initialize_response_shape(self):
        response = module.handle_request({"jsonrpc": "2.0", "id": 3, "method": "initialize", "params": {}})
        self.assertEqual(response["result"]["serverInfo"]["name"], "session-memory-local")
        self.assertEqual(response["result"]["protocolVersion"], "2024-11-05")


if __name__ == "__main__":
    unittest.main()
