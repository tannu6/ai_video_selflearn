# main.py

from idea_generation import get_topic
from script import generate_script
from image import generate_image
from voice import generate_voice
from video import create_video


def split_sentences(text):
    """Split script into clean sentences."""
    sentences = text.replace("\n", " ").split(".")
    return [s.strip() for s in sentences if s.strip()]


def run_pipeline():
    print("Selecting topic...")
    topic = get_topic()
    print("Topic:", topic)

    # ---------- SCRIPT ----------
    print("\nGenerating script...")
    script_text = generate_script(topic)

    if not script_text:
        print("❌ Script generation failed")
        return

    print("Script generated:\n", script_text)

    # ---------- SPLIT INTO SENTENCES ----------
    print("\nSplitting script into sentences...")
    sentences = split_sentences(script_text)

    if not sentences:
        print("❌ No sentences found")
        return

    audio_files = []
    image_files = []

    # ---------- PROCESS EACH SENTENCE ----------
    for i, sentence in enumerate(sentences):
        print(f"\nProcessing sentence {i+1}: {sentence}")

        # 🎤 Generate voice for this sentence
        voice_filename = f"voice_{i}.mp3"
        voice_file = generate_voice(sentence, voice_filename)

        if not voice_file:
            print("❌ Voice generation failed")
            return

        audio_files.append(voice_file)

        # 🖼 Generate image for this sentence
        img_path = generate_image(sentence, i)

        if not img_path:
            print("❌ Image generation failed")
            return

        image_files.append(img_path)

    print("\nImages created:", image_files)
    print("Audio files created:", audio_files)

    # ---------- VIDEO ----------
    print("\nAssembling synced explainer video...")
    create_video(image_files, audio_files)

    print("\n✅ DONE — final_video.mp4 created successfully!")


if __name__ == "__main__":
    run_pipeline()