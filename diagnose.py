"""
Diagnostic script to check what's wrong with Streamlit startup
"""
import sys
import os
from pathlib import Path

print("=" * 60)
print("D&D Movie Generator - Diagnostic Report")
print("=" * 60)
print()

# 1. Check Python
print("1. Python Environment")
print("-" * 60)
print(f"Python Version: {sys.version}")
print(f"Python Path: {sys.executable}")
print()

# 2. Check imports
print("2. Checking Required Imports")
print("-" * 60)

imports_to_test = [
    ("streamlit", "Streamlit (Web UI)"),
    ("pydantic", "Pydantic (Data models)"),
    ("dotenv", "Python-dotenv (Config)"),
    ("requests", "Requests (HTTP)"),
    ("pathlib", "Pathlib (Built-in)"),
]

for module_name, description in imports_to_test:
    try:
        __import__(module_name)
        print(f"✅ {description}")
    except ImportError as e:
        print(f"❌ {description}: {e}")

print()

# 3. Check project structure
print("3. Project Structure")
print("-" * 60)

project_root = Path(__file__).parent
required_files = [
    "app.py",
    "config.py",
    "src/__init__.py",
    "src/models.py",
    "src/transcript_parser.py",
    "utils/__init__.py",
    "utils/logger.py",
]

for file_path in required_files:
    full_path = project_root / file_path
    if full_path.exists():
        print(f"✅ {file_path}")
    else:
        print(f"❌ {file_path} (MISSING)")

print()

# 4. Check if config loads
print("4. Configuration Check")
print("-" * 60)

try:
    sys.path.insert(0, str(project_root))
    import config
    print(f"✅ Config loaded successfully")
    print(f"   Output Dir: {config.OUTPUT_DIR}")
    print(f"   Max Scenes: {config.MAX_SCENES_PER_MOVIE}")
    print(f"   Local Stable Diffusion: {config.USE_LOCAL_STABLE_DIFFUSION}")
except Exception as e:
    print(f"❌ Config error: {e}")
    import traceback
    traceback.print_exc()

print()

# 5. Check if app.py loads
print("5. Application Check")
print("-" * 60)

try:
    # Try to import app modules
    from src.transcript_parser import TranscriptParser
    from src.narrative_enhancer import NarrativeEnhancer
    from utils.logger import setup_logger
    
    print(f"✅ App modules import successfully")
    print(f"   TranscriptParser: OK")
    print(f"   NarrativeEnhancer: OK")
    print(f"   Logger: OK")
except Exception as e:
    print(f"❌ App module error: {e}")
    import traceback
    traceback.print_exc()

print()

# 6. Check if Streamlit works
print("6. Streamlit Check")
print("-" * 60)

try:
    import streamlit as st
    print(f"✅ Streamlit version: {st.__version__}")
    print(f"   Streamlit path: {st.__file__}")
except Exception as e:
    print(f"❌ Streamlit error: {e}")
    import traceback
    traceback.print_exc()

print()

# 7. Port check
print("7. Port Availability")
print("-" * 60)

import socket

def is_port_open(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    try:
        result = sock.connect_ex(('127.0.0.1', port))
        return result == 0
    finally:
        sock.close()

if is_port_open(8501):
    print("⚠️  Port 8501 is already in use!")
    print("   Solution: Kill existing Streamlit or use different port")
else:
    print("✅ Port 8501 is available")

print()

# 8. Summary
print("=" * 60)
print("Diagnostic Summary")
print("=" * 60)

all_ok = True
print()
print("To start the app, try one of these:")
print()
print("Option 1 (Recommended):")
print("  streamlit run app.py --logger.level=debug")
print()
print("Option 2 (Different port if 8501 busy):")
print("  streamlit run app.py --server.port 8502")
print()
print("Option 3 (Debug mode):")
print("  python -c \"import streamlit.cli; streamlit.cli.main()\" run app.py")
print()

print("=" * 60)
