import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "session_memory_maintenance.py"


class SessionMemoryMaintenanceTests(unittest.TestCase):
    def test_maintenance_returns_combined_payload(self):
        proc = subprocess.run(
            [sys.executable, str(SCRIPT)],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(proc.returncode, 0)
        payload = json.loads(proc.stdout)
        self.assertEqual(payload["status"], "ok")
        self.assertIn("gc", payload)
        self.assertIn("health", payload)
        self.assertEqual(payload["gc"]["status"], "ok")
        self.assertEqual(payload["health"]["status"], "ok")


if __name__ == "__main__":
    unittest.main()
