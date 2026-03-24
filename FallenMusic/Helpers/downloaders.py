# MIT License
# Copyright (c) 2023 AnonymousX1025

import os
from yt_dlp import YoutubeDL

# Ensure downloads folder exists
if not os.path.exists("downloads"):
    os.makedirs("downloads")

ydl_opts = {
    "format": "bestaudio[ext=m4a]/bestaudio",
    "outtmpl": "downloads/%(id)s.%(ext)s",
    "quiet": True,
    "no_warnings": True,
    "nocheckcertificate": True,
    "geo_bypass": True,

    # 🔥 HARD BYPASS (important)
    "source_address": "0.0.0.0",

    # 🔥 Strong headers
    "http_headers": {
        "User-Agent": "com.google.android.youtube/17.31.35 (Linux; U; Android 11)",
        "X-YouTube-Client-Name": "3",
        "X-YouTube-Client-Version": "17.31.35"
    },

    # 🔥 ULTRA extractor bypass
    "extractor_args": {
        "youtube": {
            "player_client": ["android", "ios", "web_embedded"],
            "skip": ["dash", "hls"]
        }
    },

    # 🔥 Extra stability
    "retries": 5,
    "fragment_retries": 5,
    "noplaylist": True,
}

ydl = YoutubeDL(ydl_opts)


def audio_dl(url: str) -> str:
    try:
        info = ydl.extract_info(url, download=False)
        file_path = os.path.join("downloads", f"{info['id']}.m4a")

        if os.path.exists(file_path):
            return file_path

        ydl.download([url])
        return file_path

    except Exception as e:
        print("Download Error:", str(e))
        return None
