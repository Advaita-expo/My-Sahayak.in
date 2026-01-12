TWA Quickstart — Build an Android App Bundle (AAB) for Play Store

Goal: Publish your PWA (https://mysahayak.in) on Google Play so tapping the Play Store icon opens the PWA in a browser-like fullscreen (Trusted Web Activity).

Prerequisites
- Node.js + npm installed
- Java JDK and Android Studio + Android SDK installed
- Bubblewrap CLI (npm) will be used to create the TWA project
- A Google Play Developer account ($25 one-time)
- Your site served over HTTPS (already done)

1) (Optional) Generate keystore & fingerprint locally

Run the PowerShell helper in this repo to create a keystore and show SHA-256:

```powershell
# generate a keystore in your user folder (or specify a path)
.\generate_keystore_and_fingerprint.ps1 -KeystorePath "C:\keys\my-sahayak.jks" -Alias my-sahayak-key
```

When done, copy the `SHA256:` fingerprint value shown. It looks like:
```
AA:BB:CC:DD:EE:FF:00:11:22:33:44:55:66:77:88:99:AA:BB:CC:DD
```

2) Install Bubblewrap CLI

```bash
npm install -g @bubblewrap/cli
```

3) Initialize a TWA project

Replace values for package id and name.

```bash
bubblewrap init --manifest=https://mysahayak.in/manifest.json --packageId=com.mysahayak.app --appVersion=1.0.0 --name="My Sahayak"
```

If you prefer to use your keystore for signing during init, add flags:

```bash
bubblewrap init --manifest=... --packageId=com.mysahayak.app --name="My Sahayak" --keystore="C:\keys\my-sahayak.jks" --keyAlias=my-sahayak-key
```

4) Build the AAB (Android App Bundle)

Open a terminal in the generated Android project (Bubblewrap prints the folder name). Then run:

```bash
# Windows
cd <generated-android-folder>\android
.\gradlew.bat bundleRelease

# macOS / Linux
./gradlew bundleRelease
```

Output: `app\build\outputs\bundle\release\app-release.aab` — upload this to Play Console.

5) Upload to Google Play Console

- Create a new app in Play Console
- Fill out store listing (title, description, screenshots, privacy policy URL on your domain)
- Release → Production or Internal testing → Upload `app-release.aab`

Important: Play App Signing

- If you accept "Play App Signing" (recommended), Google will re-sign your app. In that case you must use the *Play signing certificate* fingerprint (not your local keystore) in `assetlinks.json`.
- After uploading the AAB, go to Play Console → Setup → App integrity → App signing key certificate (SHA-256). Copy that fingerprint.

6) Deploy `assetlinks.json`

Create or update `public/.well-known/assetlinks.json` in this repo with the correct package name and the SHA-256 fingerprint (either your keystore or the Play signing key, see note above). Example:

```json
[
  {
    "relation": ["delegate_permission/common.handle_all_urls"],
    "target": {
      "namespace": "android_app",
      "package_name": "com.mysahayak.app",
      "sha256_cert_fingerprints": [
        "AA:BB:CC:...:DD"
      ]
    }
  }
]
```

Commit and push to your GitHub repo so Netlify redeploys. Verify it is available at:

https://mysahayak.in/.well-known/assetlinks.json

7) Test the installed app

- Use Play Console internal test track to send install link to a test device.
- Install from Play; the app should open as a fullscreen Trusted Web Activity that loads `https://mysahayak.in`.

Troubleshooting checklist
- `assetlinks.json` returns HTTP 200 and the JSON content; no redirects.
- The package name in `assetlinks.json` matches the AAB package id.
- The fingerprint matches the signing certificate used to sign the uploaded AAB (or Play signing key if Play re-signed).

If you want, I can:
- Prepare `assetlinks.json` with your package name and a placeholder (done) — replace `REPLACE_WITH_SHA256` with the actual fingerprint.
- Help run `bubblewrap init` locally by giving exact commands you can paste.
- Walk through uploading the AAB to Play Console step-by-step.

Next recommended move for me (pick one):
- A) Fill `assetlinks.json` now if you provide the SHA-256 and package name (I will update file and commit it)
- B) Guide you through `bubblewrap init` and `./gradlew bundleRelease` interactively

