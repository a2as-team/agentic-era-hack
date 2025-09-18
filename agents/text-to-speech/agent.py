import os
import webbrowser
from datetime import datetime
from zoneinfo import ZoneInfo
import google.auth
from google.adk.agents import Agent
from google.cloud import texttospeech
from google.cloud import storage

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
    
    # Save file locally and upload to GCP bucket
    filename = f"speech_{datetime.now().strftime('%H%M%S')}.mp3"
    with open(filename, "wb") as f:
        f.write(response.audio_content)
    
    # Upload to GCP bucket
    bucket_name = "qwiklabs-gcp-03-c44e7446f764-skillscape-hackathon-ia-tts-data"
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(filename)
    blob.upload_from_filename(filename)
    
    # Generate authenticated URL (valid for 1 hour)
    from datetime import timedelta
    authenticated_url = blob.generate_signed_url(
        version="v4",
        expiration=timedelta(hours=1),
        method="GET"
    )


    # Open in browser with HTML player
    player_url = f"file://{os.path.abspath('audio_player.html')}?file={authenticated_url}"
    webbrowser.open(player_url)
    return f"Said: '{text}' | Audio playing in browser from GCP: {authenticated_url}"

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
