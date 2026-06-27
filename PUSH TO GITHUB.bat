@echo off
title Push to GitHub
cd /d "%~dp0"

echo.
echo  ============================================
echo   PUSH SPEED-SHIPPING TO GITHUB
echo  ============================================
echo.
echo  On GitHub, open your new repo and click the green "Code" button.
echo  Copy the HTTPS link (example):
echo    https://github.com/Rendolf/speed-shipping-company.git
echo.
set /p REPO_URL="Paste your repo URL here: "

if "%REPO_URL%"=="" (
    echo  ERROR: No URL entered.
    pause
    exit /b 1
)

git remote remove origin 2>nul
git remote add origin "%REPO_URL%"
echo.
echo  Remote set to: %REPO_URL%
echo  Pushing to GitHub...
echo  (Sign in if Windows or GitHub asks.)
echo.

git push -u origin main

if errorlevel 1 (
    echo.
    echo  PUSH FAILED.
    echo  - Check the repo URL is correct
    echo  - Make sure the repo exists on GitHub
    echo  - Use a Personal Access Token if asked for a password
    echo    GitHub - Settings - Developer settings - Personal access tokens
    echo.
    pause
    exit /b 1
)

echo.
echo  SUCCESS! Code is on GitHub.
echo  Next: go to https://render.com - New Blueprint - connect this repo.
echo.
pause
