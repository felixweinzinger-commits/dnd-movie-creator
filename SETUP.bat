@echo off
REM D&D Movie Generator - Master Setup Script
REM This handles everything: directory changes, venv creation, package installation

REM ====== CRITICAL: Change to script directory ======
cd /d "%~dp0"

if errorlevel 1 (
    echo ERROR: Failed to change to project directory
    echo Expected: C:\Users\admin\Projects\dnd-movie-generator
    echo Got: %cd%
    pause
    exit /b 1
)

echo.
echo ========================================
echo  D&D Movie Generator - Setup
echo ========================================
echo.
echo Project location: %cd%
echo.

REM Verify we're in the right place
if not exist "app.py" (
    echo ERROR: app.py not found!
    echo Current directory: %cd%
    echo.
    echo This script must be run from the project directory:
    echo C:\Users\admin\Projects\dnd-movie-generator
    echo.
    echo Please ensure you're running this from the correct location.
    pause
    exit /b 1
)

echo Verified: Project files found
echo.

REM Check Python
echo Checking Python...
python --version
if errorlevel 1 (
    echo ERROR: Python not found!
    echo Please install Python 3.11+ from python.org
    pause
    exit /b 1
)

echo Python found: OK
echo.

REM Create venv
echo Creating virtual environment...
if exist "venv" (
    echo Virtual environment already exists
) else (
    python -m venv venv
    if errorlevel 1 (
        echo ERROR: Failed to create venv
        pause
        exit /b 1
    )
    echo Virtual environment created: OK
)

echo.

REM Activate venv
echo Activating virtual environment...
call venv\Scripts\activate.bat
if errorlevel 1 (
    echo ERROR: Failed to activate venv
    pause
    exit /b 1
)

echo Virtual environment activated: OK
echo.

REM Upgrade pip
echo Upgrading pip, setuptools, wheel...
python -m pip install --upgrade pip setuptools wheel
if errorlevel 1 (
    echo WARNING: pip upgrade had issues, continuing anyway
)

echo.

REM Install core packages
echo Installing core packages...
pip install streamlit==1.28.1 pydantic==2.5.0 python-dotenv==1.0.0 requests==2.31.0
if errorlevel 1 (
    echo ERROR: Failed to install core packages
    pause
    exit /b 1
)

echo Core packages installed: OK
echo.

REM Install Pillow
echo Installing Pillow (image processing)...
pip install --only-binary :all: Pillow
if errorlevel 1 (
    echo WARNING: Pillow binary unavailable, trying generic
    pip install Pillow>=10.0.0
)

echo.

REM Install other packages
echo Installing additional packages...
pip install opencv-python
if errorlevel 1 (
    echo WARNING: opencv-python failed
)

pip install numpy
if errorlevel 1 (
    echo WARNING: numpy failed
)

echo.
echo Attempting to install packages that may require C compiler...
echo (Visual Studio detected - will try to build)
echo.

REM Try scipy (requires compiler)
echo Installing scipy...
pip install scipy>=1.11.0
if errorlevel 1 (
    echo WARNING: scipy failed (optional, app will work without it)
)

echo.

REM Try PyTorch (requires compiler)
echo Installing PyTorch (this may take a minute)...
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
if errorlevel 1 (
    echo WARNING: PyTorch failed (optional, app will work without it)
)

echo.

REM Try AI/ML packages (requires compiler)
echo Installing AI/ML packages...
pip install transformers diffusers accelerate safetensors
if errorlevel 1 (
    echo WARNING: Some AI packages failed (optional, app will work without them)
)

echo.

REM Install video/audio
echo Installing video/audio packages...
pip install moviepy ffmpeg-python elevenlabs
if errorlevel 1 (
    echo WARNING: Some media packages failed, continuing
)

echo.

REM Create directories
echo Creating output directories...
if not exist "output\images" mkdir output\images
if not exist "output\videos" mkdir output\videos
if not exist "output\audio" mkdir output\audio
if not exist "output\temp" mkdir output\temp

echo Directories created: OK
echo.

REM Create .env
echo Creating configuration file...
if not exist ".env" (
    copy .env.example .env
    echo Configuration file created: OK
) else (
    echo Configuration file already exists
)

echo.

REM Summary
echo ========================================
echo  Setup Complete!
echo ========================================
echo.
echo Project directory: %cd%
echo Virtual environment: %cd%\venv
echo Configuration file: %cd%\.env
echo.
echo Next steps:
echo.
echo 1. Run the app:
echo    run_simple.bat
echo.
echo 2. Or manually:
echo    call venv\Scripts\activate.bat
echo    streamlit run app.py
echo.
echo 3. Open browser to:
echo    http://localhost:8501
echo.
echo Optional: Edit .env to add your API keys
echo.
pause
