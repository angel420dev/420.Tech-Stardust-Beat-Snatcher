# Stardust BeatSnatcher 🎵🌌

**Stardust BeatSnatcher** is a multi-tool music downloader that lets you download music from YouTube, SoundCloud, and Spotify (via a workaround). It saves your downloaded music directly to your **Music folder** so you can enjoy it offline!

**Created by**: Adeline (angel420dev)

## REQUIREMENTS

- **Python 3.x+**
- **yt-dlp**: For downloading videos and audio from YouTube and SoundCloud
- **ffmpeg**: To convert audio files to MP3 format

### Installation for **Linux**:
1. **Install dependencies** via `apt`:
    ```bash
    sudo apt update
    sudo apt install python3 python3-pip ffmpeg
    ```
2. **Install `yt-dlp`** using pip:
    ```bash
    pip3 install yt-dlp
    ```

### Installation for **Windows**:
1. **Install Python 3.x** from [python.org](https://www.python.org/downloads/).
2. **Install `yt-dlp`** using pip:
    ```bash
    pip install yt-dlp
    ```
3. **Install `ffmpeg`**:
    - Download from [ffmpeg.org](https://ffmpeg.org/download.html).
    - Follow instructions to add `ffmpeg` to your system's PATH.

## INSTALLATION

1. Clone this repository:

    ```bash
    git clone https://github.com/your-username/stardust-beatsnatcher.git
    ```

2. **Install the Python dependencies** (if not installed already):

    ```bash
    pip3 install yt-dlp
    ```

3. **Ensure `ffmpeg` is installed** as per the instructions above for your platform.

## HOW TO RUN

To run the program, navigate to the folder where the project is saved and execute the script:

```bash
python3 stardust_beatsnatcher.py

NOTES
If you need Spotify support, you can use spotdl, which will search for the track on YouTube and download it.

To avoid issues with yt-dlp or spotdl, make sure ffmpeg is installed and added to your PATH (as it’s used for audio conversion).

If you encounter any issues or have questions, feel free to open an issue in this repository or contact me directly through Discord (angel420.dev).
