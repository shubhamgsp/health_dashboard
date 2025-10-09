@echo off
echo Pushing cost reduction changes to production...
git push origin main
if %errorlevel% neq 0 (
    echo Push failed, trying pull first...
    git pull --rebase origin main
    git push origin main
)
echo Done!
pause

