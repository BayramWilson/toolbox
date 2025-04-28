import whisper
import yt_dlp
import os
import re

def sanitize_filename(name):
    # Entferne unzulässige Zeichen für Dateinamen
    return re.sub(r'[\\\\/*?:"<>|]', "", name)

def download_audio(video_url, output_file="audio"):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f"{output_file}.%(ext)s",
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
        filename = ydl.prepare_filename(info).replace('.webm', '.mp3').replace('.m4a', '.mp3')
    
    return title, filename

def transcribe_and_save(video_url):
    title, audio_file = download_audio(video_url)
    print(f"Titel des Videos: {title}")

    model = whisper.load_model("base")
    print("Transkribiere und erkenne Sprache...")
    result = model.transcribe(audio_file)

    detected_language = result['language']
    transcript_text = result['text']

    # Datei speichern
    safe_title = sanitize_filename(title)
    output_filename = f"{safe_title}.txt"
    with open(output_filename, "w", encoding="utf-8") as f:
        f.write(f"Detected language: {detected_language}\n\n")
        f.write(transcript_text)

    print(f"\nTranskript gespeichert in: {output_filename}")

    os.remove(audio_file)

if __name__ == "__main__":
    video_url = input("Gib die URL des YouTube-Videos ein: ")
    transcribe_and_save(video_url)
