# Setting Up BigQuery Credentials on Streamlit Cloud

## Problem
Your app shows "BigQuery credentials not found" on Streamlit Cloud because the `spicemoney-dwh.json` file is not available in the cloud environment (and should not be committed to Git for security reasons).

## Solution: Use Streamlit Secrets Management

### Step 1: Access Your Streamlit Cloud App Settings

1. Go to https://share.streamlit.io/
2. Find your app: **healthdashboardgit**
3. Click on the **⋮** (three dots) menu next to your app
4. Select **Settings**

### Step 2: Add Secrets

1. In the Settings page, click on the **Secrets** tab
2. You'll see a text editor where you can paste your secrets

### Step 3: Copy and Paste the Following Content

Copy the **entire content** from the `.streamlit/secrets.toml` file that was just created in your project:

```toml
[gcp_service_account]
type = "service_account"
project_id = "spicemoney-dwh"
private_key_id = "43dae62622b222a521a6c6fa1a94f1c59e97a887"
private_key = """-----BEGIN PRIVATE KEY-----
MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDQ4NWR5ddJSokF
kmt7DZx7mHV6F9jB0mmkRt7R/bUlgdEqg0vxDzvklomhQn8j7enGbFlCKfA9RaiV
QiMQulsY6dIztYWwaCbl60qeugMpLAlmc5sUjhHVk1R5Ue6JAt4YdXP3o3nvbTYp
JrB3BXG+sRqoOPhnUjzTFXUuE9vqruiTUqQ5/5DOjEQ44CV9bMmj17UP/+CJryMH
i13WJNkochinkn1nTBsoav3K8OnBlL92pxt4f5wGOQQaXEjEPSImMIYWSWitcLCv
Jdyu+RhfmNJmu0l/0OLwq2QOy7goz4cKlqFIqj7gOXHYjeauzNJv42IDIcCV/NYo
dA5A56iBAgMBAAECggEAAUvqYQ92K9d+MwsOBvBP4/LpHirlU4t4A5o7aj5GHS3j
G7DY8qDpLdzcjQqAOe7eIDcuW3TH/JL6hIKpyQ7L35Adl+iTV3b61tTqqUJdhqhM
hQnh3b//NSSTxg6ciaLIHvElTFVqPYw5Mj3Lo2sYCHQwLPi9jsnTfgciEd+M4k+h
jqkF337pqeT32lHVR000jVq7grgMsl3rEqydByUONjqkpsI00L4VRBdvFhjy9lc9
UvV3vbLty1yq8Nv/Ez2T95oRP57izucVgb/MndicHb3Ab9Nb/ePTc7OZNsEUxZCq
8Y/XEteju7j5xC7RNIzCie0tuMgRDt7ZcLn5AaoO4QKBgQDushIdKlcLHBzCletj
nTNyo2E09WVo3v5Bvaao0PxVq6xvTiU6pvVUJnIFPwu92XNwRgrPEFn5LaaEqNNa
E/QJ1C6GZ7UF1WT0mnQBclHlPWGa4n5dw++wKhA48COgRgw4p+gSXxiwClbbXy2k
vg+2rVFDliieNWjZpjxm+7MxFQKBgQDgBWLt8LShYb0yCZqkdzQlT/QRcLeIBKvy
SNUJP0DU/d7Ib4q6egwCzq87Cz5ecjKjI8cnbMKGeGA2/mmCLHnsiJwFKhcC0dIV
rCny3r6iLF4fHSkmWpQVHkyPFShECJ894Q5Qz7IrzqR7kOwYjZUnqZOZSl5tTcHb
C4Xa2Y28vQKBgQDaonbfChIylext+55hXvNp9Oar+H6L4X1owAswpEQNQLMwPJbz
M0yRaKmVzpq1qcEIPM/XvDV9fOgCqRT2dEJa4mQ/Lizsi/rt5a+OR6Vl4aROl1mC
D1+zr8OuM5+eRasaFgoHEd3uGXpXc8W+GW0ROY2u55KK34cLnS3EcpY+xQKBgFUR
1pKSwJU0H3t76CyiU7wDk6R30EontAAKplOfoIgBa/NjYCQWKq96O1LJn0KQTShk
csFG7MvRtH/NttVG/HnVGqJfbGOWuBegzEE9UtkUzh00nqbA6NDoM5x2JVdIiugd
qakIZhl6nD2MOAvO4CAypikk85zAVWhQBOGpkchlAoGBALsMeB/mkTEiEl/Jv0EB
G3oB1hibqKjjJDrsjHaMJ0phyMCoFmegbwJdJtXavtgb7W7yf3R3ZwZLmarBBT4Y
kW+xpyGn0CfMIuMIhrcUjt4O/3oX+XDSyOh+GS1nEyyK6TIKc5j4NOLwur5qC3Z4
aDU5iGJEX7pFUwPW62x0Besh
-----END PRIVATE KEY-----
"""
client_email = "mrunalinee-patole@spicemoney-dwh.iam.gserviceaccount.com"
client_id = "110559195689467570271"
auth_uri = "https://accounts.google.com/o/oauth2/auth"
token_uri = "https://oauth2.googleapis.com/token"
auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
client_x509_cert_url = "https://www.googleapis.com/robot/v1/metadata/x509/mrunalinee-patole%40spicemoney-dwh.iam.gserviceaccount.com"
universe_domain = "googleapis.com"
```

### Step 4: Save the Secrets

1. Click **Save** button
2. Your app will automatically restart with the new credentials

### Step 5: Verify the Fix

1. Go to your app: https://healthdashboardgit-kc5zbc5mqhc6r8i3yasf7y.streamlit.app/
2. You should now see "✅ Connected to BigQuery (Streamlit Cloud): spicemoney-dwh" message
3. The app should now load real data from BigQuery instead of dummy data

## Important Notes

### Security
- ✅ The `.streamlit/secrets.toml` file is already in `.gitignore` and won't be committed to Git
- ✅ Secrets are encrypted on Streamlit Cloud
- ✅ Only you (the app owner) can view/edit the secrets

### Local Development
- Your app will still work locally using the `spicemoney-dwh.json` file
- The code automatically tries Streamlit secrets first, then falls back to the local file

### Testing Locally with Secrets
If you want to test the secrets locally:
1. Keep the `.streamlit/secrets.toml` file
2. Run `streamlit run aeps_health_dashboard.py`
3. The app will use the secrets.toml file

## Troubleshooting

### If you still see the error after adding secrets:

1. **Check the format**: Make sure there are no extra spaces or missing quotes in the secrets
2. **Restart the app**: Go to Streamlit Cloud → Manage app → Reboot
3. **Check the private key**: Ensure the `private_key` is wrapped in triple quotes `"""`
4. **Verify project_id**: Confirm it matches your BigQuery project

### Check Service Account Permissions:
The service account `mrunalinee-patole@spicemoney-dwh.iam.gserviceaccount.com` needs these roles:
- BigQuery Data Viewer
- BigQuery Job User
- BigQuery Read Session User

## What Changed in the Code

The `get_bigquery_client()` function now:
1. **First tries** to load credentials from `st.secrets["gcp_service_account"]` (Streamlit Cloud)
2. **Falls back** to loading from `spicemoney-dwh.json` file (Local development)
3. Shows a clear success message indicating which method was used

This ensures your app works seamlessly in both environments!

