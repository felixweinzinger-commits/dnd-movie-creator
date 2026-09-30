"""Test script to verify D&D Movie Generator setup"""
import sys
from pathlib import Path

# Add project to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

def test_imports():
    """Test that all modules can be imported"""
    print("Testing imports...")
    try:
        import config
        print("✅ config module")
        
        from utils.logger import setup_logger
        print("✅ logger module")
        
        from src.models import Transcript, Scene, Character
        print("✅ models module")
        
        from src.transcript_parser import TranscriptParser
        print("✅ transcript_parser module")
        
        from src.narrative_enhancer import NarrativeEnhancer
        print("✅ narrative_enhancer module")
        
        from src.image_generator import ImageGenerator
        print("✅ image_generator module")
        
        from src.video_generator import VideoGenerator
        print("✅ video_generator module")
        
        from src.tts_generator import TTSGenerator
        print("✅ tts_generator module")
        
        from src.video_assembler import VideoAssembler
        print("✅ video_assembler module")
        
        return True
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False

def test_parser():
    """Test transcript parser"""
    print("\nTesting transcript parser...")
    try:
        from src.transcript_parser import TranscriptParser
        
        sample_text = """
        DM: You enter a dark tavern.
        Bard: I order an ale.
        DM: The bartender serves you.
        """
        
        parser = TranscriptParser()
        transcript = parser.parse(sample_text, "Test Campaign")
        
        assert transcript.title == "Test Campaign"
        assert len(transcript.characters) > 0
        assert len(transcript.scenes) > 0
        
        print(f"✅ Parser working: {len(transcript.scenes)} scenes, {len(transcript.characters)} characters")
        return True
    except Exception as e:
        print(f"❌ Parser error: {e}")
        return False

def test_output_dirs():
    """Test output directories"""
    print("\nTesting output directories...")
    try:
        import config
        
        assert config.OUTPUT_DIR.exists(), "Output directory missing"
        print(f"✅ Output directory: {config.OUTPUT_DIR}")
        
        return True
    except Exception as e:
        print(f"❌ Directory error: {e}")
        return False

def test_config():
    """Test configuration"""
    print("\nTesting configuration...")
    try:
        import config
        
        print(f"✅ Project root: {config.PROJECT_ROOT}")
        print(f"✅ Max scenes: {config.MAX_SCENES_PER_MOVIE}")
        print(f"✅ Video FPS: {config.VIDEO_FPS}")
        print(f"✅ Local Stable Diffusion: {config.USE_LOCAL_STABLE_DIFFUSION}")
        
        return True
    except Exception as e:
        print(f"❌ Config error: {e}")
        return False

def main():
    """Run all tests"""
    print("=" * 50)
    print("D&D Movie Generator - Setup Verification")
    print("=" * 50)
    
    results = {
        "Imports": test_imports(),
        "Parser": test_parser(),
        "Output Dirs": test_output_dirs(),
        "Config": test_config(),
    }
    
    print("\n" + "=" * 50)
    print("Test Results:")
    print("=" * 50)
    
    for test_name, result in results.items():
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{test_name}: {status}")
    
    all_passed = all(results.values())
    
    print("\n" + "=" * 50)
    if all_passed:
        print("✅ All tests passed! Ready to use.")
        print("\nNext steps:")
        print("1. Configure .env with API keys (optional)")
        print("2. Run: python -m streamlit run app.py")
        print("3. Or run: run.bat")
    else:
        print("❌ Some tests failed. Check errors above.")
    print("=" * 50)
    
    return 0 if all_passed else 1

if __name__ == "__main__":
    sys.exit(main())
