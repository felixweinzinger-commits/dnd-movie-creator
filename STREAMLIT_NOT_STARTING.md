# Streamlit Not Starting - Troubleshooting

## Quick Fixes

### Fix 1: Use New Script

```bash
run_simple.bat
```

Better than run.bat with proper error handling.

### Fix 2: Manual Run with Debug

```bash
venv\Scripts\activate.bat
python -m streamlit run app.py --logger.level=debug
```

Shows exactly what's happening.

### Fix 3: Try Different Port

```bash
venv\Scripts\activate.bat
streamlit run app.py --server.port 8502
```

Open: http://localhost:8502

### Fix 4: Reinstall Streamlit

```bash
venv\Scripts\activate.bat
pip uninstall streamlit -y
pip install streamlit --upgrade
```

---

## Step-by-Step Debug

### 1. Verify venv

```bash
dir venv
REM Should show: Lib, Scripts, pyvenv.cfg
```

### 2. Activate venv

```bash
venv\Scripts\activate.bat
REM Prompt should show (venv)
```

### 3. Verify Streamlit

```bash
pip show streamlit
REM Should show version

pip install streamlit --upgrade
REM If not found
```

### 4. Check App

```bash
python -m py_compile app.py
REM No output = OK
```

### 5. Run with Debug

```bash
python -m streamlit run app.py --logger.level=debug
```

---

## Common Issues

| Issue | Fix |
|-------|-----|
| "streamlit not found" | Activate venv first |
| Browser doesn't open | Open http://localhost:8501 manually |
| Port 8501 in use | Use port 8502: `--server.port 8502` |
| App frozen | Wait 30 seconds, check F12 console |
| Module not found | `pip install -r requirements.txt` |

---

## Last Resort

```bash
REM Clean start
rmdir /s /q venv
python -m venv venv
call venv\Scripts\activate.bat

REM Just essentials
pip install streamlit pydantic python-dotenv requests

REM Run
streamlit run app.py
```

---

## Success Looks Like

```
Collecting usage statistics...

Streamlit app running on http://localhost:8501

Browser opens automatically ✅
```

---

**Try: `run_simple.bat` first!**
