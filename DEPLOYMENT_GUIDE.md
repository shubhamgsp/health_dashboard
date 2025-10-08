# 🚀 AEPS Health Dashboard with Bugs Tracking - Deployment Guide

## 📋 **Deployment Options**

### **Option 1: Streamlit Cloud (Recommended) ⭐**

**✅ What I've Done:**
- Created deployment-ready files
- Set up proper configuration
- Added security features
- Created deployment helper script

**📋 What You Need to Do:**

#### **Step 1: GitHub Repository**
```bash
# Navigate to the deployment folder
cd aeps_health_dashboard_with_bugs

# Initialize git repository
git init
git add .
git commit -m "Initial commit: AEPS Health Dashboard with Bugs Tracking"

# Create repository on GitHub (go to https://github.com/new)
# Name: aeps-health-dashboard-bugs
# Make it private

# Connect to GitHub
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/aeps-health-dashboard-bugs.git
git push -u origin main
```

#### **Step 2: Deploy to Streamlit Cloud**
1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with GitHub
3. Click "New app"
4. Configure:
   - **Repository:** `YOUR_USERNAME/aeps-health-dashboard-bugs`
   - **Branch:** `main`
   - **Main file:** `aeps_health_dashboard.py`
   - **App URL:** `aeps-health-dashboard-bugs`
5. Click "Deploy app"

#### **Step 3: Configure Secrets**
1. Go to app settings → "Secrets"
2. Add:
```toml
[secrets]
DASHBOARD_PASSWORD = "your-secure-password-here"
GOOGLE_CREDENTIALS_PATH = "spicemoney-dwh.json"
```

#### **Step 4: Test Your Deployment**
- Access: `https://aeps-health-dashboard-bugs.streamlit.app`
- Login with your password
- Test bugs dashboard by clicking "Bugs" tile

---

### **Option 2: Internal Server Deployment**

**✅ What I've Done:**
- Created Docker configuration
- Set up docker-compose
- Added health checks

**📋 What You Need to Do:**

#### **Step 1: Server Setup**
```bash
# Copy files to your server
scp -r aeps_health_dashboard_with_bugs/ user@your-server:/opt/

# SSH to your server
ssh user@your-server
cd /opt/aeps_health_dashboard_with_bugs
```

#### **Step 2: Docker Deployment**
```bash
# Install Docker (if not installed)
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh

# Build and run
docker-compose up -d

# Check status
docker-compose ps
```

#### **Step 3: Configure Access**
- **Internal URL:** `http://your-server-ip:8501`
- **Domain:** `http://aeps-dashboard.your-company.com` (if you have DNS)

---

### **Option 3: Cloud Deployment (AWS/GCP/Azure)**

**✅ What I've Done:**
- Created Dockerfile
- Set up proper configuration
- Added health checks

**📋 What You Need to Do:**

#### **For Google Cloud Run:**
```bash
# Install gcloud CLI
# Configure your project
gcloud config set project YOUR_PROJECT_ID

# Deploy to Cloud Run
gcloud run deploy aeps-dashboard \
  --source . \
  --platform managed \
  --region asia-south1 \
  --allow-unauthenticated \
  --port 8501
```

#### **For AWS ECS:**
```bash
# Build and push to ECR
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin YOUR_ACCOUNT.dkr.ecr.us-east-1.amazonaws.com
docker build -t aeps-dashboard .
docker tag aeps-dashboard:latest YOUR_ACCOUNT.dkr.ecr.us-east-1.amazonaws.com/aeps-dashboard:latest
docker push YOUR_ACCOUNT.dkr.ecr.us-east-1.amazonaws.com/aeps-dashboard:latest
```

---

## 🔐 **Security Configuration**

### **Authentication**
The dashboard includes password protection. Set your password in:
- **Streamlit Cloud:** Environment variables
- **Docker:** Environment variables
- **Local:** Modify the code

### **Access Control**
```python
# Add IP whitelisting (optional)
ALLOWED_IPS = ['192.168.1.0/24', '10.0.0.0/8']

def check_ip_access():
    # Implement IP checking logic
    pass
```

### **Credentials Management**
- Store `spicemoney-dwh.json` securely
- Use environment variables for sensitive data
- Rotate credentials regularly

---

## 📊 **Bugs Data Management**

### **CSV File (Default)**
- File: `bugs_data.csv`
- Format: S.No, Statement, Product, Mode, status
- Update: Replace file and redeploy

### **Google Sheets Integration**
- Configure in the dashboard code
- Update Google Sheet URL if needed
- Ensure proper sharing permissions

### **Data Updates**
- **CSV:** Replace file and redeploy
- **Google Sheets:** Real-time updates
- **Both:** Automatic fallback system

---

## 🔧 **Troubleshooting**

### **Common Issues**

#### **1. Data Not Loading**
```bash
# Check credentials
ls -la spicemoney-dwh.json

# Check network access
curl -I https://bigquery.googleapis.com
```

#### **2. Bugs Dashboard Not Working**
```bash
# Check CSV file
ls -la bugs_data.csv
head -5 bugs_data.csv

# Check file permissions
chmod 644 bugs_data.csv
```

#### **3. Authentication Issues**
- Verify password in environment variables
- Check secrets configuration
- Clear browser cache

### **Logs and Monitoring**

#### **Streamlit Cloud:**
- Check app logs in Streamlit Cloud dashboard
- Monitor usage and errors

#### **Docker:**
```bash
# View logs
docker-compose logs -f

# Check container status
docker-compose ps
```

#### **Local Development:**
```bash
# Run with debug mode
streamlit run aeps_health_dashboard.py --logger.level debug
```

---

## 📈 **Performance Optimization**

### **Caching**
- Data is cached for 5 minutes
- Clear cache: Click "Refresh Data" button
- Force refresh: Restart application

### **Scaling**
- **Streamlit Cloud:** Automatic scaling
- **Docker:** Scale with docker-compose
- **Cloud:** Configure auto-scaling

### **Monitoring**
- Set up health checks
- Monitor resource usage
- Track user access

---

## 🔄 **Updates and Maintenance**

### **Code Updates**
```bash
# Update code
git add .
git commit -m "Update dashboard features"
git push origin main

# Streamlit Cloud will auto-deploy
```

### **Data Updates**
- **CSV:** Replace file and redeploy
- **Google Sheets:** Automatic updates
- **BigQuery:** Real-time data

### **Security Updates**
- Update dependencies regularly
- Rotate credentials
- Monitor access logs

---

## 📞 **Support and Help**

### **Documentation**
- README.md - General information
- This guide - Deployment instructions
- Code comments - Technical details

### **Common Commands**
```bash
# Local development
streamlit run aeps_health_dashboard.py

# Docker deployment
docker-compose up -d

# Check status
docker-compose ps

# View logs
docker-compose logs -f
```

### **Getting Help**
1. Check the logs for error messages
2. Verify all files are present
3. Test with sample data first
4. Contact support team if needed

---

## 🎯 **Next Steps After Deployment**

1. **Test all features** - Health metrics, bugs tracking, exports
2. **Share with team** - Provide URL and credentials
3. **Set up monitoring** - Track usage and performance
4. **Plan updates** - Schedule regular maintenance
5. **Gather feedback** - Improve based on user input

**Your AEPS Health Dashboard with Bugs Tracking is ready for production! 🎉**
