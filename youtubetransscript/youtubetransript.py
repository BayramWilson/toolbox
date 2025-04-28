import whisper
import yt_dlp
import os

def download_audio(video_url, output_file="audio"):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f"{output_file}.%(ext)s",  # Ohne .mp3 anhängen!
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(video_url, download=True)
        title = info.get('title', None)
        # Hole den tatsächlichen Dateinamen des Audios:
        filename = ydl.prepare_filename(info).replace('.webm', '.mp3').replace('.m4a', '.mp3')
    
    return title, filename

def transcribe_youtube_video(video_url):
    title, audio_file = download_audio(video_url)
    print(f"Titel des Videos: {title}")

    model = whisper.load_model("base")
    print("Transkribiere und erkenne Sprache...")
    result = model.transcribe(audio_file)

    detected_language = result['language']
    transcript_text = result['text']

    os.remove(audio_file)
    return detected_language, transcript_text

if __name__ == "__main__":
    video_url = input("Gib die URL des YouTube-Videos ein: ")
    language, transcript = transcribe_youtube_video(video_url)

    print(f"\nErkannte Sprache: {language}")
    print("\n--- Transkript ---\n")
    print(transcript)
