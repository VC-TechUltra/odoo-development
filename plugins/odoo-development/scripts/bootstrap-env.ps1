$ErrorActionPreference = 'Stop'

$PluginName = 'odoo-development'
$ConfigDir = if ($env:CURSOR_ODOO_CONFIG_DIR) { $env:CURSOR_ODOO_CONFIG_DIR } else { Join-Path $HOME ".cursor-$PluginName" }
$ConfigFile = Join-Path $ConfigDir 'config.env.ps1'
$LkgFile = Join-Path $ConfigDir 'lkg.env.ps1'

New-Item -ItemType Directory -Path $ConfigDir -Force | Out-Null

if (Test-Path $ConfigFile) { . $ConfigFile }

if (-not $INSTALL_BASE) {
    $defaultBase = Join-Path $HOME ".local/share/$PluginName"
    if ($Host.UI.RawUI) {
        $inputBase = Read-Host "[odoo-development] Enter install/cache base path [$defaultBase]"
        if ([string]::IsNullOrWhiteSpace($inputBase)) { $inputBase = $defaultBase }
        $INSTALL_BASE = $inputBase
    } else {
        $INSTALL_BASE = $defaultBase
    }
}
New-Item -ItemType Directory -Path $INSTALL_BASE -Force | Out-Null

function Get-PythonCandidates {
    $candidates = @('python3.12','python3.11','python3.10','python3','py')
    $result = @()
    foreach ($c in $candidates) {
        $cmd = Get-Command $c -ErrorAction SilentlyContinue
        if ($cmd) { $result += $cmd.Source }
    }
    return $result | Select-Object -Unique
}

function Get-PythonVersion($pythonBin) {
    try {
        & $pythonBin -c "import sys; print('.'.join(map(str, sys.version_info[:3])))" 2>$null
    } catch {
        ''
    }
}

function Is-VersionInRange($v) {
    try {
        $ver = [Version]$v
        return ($ver.Major -eq 3 -and $ver.Minor -ge 10 -and $ver.Minor -le 12)
    } catch {
        return $false
    }
}

$bestPython = $null
$bestVersion = [Version]'0.0.0'
foreach ($pythonBin in Get-PythonCandidates) {
    $v = Get-PythonVersion $pythonBin
    if (-not $v) { continue }
    if (-not (Is-VersionInRange $v)) { continue }
    $ver = [Version]$v
    if ($ver -gt $bestVersion) {
        $bestVersion = $ver
        $bestPython = $pythonBin
    }
}

if (-not $bestPython) {
    throw 'No local Python in supported range [3.10, 3.12].'
}

$PYTHON_BIN = $bestPython
"`$INSTALL_BASE = '$INSTALL_BASE'`n`$PYTHON_BIN = '$PYTHON_BIN'" | Set-Content -Path $ConfigFile -Encoding UTF8

try {
    & $PYTHON_BIN -m pip install --user --upgrade code-review-graph *> $null
} catch {
    # Continue to smoke test + fallback
}

function Get-CrgVersion {
    try {
        & $PYTHON_BIN -c "import importlib.metadata as md; print(md.version('code-review-graph'))"
    } catch {
        ''
    }
}

function Test-Crg {
    try {
        & code-review-graph --help *> $null
        return $true
    } catch {
        try {
            & $PYTHON_BIN -m code_review_graph --help *> $null
            return $true
        } catch {
            return $false
        }
    }
}

$currentVersion = Get-CrgVersion
if (Test-Crg) {
    if ($currentVersion) {
        "`$CRG_LKG_VERSION = '$currentVersion'" | Set-Content -Path $LkgFile -Encoding UTF8
    }
    @{ status='ok'; python=$PYTHON_BIN; codeReviewGraphVersion=$currentVersion; installBase=$INSTALL_BASE } | ConvertTo-Json -Compress
    exit 0
}

if (Test-Path $LkgFile) { . $LkgFile }
if ($CRG_LKG_VERSION) {
    try {
        & $PYTHON_BIN -m pip install --user --upgrade "code-review-graph==$CRG_LKG_VERSION" *> $null
    } catch {
    }
    if (Test-Crg) {
        @{ status='degraded'; reason='latest_failed_using_lkg'; python=$PYTHON_BIN; codeReviewGraphVersion=$CRG_LKG_VERSION; installBase=$INSTALL_BASE } | ConvertTo-Json -Compress
        exit 0
    }
}

@{ status='degraded'; reason='code_review_graph_unavailable'; python=$PYTHON_BIN; installBase=$INSTALL_BASE } | ConvertTo-Json -Compress
