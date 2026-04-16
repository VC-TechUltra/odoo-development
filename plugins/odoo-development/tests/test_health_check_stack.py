import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "health_check_stack.py"


class HealthCheckStackTests(unittest.TestCase):
    def test_offline_runs_and_returns_json(self):
        proc = subprocess.run(
            [sys.executable, str(SCRIPT), "--offline"],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertIn(proc.returncode, (0, 2))
        payload = json.loads(proc.stdout)
        self.assertIn("status", payload)
        self.assertIn("checks", payload)
        names = {c["name"] for c in payload["checks"]}
        self.assertIn("python", names)
        self.assertIn("bootstrap-prereqs", names)
        self.assertIn("session-memory-local", names)
        mem_check = next(c for c in payload["checks"] if c["name"] == "session-memory-local")
        self.assertIn("schema=", mem_check["detail"])
        self.assertIn("code", mem_check)
        self.assertIn("recommended_action", mem_check)



    def test_strict_local_ignores_optional_tool_absence(self):
        proc = subprocess.run(
            [sys.executable, str(SCRIPT), "--offline", "--strict-local"],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(proc.returncode, 0)
        payload = json.loads(proc.stdout)
        self.assertEqual(payload["status"], "ok")
        self.assertEqual(payload["mode"], "strict-local")

if __name__ == "__main__":
    unittest.main()
