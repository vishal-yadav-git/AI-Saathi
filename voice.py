import vosk
import sounddevice as sd
import json

model = vosk.Model("model")

def listen():
    rec = vosk.KaldiRecognizer(model, 16000)

    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16', channels=1) as stream:
        print("🎤 Bolna start karo...")

        while True:
            data, _ = stream.read(4000)
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                return result.get("text", "")