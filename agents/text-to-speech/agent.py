import os
import subprocess
import platform
from datetime import datetime
from zoneinfo import ZoneInfo
import google.auth
from google.adk.agents import Agent
from google.cloud import texttospeech

# Config Google Cloud
_, project_id = google.auth.default()
os.environ.setdefault("GOOGLE_CLOUD_PROJECT", project_id)
os.environ["GOOGLE_CLOUD_LOCATION"] = "us-central1"
os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "True"

def speak_text(text: str) -> str:
    """Convert text to speech and play it."""
    client = texttospeech.TextToSpeechClient()
    
    # French or English?
    is_french = any(w in text.lower() for w in ["bonjour", "salut", "merci"]) or "ç" in text
    lang = "fr-FR" 
    
    # Generate audio
    response = client.synthesize_speech(
        input=texttospeech.SynthesisInput(text=text),
        voice=texttospeech.VoiceSelectionParams(
            language_code=lang,
            ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
        ),
        audio_config=texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3
        )
    )
    
    # Save file
    filename = f"speech_{datetime.now().strftime('%H%M%S')}.mp3"
    with open(filename, "wb") as f:
        f.write(response.audio_content)
        print('Audio content written to file "output.mp3"')


    # Open in browser with HTML player
    player_url = f"file://{os.path.abspath('audio_player.html')}?file={filename}"
    if platform.system() == "Darwin":
        subprocess.run(["open", player_url], check=False)
    elif platform.system() == "Windows":
        subprocess.run(["start", player_url], shell=True, check=False)
    else:
        subprocess.run(["xdg-open", player_url], check=False)
    return f"Said: '{text}' | Audio playing in browser: {filename}"

def list_audio() -> str:
    """List MP3 files in current directory."""
    mp3_files = [f for f in os.listdir('.') if f.endswith('.mp3')]
    if mp3_files:
        return f"📁 Found {len(mp3_files)} audio files:\n" + "\n".join(f"  • {f}" for f in mp3_files)
    return "📁 No audio files found"

# Agent
root_agent = Agent(
    name="root_agent",
    model="gemini-2.5-flash",
    instruction="When user wants text spoken aloud, use speak_text(). For audio file list, use list_audio().",
    tools=[speak_text, list_audio]
)
