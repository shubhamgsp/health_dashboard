# 🐛 Active Bugs - Google Sheets Integration

## ✅ What Changed

**Active Bugs** now reads from **Google Sheets** instead of CSV for real-time updates!

### Before:
- ❌ Read from `bugs_data.csv` (static file)
- ❌ Required code redeployment to update
- ❌ No real-time updates

### After:
- ✅ Reads from **Google Sheets** (live data)
- ✅ Updates automatically when you change the sheet
- ✅ CSV as fallback for local development

---

## 📋 Google Sheets Setup

### Step 1: Create or Use Existing Bugs Sheet

You need to add a **"Bugs"** tab to your existing Google Sheets or create a new one with this structure:

**Required Columns:**
- `S.No` - Bug number/ID
- `Statement` - Bug description
- `Product` - Product affected (AEPS, BBPS, etc.)
- `Mode` - Platform (App, Web, App/Web)
- `status` - Bug status (see below)

**Status Values:**
- `open` - Bug is open and needs attention
- `pending` - Bug is pending investigation
- `wip` - Work in progress
- `Fixed` - Bug is resolved
- `Closed` - Bug is closed

---

### Step 2: Add to Your Existing Google Sheet

**Option A: Add to existing sheet** (Recommended)

If you're using the same sheet as your other data:
```
Sheet URL: https://docs.google.com/spreadsheets/d/1XyTNR14JlkM_7uHEeoQa68mLgeiAZTaCq9vR-VCff4o
```

1. Open the sheet
2. Create a new tab called **"Bugs"**
3. Add the column headers: S.No, Statement, Product, Mode, status
4. Copy your data from `bugs_data.csv` or enter new bugs

**Option B: Use a different sheet**

If you want a separate bugs tracking sheet, update the code to use the correct URL (let me know and I can help).

---

### Step 3: Share with Service Account

**IMPORTANT:** Share your Google Sheet with the service account:

1. Open your Bugs Google Sheet
2. Click **Share** (top right)
3. Add this email with **Editor** access:
   ```
   mrunalinee-patole@spicemoney-dwh.iam.gserviceaccount.com
   ```
4. Click **Send**

**Why Editor?** If you want to allow the dashboard to update the sheet in the future (e.g., auto-close bugs), give Editor access. For now, Viewer is sufficient.

---

## 📊 How Active Bugs Metric Works

### Calculation Logic:

```python
Active Bugs = Count of bugs where status is:
  - 'open'
  - 'pending'
  - 'wip'

Fixed/Closed bugs are NOT counted.
```

### Status Colors:

| Bug Count | Dashboard Status | Color |
|-----------|-----------------|-------|
| 0-2 bugs | Green | ✅ Good |
| 3-5 bugs | Yellow | ⚠️ Warning |
| 6+ bugs | Red | 🔴 Critical |

---

## 🔄 How It Updates

### Real-Time Updates:
1. You update the Google Sheet (add/change bug status)
2. Dashboard refreshes (every 5 minutes by cache)
3. New bug count appears automatically

### Cache Duration:
- **5 minutes** - Data is cached to avoid excessive API calls
- To force refresh: Wait 5 minutes or restart the app

---

## 📝 Example Sheet Structure

| S.No | Statement | Product | Mode | status |
|------|-----------|---------|------|--------|
| 1 | AEPS scanner not working | AEPS | App | open |
| 2 | Login button slow | Platform | Web | wip |
| 3 | Receipt missing bank name | AEPS | App/Web | pending |
| 4 | Dashboard blank on load | AEPS | App | Fixed |
| 5 | Voice stripe confusion | AEPS | App | open |

**Active Bugs Count:** 3 (open, wip, pending)  
**Dashboard Status:** Yellow ⚠️

---

## 🎯 Benefits of Google Sheets Integration

✅ **Real-Time Updates** - Change the sheet, dashboard updates automatically  
✅ **No Code Changes** - Update bugs without redeploying  
✅ **Collaborative** - Multiple team members can update  
✅ **Version History** - Google Sheets tracks all changes  
✅ **Easy Editing** - Familiar spreadsheet interface  
✅ **Fallback Safety** - Uses CSV if sheets unavailable  

---

## 🔍 Troubleshooting

### Issue: "Active Bugs" still shows dummy data (value: 2)

**Solution:**
1. ✅ Ensure the sheet tab is named exactly **"Bugs"** (case-sensitive)
2. ✅ Share the sheet with: `mrunalinee-patole@spicemoney-dwh.iam.gserviceaccount.com`
3. ✅ Check column names match: `status` (lowercase)
4. ✅ Wait 5 minutes for cache to refresh
5. ✅ Hard refresh browser (Ctrl+F5)

### Issue: Shows "0 bugs" when there are bugs in the sheet

**Solution:**
- Check that status values are exactly: `open`, `pending`, or `wip` (lowercase)
- The code is case-insensitive, but make sure there are no extra spaces
- Example: `"open "` won't work, but `"open"` will

### Issue: Google Sheets access error

**Solution:**
1. Verify service account email is added to sheet
2. Check that the sheet is not set to "View Only"
3. Ensure the Bugs tab exists in the sheet

---

## 📚 Current Data Source Priority

The dashboard tries to fetch bugs in this order:

1. **Google Sheets** (Primary) - Tab name: "Bugs"
   ```
   Sheet: https://docs.google.com/spreadsheets/d/1XyTNR14JlkM_7uHEeoQa68mLgeiAZTaCq9vR-VCff4o
   ```

2. **CSV File** (Fallback) - For local development
   ```
   File: bugs_data.csv
   ```

3. **Dummy Data** (Last Resort) - If both fail
   ```
   Value: 2 bugs (green status)
   ```

---

## 🚀 Deployment Status

✅ **Code Updated** - Now reads from Google Sheets first  
✅ **Auto-Deploying** - Changes pushed to Streamlit Cloud  
⏰ **Wait 1-2 minutes** for deployment  

---

## ✨ Next Steps

1. ⏰ **Wait for deployment** (1-2 minutes)
2. 📝 **Create "Bugs" tab** in your Google Sheet
3. 🔑 **Share with service account** email
4. 📊 **Add your bugs data** to the sheet
5. 🔄 **Refresh dashboard** - See real-time bug count!

---

## 💡 Future Enhancements (Optional)

Want more features? I can add:

- 📈 **Bug Trends** - Track bugs over time
- 🏷️ **By Product** - Show breakdown by AEPS, BBPS, etc.
- 📅 **By Priority** - Add priority column (High, Medium, Low)
- ⏰ **Age Tracking** - How long bugs have been open
- 🔔 **Alerts** - Notification when bugs exceed threshold

Just let me know! 🚀

