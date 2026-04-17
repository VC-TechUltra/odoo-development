# Repo graph workspace strategy

`repo-graph-local` is launched by `scripts/run-repo-graph-mcp.py` and determines the effective graph root with this precedence:

1. `CURSOR_REPO_GRAPH_ROOT` (explicit directory override)
2. Git top-level of `CURSOR_WORKSPACE_PATH` (or process working directory)
3. `CURSOR_WORKSPACE_PATH` (or process working directory) as-is

## Why this works across layouts

- **Single repo**: if your workspace is inside a Git repository, the launcher automatically lifts to the repo root.
- **Monorepo**: if your workspace points to any package/subfolder, the launcher still uses the monorepo Git top-level.
- **Nested/mixed local folders** (with or without `.git`): launcher falls back to the workspace path itself so the repo graph can still analyze local files.

## Optional override

Set `CURSOR_REPO_GRAPH_ROOT` when you want a specific folder to be used regardless of current workspace location.

Examples:

- macOS/Linux:
  ```bash
  export CURSOR_REPO_GRAPH_ROOT=/path/to/parent-workspace
  ```
- Windows PowerShell:
  ```powershell
  $env:CURSOR_REPO_GRAPH_ROOT = "D:\\workspace"
  ```

## Recommendation for multi-repo parent workspaces

If you keep many repos under one parent folder, open that parent as your Cursor workspace when you want cross-repo graph context, or set `CURSOR_REPO_GRAPH_ROOT` to that parent for the session.
