#!/usr/bin/env python3
"""Export stack health JSON to a file for CI artifacts."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHECKER = ROOT / "scripts" / "health_check_stack.py"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    parser.add_argument("--offline", action="store_true")
    parser.add_argument("--strict-local", action="store_true")
    args = parser.parse_args()

    cmd = [sys.executable, str(CHECKER)]
    if args.offline:
        cmd.append("--offline")
    if args.strict_local:
        cmd.append("--strict-local")

    proc = subprocess.run(cmd, capture_output=True, text=True, check=False)
    try:
        payload = json.loads(proc.stdout)
    except json.JSONDecodeError:
        payload = {
            "status": "degraded",
            "mode": "unknown",
            "checks": [],
            "failed_count": 1,
            "error": "HEALTH_CHECK_OUTPUT_INVALID_JSON",
            "detail": proc.stdout.strip() or proc.stderr.strip() or "no output",
        }
    payload["exit_code"] = proc.returncode

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, indent=2) + "\n")
    print(str(out))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
