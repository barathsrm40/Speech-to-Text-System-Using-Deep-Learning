import whisper
import speech_recognition as sr

r = sr.Recognizer()
model = whisper.load_model("base")

with sr.Microphone() as source:
    print("Speak now...")
    audio = r.listen(source)

with open("final_audio.wav", "wb") as f:
    f.write(audio.get_wav_data())

result = model.transcribe("final_audio.wav")
print("Final Output:")
print(result["text"])