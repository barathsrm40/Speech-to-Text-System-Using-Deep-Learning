import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source, duration=1.5)
    audio = r.listen(source)

try:
    text = r.recognize_google(audio)
    print("Improved Accuracy Output:", text)
except:
    print("Recognition failed")