import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "verify_branch_rotation.py"


class BranchRotationVerifierTests(unittest.TestCase):
    def test_branch_rotation_verifier(self):
        proc = subprocess.run([sys.executable, str(SCRIPT)], capture_output=True, text=True, check=False)
        self.assertEqual(proc.returncode, 0)
        payload = json.loads(proc.stdout)
        self.assertEqual(payload["status"], "ok")


if __name__ == "__main__":
    unittest.main()
