import assemblyai as aai

# Set your AssemblyAI API Key
aai.settings.api_key = "22b87c4a57e04c73914de4b75edd05c1"

def transcribe_audio(audio_path):
    """Send audio to AssemblyAI for transcription"""
    config = aai.TranscriptionConfig()
    transcript = aai.Transcriber(config=config).transcribe(audio_path)
    
    return transcript.text
