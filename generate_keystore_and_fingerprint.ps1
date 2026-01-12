<#
PowerShell helper: generate a keystore and show SHA-256 fingerprint.
Usage (PowerShell):
  .\generate_keystore_and_fingerprint.ps1 -KeystorePath "C:\keys\my-sahayak.jks" -Alias my-sahayak-key

You will be prompted for keystore password and key details by keytool.
#>

param(
  [string]$KeystorePath = "$env:USERPROFILE\\my-sahayak.jks",
  [string]$Alias = "my-sahayak-key"
)

$keytool = "keytool"

Write-Host "Generating keystore at: $KeystorePath"
& $keytool -genkeypair -v -keystore $KeystorePath -alias $Alias -keyalg RSA -keysize 2048 -validity 10000

Write-Host `n"--- Keystore generated ---`n"
Write-Host "Now showing SHA-256 fingerprint (you will be prompted for the keystore password):`
"
& $keytool -list -v -keystore $KeystorePath -alias $Alias

Write-Host `n"Copy the line that starts with 'SHA256:' — that is the certificate fingerprint you need for assetlinks.json.`n"
