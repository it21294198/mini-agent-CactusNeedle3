# CactusNeedle3

A Python project exploring local AI capabilities with [Needle](https://github.com/cactus-compute/needle), including speech-to-text transcription and the foundations for building voice-controlled AI agents.

## Features

- **Speech-to-Text:** Transcribe audio recordings using Needle's transcription functionality.
- **Audio Conversion:** Convert MP3 and other supported audio formats into compatible WAV files using FFmpeg.
- **Local AI Exploration:** Experiment with lightweight AI inference and tool calling.
- **Voice Assistant Foundation:** Prepare for integrating speech recognition with Python tools and automated workflows.

## Tech Stack

- Python 3.10+
- Cactus Needle (`cactus-needle`)
- FFmpeg
- Python virtual environment (`venv`)

## Project Structure

```text
CactusNeedle3/
├── .venv/              # Python virtual environment
├── needle-voice.py     # Audio transcription script
├── test.wav            # Original MP3 audio (incorrect extension)
├── test_fixed.wav      # Converted WAV audio
└── README.md           # Project documentation
```

## Prerequisites

Ensure the following tools are installed:

- Python 3.10 or newer
- Homebrew on macOS
- FFmpeg

Install FFmpeg:

```bash
brew install ffmpeg
```

## Installation

### 1. Clone the Repository

If the project is hosted on GitHub:

```bash
git clone <YOUR_REPOSITORY_URL>
cd CactusNeedle3
```

Alternatively, navigate to your existing project directory.

### 2. Create a Virtual Environment

```bash
python3 -m venv .venv
```

### 3. Activate the Virtual Environment

On macOS or Linux:

```bash
source .venv/bin/activate
```

### 4. Install Needle

```bash
python -m pip install --upgrade pip
python -m pip install cactus-needle
```

## Audio Preparation

Needle's WAV reader expects a valid WAV file, not an MP3 file renamed with a `.wav` extension.

For example, the command below identifies the actual format of your audio:

```bash
file test.wav
```

If the output identifies the file as MPEG Layer III audio, convert it before transcription.

### Convert Audio to WAV

```bash
ffmpeg -i test.wav \
  -ar 16000 \
  -ac 1 \
  -c:a pcm_s16le \
  test_fixed.wav
```

This produces audio with the following properties:

| Property | Value |
|---|---|
| Container | WAV |
| Audio encoding | PCM signed 16-bit little-endian |
| Sample rate | 16,000 Hz |
| Channels | Mono |

Verify the converted file:

```bash
file test_fixed.wav
```

You can also inspect its audio properties:

```bash
ffprobe -v error \
  -show_entries stream=codec_name,sample_rate,channels \
  -of default=noprint_wrappers=1 \
  test_fixed.wav
```

## Speech-to-Text Transcription

Create or update `needle-voice.py`:

```python
import needle

def main():
    audio_file = "test_fixed.wav"

    result = needle.transcribe(audio_file)

    print("Transcription:", result["text"])

if __name__ == "__main__":
    main()
```

Run the script:

```bash
python needle-voice.py
```

The first execution may download the model configuration and required model assets.

If transcription succeeds, the recognized speech will be printed to the terminal.

## Troubleshooting

### Error: `wave.Error: test.wav is not a WAV file`

**Cause:** The file contains MP3 audio or another unsupported format.

**Solution:** Convert it to WAV using FFmpeg:

```bash
ffmpeg -i test.wav -ar 16000 -ac 1 -c:a pcm_s16le test_fixed.wav
```

Update the Python script to use `test_fixed.wav`.

### Error: `ffmpeg: command not found`

Install FFmpeg:

```bash
brew install ffmpeg
```

### Error: `ModuleNotFoundError: No module named 'needle'`

Activate the virtual environment and install the package:

```bash
source .venv/bin/activate
python -m pip install cactus-needle
```

### Transcription Returns Incorrect or Empty Text

Check that:

- The recording contains audible speech.
- The audio file is not corrupted.
- The correct file path is being used.
- The recording language is supported by the model.
- The audio is clear enough for speech recognition.

## Future Improvements

Potential extensions include:

- Real-time microphone transcription.
- Voice-controlled Python tools.
- Natural-language commands for desktop applications.
- Integration with REST APIs and backend services.
- A local voice assistant using Needle's tool-calling capabilities.
- Integration with Rust/Axum microservices.
- Speech-driven hardware control with appropriate safety validation.

## Resources

- [Needle GitHub Repository](https://github.com/cactus-compute/needle)
- [FFmpeg Documentation](https://ffmpeg.org/documentation.html)
- [Python Documentation](https://docs.python.org/3/)

## License

Add an appropriate license before distributing this project publicly.