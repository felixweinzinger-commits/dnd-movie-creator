"""
Configuration module for D&D Transcript to Movie Generator
"""
import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Project Paths
PROJECT_ROOT = Path(__file__).parent
SRC_DIR = PROJECT_ROOT / "src"
SAMPLES_DIR = PROJECT_ROOT / "samples"
OUTPUT_DIR = PROJECT_ROOT / "output"

# API Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
PIKA_API_KEY = os.getenv("PIKA_API_KEY", "")
PIKA_API_URL = os.getenv("PIKA_API_URL", "https://api.pika.art/v1")
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY", "")

# Model Configuration
STABLE_DIFFUSION_MODEL = os.getenv("STABLE_DIFFUSION_MODEL", "runwayml/stable-diffusion-v1-5")
USE_LOCAL_STABLE_DIFFUSION = os.getenv("USE_LOCAL_STABLE_DIFFUSION", "true").lower() == "true"

# Processing Settings
MAX_SCENES_PER_MOVIE = int(os.getenv("MAX_SCENES_PER_MOVIE", "30"))
IMAGE_RESOLUTION = int(os.getenv("IMAGE_RESOLUTION", "768"))
VIDEO_FPS = int(os.getenv("VIDEO_FPS", "24"))
BATCH_SIZE = int(os.getenv("BATCH_SIZE", "5"))
TIMEOUT_MINUTES = int(os.getenv("TIMEOUT_MINUTES", "120"))

# FFmpeg Configuration
FFMPEG_PATH = os.getenv("FFMPEG_PATH", "ffmpeg")

# Narrative Enhancement Settings
NARRATOR_STYLE = "epic"
SCENE_DETAIL_LEVEL = "medium"  # low, medium, high

# Voice Settings
DEFAULT_NARRATOR_VOICE = "male_narrator"
CHARACTER_VOICES = {
    "default": "en_male_1",
    "female": "en_female_1",
    "old": "en_male_2",
}

# Image Generation Settings
IMG_NEGATIVE_PROMPT = "blurry, distorted, low quality, ugly, bad anatomy"
IMG_GUIDANCE_SCALE = 7.5
IMG_NUM_INFERENCE_STEPS = 50

# Video Generation Settings
VIDEO_DURATION = 6  # seconds per scene
VIDEO_QUALITY = "medium"  # low, medium, high

# Ensure output directory exists
OUTPUT_DIR.mkdir(exist_ok=True, parents=True)
SAMPLES_DIR.mkdir(exist_ok=True, parents=True)

# Logging Configuration
LOG_LEVEL = "INFO"
LOG_FILE = PROJECT_ROOT / "dnd_generator.log"
