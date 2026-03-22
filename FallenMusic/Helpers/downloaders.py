# MIT License
#
# Copyright (c) 2023 AnonymousX1025
# ... (license same rehega)

import os
from yt_dlp import YoutubeDL

# Cookies file banao
cookies_content = os.environ.get('COOKIES_CONTENT')
if cookies_content:
    with open('/tmp/cookies.txt', 'w') as f:
        f.write(cookies_content)

ydl_opts = {
    "format": "bestaudio/best",
    "outtmpl": "downloads/%(id)s.%(ext)s",
    "geo_bypass": True,
    "nocheckcertificate": True,
    "quiet": True,
    "no_warnings": True,
    "prefer_ffmpeg": True,
    "cookiefile": "/tmp/cookies.txt",  # ← Yeh add hua
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
    sin = ydl.extract_info(url, False)
    x_file = os.path.join("downloads", f"{sin['id']}.mp3")
    if os.path.exists(x_file):
        return x_file
    ydl.download([url])
    return x_file
