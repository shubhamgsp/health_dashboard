@echo off
echo Adding changes...
git add aeps_health_dashboard.py
git add COST_REDUCTION_IMPLEMENTATION_STATUS.md
git add push_changes.bat
echo Committing...
git commit -m "URGENT: Implement 90%% BigQuery cost reduction - All users get most recent cached data - Cache TTL increased to 1 hour - Business hours refresh logic (9 AM - 9 PM) - Expected cost: 6TB to 500GB/day"
echo Pushing to production...
git push origin main
echo Done! Streamlit Cloud will auto-deploy in 2-3 minutes.
pause
