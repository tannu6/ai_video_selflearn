from moviepy import ImageClip, AudioFileClip, concatenate_videoclips


def create_video(images, audio_files):
    clips = []

    for img, audio_path in zip(images, audio_files):
        audio = AudioFileClip(audio_path)

        # Set image duration equal to audio duration
        image_clip = ImageClip(img).with_duration(audio.duration)

        # Attach audio
        image_clip = image_clip.with_audio(audio)

        clips.append(image_clip)

    final_video = concatenate_videoclips(clips)

    final_video.write_videofile("final_video.mp4", fps=24)