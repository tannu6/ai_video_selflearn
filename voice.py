
import pyttsx3
def generate_voice(text, filename):
    try:
        engine = pyttsx3.init()

        engine.save_to_file(text, filename)
        engine.runAndWait()

        return filename

    except Exception as e:
        print("Voice generation error:", e)
        return None