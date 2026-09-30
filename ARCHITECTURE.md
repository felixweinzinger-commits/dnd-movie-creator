# Architecture - D&D Movie Generator

## System Overview

```
Streamlit Web UI (app.py)
    ↓
Parser → Enhancer → Generator
    ↓
Processing Pipeline:
1. Parse Transcript
2. Extract Scenes
3. Enhance with AI
4. Generate Images (Stable Diffusion)
5. Create Videos (Pika Labs)
6. Generate Narration (ElevenLabs)
7. Assemble Movie (FFmpeg)
    ↓
Output: MP4 Video File
```

## Core Components

### 1. Data Models (models.py)
- `Character` - Speaker with type and voice
- `Scene` - Segments with actions
- `Transcript` - Complete structure
- Enums: CharacterType, SceneType

### 2. Transcript Parser (transcript_parser.py)
- Regex-based D&D dialogue parsing
- Character extraction
- Scene segmentation
- Location detection
- Output: Structured Transcript

### 3. Narrative Enhancer (narrative_enhancer.py)
- AI scene enhancement (GPT-4o Mini)
- Visual description generation
- Narration text generation
- Fallback: Basic descriptions

### 4. Image Generator (image_generator.py)
- Stable Diffusion (local/API)
- Generates 512x512 images
- Fallback: PIL placeholders
- Memory-efficient for CPU

### 5. Video Generator (video_generator.py)
- Pika Labs API for animation
- 6-second clips per scene
- Fallback: OpenCV effects
- Multiple quality levels

### 6. TTS Generator (tts_generator.py)
- ElevenLabs for voices
- Character voice mapping
- Fallback: Silent WAV files
- Multiple voice types

### 7. Video Assembler (video_assembler.py)
- FFmpeg integration
- Video concatenation
- Audio synchronization
- Final MP4 output

## Data Flow

```
Raw Transcript
    ↓ Parser
Structured Scenes + Characters
    ↓ Enhancer
Enhanced with AI descriptions
    ↓ Image Gen
Images: scene_000.png...
    ↓ Video Gen
Videos: scene_000.mp4...
    ↓ TTS Gen
Audio: narration_000.mp3...
    ↓ Assembler
Final: dnd_movie.mp4
```

## File Structure

```
dnd-movie-generator/
├── app.py                  # Streamlit UI
├── config.py               # Settings
├── requirements.txt        # Dependencies
├── run.bat                 # Quick start
│
├── src/
│   ├── models.py           # Data classes
│   ├── transcript_parser.py
│   ├── narrative_enhancer.py
│   ├── image_generator.py
│   ├── video_generator.py
│   ├── tts_generator.py
│   └── video_assembler.py
│
├── utils/
│   └── logger.py
│
├── output/
│   ├── images/
│   ├── videos/
│   ├── audio/
│   └── temp/
│
└── samples/
    └── sample_transcript.txt
```

## Processing Phases

| Phase | Time | Function |
|-------|------|----------|
| Parsing | 5-10s | Extract structure |
| Enhancement | 10-30s | AI descriptions |
| Images | 1-5min/scene | Stable Diffusion |
| Videos | 2-10min/scene | Pika Labs |
| Audio | 1-2min/scene | ElevenLabs |
| Assembly | 1-2min | FFmpeg |

**Total: 10-45 min for 10-30 scenes**

## API Providers

| Service | Purpose | Cost | Fallback |
|---------|---------|------|----------|
| OpenAI | Narration | Free tier | Basic text |
| Pika Labs | Video | Free tier | OpenCV |
| ElevenLabs | Voice | Free tier | Silent audio |
| Stable Diffusion | Images | FREE | PIL images |

## Error Handling

**Strategy:** Graceful Degradation
- API unavailable → Use fallback
- Memory error → Lower resolution
- Invalid input → Placeholder
- No GPU → Use CPU

## Configuration

Key settings in `config.py`:
- `MAX_SCENES_PER_MOVIE` = 30
- `IMAGE_RESOLUTION` = 768
- `VIDEO_FPS` = 24
- `VIDEO_DURATION` = 6 seconds

Override in `.env` file

## Extensibility

Easy to add:
- New scene types
- Character voices
- Image models
- Video generators
- Background music
- Subtitles
- Transitions
- Effects

---

**Design:** Modular, fallback-driven, configuration-based
