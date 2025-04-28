Absolutely! Here’s the full **README.md** in Markdown format:

```markdown
# YouTube Auto Transcription Tool 🎙️

This tool downloads audio from a YouTube video and automatically transcribes it using OpenAI's Whisper model. It detects the language of the audio and provides an accurate transcript.

## Features

- 🎯 **Automatic language detection**
- 📝 **Accurate transcriptions** with Whisper
- 🔗 **Works with any YouTube video**
- 🎧 **Audio-only download** for efficient processing

## Requirements

- Python 3.8+
- `ffmpeg` installed on your system
- Python packages:
  - `yt-dlp`
  - `openai-whisper`
  - `torch`

Install dependencies with:

```bash
pip install -r requirements.txt
```

## Install ffmpeg (if not installed)

**Ubuntu:**

```bash
sudo apt update
sudo apt install ffmpeg
```

**Mac (Homebrew):**

```bash
brew install ffmpeg
```

**Windows:**

Download from [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html) and add to PATH.

## Usage

Run the script:

```bash
python youtubetranscript.py
```

Enter the YouTube video URL when prompted.  
The tool will:

1. Download the audio.
2. Detect the language automatically.
3. Transcribe the audio.
4. Output the detected language and transcript.

## Example

```bash
Gib die URL des YouTube-Videos ein: https://www.youtube.com/watch?v=dQw4w9WgXcQ
Titel des Videos: Rick Astley - Never Gonna Give You Up (Video)
Transkribiere und erkenne Sprache...

Detected language: en

--- Transcript ---

We're no strangers to love...
```

## License

MIT License
```

---

Let me know if you'd like to add anything else, like badges or links! 🚀