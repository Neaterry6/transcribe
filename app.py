from flask import Flask, request, jsonify
import os
from assemblyai_transcriber import transcribe_audio

app = Flask(__name__)

@app.route("/transcribe", methods=["POST"])
def transcribe():
    if "audio" not in request.files:
        return jsonify({"error": "❌ No audio file uploaded!"}), 400

    audio_file = request.files["audio"]
    file_path = "uploads/temp_audio.mp3"  # Adjust format if needed
    audio_file.save(file_path)

    # Transcribe using AssemblyAI
    transcription = transcribe_audio(file_path)

    os.remove(file_path)  # Cleanup
    return jsonify({"transcription": transcription})

if __name__ == "__main__":
    PORT = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=PORT, debug=True)
