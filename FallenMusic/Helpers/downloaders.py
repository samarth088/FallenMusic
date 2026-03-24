# MIT License
# Copyright (c) 2023 AnonymousX1025

import os
import random
from yt_dlp import YoutubeDL

# Ensure downloads folder exists
if not os.path.exists("downloads"):
    os.makedirs("downloads")

# 🔥 Random user agents (anti-detection)
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

    # 🔥 IMPORTANT
    "default_search": "ytsearch",

    # 🔥 Anti-detection
    "http_headers": {
        "User-Agent": random.choice(USER_AGENTS)
    },

    # 🔥 Stable extractor
    "extractor_args": {
        "youtube": {
            "player_client": ["web", "android"]
        }
    },

    # 🔥 Stability
    "retries": 5,
    "fragment_retries": 5,
    "noplaylist": True,
}

ydl = YoutubeDL(ydl_opts)


def audio_dl(url: str) -> str:
    try:
        info = ydl.extract_info(url, download=True)

        # 🔥 Handle search result
        if "entries" in info:
            info = info["entries"][0]

        file_path = os.path.join("downloads", f"{info['id']}.webm")

        if os.path.exists(file_path):
            return file_path

        return file_path

    except Exception as e:
        print("Download Error:", str(e))

        # 🔥 fallback search
        try:
            info = ydl.extract_info(f"ytsearch:{url}", download=True)

            if "entries" in info:
                info = info["entries"][0]

            file_path = os.path.join("downloads", f"{info['id']}.webm")
            return file_path

        except Exception as e:
            print("Fallback Error:", str(e))
            return None
