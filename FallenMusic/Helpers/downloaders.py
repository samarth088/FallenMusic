# MIT License
#
# Copyright (c) 2023 AnonymousX1025

import os
from yt_dlp import YoutubeDL

# 👉 Ensure downloads folder exists
if not os.path.exists("downloads"):
    os.makedirs("downloads")

# 👉 FINAL yt-dlp config (Render + cookies working)
ydl_opts = {
    "format": "bestaudio/best",
    "outtmpl": "downloads/%(id)s.%(ext)s",
    "geo_bypass": True,
    "nocheckcertificate": True,
    "quiet": True,
    "no_warnings": True,
    "prefer_ffmpeg": True,

    # ✅ IMPORTANT: Render secret file path
    "cookiefile": "/etc/secrets/cookies.txt",

    # ✅ Avoid bot detection
    "http_headers": {
        "User-Agent": "Mozilla/5.0",
        "Referer": "https://www.youtube.com/"
    },

    # ✅ Playlist issues avoid
    "noplaylist": True,

    # ✅ Audio convert
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "320",
        }
    ],
}

ydl = YoutubeDL(ydl_opts)


def audio_dl(url: str) -> str:
    try:
        info = ydl.extract_info(url, download=False)
        file_path = os.path.join("downloads", f"{info['id']}.mp3")

        if os.path.exists(file_path):
            return file_path

        ydl.download([url])
        return file_path

    except Exception as e:
        print("Download Error:", str(e))
        return None
