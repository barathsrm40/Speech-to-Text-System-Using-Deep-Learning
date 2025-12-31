from model_loader import load_asr_model

def transcribe_audio(audio_file):
    """
    Transcribes the given audio file to text using the ASR model.
    
    Args:
        audio_file (str): Path to the audio file.
    
    Returns:
        str: Transcribed text.
    """
    model = load_asr_model()
    result = model.transcribe(audio_file)
    return result.get("text", "")  # Use get to avoid KeyError if "text" is missing

if __name__ == "__main__":
    audio_path = "audio.wav"
    try:
        text = transcribe_audio(audio_path)
        print("Recognized Text:")
        print(text if text else "[No text recognized]")
    except Exception as e:
        print(f"Error during transcription: {e}")