import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STORE = ROOT / "scripts" / "session_memory_store.py"


class SessionMemoryStoreTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.env = os.environ.copy()
        self.env["CURSOR_ODOO_CONFIG_DIR"] = self.tmp.name
        self.workspace = str(Path(self.tmp.name) / "workspace")
        Path(self.workspace).mkdir(parents=True, exist_ok=True)

    def run_store(self, *args: str) -> dict:
        out = subprocess.check_output(
            [sys.executable, str(STORE), *args],
            env=self.env,
        ).decode("utf-8")
        return json.loads(out)

    def test_init_put_list_summary_clear(self) -> None:
        init = self.run_store(
            "init",
            "--workspace",
            self.workspace,
            "--branch",
            "main",
            "--session-id",
            "s1",
            "--ttl-hours",
            "48",
        )
        self.assertEqual(init["status"], "ok")

        put = self.run_store(
            "put",
            "--workspace",
            self.workspace,
            "--branch",
            "main",
            "--session-id",
            "s1",
            "--key",
            "decision",
            "--value",
            "approved",
        )
        self.assertEqual(put["status"], "ok")

        listing = self.run_store(
            "list",
            "--workspace",
            self.workspace,
            "--branch",
            "main",
            "--session-id",
            "s1",
            "--limit",
            "10",
        )
        self.assertEqual(listing["status"], "ok")
        self.assertGreaterEqual(len(listing["items"]), 1)

        summary = self.run_store(
            "summary",
            "--workspace",
            self.workspace,
            "--branch",
            "main",
            "--session-id",
            "s1",
            "--limit",
            "10",
        )
        self.assertEqual(summary["status"], "ok")
        self.assertIn("decision", summary["summary"])

        ns = self.run_store(
            "namespace-info",
            "--workspace",
            self.workspace,
            "--branch",
            "main",
            "--session-id",
            "s1",
        )
        self.assertEqual(ns["status"], "ok")
        self.assertEqual(ns["branch"], "main")

        cleared = self.run_store(
            "clear",
            "--workspace",
            self.workspace,
            "--branch",
            "main",
            "--session-id",
            "s1",
        )
        self.assertEqual(cleared["status"], "ok")

        after = self.run_store(
            "namespace-info",
            "--workspace",
            self.workspace,
            "--branch",
            "main",
            "--session-id",
            "s1",
        )
        self.assertEqual(after["status"], "missing")


    def test_sensitive_content_rejected(self) -> None:
        proc = subprocess.run(
            [
                sys.executable,
                str(STORE),
                "put",
                "--workspace",
                self.workspace,
                "--branch",
                "main",
                "--session-id",
                "s1",
                "--key",
                "api_token",
                "--value",
                "secret123",
            ],
            env=self.env,
            capture_output=True,
            text=True,
        )
        self.assertEqual(proc.returncode, 2)
        payload = json.loads(proc.stdout)
        self.assertEqual(payload["status"], "error")

    def test_branch_isolation(self) -> None:
        self.run_store("put", "--workspace", self.workspace, "--branch", "main", "--session-id", "s1", "--key", "k", "--value", "v1")
        self.run_store("put", "--workspace", self.workspace, "--branch", "feature", "--session-id", "s1", "--key", "k", "--value", "v2")

        main_summary = self.run_store("summary", "--workspace", self.workspace, "--branch", "main", "--session-id", "s1")
        feature_summary = self.run_store("summary", "--workspace", self.workspace, "--branch", "feature", "--session-id", "s1")

        self.assertIn("v1", main_summary["summary"])
        self.assertNotIn("v2", main_summary["summary"])
        self.assertIn("v2", feature_summary["summary"])


if __name__ == "__main__":
    unittest.main()
