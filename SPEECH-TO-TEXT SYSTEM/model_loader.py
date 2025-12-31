import whisper

def load_asr_model(model_name="base"):
    print("Loading Whisper Model...")
    model = whisper.load_model(model_name)
    print("Model Loaded Successfully")
    return model