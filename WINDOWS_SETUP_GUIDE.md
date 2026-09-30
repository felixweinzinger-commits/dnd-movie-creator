# Windows Setup Guide - Complete Solution

## Problem You Had

```
Error: [WinError 5] Zugriff verweigert: 'C:\\Windows\\system32\\venv'
```

This means the script was running from the wrong directory (Windows\system32).

## Root Cause

Batch scripts don't automatically run from their own directory on Windows. They need to explicitly change directory.

## SOLUTION - Do This Now

### Step 1: Navigate to Project Directory

```bash
cd C:\Users\admin\Projects\dnd-movie-generator
```

### Step 2: Run Master Setup Script

```bash
SETUP.bat
```

This script:
- ✅ Changes to correct directory automatically
- ✅ Verifies project files exist
- ✅ Checks Python is installed
- ✅ Creates virtual environment
- ✅ Installs all dependencies
- ✅ Creates output directories
- ✅ Creates .env config file

### Step 3: Run the App

After SETUP.bat finishes:

```bash
run_simple.bat
```

Or manually:

```bash
call venv\Scripts\activate.bat
streamlit run app.py
```

---

## Why This Happened

**Old scripts:**
```batch
python -m venv venv    ← Tries to create in current directory
```

**Current directory was:** `C:\Windows\system32` (default for batch files)

**New scripts have:**
```batch
cd /d "%~dp0"          ← Changes to script's directory
python -m venv venv    ← Creates in correct location
```

The `/d` flag allows changing drives (C:, D:, etc.)

---

## Files Updated

| File | Change |
|------|--------|
| `SETUP.bat` | ✨ NEW - Master setup script |
| `install.bat` | 📝 Added directory change |
| `run.bat` | 📝 Added directory change |
| `run_simple.bat` | 📝 Added directory change |

---

## How to Use Moving Forward

### Always use from File Explorer:

1. Open: `C:\Users\admin\Projects\dnd-movie-generator`
2. Double-click: `SETUP.bat` (first time only)
3. Double-click: `run_simple.bat` (every time you want to run app)

### Or from Command Prompt:

```bash
# First time - setup everything
cd C:\Users\admin\Projects\dnd-movie-generator
SETUP.bat

# Every time - run the app
cd C:\Users\admin\Projects\dnd-movie-generator
run_simple.bat
```

---

## Key Windows Batch Commands

```batch
cd C:\path        ← Change directory (same drive)
cd /d C:\path     ← Change directory (any drive)
%~dp0             ← Full path of script directory
"%~dp0"           ← Quoted (handles spaces in path)
pause             ← Wait for key press
```

---

## Verification

After SETUP.bat, you should have:

```
C:\Users\admin\Projects\dnd-movie-generator\
├── venv\              ✅ Virtual environment
├── .env               ✅ Configuration file
├── output\
│   ├── images\
│   ├── videos\
│   ├── audio\
│   └── temp\
└── app.py, config.py, etc.
```

---

## Success Indicators

✅ SETUP.bat shows:
```
Project location: C:\Users\admin\Projects\dnd-movie-generator
Verified: Project files found
Python found: OK
Virtual environment created: OK
Core packages installed: OK
...
Setup Complete!
```

✅ run_simple.bat shows:
```
Working directory: C:\Users\admin\Projects\dnd-movie-generator
Activating virtual environment...
Starting Streamlit Application
URL: http://localhost:8501
```

✅ Browser opens to http://localhost:8501 ✅

---

## Quick Reference

| What | Command | Notes |
|------|---------|-------|
| First setup | `SETUP.bat` | Run once from project folder |
| Run app | `run_simple.bat` | Run from project folder |
| Manual run | `call venv\Scripts\activate.bat` then `streamlit run app.py` | For debugging |
| Clean reinstall | Delete `venv` folder, run `SETUP.bat` | Start fresh |

---

## If SETUP.bat Fails

### Check 1: Are you in the right directory?

```bash
# Type in Command Prompt:
cd C:\Users\admin\Projects\dnd-movie-generator
dir app.py

# Should show: app.py
# If not found - wrong directory!
```

### Check 2: Is Python installed?

```bash
python --version
# Should show: Python 3.14.7

# If not found:
# - Install from python.org
# - Make sure to add to PATH during installation
```

### Check 3: Can you run commands in this directory?

```bash
# Type:
dir
# Should show: app.py, config.py, venv, etc.

# If empty - wrong directory!
```

---

## Advanced Options

### Custom Python Installation

```bash
"C:\Program Files\Python314\python.exe" -m venv venv
```

### Specific Python Version

```bash
python3.11 -m venv venv
```

### Install specific package

```bash
call venv\Scripts\activate.bat
pip install <package_name>
```

---

## Troubleshooting Checklist

- [ ] Did you navigate to project folder first?
- [ ] Does `dir` show app.py in current folder?
- [ ] Is Python installed? (`python --version`)
- [ ] Do you have write permissions in this folder?
- [ ] Is there enough disk space (2-3 GB)?

---

## Summary

**Old Problem:** Scripts ran from wrong directory (Windows\system32)

**New Solution:** Scripts automatically change to correct directory

**What Changed:**
```batch
cd /d "%~dp0"    ← Added to all .bat scripts
```

**Result:** Everything works correctly from any location

---

**Try Now:**
```bash
cd C:\Users\admin\Projects\dnd-movie-generator
SETUP.bat
```

Should work! 🚀
