# Visual Studio Setup - Full Feature Installation

## Great News!

You have Visual Studio installed, which has the C++ compiler we need. Now we can install **everything** including:

✅ PyTorch (local image generation)  
✅ Transformers (advanced NLP)  
✅ Diffusers (image generation)  
✅ Scipy (advanced math)  

## Do This Now

### Step 1: Verify Visual Studio C++ Tools

Visual Studio needs C++ build tools. Check if they're installed:

```bash
# Check if cl.exe (C++ compiler) is available:
where cl.exe

# If found: C:\Program Files\...\cl.exe
# If not found: See "Install C++ Tools" section below
```

### Step 2: Fresh Setup with Full Features

```bash
cd C:\Users\admin\Projects\dnd-movie-generator

# Clean old venv
rmdir /s /q venv

# Run updated setup (now includes all packages)
SETUP.bat
```

This will now install:
- ✅ All core packages
- ✅ scipy
- ✅ PyTorch
- ✅ Transformers
- ✅ Diffusers
- ✅ All AI/ML packages

### Step 3: Run App with Full Features

```bash
run_simple.bat
```

Open: **http://localhost:8501**

Now you have:
- ✅ Local Stable Diffusion support
- ✅ Advanced NLP features
- ✅ Full AI capabilities

---

## If C++ Tools Not Installed

### Option 1: Install via Visual Studio Installer (Easiest)

```bash
# 1. Open Visual Studio Installer
#    (search "Visual Studio Installer" in Start Menu)

# 2. Click "Modify" on your Visual Studio installation

# 3. Go to "Workloads" tab

# 4. Check: "Desktop development with C++"

# 5. Click "Modify" button

# 6. Wait for installation
```

### Option 2: Install Visual Studio Build Tools (Standalone)

```bash
# 1. Download from:
# https://visualstudio.microsoft.com/downloads/

# 2. Scroll down to "Tools for Visual Studio 2022"

# 3. Download "Build Tools for Visual Studio 2022"

# 4. Run installer

# 5. Select "Desktop development with C++"

# 6. Install
```

---

## Verify C++ Compiler Works

```bash
# In Command Prompt, check:
where cl.exe

# Should show path like:
# C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.xx.xxxxx\bin\Hostx64\x64\cl.exe
```

---

## Full Installation Process

### Step 1: Check Compiler

```bash
where cl.exe
# Should find C++ compiler
```

### Step 2: Clean Setup

```bash
cd C:\Users\admin\Projects\dnd-movie-generator
rmdir /s /q venv
```

### Step 3: Run Setup

```bash
SETUP.bat
```

Expected output:
```
Installing scipy...
(builds from source - takes a minute)

Installing PyTorch (this may take a minute)...
(may take 2-5 minutes)

Installing AI/ML packages...
(builds from source)

... Setup Complete!
```

### Step 4: Verify All Packages

```bash
call venv\Scripts\activate.bat
pip list
```

Should see:
- ✅ torch
- ✅ transformers
- ✅ diffusers
- ✅ scipy
- ✅ All others

### Step 5: Run App

```bash
run_simple.bat
```

Open: http://localhost:8501

---

## Full Feature Comparison

| Feature | Without VC++ | With VC++ |
|---------|-------------|-----------|
| **Web UI** | ✅ | ✅ |
| **Parsing** | ✅ | ✅ |
| **Images (PIL)** | ✅ | ✅ |
| **Images (Local Diffusion)** | ❌ | ✅ |
| **Videos (OpenCV)** | ✅ | ✅ |
| **Videos (Pika API)** | ❌ | ✅ |
| **Voice (API)** | ✅ | ✅ |
| **NLP Enhancement** | ❌ | ✅ |
| **Advanced Math** | ❌ | ✅ |

---

## Installation Times

| Package | Time |
|---------|------|
| numpy | 1-2 min |
| scipy | 2-3 min |
| torch | 3-5 min |
| transformers | 2-3 min |
| diffusers | 1-2 min |
| **Total** | **10-15 min** |

---

## Troubleshooting

### Issue: "cl.exe not found"

**Fix:** C++ tools not installed

```bash
# Install via Visual Studio Installer
# Select: Desktop development with C++
```

### Issue: "error: Microsoft Visual C++ 14.x is required"

**Fix:** Need specific Visual C++ version

```bash
# Download from:
# https://visualstudio.microsoft.com/visual-cpp-build-tools/

# Or use Visual Studio Installer to add C++ tools
```

### Issue: "Permission denied" during installation

**Fix:** Run as Administrator

```bash
# Right-click Command Prompt
# Select "Run as administrator"
# Then run SETUP.bat
```

### Issue: Installation stuck/frozen

**Fix:** Wait longer (PyTorch is large - 1+ hour possible)

```bash
# Or install without PyTorch:
pip install streamlit pydantic python-dotenv requests
pip install pillow opencv-python numpy
pip install elevenlabs moviepy ffmpeg-python
```

---

## After Full Installation

You can now use:

### Local Image Generation

```python
from diffusers import StableDiffusionPipeline
pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")
image = pipe("A fantasy tavern").images[0]
```

### Advanced Transformers

```python
from transformers import pipeline
generator = pipeline("text-generation", model="gpt2")
text = generator("The adventure begins")[0]['generated_text']
```

### Local Processing

All AI features now run locally without API calls!

---

## Next Steps

1. **Check C++ compiler:** `where cl.exe`
2. **If not found:** Install via Visual Studio Installer
3. **Clean setup:** `rmdir /s /q venv`
4. **Full install:** `SETUP.bat`
5. **Run app:** `run_simple.bat`
6. **Enjoy full features!** 🎬

---

## Summary

| Item | Status |
|------|--------|
| Visual Studio | ✅ Installed |
| C++ Compiler | ✅ Available |
| Full Installation | ✅ Possible |
| All Features | ✅ Enabled |
| Setup Time | ~10-15 min |

---

**With Visual Studio, you get the complete system!** 🚀

Now run:
```bash
cd C:\Users\admin\Projects\dnd-movie-generator
rmdir /s /q venv
SETUP.bat
```
