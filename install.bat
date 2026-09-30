@echo off
REM D&D Movie Generator - Installation Script
REM This script handles the Pillow build issue on Windows

REM CRITICAL: Change to script directory first!
cd /d "%~dp0"

echo.
echo ========================================
echo  D&D Movie Generator - Installation
echo ========================================
echo.
echo Working directory: %cd%
echo.
pause

REM Check Python version
python --version
if errorlevel 1 (
    echo ERROR: Python not found in PATH
    echo Please install Python 3.11+ and add to PATH
    pause
    exit /b 1
)

REM Create virtual environment
echo.
echo Creating virtual environment...
python -m venv venv
if errorlevel 1 (
    echo ERROR: Failed to create virtual environment
    pause
    exit /b 1
)

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Upgrade pip (critical for Windows builds)
echo.
echo Upgrading pip, setuptools, wheel...
python -m pip install --upgrade pip setuptools wheel
if errorlevel 1 (
    echo WARNING: Failed to upgrade pip
)

REM Install pre-built wheels (no build needed)
echo.
echo Installing core dependencies...
pip install streamlit==1.28.1 pydantic==2.5.0 python-dotenv==1.0.0 requests==2.31.0
if errorlevel 1 (
    echo ERROR: Failed to install core dependencies
    pause
    exit /b 1
)

REM Install Pillow with pre-built wheel
echo.
echo Installing Pillow (image processing)...
pip install --only-binary :all: Pillow
if errorlevel 1 (
    echo WARNING: Pillow binary not available, trying generic install...
    pip install Pillow>=10.0.0
)

REM Install OpenCV
echo.
echo Installing OpenCV...
pip install opencv-python>=4.8.0
if errorlevel 1 (
    echo ERROR: Failed to install OpenCV
)

REM Install numerical packages
echo.
echo Installing numerical packages...
pip install numpy scipy
if errorlevel 1 (
    echo ERROR: Failed to install numpy/scipy
)

REM Install PyTorch (CPU version is smaller)
echo.
echo Installing PyTorch (CPU version - this may take a minute)...
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
if errorlevel 1 (
    echo ERROR: Failed to install PyTorch
    pause
    exit /b 1
)

REM Install transformers and diffusion
echo.
echo Installing AI/ML packages...
pip install transformers diffusers accelerate safetensors
if errorlevel 1 (
    echo WARNING: Some AI packages failed to install
)

REM Install video/audio
echo.
echo Installing video/audio packages...
pip install moviepy ffmpeg-python
if errorlevel 1 (
    echo WARNING: Some video packages failed
)

REM Install API clients
echo.
echo Installing API clients...
pip install elevenlabs
if errorlevel 1 (
    echo WARNING: ElevenLabs failed to install
)

REM Create .env file if it doesn't exist
if not exist ".env" (
    echo.
    echo Creating .env configuration file...
    copy .env.example .env
    echo Configuration file created!
)

REM Create output directory
if not exist "output" (
    mkdir output
    mkdir output\images
    mkdir output\videos
    mkdir output\audio
    mkdir output\temp
)

echo.
echo ========================================
echo  Installation Complete!
echo ========================================
echo.
echo Next steps:
echo 1. Start the app with: run.bat
echo 2. Or manually: streamlit run app.py
echo.
echo Optional: Edit .env with your API keys
echo.
pause
