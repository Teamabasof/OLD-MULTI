import asyncio
from pyrogram import Client
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from variables import FORCE_SUB


async def ForceSub(bot: Client, cmd: Message):
    try:
        user = await bot.get_chat_member(chat_id=(int(FORCE_SUB) if FORCE_SUB.startswith("-100") else FORCE_SUB), user_id=cmd.from_user.id)
        if user.status == "banned":
            await bot.send_message(
                chat_id=cmd.from_user.id,
                text="Access Denied ⚠. Contact my [Support Group](https://t.me/BETA_BOTSUPPORT).",
                parse_mode="markdown",
                disable_web_page_preview=True
            )
            return 400
    except UserNotParticipant:
        await bot.send_message(
            chat_id=cmd.from_user.id,
            text="**Please Join My Updates Channel to use this Bot!**\n\nDue to Overload, Only Channel Subscribers can use the Bot!",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="📢 Join Updates Channel 📢", url=f"https://t.me/{FORCE_SUB}")
                    ]
                ]
            ),
            parse_mode="markdown"
        )
        return 400
    except Exception:
        await bot.send_message(
            chat_id=cmd.from_user.id,
            text="Something Went Wrong. Contact my [Support Group](https://t.me/BETA_BOTSUPPORT)",
            parse_mode="markdown",
            disable_web_page_preview=True
        )
        return 400
    return 200
