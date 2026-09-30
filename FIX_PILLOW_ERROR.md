# Fix: Pillow Build Failure on Windows

## Problem

You got this error:
```
ERROR: Failed to build 'pillow' when getting requirements to build wheel
KeyError: '__version__'
```

## Solution: Use the New Installer

I've created an improved installation script that fixes this issue.

### Step 1: Clean Up (Optional)

If you already tried installing, clean up first:

```bash
cd C:\Users\admin\Projects\dnd-movie-generator

# Delete the broken environment
rmdir /s /q venv

# Clear pip cache
pip cache purge
```

### Step 2: Run New Installer

```bash
install.bat
```

**This script:**
- ✅ Upgrades pip, setuptools, wheel first (CRITICAL)
- ✅ Installs pre-built Pillow wheels (no building)
- ✅ Uses CPU-friendly PyTorch
- ✅ Handles all dependencies properly
- ✅ Creates output directories

### Step 3: Run the App

```bash
run.bat
```

Done! The app should now start.

---

## If Script Still Fails

### Option 1: Minimal Quick Setup

```bash
# Create environment
python -m venv venv
venv\Scripts\activate.bat

# Upgrade tools FIRST (this is critical!)
python -m pip install --upgrade pip setuptools wheel

# Install just the essentials
pip install streamlit pydantic python-dotenv requests

# Try to run app
streamlit run app.py
```

The app will work with just these basics. Other features optional.

### Option 2: Manual Step-by-Step

```bash
# 1. Activate
venv\Scripts\activate.bat

# 2. Upgrade critical tools
python -m pip install --upgrade pip setuptools wheel

# 3. Install one by one
pip install streamlit
pip install pydantic
pip install python-dotenv
pip install requests
pip install opencv-python
pip install numpy

# 4. Try PyTorch (CPU version)
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu

# 5. Install Pillow with pre-built wheel
pip install --only-binary :all: Pillow

# 6. Continue with others
pip install transformers diffusers accelerate

# 7. Run app
streamlit run app.py
```

---

## Why This Happened

Older `pip` tries to **build Pillow from source** on Windows, which requires:
- C++ compiler
- Build tools
- Development headers

The fix:
- ✅ Upgrades pip to use pre-built wheels
- ✅ Explicitly requests binary wheels only
- ✅ Skips all source compilation

---

## What Changed

**Old requirements.txt:**
```
pillow==10.1.0  ← Tries exact version, may require build
```

**New requirements.txt:**
```
Pillow>=10.0.0  ← Allows any compatible version, prefers wheels
```

**Old installation:**
```
pip install -r requirements.txt
```

**New installation:**
```
install.bat  ← Handles everything properly
```

---

## Verify It Works

After installation, check:

```bash
# Activate environment
venv\Scripts\activate.bat

# Check Pillow is installed
pip show Pillow

# Check Streamlit works
streamlit --version

# Run app
streamlit run app.py
```

Should open browser at: `http://localhost:8501`

---

## Key Points

1. **Upgrade pip first** - This is the most important step
2. **Use pre-built wheels** - Add `--only-binary :all:` for Pillow
3. **CPU PyTorch** - Use `--index-url https://download.pytorch.org/whl/cpu`
4. **Run install.bat** - New script handles it all

---

## If Still Having Issues

The app is very resilient! You can skip problematic packages:

```bash
# Minimal setup that definitely works
python -m venv venv
venv\Scripts\activate.bat
pip install streamlit pydantic python-dotenv requests
streamlit run app.py
```

The app will:
- ✅ Load and run
- ✅ Parse transcripts
- ✅ Show web UI
- ✅ Use fallback implementations

Missing packages just disable advanced features, but core works!

---

**Try `install.bat` first. It should fix everything!**
