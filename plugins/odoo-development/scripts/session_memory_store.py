#!/usr/bin/env python3
"""Local session memory store for workspace/branch/session-scoped state."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sqlite3
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

DEFAULT_TTL_HOURS = 48
MAX_VALUE_LEN = 2000
SENSITIVE_MARKERS = ("password", "token", "secret", "api_key", "private_key", "authorization")
PLUGIN_HOME = Path(os.environ.get("CURSOR_ODOO_CONFIG_DIR", Path.home() / ".cursor-odoo-development"))
DB_PATH = PLUGIN_HOME / "session-memory.db"


@dataclass
class Namespace:
    workspace: str
    branch: str
    session_id: str

    @property
    def key(self) -> str:
        payload = f"{self.workspace}|{self.branch}|{self.session_id}".encode("utf-8")
        return hashlib.sha256(payload).hexdigest()


def now_ts() -> int:
    return int(time.time())


def ensure_db(conn: sqlite3.Connection) -> None:
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS namespaces (
            namespace_key TEXT PRIMARY KEY,
            workspace TEXT NOT NULL,
            branch TEXT NOT NULL,
            session_id TEXT NOT NULL,
            ttl_seconds INTEGER NOT NULL,
            created_at INTEGER NOT NULL,
            updated_at INTEGER NOT NULL,
            expires_at INTEGER NOT NULL
        )
        """
    )
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS memory_entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            namespace_key TEXT NOT NULL,
            kind TEXT NOT NULL,
            key TEXT NOT NULL,
            value TEXT NOT NULL,
            created_at INTEGER NOT NULL,
            FOREIGN KEY(namespace_key) REFERENCES namespaces(namespace_key)
        )
        """
    )
    conn.execute("CREATE INDEX IF NOT EXISTS idx_memory_namespace_created ON memory_entries(namespace_key, created_at DESC)")
    conn.commit()


def connect() -> sqlite3.Connection:
    PLUGIN_HOME.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    ensure_db(conn)
    gc_expired(conn)
    return conn


def detect_workspace_branch() -> tuple[str, str]:
    workspace = os.environ.get("CURSOR_WORKSPACE_PATH") or os.getcwd()
    branch = os.environ.get("CURSOR_GIT_BRANCH")
    if not branch:
        import subprocess

        try:
            branch = (
                subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"], cwd=workspace, stderr=subprocess.DEVNULL)
                .decode("utf-8")
                .strip()
            )
        except Exception:
            branch = "unknown"
    return workspace, branch


def detect_session_id() -> str:
    return os.environ.get("CURSOR_SESSION_ID") or f"manual-{now_ts()}"


def upsert_namespace(conn: sqlite3.Connection, ns: Namespace, ttl_hours: int = DEFAULT_TTL_HOURS) -> dict:
    ts = now_ts()
    ttl_seconds = ttl_hours * 3600
    expires = ts + ttl_seconds
    conn.execute(
        """
        INSERT INTO namespaces(namespace_key, workspace, branch, session_id, ttl_seconds, created_at, updated_at, expires_at)
        VALUES(?, ?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(namespace_key) DO UPDATE SET
          updated_at=excluded.updated_at,
          expires_at=excluded.expires_at,
          ttl_seconds=excluded.ttl_seconds
        """,
        (ns.key, ns.workspace, ns.branch, ns.session_id, ttl_seconds, ts, ts, expires),
    )
    conn.commit()
    return {"namespace_key": ns.key, "workspace": ns.workspace, "branch": ns.branch, "session_id": ns.session_id, "expires_at": expires}




def validate_entry(key: str, value: str) -> None:
    lowered = f"{key} {value}".lower()
    if any(marker in lowered for marker in SENSITIVE_MARKERS):
        raise ValueError("Refusing to store potentially sensitive content in session memory")
    if len(value) > MAX_VALUE_LEN:
        raise ValueError(f"Memory value exceeds max length ({MAX_VALUE_LEN})")

def gc_expired(conn: sqlite3.Connection) -> int:
    ts = now_ts()
    keys = [r[0] for r in conn.execute("SELECT namespace_key FROM namespaces WHERE expires_at <= ?", (ts,)).fetchall()]
    if not keys:
        return 0
    conn.executemany("DELETE FROM memory_entries WHERE namespace_key=?", [(k,) for k in keys])
    conn.executemany("DELETE FROM namespaces WHERE namespace_key=?", [(k,) for k in keys])
    conn.commit()
    return len(keys)


def put_entry(conn: sqlite3.Connection, ns: Namespace, key: str, value: str, kind: str = "note") -> dict:
    validate_entry(key, value)
    ts = now_ts()
    conn.execute(
        "INSERT INTO memory_entries(namespace_key, kind, key, value, created_at) VALUES (?, ?, ?, ?, ?)",
        (ns.key, kind, key, value, ts),
    )
    conn.execute("UPDATE namespaces SET updated_at=? WHERE namespace_key=?", (ts, ns.key))
    conn.commit()
    return {"status": "ok", "kind": kind, "key": key}


def list_entries(conn: sqlite3.Connection, ns: Namespace, limit: int = 20) -> list[dict]:
    rows = conn.execute(
        "SELECT kind, key, value, created_at FROM memory_entries WHERE namespace_key=? ORDER BY created_at DESC LIMIT ?",
        (ns.key, limit),
    ).fetchall()
    return [{"kind": r[0], "key": r[1], "value": r[2], "created_at": r[3]} for r in rows]


def summary(entries: Iterable[dict]) -> str:
    lines = []
    for item in entries:
        lines.append(f"- [{item['kind']}] {item['key']}: {item['value']}")
    return "\n".join(lines)


def resolve_namespace(args: argparse.Namespace) -> Namespace:
    workspace, branch = detect_workspace_branch()
    return Namespace(
        workspace=args.workspace or workspace,
        branch=args.branch or branch,
        session_id=args.session_id or detect_session_id(),
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Session memory local store")
    sub = parser.add_subparsers(dest="command", required=True)

    def add_common(p: argparse.ArgumentParser) -> None:
        p.add_argument("--workspace", default=None)
        p.add_argument("--branch", default=None)
        p.add_argument("--session-id", default=None)

    p_init = sub.add_parser("init")
    add_common(p_init)
    p_init.add_argument("--ttl-hours", type=int, default=DEFAULT_TTL_HOURS)

    p_put = sub.add_parser("put")
    add_common(p_put)
    p_put.add_argument("--key", required=True)
    p_put.add_argument("--value", required=True)
    p_put.add_argument("--kind", default="note")

    p_list = sub.add_parser("list")
    add_common(p_list)
    p_list.add_argument("--limit", type=int, default=20)

    p_summary = sub.add_parser("summary")
    add_common(p_summary)
    p_summary.add_argument("--limit", type=int, default=20)

    p_clear = sub.add_parser("clear")
    add_common(p_clear)

    p_ns = sub.add_parser("namespace-info")
    add_common(p_ns)

    sub.add_parser("gc")
    sub.add_parser("health")

    args = parser.parse_args()
    conn = connect()

    if args.command == "gc":
        deleted = gc_expired(conn)
        print(json.dumps({"status": "ok", "deleted_namespaces": deleted}))
        return 0

    if args.command == "health":
        print(json.dumps({"status": "ok", "db": str(DB_PATH)}))
        return 0

    ns = resolve_namespace(args)

    if args.command == "init":
        payload = upsert_namespace(conn, ns, args.ttl_hours)
        print(json.dumps({"status": "ok", **payload}))
        return 0


    if args.command == "namespace-info":
        row = conn.execute(
            "SELECT workspace, branch, session_id, expires_at FROM namespaces WHERE namespace_key=?",
            (ns.key,),
        ).fetchone()
        if row:
            print(json.dumps({
                "status": "ok",
                "namespace_key": ns.key,
                "workspace": row[0],
                "branch": row[1],
                "session_id": row[2],
                "expires_at": row[3],
            }))
        else:
            print(json.dumps({"status": "missing", "namespace_key": ns.key}))
        return 0

    upsert_namespace(conn, ns, DEFAULT_TTL_HOURS)

    if args.command == "put":
        try:
            payload = put_entry(conn, ns, args.key, args.value, args.kind)
        except ValueError as exc:
            print(json.dumps({"status": "error", "error": str(exc)}))
            return 2
        print(json.dumps(payload))
        return 0

    if args.command == "list":
        items = list_entries(conn, ns, args.limit)
        print(json.dumps({"status": "ok", "items": items}))
        return 0

    if args.command == "summary":
        items = list_entries(conn, ns, args.limit)
        print(json.dumps({"status": "ok", "summary": summary(items), "count": len(items)}))
        return 0

    if args.command == "clear":
        conn.execute("DELETE FROM memory_entries WHERE namespace_key=?", (ns.key,))
        conn.execute("DELETE FROM namespaces WHERE namespace_key=?", (ns.key,))
        conn.commit()
        print(json.dumps({"status": "ok", "cleared_namespace": ns.key}))
        return 0

    return 1


if __name__ == "__main__":
    sys.exit(main())
