# 🎬 START HERE - D&D Movie Generator

Your AI-powered D&D movie generator is ready! Transform transcripts into animated films.

## Quick Start (5 Minutes)

### 1. Install
```bash
cd C:\Users\admin\Projects\dnd-movie-generator
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
```

### 2. Run
```bash
run.bat
```
Or: `streamlit run app.py`

Opens: `http://localhost:8501`

### 3. Generate
1. Upload D&D transcript
2. Preview parsed content
3. Click "Generate"
4. Download MP4 from `output/`

## What You Have

✨ **Features:**
- 📝 Parse D&D transcripts
- 🎨 Generate fantasy artwork (Stable Diffusion)
- 🎬 Create animated videos (Pika Labs)
- 🔊 Add voice narration (ElevenLabs)
- 🎞️ Assemble final movie (FFmpeg)

## Documentation

| File | Purpose |
|------|---------|
| `README.md` | Full documentation |
| `QUICKSTART.md` | 5-minute reference |
| `SETUP.md` | Detailed setup |
| `ARCHITECTURE.md` | System design |
| `FILES.md` | File directory |

## File Structure

```
├── app.py              # Main web app
├── config.py           # Configuration
├── requirements.txt    # Dependencies
├── run.bat             # Quick start
├── src/                # Processing modules
│   ├── models.py
│   ├── transcript_parser.py
│   ├── narrative_enhancer.py
│   ├── image_generator.py
│   ├── video_generator.py
│   ├── tts_generator.py
│   └── video_assembler.py
├── utils/              # Utilities
├── samples/            # Example transcript
└── output/             # Generated files
    ├── images/
    ├── videos/
    ├── audio/
    └── dnd_movie.mp4
```

## Generate Your First Movie

### Option 1: Use Sample (Fastest)
```
1. App → "📝 Upload" tab
2. Copy samples/sample_transcript.txt
3. Paste into text area
4. Click Preview
5. Go to "🎨 Generate"
6. Click "Generate Movie"
7. Download dnd_movie.mp4
```

### Option 2: Your Transcript
Format like D&D dialogue:
```
DM: You enter a tavern.
Bard: I order an ale.
DM: The bartender serves you.
```

## Configuration (Optional)

### Works Without API Keys
Fallbacks included:
- ✅ Local Stable Diffusion (free)
- ✅ Placeholder videos (free)
- ✅ Silent narration (free)

### Add API Keys for Better Results
```bash
# Edit .env
notepad .env

# Add (free tiers available):
OPENAI_API_KEY=...
PIKA_API_KEY=...
ELEVENLABS_API_KEY=...
```

## Output Files

```
output/
├── images/          # Generated scenes
├── videos/          # Animated clips
├── audio/           # Narration
└── dnd_movie.mp4    # Final video
```

## Troubleshooting

**"Module not found"**
```bash
pip install -r requirements.txt --force-reinstall
```

**"FFmpeg not found"**
```bash
choco install ffmpeg
```

**Slow generation**
- Use fewer scenes
- Lower resolution in config
- Install GPU support

**Out of memory**
- Reduce MAX_SCENES in config
- Lower IMAGE_RESOLUTION

## How It Works

```
Transcript → Parse → Enhance (AI)
    ↓
Generate Images → Create Videos
    ↓
Add Narration → Assemble Movie
    ↓
Final MP4 Download!
```

## Next Steps

1. Run: `run.bat`
2. Upload sample or your transcript
3. Click generate
4. Download video!

## Learn More

- `README.md` - Full docs
- `QUICKSTART.md` - Quick ref
- `ARCHITECTURE.md` - How it works
- `SETUP.md` - Setup details

---

**Ready?** Run `run.bat` now! 🎲🎬
