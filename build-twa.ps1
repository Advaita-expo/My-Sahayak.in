#!/usr/bin/env pwsh
<#
.SYNOPSIS
Automated TWA Build Script for My Sahayak
Builds an Android App Bundle (AAB) from your PWA for Google Play Store submission.

.DESCRIPTION
This script:
1. Installs Bubblewrap (if not already installed)
2. Initializes a TWA project from your PWA manifest
3. Builds the Android App Bundle (AAB)
4. Shows output location and next steps

.USAGE
.\build-twa.ps1

.NOTES
Requires: Node.js, npm, Java JDK, Android Studio + SDK
Time: ~15-30 minutes on first run (slower on subsequent builds)
#>

param(
    [string]$ManifestUrl = "https://mysahayak.in/manifest.json",
    [string]$PackageId = "com.mysahayak.app",
    [string]$AppName = "My Sahayak",
    [string]$AppVersion = "1.0.0"
)

Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "My Sahayak TWA Builder" -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host ""

# Check if Node.js is installed
Write-Host "Checking prerequisites..." -ForegroundColor Yellow
$nodeCheck = node --version 2>$null
if (-not $nodeCheck) {
    Write-Host "ERROR: Node.js not found. Install from https://nodejs.org" -ForegroundColor Red
    exit 1
}
Write-Host "✓ Node.js found: $nodeCheck" -ForegroundColor Green

# Check if Java is installed
$javaCheck = java -version 2>&1 | Select-Object -First 1
if (-not $javaCheck) {
    Write-Host "ERROR: Java not found. Install JDK from https://adoptium.net" -ForegroundColor Red
    exit 1
}
Write-Host "✓ Java found" -ForegroundColor Green

Write-Host ""
Write-Host "Installing/updating Bubblewrap..." -ForegroundColor Yellow
npm install -g @bubblewrap/cli --quiet

Write-Host ""
Write-Host "Initializing TWA project..." -ForegroundColor Yellow
Write-Host "Manifest: $ManifestUrl"
Write-Host "Package ID: $PackageId"
Write-Host "App Name: $AppName"
Write-Host ""

# Initialize Bubblewrap (will use Play App Signing by default)
bubblewrap init `
    --manifest=$ManifestUrl `
    --packageId=$PackageId `
    --appVersion=$AppVersion `
    --name=$AppName

if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: Bubblewrap init failed" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "Building Android App Bundle (AAB)..." -ForegroundColor Yellow

# Find the generated android folder
$androidFolder = Get-ChildItem -Filter "android" -Recurse -ErrorAction SilentlyContinue | Select-Object -First 1
if (-not $androidFolder) {
    Write-Host "ERROR: Android folder not found. Check Bubblewrap init output." -ForegroundColor Red
    exit 1
}

Push-Location $androidFolder.FullName

Write-Host "Working directory: $(Get-Location)" -ForegroundColor Gray

# Build the AAB
if ($IsWindows) {
    .\gradlew.bat bundleRelease
} else {
    ./gradlew bundleRelease
}

if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: Gradle build failed" -ForegroundColor Red
    Pop-Location
    exit 1
}

Pop-Location

Write-Host ""
Write-Host "==========================================" -ForegroundColor Green
Write-Host "✓ BUILD SUCCESSFUL!" -ForegroundColor Green
Write-Host "==========================================" -ForegroundColor Green
Write-Host ""

$aabPath = "$($androidFolder.FullName)\app\build\outputs\bundle\release\app-release.aab"
Write-Host "Output AAB: $aabPath" -ForegroundColor Cyan
Write-Host ""
Write-Host "NEXT STEPS:" -ForegroundColor Yellow
Write-Host "1. Go to Google Play Console"
Write-Host "2. Release → Internal testing → Create release"
Write-Host "3. Upload: $aabPath"
Write-Host "4. Fill release notes and store listing"
Write-Host "5. Review and publish to internal testing"
Write-Host "6. Copy the Play signing certificate SHA-256 from Setup -> App integrity"
Write-Host "7. Tell me the SHA-256 and I'll update assetlinks.json"
Write-Host ""
Write-Host "AAB file is ready for upload!"
