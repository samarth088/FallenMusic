# MIT License
# Copyright (c) 2023 AnonymousX1025

import os
import random
from yt_dlp import YoutubeDL

if not os.path.exists("downloads"):
    os.makedirs("downloads")

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (Linux; Android 11)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X)"
]

ydl_opts = {
    "format": "bestaudio/best",
    "outtmpl": "downloads/%(id)s.%(ext)s",

    "quiet": True,
    "no_warnings": True,
    "nocheckcertificate": True,
    "geo_bypass": True,

    "default_search": "ytsearch",

    "http_headers": {
        "User-Agent": random.choice(USER_AGENTS)
    },

    "noplaylist": True,
}

ydl = YoutubeDL(ydl_opts)


def audio_dl(url: str) -> str:
    try:
        info = ydl.extract_info(url, download=True)

        # 🔥 if search result
        if "entries" in info:
            info = info["entries"][0]

        # 🔥 REAL FILE PATH (IMPORTANT)
        file_path = ydl.prepare_filename(info)

        # sometimes ext mismatch → fix
        if not os.path.exists(file_path):
            base = file_path.rsplit(".", 1)[0]
            for ext in ["webm", "m4a", "mp3", "opus"]:
                if os.path.exists(base + "." + ext):
                    return base + "." + ext

        return file_path

    except Exception as e:
        print("Download Error:", str(e))
        return None
