# How to Get Your Android Signing Key Fingerprint

## Option 1: Use Google Play Console (Easiest - Recommended)

If you already have the Google Play APK uploaded:

1. Go to **Google Play Console** → Your app
2. Go to **Release** → **Setup** → **App signing**
3. Copy the **SHA-256 certificate fingerprint**
4. It looks like: `AA:BB:CC:DD:EE:FF:00:11:22:33:44:55:66:77:88:99:AA:BB:CC:DD`

---

## Option 2: Generate a New Signing Key

If you don't have one yet, Android Studio will generate it.

**Using Android Studio:**

1. Open Android Studio
2. Go to **Build** → **Generate Signed Bundle/APK**
3. Click **Create new** to generate a new key
4. Fill in the details:
   - **Key store path**: Choose a location to save (e.g., `C:\keys\my-sahayak.jks`)
   - **Key store password**: Create a strong password (save it!)
   - **Key alias**: `my-sahayak-key`
   - **Key password**: Same as key store password
   - **Validity**: `10000` days (25+ years)

5. After creation, the fingerprint will be shown
6. Copy the **SHA-256 value**

---

## Option 3: Get Fingerprint from Existing Key (Command Line)

If you already have a `my-sahayak.jks` file:

```bash
# Windows (PowerShell)
keytool -list -v -keystore "C:\path\to\my-sahayak.jks" -alias my-sahayak-key

# Mac/Linux
keytool -list -v -keystore /path/to/my-sahayak.jks -alias my-sahayak-key
```

It will ask for the key store password, then show the SHA-256 fingerprint.

---

## Once You Have the Fingerprint

Provide it to me and I'll create your `assetlinks.json` file with:
- Your fingerprint
- Your package name (e.g., `com.mysahayak.app`)
- Proper configuration for TWA

Example fingerprint format:
```
AA:BB:CC:DD:EE:FF:00:11:22:33:44:55:66:77:88:99:AA:BB:CC:DD
```
