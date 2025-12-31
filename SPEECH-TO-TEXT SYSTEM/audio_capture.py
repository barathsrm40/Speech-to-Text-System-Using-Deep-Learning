import speech_recognition as sr

def record_audio(filename="audio.wav", duration=None):
    """
    Records audio from the microphone and saves it as a WAV file.

    Parameters:
        filename (str): Name of the output audio file
        duration (int or None): Recording duration in seconds.
                                If None, records until silence is detected.

    Returns:
        bool: True if audio recorded successfully, False otherwise
    """

    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=1.0)
            
            if duration:
                audio = recognizer.record(source, duration=duration)
            else:
                audio = recognizer.listen(source)

        with open(filename, "wb") as audio_file:
            audio_file.write(audio.get_wav_data())

        return True

    except Exception:
        return False