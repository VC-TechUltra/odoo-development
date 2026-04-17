# Repo graph workspace strategy

`repo-graph-local` is launched by `scripts/run-repo-graph-mcp.py` and determines the effective graph root with this precedence:

1. `CURSOR_ACTIVE_REPO_PATH` (active repo override for multi-repo workspaces)
2. `CURSOR_REPO_GRAPH_ROOT` (explicit directory override)
3. Git top-level of `CURSOR_WORKSPACE_PATH` (or process working directory)
4. `CURSOR_WORKSPACE_PATH` (or process working directory) as-is

## Why this works across layouts

- **Single repo**: if your workspace is inside a Git repository, the launcher automatically lifts to the repo root.
- **Monorepo**: if your workspace points to any package/subfolder, the launcher still uses the monorepo Git top-level.
- **Nested/mixed local folders** (with or without `.git`): launcher falls back to the workspace path itself so the repo graph can still analyze local files.

## Optional override

Set `CURSOR_ACTIVE_REPO_PATH` when switching between multiple repos under one parent workspace.  
Set `CURSOR_REPO_GRAPH_ROOT` for a broader static override when you want one fixed root.

Examples:

- macOS/Linux:
  ```bash
  export CURSOR_ACTIVE_REPO_PATH=/path/to/current-repo
  export CURSOR_REPO_GRAPH_ROOT=/path/to/parent-workspace
  ```
- Windows PowerShell:
  ```powershell
  $env:CURSOR_ACTIVE_REPO_PATH = "D:\\workspace\\repo-a"
  $env:CURSOR_REPO_GRAPH_ROOT = "D:\\workspace"
  ```

## Recommendation for multi-repo parent workspaces

If you keep many repos under one parent folder, open that parent as your Cursor workspace for broad context and set `CURSOR_ACTIVE_REPO_PATH` per active repo so both `repo-graph-local` and `session-memory-local` resolve to the same scope.
