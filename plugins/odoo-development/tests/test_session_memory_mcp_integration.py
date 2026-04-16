import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SERVER = ROOT / "scripts" / "session_memory_mcp.py"


def write_message(proc: subprocess.Popen, payload: dict) -> None:
    data = json.dumps(payload).encode("utf-8")
    proc.stdin.write(f"Content-Length: {len(data)}\r\n\r\n".encode("utf-8"))
    proc.stdin.write(data)
    proc.stdin.flush()


def read_message(proc: subprocess.Popen) -> dict:
    content_length = None
    while True:
        line = proc.stdout.readline()
        if not line:
            raise RuntimeError("No response from MCP server")
        line = line.decode("utf-8").strip()
        if not line:
            break
        if line.lower().startswith("content-length:"):
            content_length = int(line.split(":", 1)[1].strip())
    if content_length is None:
        raise RuntimeError("Missing Content-Length header")
    body = proc.stdout.read(content_length)
    return json.loads(body.decode("utf-8"))


class SessionMemoryMcpIntegrationTests(unittest.TestCase):
    def test_invalid_header_returns_parse_error_and_server_recovers(self):
        proc = subprocess.Popen(
            [sys.executable, str(SERVER)],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        try:
            proc.stdin.write(b"Content-Length: abc\r\n\r\n")
            proc.stdin.flush()

            resp_error = read_message(proc)
            self.assertIn("error", resp_error)
            self.assertEqual(resp_error["error"]["code"], -32700)

            write_message(proc, {"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {}})
            resp_init = read_message(proc)
            self.assertEqual(resp_init["id"], 1)
            self.assertIn("result", resp_init)
        finally:
            proc.terminate()
            try:
                proc.communicate(timeout=5)
            except subprocess.TimeoutExpired:
                proc.kill()
                proc.communicate(timeout=5)

    def test_initialize_list_and_health_tool(self):
        proc = subprocess.Popen(
            [sys.executable, str(SERVER)],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        try:
            write_message(proc, {"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {}})
            resp_init = read_message(proc)
            self.assertEqual(resp_init["id"], 1)
            self.assertEqual(resp_init["result"]["serverInfo"]["name"], "session-memory-local")

            write_message(proc, {"jsonrpc": "2.0", "id": 2, "method": "tools/list", "params": {}})
            resp_list = read_message(proc)
            tools = {t["name"] for t in resp_list["result"]["tools"]}
            self.assertIn("health_check", tools)

            write_message(
                proc,
                {
                    "jsonrpc": "2.0",
                    "id": 3,
                    "method": "tools/call",
                    "params": {"name": "health_check", "arguments": {}},
                },
            )
            resp_call = read_message(proc)
            content = resp_call["result"]["content"]
            payload = json.loads(content[0]["text"])
            self.assertEqual(payload["status"], "ok")
        finally:
            proc.terminate()
            try:
                proc.communicate(timeout=5)
            except subprocess.TimeoutExpired:
                proc.kill()
                proc.communicate(timeout=5)


if __name__ == "__main__":
    unittest.main()
