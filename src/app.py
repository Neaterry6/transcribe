from flask import Flask, request, jsonify
from transcriber.py import VoskTranscriber
import os
import wave

app = Flask(__name__)
transcriber = VoskTranscriber("models/vosk-model-en-us-0.22")

@app.route("/transcribe", methods=["POST"])
def transcribe_audio():
    if "audio" not in request.files:
        return jsonify({"error": "❌ No audio file uploaded!"}), 400

    audio_file = request.files["audio"]
    file_path = "uploads/temp_audio.wav"
    audio_file.save(file_path)

    # Transcribe audio using Vosk
    transcription = transcriber.transcribe(file_path)
    
    os.remove(file_path)  # Cleanup
    return jsonify({"transcription": transcription})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True
