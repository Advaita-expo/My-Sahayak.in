# Trusted Web Activity Setup for mysahayak.in

## Prerequisites Checklist

- [ ] PWA deployed to `https://mysahayak.in` (with HTTPS working)
- [ ] Android Studio installed
- [ ] Node.js and npm installed
- [ ] Git installed
- [ ] Android SDK installed (comes with Android Studio)
- [ ] Google Play Developer account created ($25 fee, one-time)

## Step 1: Clone TWA Starter Kit

```powershell
# Open PowerShell and run:
git clone https://github.com/GoogleChromeLabs/pwa-to-play.git
cd pwa-to-play
npm install
```

## Step 2: Create Your TWA Configuration

```powershell
npm run create -- `
  --name "My Sahayak" `
  --url "https://mysahayak.in" `
  --package "com.mysahayak.app" `
  --host "mysahayak.in"
```

**What this does:**
- `--name`: Your app name on Play Store
- `--url`: Your deployed PWA URL
- `--package`: Unique package name (reverse domain style)
- `--host`: Your domain (must match PWA domain)

## Step 3: Set Up assetlinks.json

Before building, create verification file:

**File location:** Place on your server at:
```
https://mysahayak.in/.well-known/assetlinks.json
```

**Content:** (I'll create this for you once you provide your SHA-256 fingerprint)

```json
[
  {
    "relation": ["delegate_permission/common.handle_all_urls"],
    "target": {
      "namespace": "android_app",
      "package_name": "com.mysahayak.app",
      "sha256_cert_fingerprints": [
        "XX:XX:XX:XX:XX:XX:XX:XX:XX:XX:XX:XX:XX:XX:XX:XX:XX:XX:XX:XX"
      ]
    }
  }
]
```

## Step 4: Build Android App Bundle (AAB)

```powershell
# Navigate to Android app directory
cd pwa-to-play/AndroidApp

# Build release bundle
.\gradlew.bat bundleRelease

# Output location:
# AndroidApp\app\build\outputs\bundle\release\app-release.aab
```

This creates `app-release.aab` (ready for Play Store)

## Step 5: Upload to Google Play Console

1. Go to **Google Play Console** → Create new app
2. Fill in app details:
   - App name: "My Sahayak"
   - Default language: English
   - App category: Lifestyle
   - Content rating: Fill out questionnaire
3. Go to **Release** → **Production**
4. Upload your `app-release.aab` file
5. Fill in:
   - Screenshots (at least 2)
   - App description
   - Privacy policy URL: `https://mysahayak.in/privacy`
   - Contact email
6. Review and submit for approval

## Estimated Timeline

- Setup: 30 minutes
- Build: 5 minutes
- Play Store review: 2-4 hours
- **Live on Play Store**: Same day!

## Troubleshooting

### "assetlinks.json not found"
- Make sure file is at: `https://mysahayak.in/.well-known/assetlinks.json`
- Test it: Open in browser, should show JSON content
- Make sure HTTPS is working

### Build fails with "SDK not found"
- Open Android Studio
- Go to **Tools** → **SDK Manager**
- Install "Android SDK Build-Tools 33"
- Install "Android API 33"

### "Certificate signature mismatch"
- Verify your SHA-256 fingerprint is correct
- Must match the key used to sign the AAB

## After Launch

Every time you update your PWA:
1. Deploy to `https://mysahayak.in`
2. Users get update automatically (no Play Store resubmission needed!)
3. That's it! PWA updates work seamlessly

## Key Files Created

```
pwa-to-play/
├── AndroidApp/                    # Android project
│   ├── app/
│   │   ├── build.gradle           # Build configuration
│   │   └── src/main/AndroidManifest.xml
│   └── build.gradle
├── build.gradle
└── gradlew                         # Gradle wrapper (Windows: gradlew.bat)
```

## Next Steps

1. **Get your SHA-256 fingerprint** from Android Studio
2. **Send it to me** → I'll create assetlinks.json
3. **Deploy assetlinks.json** to your server
4. **Build the AAB** using the gradlew command
5. **Upload to Play Store**
6. **Live!**

---

**Questions?** Let me know your fingerprint and I'll create the exact assetlinks.json for you!
