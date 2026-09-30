@echo off
REM D&D Movie Generator - Simple Run Script
REM This script properly activates venv and runs Streamlit

REM CRITICAL: Change to script directory first!
cd /d "%~dp0"

echo.
echo ========================================
echo  D&D Transcript to Movie Generator
echo ========================================
echo.

setlocal enabledelayedexpansion

REM Check if venv exists
if not exist "venv" (
    echo.
    echo ERROR: Virtual environment not found!
    echo.
    echo Please run install.bat first:
    echo   install.bat
    echo.
    pause
    exit /b 1
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Verify Streamlit is installed
python -m pip show streamlit > nul 2>&1
if errorlevel 1 (
    echo.
    echo ERROR: Streamlit not installed!
    echo.
    echo Running minimal install...
    python -m pip install streamlit pydantic python-dotenv requests
    if errorlevel 1 (
        echo.
        echo Failed to install Streamlit
        echo Please check your internet connection
        pause
        exit /b 1
    )
)

REM Create output directories if needed
if not exist "output\images" mkdir output\images
if not exist "output\videos" mkdir output\videos
if not exist "output\audio" mkdir output\audio
if not exist "output\temp" mkdir output\temp

REM Create .env if needed
if not exist ".env" (
    copy .env.example .env
)

REM Display info
echo.
echo ========================================
echo  Starting Streamlit Application
echo ========================================
echo.
echo URL: http://localhost:8501
echo.
echo To stop: Press Ctrl+C
echo.

REM Run Streamlit with debug output
echo.
echo Launching app (this may take 10-30 seconds)...
echo.

REM Try to run Streamlit
python -m streamlit run app.py --logger.level=debug

REM If that failed, show error
if errorlevel 1 (
    echo.
    echo ========================================
    echo  ERROR: Streamlit failed to start
    echo ========================================
    echo.
    echo Troubleshooting:
    echo.
    echo 1. Check internet connection
    echo 2. Check if port 8501 is available
    echo 3. Try: streamlit run app.py --server.port 8502
    echo 4. Check installed packages: pip list
    echo.
    pause
    exit /b 1
)

pause
