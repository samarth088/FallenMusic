# MIT License
# Copyright (c) 2023 AnonymousX1025

import asyncio
import os

from pyrogram import filters
from pyrogram.enums import ChatMemberStatus
from pyrogram.errors import (
    ChatAdminRequired,
    UserAlreadyParticipant,
    UserNotParticipant,
)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from pytgcalls import StreamType
from pytgcalls.exceptions import NoActiveGroupCall
from pytgcalls.types import AudioPiped, HighQualityAudio
from youtube_search import YoutubeSearch

from FallenMusic import (
    ASS_ID,
    ASS_NAME,
    BOT_NAME,
    LOGGER,
    app,
    app2,
    pytgcalls,
)
from FallenMusic.Helpers.downloaders import audio_dl
from FallenMusic.Helpers.gets import get_file_name, get_url
from FallenMusic.Helpers.active import stream_on, add_active_chat


@app.on_message(
    filters.command(["play", "vplay", "p"])
    & filters.group
)
async def play(_, message: Message):
    fallen = await message.reply_text("🎧 Processing...")

    try:
        await message.delete()
    except:
        pass

    # 🔥 ensure assistant join
    try:
        await app.get_chat_member(message.chat.id, ASS_ID)
    except:
        try:
            link = await app.export_chat_invite_link(message.chat.id)
            await app2.join_chat(link)
        except:
            return await fallen.edit_text("❌ Assistant join failed")

    audio = (
        (message.reply_to_message.audio or message.reply_to_message.voice)
        if message.reply_to_message
        else None
    )

    url = get_url(message)

    # 🎵 AUDIO FILE
    if audio:
        file_name = get_file_name(audio)
        file_path = await message.reply_to_message.download(file_name)

    # 🔗 DIRECT URL
    elif url:
        file_path = audio_dl(url)

        # 🔥 fallback search if blocked
        if not file_path:
            file_path = audio_dl(f"ytsearch:{url}")

        if not file_path:
            return await fallen.edit_text("❌ Failed to fetch audio")

    # 🔍 SEARCH QUERY
    else:
        if len(message.command) < 2:
            return await fallen.edit_text("❌ Give song name")

        query = message.text.split(None, 1)[1]

        # 🔥 direct search (no youtube_search dependency)
        file_path = audio_dl(f"ytsearch:{query}")

        if not file_path:
            return await fallen.edit_text("❌ No results found")

    # 🎧 PLAY
    stream = AudioPiped(file_path, audio_parameters=HighQualityAudio())

    try:
        await pytgcalls.join_group_call(
            message.chat.id,
            stream,
            stream_type=StreamType().pulse_stream,
        )
    except NoActiveGroupCall:
        return await fallen.edit_text("❌ Start voice chat first")

    await stream_on(message.chat.id)
    await add_active_chat(message.chat.id)

    return await fallen.delete()
