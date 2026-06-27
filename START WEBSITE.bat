@echo off



title Speed-Shipping and Security Company



cd /d "%~dp0"







echo.



echo  ============================================



echo   SPEED-SHIPPING AND SECURITY COMPANY



echo  ============================================



echo.



echo  IMPORTANT - HOW TO VIEW THE SITE:



echo  ---------------------------------



echo  1. Keep THIS window OPEN the whole time.



echo     (If you close it, the site stops — "connection refused")



echo  2. Use ONLY the link shown below (port 5080).



echo  3. Do NOT use old links on port 5000 or 5050.



echo  4. Press Ctrl+F5 in the browser after starting.



echo.



echo  Static folder = CSS, images, JavaScript only.



echo  Pages are built by Python/Flask when you run this file.



echo.



echo  Officer panel login: Rendolf_001



echo.







set "PYCMD="



where py >nul 2>&1 && set "PYCMD=py"



if not defined PYCMD where python >nul 2>&1 && set "PYCMD=python"







if not defined PYCMD (



    echo  ERROR: Python was not found on this computer.



    echo  Install Python from https://www.python.org/downloads/



    echo  During install, tick "Add Python to PATH".



    echo.



    pause



    exit /b 1



)







echo  Using: %PYCMD%



echo  Installing dependencies...



%PYCMD% -m pip install -r requirements.txt -q 2>nul



set FLASK_LOCAL=1







echo  Stopping any old servers on ports 5000, 5050, 5080...



for /f "tokens=5" %%a in ('netstat -ano ^| findstr ":5000" ^| findstr "LISTENING"') do taskkill /F /PID %%a >nul 2>&1



for /f "tokens=5" %%a in ('netstat -ano ^| findstr ":5050" ^| findstr "LISTENING"') do taskkill /F /PID %%a >nul 2>&1



for /f "tokens=5" %%a in ('netstat -ano ^| findstr ":5080" ^| findstr "LISTENING"') do taskkill /F /PID %%a >nul 2>&1



timeout /t 2 /nobreak >nul







echo.



echo  Server starting...



echo  Homepage:  http://127.0.0.1:5080



echo  *** USE THIS LINK ONLY (port 5080) ***



echo  Tracking:  http://127.0.0.1:5080/track?code=SS3409536472



echo.



echo  Do NOT use port 5000 or 5050 - old links will not show your ledger.



echo.



start /MIN cmd /c "timeout /t 4 /nobreak >nul && start "" "http://127.0.0.1:5080/track?code=SS3409536472""



echo  Browser will open automatically in a few seconds.



echo.



%PYCMD% app.py







if errorlevel 1 (



    echo.



    echo  ERROR: The server stopped unexpectedly.



    echo  Read any error message above, then press a key to close.



    pause



)



