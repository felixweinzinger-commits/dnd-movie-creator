# ⚡ DO THIS NOW - Fix Directory Issue

## Problem
```
Error: [WinError 5] Zugriff verweigert: 'C:\\Windows\\system32\\venv'
```

Scripts running from wrong directory.

## Solution (2 Steps)

### Step 1: Open Command Prompt

Press: `Win + R`

Type: `cmd`

Press: `Enter`

### Step 2: Run Master Setup

```bash
cd C:\Users\admin\Projects\dnd-movie-generator
SETUP.bat
```

Wait for it to finish.

---

## That's It!

After SETUP.bat completes:

```bash
run_simple.bat
```

App starts! 🚀

---

## What SETUP.bat Does

- ✅ Changes to correct directory
- ✅ Verifies project files
- ✅ Creates virtual environment
- ✅ Installs all packages
- ✅ Creates output folders
- ✅ Creates config file

---

## If You Want Manual Steps

```bash
cd C:\Users\admin\Projects\dnd-movie-generator
python -m venv venv
call venv\Scripts\activate.bat
pip install streamlit pydantic python-dotenv requests
streamlit run app.py
```

---

## Success

Should see:
```
Streamlit app running on http://localhost:8501
```

Browser opens → App starts ✅

---

**Do: `SETUP.bat` first!**
