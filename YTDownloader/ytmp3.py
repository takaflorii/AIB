import argparse
import traceback
import os
import shutil

def download_audio(url, out_dir=None):
    # always use yt-dlp to fetch audio, pytube removed
    try:
        from yt_dlp import YoutubeDL
    except Exception as imp_e:
        print(f"yt-dlp not installed: {imp_e}")
        return
    # prepare yt-dlp options for audio mp3
    tmpl = "%(title)s.%(ext)s"
    if out_dir:
        tmpl = os.path.join(out_dir, tmpl)
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": tmpl,
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }],
    }
    ffmpeg_path = shutil.which("ffmpeg")
    if ffmpeg_path:
        ydl_opts["ffmpeg_location"] = ffmpeg_path
    else:
        ydl_opts.pop("postprocessors")
    try:
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            downloaded_ext = info.get('ext')
            title = info.get('title')
        if not ffmpeg_path:
            src = f"{title}.{downloaded_ext}"
            dst = f"{title}.mp3"
            try:
                os.replace(src, dst)
                print(f"Downloaded audio saved as {dst} (ffmpeg not installed, file may not be true mp3)")
                if os.path.exists(src):
                    try:
                        os.remove(src)
                    except Exception:
                        pass
            except Exception:
                print(f"Could not rename {src} to {dst}")
        else:
            print("Audio downloaded successfully")
    except Exception as yde:
        print(f"yt-dlp download failed: {yde}")
        traceback.print_exc()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download YouTube audio as MP3")
    parser.add_argument("url", nargs="?", help="YouTube video URL")
    parser.add_argument("-o", "--output", help="Directory to save file", default=".")
    args = parser.parse_args()
    if args.url:
        url = args.url
    else:
        url = input("Enter the YouTube video URL: ")
    download_audio(url, out_dir=args.output)