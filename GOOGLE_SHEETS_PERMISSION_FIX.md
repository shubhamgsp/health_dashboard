# 🔧 Fix Google Sheets Permission Error (403)

## 🚨 **Problem Identified**

Your Streamlit app is getting a **403 Permission Error** when trying to access the new Google Sheet for product metrics:

```
Error loading Google Sheets: <HttpError 403 when requesting 
https://sheets.googleapis.com/v4/spreadsheets/1LMDeoOLzfMaLfuVown4If6ffI1agZlEzjTHzFgBuqRw
returned "The caller does not have permission"
```

## ✅ **Solution: Share the Google Sheet**

### **Step 1: Open the Updated Sheet**
Click this link to open the sheet that needs to be shared:
👉 **https://docs.google.com/spreadsheets/d/1DLU87T3DW9ruoR_U_jVCTV8hvuVCRSw8VMWLaN1PUBU/edit?gid=272453504#gid=272453504**

**Note**: The worksheet name is 'Sheet2' (data has been moved to this new sheet)

### **Step 2: Share with Service Account**
1. Click the **"Share"** button (top right corner)
2. In the "Add people and groups" field, enter:
   ```
   mrunalinee-patole@spicemoney-dwh.iam.gserviceaccount.com
   ```
3. Set permission to **"Viewer"**
4. Click **"Send"**

### **Step 3: Verify All Sheets Are Shared**

Your app accesses these Google Sheets. Make sure ALL are shared:

| Sheet ID | Purpose | Status | Action Needed |
|----------|---------|--------|---------------|
| `1HaW-pC5niZNm0_ii4zoXG-xR781dmDmbPjQf6W_b7Y8` | Anomaly Dashboard | ✅ Working | None |
| `1XyTNR14JlkM_7uHEeoQa68mLgeiAZTaCq9vR-VCff4o` | Login Data | ✅ Working | None |
| `1DLU87T3DW9ruoR_U_jVCTV8hvuVCRSw8VMWLaN1PUBU` | Bugs Data | ✅ Working | None |
| `1LMDeoOLzfMaLfuVown4If6ffI1agZlEzjTHzFgBuqRw` | **Product Metrics (NEW)** | ❌ **403 Error** | **Share with service account** |

## 🧪 **Test the Fix**

### **Option 1: Quick Test (Recommended)**
1. Share the sheet as described above
2. Wait 30 seconds
3. Refresh your Streamlit app
4. The error should disappear

### **Option 2: Detailed Test**
Run the test script to verify all sheets are accessible:

```bash
python test_google_sheets_access.py
```

This will show you exactly which sheets need to be shared.

## 🔍 **Why This Happens**

- **Local Environment**: Works because you're logged in with your personal Google account
- **Streamlit Cloud**: Uses a service account (`mrunalinee-patole@spicemoney-dwh.iam.gserviceaccount.com`) that needs explicit permission to access each sheet

## 📋 **Complete Checklist**

- [ ] Share `1LMDeoOLzfMaLfuVown4If6ffI1agZlEzjTHzFgBuqRw` with service account
- [ ] Set permission to "Viewer"
- [ ] Wait 30 seconds for permissions to propagate
- [ ] Refresh your Streamlit app
- [ ] Verify no more 403 errors
- [ ] Confirm real data loads instead of sample data

## 🚀 **Expected Result**

**Before Fix:**
```
❌ Error loading Google Sheets: <HttpError 403...>
⚠️ Google Sheets not available. Using sample data.
```

**After Fix:**
```
✅ Connected to Google Sheets: Product Metrics loaded
✅ Real data loaded from Google Sheets
```

## 🆘 **Still Having Issues?**

If you're still seeing errors after sharing:

1. **Double-check the email**: `mrunalinee-patole@spicemoney-dwh.iam.gserviceaccount.com`
2. **Verify permission level**: Should be "Viewer" (not "Editor")
3. **Wait longer**: Sometimes takes up to 2 minutes for permissions to propagate
4. **Check sheet URL**: Make sure you're sharing the correct sheet
5. **Test locally**: Run `python test_google_sheets_access.py` to verify

## 📞 **Need Help?**

If you continue to have issues:
1. Run the test script: `python test_google_sheets_access.py`
2. Check the output for specific error messages
3. Verify all sheets are shared with the service account
4. Ensure the service account has "Viewer" access (not "Editor")

---

**🎯 Goal**: Get your product metrics tile working on the deployed Streamlit app with real Google Sheets data instead of sample data.
