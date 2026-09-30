"""D&D Transcript to Movie Generator - Main Streamlit Application"""
import streamlit as st
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from src.transcript_parser import TranscriptParser
from src.narrative_enhancer import NarrativeEnhancer
from src.image_generator import ImageGenerator
from src.video_generator import VideoGenerator
from src.tts_generator import TTSGenerator
from src.video_assembler import VideoAssembler
from utils.logger import setup_logger
import config

logger = setup_logger(__name__)

st.set_page_config(page_title="D&D Movie Generator", page_icon="🎬", layout="wide")
st.title("🎬 D&D Transcript to Movie Generator 🐉")
st.markdown("Transform D&D transcripts into epic animated videos!")

# Sidebar
with st.sidebar:
    st.header("⚙️ Configuration")
    openai = "✅" if config.OPENAI_API_KEY else "❌"
    pika = "✅" if config.PIKA_API_KEY else "❌"
    elevenlabs = "✅" if config.ELEVENLABS_API_KEY else "❌"
    stable = "✅" if config.USE_LOCAL_STABLE_DIFFUSION else "❌"
    st.write(f"OpenAI: {openai} | Pika: {pika}")
    st.write(f"ElevenLabs: {elevenlabs} | Stable Diff: {stable}")
    st.info("Missing keys? Fallbacks will be used.")

# Main content
tab1, tab2, tab3 = st.tabs(["📝 Upload", "🎨 Generate", "ℹ️ Info"])

with tab1:
    st.header("Upload D&D Transcript")
    upload_method = st.radio("Method:", ["Text Input", "File Upload"])
    
    transcript_text = None
    transcript_title = "My Campaign"
    
    if upload_method == "Text Input":
        transcript_title = st.text_input("Title:", value="My D&D Campaign")
        transcript_text = st.text_area("Paste transcript:", height=300, placeholder="DM: The party enters...")
    else:
        uploaded_file = st.file_uploader("Upload file:", type=["txt", "md"])
        if uploaded_file:
            transcript_text = uploaded_file.read().decode("utf-8")
            transcript_title = uploaded_file.name.split(".")[0]
    
    if transcript_text:
        st.success(f"✅ {len(transcript_text)} characters loaded")
        if st.button("📋 Preview"):
            parser = TranscriptParser()
            transcript = parser.parse(transcript_text, transcript_title)
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Scenes", len(transcript.scenes))
            with col2:
                st.metric("Characters", len(transcript.characters))
            with col3:
                st.metric("Duration", f"{transcript.duration_minutes:.1f} min")

with tab2:
    st.header("Generate Movie")
    if 'transcript_text' in locals() and transcript_text:
        if st.button("🚀 START GENERATION"):
            progress_bar = st.progress(0)
            status = st.empty()
            
            try:
                status.write("⏳ Parsing...")
                parser = TranscriptParser()
                transcript = parser.parse(transcript_text, transcript_title)
                if len(transcript.scenes) > config.MAX_SCENES_PER_MOVIE:
                    transcript.scenes = transcript.scenes[:config.MAX_SCENES_PER_MOVIE]
                progress_bar.progress(15)
                
                status.write("⏳ Enhancing narratives...")
                enhancer = NarrativeEnhancer()
                for scene in transcript.scenes:
                    enhancer.enhance_scene(scene)
                    enhancer.enhance_narration(scene)
                progress_bar.progress(30)
                
                status.write("⏳ Generating images...")
                img_gen = ImageGenerator()
                img_paths = img_gen.generate_batch(transcript.scenes)
                progress_bar.progress(50)
                
                status.write("⏳ Generating videos...")
                video_gen = VideoGenerator()
                video_paths = video_gen.generate_batch(img_paths)
                progress_bar.progress(70)
                
                status.write("⏳ Generating narration...")
                tts_gen = TTSGenerator()
                narrations = [s.narration or "" for s in transcript.scenes]
                audio_paths = tts_gen.generate_batch(narrations)
                progress_bar.progress(85)
                
                status.write("⏳ Assembling video...")
                assembler = VideoAssembler()
                final_video = assembler.assemble_video(video_paths, audio_paths, 
                    f"{transcript_title.replace(' ', '_')}_movie.mp4")
                progress_bar.progress(100)
                
                if final_video:
                    st.success(f"✅ Done! {final_video}")
                    st.video(final_video)
                else:
                    st.error("❌ Failed")
            except Exception as e:
                st.error(f"❌ Error: {e}")
    else:
        st.warning("Upload transcript first")

with tab3:
    st.header("About")
    st.markdown("""
    **Features:**
    - Parse D&D transcripts
    - Generate fantasy art (Stable Diffusion)
    - Create video clips (Pika Labs)
    - Add narration (ElevenLabs)
    - Assemble final movie (FFmpeg)
    
    **Output:** `{}`
    """.format(config.OUTPUT_DIR))

st.markdown("---")
st.markdown("<div style='text-align: center'>🐉 D&D Movie Generator v1.0</div>", unsafe_allow_html=True)
