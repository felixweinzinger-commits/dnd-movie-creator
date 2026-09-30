# Quick Start Guide - D&D Movie Generator

## 🚀 Get Started in 5 Minutes

### Step 1: Install (2 min)

```bash
cd C:\Users\admin\Projects\dnd-movie-generator
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
```

### Step 2: Configure (1 min - Optional)

```bash
copy .env.example .env
# Edit .env with your API keys (optional - fallbacks work)
notepad .env
```

### Step 3: Run (1 min)

```bash
# Option A: Double-click
run.bat

# Option B: Command line
streamlit run app.py
```

Browser opens: `http://localhost:8501`

## 📝 Using the Application

### Generate Your First Movie

1. **Upload Transcript**
   - Go to "📝 Upload" tab
   - Paste your D&D transcript or upload file
   - Click "Preview" to verify parsing

2. **Generate Movie**
   - Go to "🎨 Generate" tab
   - Click "🚀 START GENERATION"
   - Watch progress bars
   - Download video from `output/` folder

### Example Transcript

```
DM: You find yourselves in a tavern.
Bard: I order an ale and ask the bartender about local rumors.
DM: The bartender leans in and whispers about treasure in the forest.
Rogue: We should investigate. When do we leave?
DM: At first light. You prepare for adventure.
```

## 📊 What Gets Generated

```
output/
├── images/                # Fantasy scene artwork
├── videos/                # Animated clips
├── audio/                 # Narration voices
└── dnd_movie.mp4          # Final assembled movie
```

## 🎁 Included Sample

Test with built-in example:
- File: `samples/sample_transcript.txt`
- Copy content to app and generate!

## 🔑 API Keys (Optional)

All free tier with fallbacks:

| Service | Key | Purpose | Cost |
|---------|-----|---------|------|
| OpenAI | `OPENAI_API_KEY` | Narrative enhancement | Free tier available |
| Pika Labs | `PIKA_API_KEY` | Video generation | Free tier $10 credit |
| ElevenLabs | `ELEVENLABS_API_KEY` | Voice narration | Free tier 10k chars/mo |

**No keys?** No problem! Fallbacks provide basic but functional output.

## 🛠️ Troubleshooting

### "Module not found" errors
```bash
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

### "FFmpeg not found"
```bash
# Windows: Install via chocolatey
choco install ffmpeg
# Or manually: download from ffmpeg.org and add to PATH
```

### Slow image generation
```bash
# Edit config.py:
IMAGE_RESOLUTION = 512      # Lower res
IMG_NUM_INFERENCE_STEPS = 25 # Fewer steps

# Or use GPU:
pip install torch --index-url https://download.pytorch.org/whl/cu118
```

### Out of memory
```bash
# Reduce scenes in config.py:
MAX_SCENES_PER_MOVIE = 10  # Instead of 30
```

## 📚 Examples

### Minimal Transcript
```
DM: You wake up in a cave.
Fighter: We look around cautiously.
DM: You find a treasure chest.
```

### Full Example
See `samples/sample_transcript.txt` (500+ lines)

## 🎓 How It Works

```
Your Transcript
    ↓
Parse & Extract Scenes
    ↓
AI-Enhanced Descriptions
    ↓
Generate Images (Stable Diffusion)
    ↓
Create Videos (Pika Labs)
    ↓
Generate Narration (ElevenLabs)
    ↓
Assemble Movie (FFmpeg)
    ↓
Final Video! 🎬
```

## 💡 Tips

1. **Better Results**: Add descriptive text to scenes
2. **Faster Generation**: Use fewer scenes (max 30)
3. **Longer Duration**: More scenes = longer movie
4. **Custom Narration**: Edit narration prompts in app
5. **Reuse Videos**: Output files are saved, check before re-running

## 🎯 Common Use Cases

### Quick Test
- Use built-in sample
- Takes ~5 minutes
- Good for learning

### Full Campaign
- Upload full session
- Takes 20-60 minutes
- Generates 10-30 minute video

### Custom Movie
- Write custom script
- Format as D&D transcript
- Generate unique content

## 🔍 Check Your Setup

Run test to verify everything:
```bash
python test_setup.py
```

## 📖 Full Documentation

- Setup details: `SETUP.md`
- Project structure: `README.md`
- Configuration: `config.py`

## ✨ Next Steps

1. ✅ Install dependencies
2. ✅ Configure API keys (optional)
3. ✅ Run the app
4. ✅ Try with sample transcript
5. ✅ Generate your own movie!

---

**Questions?** Check README.md or SETUP.md for detailed guides.

**Ready?** Run: `run.bat` or `streamlit run app.py`
