$ErrorActionPreference = 'Stop'

$RootDir = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$Store = Join-Path $RootDir 'scripts/session_memory_store.py'

$workspace = Join-Path $env:TEMP 'odoo-mem-test-ps1'
$branch = 'feature-test'
$sessionId = 'sess-ps1'

$init = python $Store init --workspace $workspace --branch $branch --session-id $sessionId --ttl-hours 48 | ConvertFrom-Json
if ($init.status -ne 'ok') { throw 'init failed' }

python $Store put --workspace $workspace --branch $branch --session-id $sessionId --key decision --value phase3-test --kind note | Out-Null

$list = python $Store list --workspace $workspace --branch $branch --session-id $sessionId --limit 5 | ConvertFrom-Json
if ($list.status -ne 'ok' -or $list.items.Count -lt 1) { throw 'list failed' }

$ns = python $Store namespace-info --workspace $workspace --branch $branch --session-id $sessionId | ConvertFrom-Json
if ($ns.status -ne 'ok' -or $ns.branch -ne $branch) { throw 'namespace-info failed' }

python $Store clear --workspace $workspace --branch $branch --session-id $sessionId | Out-Null
