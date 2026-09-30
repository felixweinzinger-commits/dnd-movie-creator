# Setup Instructions for D&D Movie Generator

## Quick Start (Windows)

### Step 1: Install Python Dependencies

```bash
# Navigate to project directory
cd C:\Users\admin\Projects\dnd-movie-generator

# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate.bat

# Install dependencies
pip install -r requirements.txt
```

### Step 2: Configure Environment (Optional)

```bash
# Copy environment template
copy .env.example .env

# Edit .env with your API keys (Notepad):
notepad .env
```

**Optional API Keys:**
- `OPENAI_API_KEY` - For narrative enhancement (GPT-4o Mini)
- `PIKA_API_KEY` - For video generation (Pika Labs)
- `ELEVENLABS_API_KEY` - For voice generation (ElevenLabs)

**Note:** All APIs are optional. The generator includes fallback implementations using local/placeholder methods.

### Step 3: Run the Application

**Option A: Using batch file (Easiest)**
```bash
run.bat
```

**Option B: Manual start**
```bash
venv\Scripts\activate.bat
streamlit run app.py
```

The app will open at: `http://localhost:8501`

## System Requirements

### Minimum
- Python 3.11+
- 4GB RAM
- 2GB disk space for output

### Recommended
- Python 3.11+
- 8GB+ RAM (for local Stable Diffusion)
- GPU with CUDA (NVIDIA) for faster image generation
- 10GB+ disk space

## Dependencies Overview

The project uses:
- **streamlit** - Web UI
- **pydantic** - Data validation
- **python-dotenv** - Environment configuration
- **pillow** - Image processing
- **opencv-python** - Video processing
- **moviepy** - Video composition
- **torch/torchvision** - PyTorch for Stable Diffusion
- **diffusers** - Hugging Face Stable Diffusion
- **requests** - API calls
- **elevenlabs** - ElevenLabs client

## Troubleshooting

### Issue: Python not found
```bash
# Make sure Python is installed and in PATH
python --version

# Or use full path
C:\Python311\python.exe -m venv venv
```

### Issue: FFmpeg not found
```bash
# Install FFmpeg
choco install ffmpeg

# Or download from: https://ffmpeg.org/download.html
# Add to PATH manually
```

### Issue: Dependencies won't install
```bash
# Clear pip cache
pip cache purge

# Upgrade pip
python -m pip install --upgrade pip

# Try again
pip install -r requirements.txt
```

### Issue: Memory error when generating images
```bash
# Edit config.py and reduce:
IMAGE_RESOLUTION = 512  # Instead of 768
IMG_NUM_INFERENCE_STEPS = 25  # Instead of 50
```

### Issue: Slow generation
- Use local Pika Labs (set API key)
- Use local ElevenLabs (set API key)
- Reduce number of scenes
- Use GPU (install CUDA PyTorch version)

## GPU Setup (Optional - For Faster Generation)

### NVIDIA GPU with CUDA

```bash
# Uninstall current torch
pip uninstall -y torch torchvision torchaudio

# Install with CUDA support
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

### Check GPU is working
```bash
python -c "import torch; print(torch.cuda.is_available())"
```

Should return: `True`

## File Structure After Setup

```
dnd-movie-generator/
├── venv/                     # Virtual environment
├── app.py                    # Main application
├── config.py                 # Configuration
├── requirements.txt          # Dependencies
├── run.bat                   # Quick start script
├── test_setup.py            # Setup test
├── .env                      # Your config (after copy)
├── .env.example              # Template
├── src/                      # Source code
├── utils/                    # Utilities
├── samples/                  # Example transcripts
├── output/                   # Generated files
│   ├── images/
│   ├── videos/
│   └── audio/
└── README.md                 # Documentation
```

## Next Steps

1. Follow Quick Start above
2. Try with sample transcript: `samples/sample_transcript.txt`
3. Check output in: `output/` folder
4. Add your own transcripts and generate!

## Support

- Check logs in terminal
- Verify API keys in `.env`
- Test with sample transcript first
- Review output/errors in browser console

---

**Ready to start?** Run: `run.bat`
