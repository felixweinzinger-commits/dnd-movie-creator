# File Directory - D&D Movie Generator

## Project Root Files

| File | Purpose |
|------|---------|
| `app.py` | Main Streamlit web application UI |
| `config.py` | Central configuration management |
| `requirements.txt` | Python package dependencies |
| `run.bat` | Quick-start batch script |
| `test_setup.py` | Setup verification script |
| `.env.example` | Environment variable template |
| `.env` | Your local configuration (create from .example) |

## Documentation Files

| File | Purpose |
|------|---------|
| `README.md` | Main project documentation |
| `QUICKSTART.md` | 5-minute quick start guide |
| `SETUP.md` | Detailed setup instructions |
| `ARCHITECTURE.md` | System architecture & design |
| `FILES.md` | This file - directory listing |

## Source Code - `src/` Directory

| File | Purpose | Key Classes |
|------|---------|-------------|
| `__init__.py` | Package initialization | - |
| `models.py` | Pydantic data models | Character, Scene, Transcript, etc. |
| `transcript_parser.py` | D&D transcript parsing | TranscriptParser |
| `narrative_enhancer.py` | AI narrative enhancement | NarrativeEnhancer |
| `image_generator.py` | Image generation (Stable Diffusion) | ImageGenerator |
| `video_generator.py` | Video generation (Pika Labs) | VideoGenerator |
| `tts_generator.py` | Text-to-speech (ElevenLabs) | TTSGenerator |
| `video_assembler.py` | Final video assembly (FFmpeg) | VideoAssembler |

## Utilities - `utils/` Directory

| File | Purpose |
|------|---------|
| `__init__.py` | Package initialization |
| `logger.py` | Logging configuration |

## Sample Data - `samples/` Directory

| File | Purpose |
|------|---------|
| `sample_transcript.txt` | Example D&D transcript (complete session) |

## Output - `output/` Directory

**Auto-created during generation:**

| Folder | Contains |
|--------|----------|
| `images/` | Generated scene images (PNG) |
| `videos/` | Generated video clips (MP4) |
| `audio/` | Generated narration audio (MP3/WAV) |
| `temp/` | Temporary files (FFmpeg working files) |

**Final Output:**
- `dnd_movie.mp4` - Final assembled movie

## Total File Count

- **Core App:** 7 files
- **Documentation:** 5 files
- **Source Code:** 9 files
- **Utilities:** 2 files
- **Samples:** 1 file
- **Total: 24 files**

## File Dependencies

```
app.py
├── config.py
├── src/transcript_parser.py
│   └── src/models.py
├── src/narrative_enhancer.py
│   ├── config.py
│   └── src/models.py
├── src/image_generator.py
│   ├── config.py
│   └── src/models.py
├── src/video_generator.py
│   ├── config.py
│   └── src/models.py
├── src/tts_generator.py
│   └── config.py
├── src/video_assembler.py
│   └── config.py
└── utils/logger.py

config.py
└── .env (optional)
```

## Configuration Sources

### config.py
Default settings for:
- Paths (PROJECT_ROOT, OUTPUT_DIR, etc.)
- API keys (loaded from .env)
- Model settings (resolution, FPS, etc.)
- Processing parameters

### .env File
Optional overrides for:
- API keys
- Model configuration
- Output paths
- Processing limits

## Module Imports

### Main App (app.py)
```python
from src.transcript_parser import TranscriptParser
from src.narrative_enhancer import NarrativeEnhancer
from src.image_generator import ImageGenerator
from src.video_generator import VideoGenerator
from src.tts_generator import TTSGenerator
from src.video_assembler import VideoAssembler
from utils.logger import setup_logger
import config
```

### Typical Processing Flow
```
config.py → app.py
    ↓
TranscriptParser → Scene Objects
    ↓
NarrativeEnhancer → Enhanced Scenes
    ↓
ImageGenerator → Images
    ↓
VideoGenerator → Videos
    ↓
TTSGenerator → Audio
    ↓
VideoAssembler → Final Movie
```

## Generated Output Structure

```
output/
├── images/
│   ├── scene_000.png
│   ├── scene_001.png
│   └── scene_00X.png
├── videos/
│   ├── scene_000.mp4
│   ├── scene_001.mp4
│   └── scene_00X.mp4
├── audio/
│   ├── narration_000.mp3
│   ├── narration_001.mp3
│   └── narration_00X.mp3
├── temp/
│   ├── concat.txt (FFmpeg concat file)
│   └── audio_concat.txt
└── dnd_movie.mp4 (Final output)
```

## Quick Reference

**To run:** `run.bat` or `streamlit run app.py`

**To test:** `python test_setup.py`

**To configure:** Edit `.env` file

**To use sample:** Paste contents of `samples/sample_transcript.txt`

**To troubleshoot:** Check README.md or SETUP.md

---

**All files created and ready to use!**
