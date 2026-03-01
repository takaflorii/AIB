from pytube import YouTube
import traceback
import os

# This script tries pytube first, then falls back to yt-dlp.
# Changed to download highest-resolution MP4 video.

def download_video(url):
    try:
        yt = YouTube(url)
        video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        if video is None:
            video = yt.streams.get_highest_resolution()
        out = video.download()
        # ensure .mp4 extension
        base, ext = os.path.splitext(out)
        if ext.lower() != ".mp4":
            new = base + ".mp4"
            os.replace(out, new)
            out = new
        print(f"Video downloaded successfully: {out}")
    except Exception as e:
        print(f"There was an error: {e}")
        traceback.print_exc()
        print("Falling back to yt-dlp...")
        try:
            from yt_dlp import YoutubeDL
        except Exception as imp_e:
            print(f"yt-dlp not available: {imp_e}")
            return

        ydl_opts = {
            # download best mp4 video (merge video+audio) using ffmpeg if available
            "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4",
            "outtmpl": "%(title)s.%(ext)s",
        }
        try:
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            print("Video downloaded with yt-dlp successfully!")
        except Exception as yde:
            print(f"yt-dlp failed: {yde}")
            traceback.print_exc()


if __name__ == "__main__":
    url = input("Enter the YouTube video URL: ")
    download_video(url)
