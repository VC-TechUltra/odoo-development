#!/usr/bin/env python3
"""Minimal MCP stdio server for session memory operations."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

SCRIPT = Path(__file__).with_name("session_memory_store.py")

TOOLS = [
    {
        "name": "health_check",
        "description": "Health check for session memory store",
        "inputSchema": {"type": "object", "properties": {}, "additionalProperties": False},
    },
    {
        "name": "session_init",
        "description": "Initialize/resume session namespace",
        "inputSchema": {
            "type": "object",
            "properties": {
                "workspace": {"type": "string"},
                "branch": {"type": "string"},
                "session_id": {"type": "string"},
                "ttl_hours": {"type": "integer", "minimum": 1},
            },
            "additionalProperties": False,
        },
    },
    {
        "name": "memory_put",
        "description": "Store a memory item for current namespace",
        "inputSchema": {
            "type": "object",
            "properties": {
                "workspace": {"type": "string"},
                "branch": {"type": "string"},
                "session_id": {"type": "string"},
                "key": {"type": "string"},
                "value": {"type": "string"},
                "kind": {"type": "string"},
            },
            "required": ["key", "value"],
            "additionalProperties": False,
        },
    },
    {
        "name": "memory_list",
        "description": "List memory entries for current namespace",
        "inputSchema": {
            "type": "object",
            "properties": {
                "workspace": {"type": "string"},
                "branch": {"type": "string"},
                "session_id": {"type": "string"},
                "limit": {"type": "integer", "minimum": 1, "maximum": 200},
            },
            "additionalProperties": False,
        },
    },
    {
        "name": "memory_summary",
        "description": "Summarize memory entries for current namespace",
        "inputSchema": {
            "type": "object",
            "properties": {
                "workspace": {"type": "string"},
                "branch": {"type": "string"},
                "session_id": {"type": "string"},
                "limit": {"type": "integer", "minimum": 1, "maximum": 200},
            },
            "additionalProperties": False,
        },
    },
    {
        "name": "namespace_info",
        "description": "Get metadata for current namespace",
        "inputSchema": {
            "type": "object",
            "properties": {
                "workspace": {"type": "string"},
                "branch": {"type": "string"},
                "session_id": {"type": "string"}
            },
            "additionalProperties": False,
        },
    },
    {
        "name": "memory_clear",
        "description": "Clear current namespace memory",
        "inputSchema": {
            "type": "object",
            "properties": {
                "workspace": {"type": "string"},
                "branch": {"type": "string"},
                "session_id": {"type": "string"},
            },
            "additionalProperties": False,
        },
    },
]


def read_message() -> dict | None:
    content_length = None
    while True:
        line = sys.stdin.buffer.readline()
        if not line:
            return None
        line = line.decode("utf-8").strip()
        if not line:
            break
        if line.lower().startswith("content-length:"):
            content_length = int(line.split(":", 1)[1].strip())
    if content_length is None:
        return None
    body = sys.stdin.buffer.read(content_length)
    return json.loads(body.decode("utf-8"))


def write_message(payload: dict) -> None:
    encoded = json.dumps(payload).encode("utf-8")
    sys.stdout.buffer.write(f"Content-Length: {len(encoded)}\r\n\r\n".encode("utf-8"))
    sys.stdout.buffer.write(encoded)
    sys.stdout.buffer.flush()


def run_store(command: str, params: dict) -> dict:
    args = [sys.executable, str(SCRIPT), command]
    for key in ("workspace", "branch", "session_id", "key", "value", "kind", "limit", "ttl_hours"):
      if key in params and params[key] is not None:
          cli_key = "--" + key.replace("_", "-")
          args.extend([cli_key, str(params[key])])
    out = subprocess.check_output(args, stderr=subprocess.STDOUT)
    return json.loads(out.decode("utf-8"))


def success_response(request_id, result: dict) -> dict:
    return {"jsonrpc": "2.0", "id": request_id, "result": result}


def error_response(request_id, message: str) -> dict:
    return {"jsonrpc": "2.0", "id": request_id, "error": {"code": -32000, "message": message}}


def handle_request(req: dict) -> dict | None:
    method = req.get("method")
    req_id = req.get("id")
    params = req.get("params", {}) or {}

    if method == "initialize":
        return success_response(
            req_id,
            {
                "protocolVersion": "2024-11-05",
                "serverInfo": {"name": "session-memory-local", "version": "0.1.0"},
                "capabilities": {"tools": {}},
            },
        )

    if method == "notifications/initialized":
        return None

    if method == "tools/list":
        return success_response(req_id, {"tools": TOOLS})

    if method == "tools/call":
        name = params.get("name")
        arguments = params.get("arguments", {}) or {}
        try:
            if name == "health_check":
                result = run_store("health", arguments)
            elif name == "session_init":
                result = run_store("init", arguments)
            elif name == "memory_put":
                result = run_store("put", arguments)
            elif name == "memory_list":
                result = run_store("list", arguments)
            elif name == "memory_summary":
                result = run_store("summary", arguments)
            elif name == "namespace_info":
                result = run_store("namespace-info", arguments)
            elif name == "memory_clear":
                result = run_store("clear", arguments)
            else:
                return error_response(req_id, f"Unknown tool: {name}")

            return success_response(req_id, {"content": [{"type": "text", "text": json.dumps(result)}]})
        except subprocess.CalledProcessError as exc:
            message = exc.output.decode("utf-8", errors="replace") if exc.output else str(exc)
            return error_response(req_id, message)
        except Exception as exc:
            return error_response(req_id, str(exc))

    return error_response(req_id, f"Unsupported method: {method}")


def main() -> int:
    while True:
        request = read_message()
        if request is None:
            return 0
        response = handle_request(request)
        if response is not None and "id" in response:
            write_message(response)


if __name__ == "__main__":
    raise SystemExit(main())
