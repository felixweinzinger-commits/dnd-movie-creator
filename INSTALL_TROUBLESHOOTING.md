# Installation Troubleshooting Guide

## Error: "Getting requirements to build wheel did not run successfully"

This is a common Windows issue with Pillow trying to build from source.

### Quick Fix

Use the improved installation script:

```bash
install.bat
```

This script:
- ✅ Upgrades pip/setuptools/wheel first
- ✅ Installs pre-built binary wheels
- ✅ Handles Pillow specially
- ✅ Uses CPU-friendly PyTorch
- ✅ Creates all necessary directories

### Manual Installation (If script fails)

```bash
# 1. Navigate to project
cd C:\Users\admin\Projects\dnd-movie-generator

# 2. Create environment
python -m venv venv
venv\Scripts\activate.bat

# 3. Upgrade tools FIRST
python -m pip install --upgrade pip setuptools wheel

# 4. Install core only
pip install streamlit pydantic python-dotenv requests

# 5. Install Pillow with pre-built wheels
pip install --only-binary :all: Pillow

# 6. Install other packages
pip install opencv-python numpy scipy

# 7. Install PyTorch (CPU version)
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu

# 8. Install AI packages
pip install transformers diffusers accelerate safetensors

# 9. Install video packages
pip install moviepy ffmpeg-python

# 10. Install API clients
pip install elevenlabs

# 11. Create config
copy .env.example .env

# 12. Run app
streamlit run app.py
```

## Common Installation Issues

### "Python not found"
```bash
# Check if Python is installed
python --version

# If not, install from python.org
# Make sure to add Python to PATH during installation
```

### "FFmpeg not found" (optional, needed only for final assembly)
```bash
# Install via chocolatey (Windows package manager)
choco install ffmpeg

# Or manually:
# 1. Download from https://ffmpeg.org/download.html
# 2. Extract to C:\ffmpeg
# 3. Add C:\ffmpeg\bin to PATH
```

### "Module not found" errors
```bash
# Make sure venv is activated
venv\Scripts\activate.bat

# Then reinstall
pip install --upgrade -r requirements.txt
```

### Out of disk space
The installation needs about 2-3 GB:
- PyTorch: ~1 GB
- Other packages: ~500 MB
- Project files: ~100 MB

Free up space and try again.

### Pillow still failing to build

Try installing a specific pre-built version:

```bash
# Using pre-built wheel directly
pip install Pillow --only-binary :all: --upgrade

# Or specific version
pip install --only-binary :all: Pillow==10.0.0
```

### PyTorch taking too long

CPU version (default) is large (~500 MB). Wait or:

```bash
# Skip PyTorch initially
pip install --no-deps transformers diffusers

# Install PyTorch later
pip install torch
```

### "KeyError: '__version__'" 

This specific error means an old package is corrupting the build. Fix:

```bash
# Clear pip cache
pip cache purge

# Clear build cache
rmdir /s "%TEMP%\pip-build-*"

# Upgrade everything
python -m pip install --upgrade pip setuptools wheel

# Retry installation
pip install --only-binary :all: Pillow
```

## If All Else Fails

### Start completely fresh:

```bash
# Delete virtual environment
rmdir /s venv

# Delete cache
rmdir /s __pycache__

# Run installer again
install.bat
```

### Use minimal installation (no AI):

```bash
# Just Streamlit + basic packages
pip install streamlit pydantic python-dotenv requests opencv-python

# Run app (will use fallbacks)
streamlit run app.py
```

### Check Python compatibility:

```bash
python --version

# Should be 3.11 or higher
# If older, download from python.org
```

## Verify Installation

Run verification script:

```bash
python test_setup.py
```

Should show:
```
✅ config module
✅ logger module
✅ models module
✅ transcript_parser module
✅ narrative_enhancer module
✅ image_generator module
✅ video_generator module
✅ tts_generator module
✅ video_assembler module

All tests passed!
```

## If Only Some Packages Fail

The app still works! Failed packages just disable certain features:

- **Pillow fails** → Uses PIL fallback
- **PyTorch fails** → Uses API only (no local images)
- **OpenCV fails** → Uses PIL video fallback
- **ElevenLabs fails** → Uses silent audio
- **Transformers fails** → Uses basic narration

All are optional - core functionality remains!

## Getting Help

1. Check Python version: `python --version`
2. Clear cache: `pip cache purge`
3. Upgrade tools: `python -m pip install --upgrade pip setuptools wheel`
4. Try minimal install: `pip install streamlit pydantic python-dotenv`
5. Then add packages one at a time

## Success Indicators

After installation, you should have:
- ✅ `venv/` directory
- ✅ `.env` configuration file
- ✅ `streamlit` installed (check: `pip show streamlit`)
- ✅ App starts (check: `streamlit run app.py`)

---

**Still having issues?** The app can run with minimal packages. Try:

```bash
pip install streamlit pydantic python-dotenv requests
streamlit run app.py
```

The web UI works, and fallbacks handle missing packages!
