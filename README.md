# 🏥 AEPS Health Monitor Dashboard with Bugs Tracking

## 📊 **Overview**
A comprehensive health monitoring dashboard for AEPS (Aadhaar Enabled Payment System) with integrated bugs tracking functionality.

## ✨ **Features**

### **Core Health Metrics**
- Transaction Success Rate monitoring
- 2FA Success Rate tracking
- GTV Performance analytics
- Login Success Rate monitoring
- Bot Analytics and fraud detection
- RFM Score analysis

### **Bugs Tracking System** 🐛
- **Real-time bugs monitoring** from Google Sheets/CSV
- **Interactive bugs dashboard** with filtering and analytics
- **Product-wise bug breakdown** (Aeps, Platform Exp, Matm, Dmt, Inventory)
- **Status tracking** (Fixed, Open, Pending, WIP)
- **Export functionality** for bug reports
- **Trend analysis** and fix rate calculations

### **Advanced Analytics**
- Churn analysis and user retention
- Geographic analysis
- Bank error analysis
- Cash product performance
- Distributor analytics

## 🚀 **Quick Start**

### **Local Development**
```bash
# Install dependencies
pip install -r requirements.txt

# Run the dashboard
streamlit run aeps_health_dashboard.py --server.port 8501
```

### **Access the Dashboard**
- **Main Dashboard:** http://localhost:8501
- **Bugs Dashboard:** Click the "Bugs" tile in Operations section

## 📁 **File Structure**
```
aeps_health_dashboard_with_bugs/
├── aeps_health_dashboard.py      # Main dashboard application
├── bugs_data.csv                 # Bugs data file
├── requirements.txt              # Python dependencies
├── README.md                     # This file
├── .streamlit/
│   └── config.toml              # Streamlit configuration
├── .gitignore                   # Git ignore rules
└── deploy_to_streamlit.py       # Deployment helper
```

## 🔧 **Configuration**

### **Data Sources**
1. **BigQuery Integration** - Real-time transaction data
2. **Google Sheets** - Bugs tracking data
3. **CSV Fallback** - Local bugs data file

### **Environment Variables**
```bash
# For production deployment
DASHBOARD_PASSWORD=your-secure-password
GOOGLE_CREDENTIALS_PATH=spicemoney-dwh.json
```

## 🚀 **Deployment Options**

### **Option 1: Streamlit Cloud (Recommended)**
1. Push to GitHub repository
2. Deploy via [share.streamlit.io](https://share.streamlit.io)
3. Configure environment variables
4. Access your live dashboard

### **Option 2: Internal Server**
```bash
streamlit run aeps_health_dashboard.py --server.port 8501 --server.address 0.0.0.0
```

### **Option 3: Docker Deployment**
```bash
docker build -t aeps-dashboard .
docker run -p 8501:8501 aeps-dashboard
```

## 🔐 **Security Features**
- Password authentication
- IP whitelisting (optional)
- Secure credential management
- Access logging

## 📊 **Bugs Tracking Usage**

### **Adding New Bugs**
1. Update the `bugs_data.csv` file
2. Or update the Google Sheet directly
3. Dashboard automatically reflects changes

### **Bugs Dashboard Features**
- **Filter by Product:** Aeps, Platform Exp, Matm, Dmt, Inventory
- **Filter by Status:** Fixed, Open, Pending, WIP
- **Export Data:** Download filtered results as CSV
- **Analytics:** Charts and trend analysis

## 🛠️ **Troubleshooting**

### **Common Issues**
1. **Data not loading:** Check credentials and network access
2. **Bugs not showing:** Verify CSV file format and location
3. **Authentication issues:** Check password configuration

### **Support**
- Check the logs in Streamlit Cloud
- Verify all dependencies are installed
- Ensure data sources are accessible

## 📈 **Performance**
- **Caching:** 5-minute cache for data refresh
- **Optimization:** Efficient data processing
- **Scalability:** Handles large datasets

## 🔄 **Updates**
- **Automatic deployment** from GitHub
- **Version control** for all changes
- **Rollback capability** if needed

## 📞 **Support**
For technical support or feature requests, contact the development team.

---
**Built with ❤️ for AEPS Health Monitoring**
