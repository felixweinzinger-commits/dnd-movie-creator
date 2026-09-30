# 🎬 D&D Transcript to Movie Generator

Transform your D&D campaign transcripts into epic animated videos with AI!

## Features

✨ **Core:**
- 📝 Parse D&D transcripts (extract scenes, characters, dialogue)
- 🎨 Generate fantasy artwork (Stable Diffusion)
- 🎬 Create animated videos (Pika Labs)
- 🔊 Add narration (ElevenLabs TTS)
- 🎞️ Assemble final movie (FFmpeg)

## Tech Stack

- **UI**: Streamlit
- **Image**: Stable Diffusion (Local)
- **Video**: Pika Labs API
- **Audio**: ElevenLabs TTS
- **Assembly**: FFmpeg
- **LLM**: GPT-4o Mini

## Installation

```bash
# Navigate to project
cd C:\Users\admin\Projects\dnd-movie-generator

# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Setup environment
copy .env.example .env
# Edit .env with your API keys (optional)
```

## Configuration

Edit `.env` file with optional API keys:

```env
OPENAI_API_KEY=your_key
PIKA_API_KEY=your_key
ELEVENLABS_API_KEY=your_key
USE_LOCAL_STABLE_DIFFUSION=true
```

All APIs are optional - fallbacks included.

## Usage

```bash
# Start Streamlit app
streamlit run app.py
```

### Workflow

1. Upload D&D transcript (text or file)
2. Preview parsed content
3. Click "Generate Movie"
4. Wait for processing (5-30 min depending on scenes)
5. Download final video from `output/` folder

## Output Files

```
output/
├── images/          # Scene images
├── videos/          # Video clips
├── audio/           # Narration audio
├── temp/            # Temporary files
└── dnd_movie.mp4    # Final movie
```

## Free Tier

Completely free tools:
✅ Stable Diffusion (local)
✅ FFmpeg (open source)
✅ Streamlit (free)
✅ API free tiers available

Cost: $0-5 per movie

## Transcript Format

```
DM: "Narrative description"
Bard: "Character dialogue"
[SCENE] Location Name
Location: The Tavern
```

See `samples/sample_transcript.txt` for example.

## Troubleshooting

**FFmpeg not found:**
```bash
choco install ffmpeg  # Windows
# Or download from ffmpeg.org
```

**Out of memory:**
- Lower `IMAGE_RESOLUTION` in config
- Reduce scenes with `MAX_SCENES_PER_MOVIE`

**No APIs configured:**
- Fallbacks will be used
- Results functional but basic

**Slow performance:**
- GPU recommended
- Use API services instead of local

## Project Structure

```
dnd-movie-generator/
├── app.py                    # Main app
├── config.py                 # Configuration
├── requirements.txt          # Dependencies
├── .env.example              # Template
├── README.md                 # This file
├── src/
│   ├── models.py            # Data models
│   ├── transcript_parser.py # Parse transcripts
│   ├── narrative_enhancer.py # AI enhancement
│   ├── image_generator.py   # Image gen
│   ├── video_generator.py   # Video gen
│   ├── tts_generator.py     # Voice gen
│   └── video_assembler.py   # Assembly
├── utils/
│   └── logger.py            # Logging
├── samples/
│   └── sample_transcript.txt # Example
└── output/                   # Generated files
```

## Example

See `samples/sample_transcript.txt` for working example.

---

**Made with 🎲 for D&D enthusiasts**
