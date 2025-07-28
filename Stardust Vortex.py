#!/usr/bin/env python3
import os
import subprocess
import sys

MUSIC_DIR = os.path.expanduser("~/Music")
VIDEO_DIR = os.path.expanduser("~/Videos")

BANNER = r"""
  ██████╗ ██████╗ ██████╗ ███████╗██████╗ ███████╗████████╗    ██████╗ ███████╗ █████╗ ████████╗
 ██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔══██╗██╔════╝╚══██╔══╝    ██╔══██╗██╔════╝██╔══██╗╚══██╔══╝
 ██║     ██║   ██║██████╔╝█████╗  ██████╔╝█████╗     ██║       ██████╔╝█████╗  ███████║   ██║   
 ██║     ██║   ██║██╔══██╗██╔══╝  ██╔═══╝ ██╔══╝     ██║       ██╔═══╝ ██╔══╝  ██╔══██║   ██║   
 ╚██████╗╚██████╔╝██║  ██║███████╗██║     ███████╗   ██║       ██║     ███████╗██║  ██║   ██║   
  ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝     ╚══════╝   ╚═╝       ╚═╝     ╚══════╝╚═╝  ╚═╝   ╚═╝   
                        🌌 Stardust Vortex - v1.1 🌌
"""

def download_audio(url):
    try:
        print(f"\n🎧 Downloading audio from: {url}\n")
        subprocess.run([
            "yt-dlp", "--extract-audio", "--audio-format", "mp3", "-o",
            os.path.join(MUSIC_DIR, "%(title)s.%(ext)s"), url
        ])
        print("\n✅ Done! Check your Music folder.")
    except Exception as e:
        print(f"❌ Error: {e}")

def download_video():
    try:
        url = input("🎥 Enter the YouTube video URL: ").strip()
        out_path = os.path.join(VIDEO_DIR, "%(title)s.%(ext)s")
        print(f"\n📽️  Downloading video to: {out_path}")
        subprocess.run([
            "yt-dlp", "-f", "bestvideo+bestaudio",
            "--merge-output-format", "mp4",
            "-o", out_path, url
        ])
        print("\n✅ Video download complete!")
    except Exception as e:
        print(f"❌ Error: {e}")

def download_playlist():
    try:
        url = input("📺 Enter the YouTube playlist URL: ").strip()
        out_path = os.path.join(VIDEO_DIR, "%(playlist_title)s/%(title)s.%(ext)s")
        print(f"\n📥 Downloading playlist to: {VIDEO_DIR}/<playlist_name>/")
        subprocess.run([
            "yt-dlp", "-f", "bestvideo+bestaudio",
            "--yes-playlist", "--merge-output-format", "mp4",
            "-o", out_path, url
        ])
        print("\n✅ Playlist downloaded!")
    except Exception as e:
        print(f"❌ Error: {e}")

def menu():
    os.system("clear")
    print(BANNER)
    print("1. Download from YouTube (Audio Only)")
    print("2. Download from SoundCloud (Audio Only)")
    print("3. Paste any supported link (Audio Only)")
    print("4. Download a YouTube Video (MP4)")
    print("5. Download a YouTube Playlist (MP4)")
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
    elif choice == "4":
        download_video()
    elif choice == "5":
        download_playlist()
    elif choice == "0":
        print("👋 Bye!")
        sys.exit()
    else:
        print("❌ Invalid choice.")

    input("\nPress Enter to return to the menu...")
    menu()

if __name__ == "__main__":
    menu()
