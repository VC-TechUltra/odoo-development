import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "export_health_report.py"


class ExportHealthReportTests(unittest.TestCase):
    def test_export_health_report_writes_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "health.json"
            proc = subprocess.run(
                [sys.executable, str(SCRIPT), "--offline", "--strict-local", "--output", str(output)],
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(proc.returncode, 0)
            self.assertTrue(output.exists())
            payload = json.loads(output.read_text())
            self.assertIn("status", payload)
            self.assertIn("checks", payload)
            self.assertIn("exit_code", payload)


if __name__ == "__main__":
    unittest.main()
