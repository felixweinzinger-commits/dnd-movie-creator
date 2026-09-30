@echo off
REM D&D Movie Generator - Run Script (Improved)

REM CRITICAL: Change to script directory first!
cd /d "%~dp0"

echo.
echo ========================================
echo  D&D Transcript to Movie Generator
echo ========================================
echo.
echo Working directory: %cd%
echo.

REM Check if venv exists, if not run installer
if not exist "venv" (
    echo Virtual environment not found!
    echo Running installer...
    call install.bat
    if errorlevel 1 (
        echo Installation failed. Please run: install.bat
        pause
        exit /b 1
    )
)

REM Activate virtual environment
call venv\Scripts\activate.bat
if errorlevel 1 (
    echo ERROR: Failed to activate virtual environment
    pause
    exit /b 1
)

REM Check if Streamlit is installed
pip show streamlit > nul 2>&1
if errorlevel 1 (
    echo Streamlit not found. Installing dependencies...
    pip install streamlit pydantic python-dotenv requests
    if errorlevel 1 (
        echo ERROR: Failed to install dependencies
        pause
        exit /b 1
    )
)

REM Check if .env exists
if not exist ".env" (
    echo Creating .env from template...
    copy .env.example .env
    echo.
    echo Configuration file created at: .env
    echo You can optionally add API keys for better results.
)

REM Create output directory if needed
if not exist "output" (
    mkdir output
    mkdir output\images
    mkdir output\videos
    mkdir output\audio
    mkdir output\temp
)

REM Start Streamlit app
echo.
echo ========================================
echo  Starting Streamlit Application
echo ========================================
echo.
echo Browser will open at: http://localhost:8501
echo.
echo Press Ctrl+C to stop the server
echo.

streamlit run app.py

pause
