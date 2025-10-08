@echo off
echo 🚀 AEPS Health Dashboard with Bugs Tracking - Quick Deploy
echo ============================================================

echo.
echo 📋 DEPLOYMENT OPTIONS:
echo.
echo 1. Streamlit Cloud (Recommended - Free, Easy)
echo 2. Local Docker Deployment
echo 3. Internal Server Deployment
echo.

set /p choice="Choose deployment option (1-3): "

if "%choice%"=="1" (
    echo.
    echo 🌐 STREAMLIT CLOUD DEPLOYMENT
    echo =============================
    echo.
    echo 📋 What you need to do:
    echo 1. Create GitHub repository: aeps-health-dashboard-bugs
    echo 2. Push this code to GitHub
    echo 3. Deploy via share.streamlit.io
    echo.
    echo 🔗 Run the deployment helper:
    python deploy_to_streamlit.py
    echo.
    pause
) else if "%choice%"=="2" (
    echo.
    echo 🐳 DOCKER DEPLOYMENT
    echo ====================
    echo.
    echo Building Docker image...
    docker build -t aeps-dashboard .
    
    echo.
    echo Starting container...
    docker run -d -p 8501:8501 --name aeps-dashboard aeps-dashboard
    
    echo.
    echo ✅ Dashboard running at: http://localhost:8501
    echo.
    echo To stop: docker stop aeps-dashboard
    echo To remove: docker rm aeps-dashboard
    echo.
    pause
) else if "%choice%"=="3" (
    echo.
    echo 🖥️ INTERNAL SERVER DEPLOYMENT
    echo ==============================
    echo.
    echo 📋 Manual steps required:
    echo 1. Copy files to your server
    echo 2. Install Docker on server
    echo 3. Run: docker-compose up -d
    echo.
    echo 📖 See DEPLOYMENT_GUIDE.md for detailed instructions
    echo.
    pause
) else (
    echo ❌ Invalid choice. Please run the script again.
    pause
)

echo.
echo 🎉 Deployment setup complete!
echo.
echo 📖 For detailed instructions, see DEPLOYMENT_GUIDE.md
echo 📞 Need help? Check the README.md file
echo.
pause
