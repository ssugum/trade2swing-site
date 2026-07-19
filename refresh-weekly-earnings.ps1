<#
    Weekly Earnings Refresh Script
    - Copies latest dashboard
    - Creates backup
    - Logs all actions
    - Git commit + push
#>

# -------------------------------
# CONFIG
# -------------------------------

$projectRoot = "C:\Users\ssugu\OneDrive\Importantdocs\Claude\Projects\trade2swing"
$src = "C:\Users\ssugu\OneDrive\Importantdocs\Claude\Projects\Earnings Analyis\Weekly_Earnings_Dashboard.html"
$dst = "$projectRoot\dashboard\weekly-earnings-dashboard.html"
$backupDir = "$projectRoot\dashboard\backups"
$logFile = "$projectRoot\weekly_refresh.log"

# -------------------------------
# LOGGING FUNCTION
# -------------------------------

function Log {
    param([string]$msg)
    $timestamp = (Get-Date).ToString("yyyy-MM-dd HH:mm:ss")
    $entry = "$timestamp  $msg"
    Add-Content -Path $logFile -Value $entry
    Write-Host $entry
}

# -------------------------------
# START
# -------------------------------

Log "=== Weekly Earnings Refresh Started ==="

try {

    # Ensure backup directory exists
    if (!(Test-Path $backupDir)) {
        New-Item -ItemType Directory -Path $backupDir | Out-Null
        Log "Created backup directory: $backupDir"
    }

    # Backup existing dashboard
    if (Test-Path $dst) {
        $backupFile = "$backupDir\weekly-earnings-dashboard_$(Get-Date -Format 'yyyyMMdd_HHmmss').html"
        Copy-Item $dst $backupFile -Force
        Log "Backup created: $backupFile"
    } else {
        Log "No existing dashboard found — skipping backup."
    }

    # Copy new dashboard
    Copy-Item $src $dst -Force
    Log "Copied new dashboard to: $dst"

    # Git operations
    Set-Location $projectRoot
    git config --global user.name "ssugum"
    git config --global user.email "ssugum@gmail.com"

    git add .
    $today = Get-Date -Format "yyyy-MM-dd"
    $commitMessage = "Weekly Earnings Release $today"
    git commit -m $commitMessage
    git push

    Log "Git commit + push completed."
    Log "=== Weekly Earnings Refresh Completed Successfully ==="

} catch {
    Log "ERROR: $($_.Exception.Message)"
    Log "=== Weekly Earnings Refresh FAILED ==="
}