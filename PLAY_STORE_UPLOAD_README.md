My Sahayak — Play Store Upload Guide

Summary
- You already have the signed Android App Bundle (AAB) and APK in `My Sahayak - Google Play package`:
  - `My Sahayak.aab` (preferred for Play)
  - `My Sahayak.apk` (signed APK)
  - `signing.keystore` and `signing-key-info.txt`

Quick checks (local)
- Confirm `My Sahayak.aab` exists:
  - Path: `My Sahayak - Google Play package\My Sahayak.aab`
- If you want to verify the APK signature (optional):

  PowerShell / CMD:
  ```powershell
  # apksigner is in Android SDK build-tools; add it to PATH or run from its folder
  apksigner verify --print-certs "My Sahayak - Google Play package\My Sahayak.apk"
  ```

- If you need to rebuild AAB from project:

  Windows (from project root):
  ```powershell
  .\gradlew.bat bundleRelease
  # output: app/build/outputs/bundle/release/app-release.aab
  ```

Play Console upload steps (recommended)
1. Sign in to Play Console: https://play.google.com/console
2. Create new app (if not already): "Create app" → choose app details.
3. Complete required sections before release: Store listing, Content rating, Privacy policy URL, App access/data safety, Pricing & distribution.
4. Upload AAB:
   - Go to "Release" → "Production" (or Testing → Internal testing first).
   - Create new release → Upload `My Sahayak.aab` from `My Sahayak - Google Play package`.
   - Add release notes and save.
5. Review & rollout:
   - You can start with Internal/Closed testing for verification.
   - Then promote to Production (use staged rollout if desired).

Important notes
- New apps: Play requires AAB (not APK) for new apps. You already have `My Sahayak.aab` — good.
- Versioning: Ensure `versionCode` in the uploaded bundle is higher than any published version.
- Play App Signing: It's recommended to opt into Play App Signing (Play will manage signing key). If you already used `signing.keystore` to sign the AAB, keep a secure backup.
- Keep `signing.keystore` and its passwords safe — losing keys prevents updates if you opt-out of Play App Signing.

Testing before production
- Use Internal testing track to verify the build on devices quickly.
- Invite testers or create a testing list; install via Play internal testing link.

If you want, I can:
- Provide the exact UI path and screenshots for Play Console steps.
- Create release notes text and store listing drafts (title, short/long description, screenshots captions).
- Provide commands to upload the AAB via `play-cli` tools (if you want automated uploads).

Next recommended action: Log into Play Console and upload `My Sahayak.aab` to an internal testing release, then share any errors or warnings you see there so I can help fix them.