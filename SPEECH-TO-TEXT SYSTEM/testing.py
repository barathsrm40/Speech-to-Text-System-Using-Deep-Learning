test_files = ["audio1.wav", "audio2.wav", "audio3.wav"]

import whisper
model = whisper.load_model("base")

for file in test_files:
    print("Testing:", file)
    result = model.transcribe(file)
    print(result["text"])