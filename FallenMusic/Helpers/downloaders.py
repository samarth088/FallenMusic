# MIT License
# Copyright (c) 2023 AnonymousX1025

import os
from yt_dlp import YoutubeDL

# Ensure downloads folder exists
if not os.path.exists("downloads"):
    os.makedirs("downloads")

ydl_opts = {
    "format": "bestaudio/best",
    "outtmpl": "downloads/%(id)s.%(ext)s",

    "quiet": True,
    "no_warnings": True,
    "nocheckcertificate": True,
    "geo_bypass": True,

    # 🔥 IMPORTANT (search fix)
    "default_search": "ytsearch",

    # 🔥 Stable headers (not overkill)
    "http_headers": {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    },

    # 🔥 CLEAN extractor (no over-bypass)
    "extractor_args": {
        "youtube": {
            "player_client": ["web", "android"]
        }
    },

    "noplaylist": True,
}

ydl = YoutubeDL(ydl_opts)


def audio_dl(url: str) -> str:
    try:
        info = ydl.extract_info(url, download=True)

        file_path = os.path.join("downloads", f"{info['id']}.webm")

        return file_path

    except Exception as e:
        print("Download Error:", str(e))
        return None
