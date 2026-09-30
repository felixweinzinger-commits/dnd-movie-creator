# 🚀 QUICK FIX - Streamlit Not Starting

**You have:** Streamlit app that won't start / browser not opening

**Try this NOW:**

## Option 1: Use New Script (RECOMMENDED)

```bash
run_simple.bat
```

This has better error handling and more info.

## Option 2: Manual with Debug Info

```bash
cd C:\Users\admin\Projects\dnd-movie-generator
venv\Scripts\activate.bat
python -m streamlit run app.py --logger.level=debug
```

Then:
- Wait 30 seconds
- Open browser to: http://localhost:8501
- Check what errors appear

## Option 3: Clean Install

```bash
# Delete venv
rmdir /s /q venv

# Fresh environment
python -m venv venv
venv\Scripts\activate.bat

# Install minimal
pip install streamlit pydantic python-dotenv requests

# Run
streamlit run app.py
```

Wait 10-30 seconds, then open: http://localhost:8501

## Option 4: Different Port

If port 8501 is in use:

```bash
venv\Scripts\activate.bat
streamlit run app.py --server.port 8502
```

Open: http://localhost:8502

---

## Most Likely Cause

**venv not activated** when running streamlit

**Fix:**
```bash
# ALWAYS do this first:
venv\Scripts\activate.bat

# Prompt should show: (venv) C:\path\>

# THEN run app:
streamlit run app.py
```

---

## What Should Happen

1. ✅ See: "Streamlit app running on http://localhost:8501"
2. ✅ Browser opens automatically
3. ✅ See D&D Movie Generator UI
4. ✅ Three tabs: Upload, Generate, Info

---

## If Still Stuck

1. Try: `run_simple.bat` (new script)
2. Read: `STREAMLIT_NOT_STARTING.md` (full guide)
3. Check: `INSTALL_TROUBLESHOOTING.md` (general help)

---

**Start with: `run_simple.bat`**
