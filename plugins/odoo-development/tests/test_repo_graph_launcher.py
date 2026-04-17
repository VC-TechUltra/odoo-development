from __future__ import annotations

import importlib.util
import os
import subprocess
import tempfile
import unittest
from pathlib import Path


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "scripts" / "run-repo-graph-mcp.py"
_spec = importlib.util.spec_from_file_location("run_repo_graph_mcp", SCRIPT_PATH)
assert _spec and _spec.loader
launcher = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(launcher)


class RepoGraphLauncherResolutionTests(unittest.TestCase):
    def test_override_wins_when_valid(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            workspace = Path(tmp) / "workspace"
            override = Path(tmp) / "override"
            workspace.mkdir()
            override.mkdir()

            prev_workspace = os.environ.get("CURSOR_WORKSPACE_PATH")
            prev_override = os.environ.get("CURSOR_REPO_GRAPH_ROOT")
            try:
                os.environ["CURSOR_WORKSPACE_PATH"] = str(workspace)
                os.environ["CURSOR_REPO_GRAPH_ROOT"] = str(override)
                resolved = launcher._resolve_repo_graph_root()
                self.assertEqual(resolved, override.resolve())
            finally:
                if prev_workspace is None:
                    os.environ.pop("CURSOR_WORKSPACE_PATH", None)
                else:
                    os.environ["CURSOR_WORKSPACE_PATH"] = prev_workspace
                if prev_override is None:
                    os.environ.pop("CURSOR_REPO_GRAPH_ROOT", None)
                else:
                    os.environ["CURSOR_REPO_GRAPH_ROOT"] = prev_override

    def test_non_git_workspace_falls_back_to_workspace(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            workspace = Path(tmp) / "workspace"
            workspace.mkdir()

            prev_workspace = os.environ.get("CURSOR_WORKSPACE_PATH")
            prev_override = os.environ.get("CURSOR_REPO_GRAPH_ROOT")
            try:
                os.environ["CURSOR_WORKSPACE_PATH"] = str(workspace)
                os.environ.pop("CURSOR_REPO_GRAPH_ROOT", None)
                resolved = launcher._resolve_repo_graph_root()
                self.assertEqual(resolved, workspace.resolve())
            finally:
                if prev_workspace is None:
                    os.environ.pop("CURSOR_WORKSPACE_PATH", None)
                else:
                    os.environ["CURSOR_WORKSPACE_PATH"] = prev_workspace
                if prev_override is None:
                    os.environ.pop("CURSOR_REPO_GRAPH_ROOT", None)
                else:
                    os.environ["CURSOR_REPO_GRAPH_ROOT"] = prev_override

    def test_git_workspace_resolves_to_top_level(self) -> None:
        if subprocess.run(["git", "--version"], capture_output=True, text=True).returncode != 0:
            self.skipTest("git is not available")

        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp) / "repo"
            nested = repo / "services" / "api"
            nested.mkdir(parents=True)
            subprocess.run(["git", "init"], cwd=repo, check=True, capture_output=True, text=True)

            prev_workspace = os.environ.get("CURSOR_WORKSPACE_PATH")
            prev_override = os.environ.get("CURSOR_REPO_GRAPH_ROOT")
            try:
                os.environ["CURSOR_WORKSPACE_PATH"] = str(nested)
                os.environ.pop("CURSOR_REPO_GRAPH_ROOT", None)
                resolved = launcher._resolve_repo_graph_root()
                self.assertEqual(resolved, repo.resolve())
            finally:
                if prev_workspace is None:
                    os.environ.pop("CURSOR_WORKSPACE_PATH", None)
                else:
                    os.environ["CURSOR_WORKSPACE_PATH"] = prev_workspace
                if prev_override is None:
                    os.environ.pop("CURSOR_REPO_GRAPH_ROOT", None)
                else:
                    os.environ["CURSOR_REPO_GRAPH_ROOT"] = prev_override


if __name__ == "__main__":
    unittest.main()
