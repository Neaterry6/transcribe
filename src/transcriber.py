from vosk import Model, KaldiRecognizer
import wave
import json

class VoskTranscriber:
    def __init__(self, model_path):
        self.model = Model(model_path)

    def transcribe(self, audio_path):
        wf = wave.open(audio_path, "rb")
        recognizer = KaldiRecognizer(self.model, wf.getframerate())
        recognizer.SetWords(True)

        transcription = ""
        while True:
            data = wf.readframes(4000)
            if len(data) == 0:
                break
            if recognizer.AcceptWaveform(data):
                result = json.loads(recognizer.Result())
                transcription += result.get("text", "") + " "

        return transcription.strip(
