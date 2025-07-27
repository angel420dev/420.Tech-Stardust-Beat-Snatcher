import os
import subprocess
import sys

MUSIC_DIR = os.path.expanduser("~/Music")

BANNER = r"""
  ██████╗ ██████╗ ██████╗ ███████╗██████╗ ███████╗████████╗    ██████╗ ███████╗ █████╗ ████████╗
 ██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔══██╗██╔════╝╚══██╔══╝    ██╔══██╗██╔════╝██╔══██╗╚══██╔══╝
 ██║     ██║   ██║██████╔╝█████╗  ██████╔╝█████╗     ██║       ██████╔╝█████╗  ███████║   ██║   
 ██║     ██║   ██║██╔══██╗██╔══╝  ██╔═══╝ ██╔══╝     ██║       ██╔═══╝ ██╔══╝  ██╔══██║   ██║   
 ╚██████╗╚██████╔╝██║  ██║███████╗██║     ███████╗   ██║       ██║     ███████╗██║  ██║   ██║   
  ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝     ╚══════╝   ╚═╝       ╚═╝     ╚══════╝╚═╝  ╚═╝   ╚═╝   
                        🌌 STARDUST BEATSNATCHER - v1.0 🌌
"""

def download_audio(url):
    try:
        print(f"\n🎧 Downloading from: {url}\n")
        subprocess.run([
            "yt-dlp", "--extract-audio", "--audio-format", "mp3", "-o",
            os.path.join(MUSIC_DIR, "%(title)s.%(ext)s"), url
        ])
        print("\n✅ Done! Check your Music folder.")
    except Exception as e:
        print(f"❌ Error: {e}")

def menu():
    os.system("clear")
    print(BANNER)
    print("1. Download from YouTube")
    print("2. Download from SoundCloud")
    print("3. Paste link (yt/soundcloud/others supported)")
    print("0. Exit\n")

    choice = input("🎵 Choose an option: ").strip()

    if choice == "1":
        url = input("🔗 Enter YouTube URL: ").strip()
        download_audio(url)
    elif choice == "2":
        url = input("🔗 Enter SoundCloud URL: ").strip()
        download_audio(url)
    elif choice == "3":
        url = input("🔗 Paste any supported link: ").strip()
        download_audio(url)
    elif choice == "0":
        print("👋 Bye!")
        sys.exit()
    else:
        print("❌ Invalid choice.")

    input("\nPress Enter to return to the menu...")
    menu()

if __name__ == "__main__":
    menu()
