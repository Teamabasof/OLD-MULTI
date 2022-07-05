import asyncio
from pyrogram import Client
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from variables import FORCE_SUB


async def BanChek(bot: Client, cmd: Message):
    if not FORCE_SUB:
      return False
    try:
        user = await bot.get_chat_member(chat_id=(int(FORCE_SUB) if FORCE_SUB.startswith("-100") else FORCE_SUB), user_id=cmd.from_user.id)                 
        if user.status == "banned":
            await bot.send_message(
                chat_id=cmd.from_user.id,
                text="⚠️**𝚂𝙾𝚁𝚁𝚈 𝙳𝚄𝙳𝙴 𝚈𝙾𝚄 𝙰𝚁𝙴 𝙱𝙰𝙽𝙽𝙴𝙳 \n𝙰𝙲𝙲𝙴𝚂𝚂 𝙳𝙴𝙽𝙸𝙴𝙳 ⚠️ 𝙲𝙾𝙽𝚃𝙰𝙲𝚃 [𝚂𝚄𝙿𝙿𝙾𝚁𝚃 𝙶𝚁𝙾𝚄𝙿](https://t.me/BETA_BOTSUPPORT)**",
                parse_mode="markdown",
                disable_web_page_preview=True
            )
            return 400
    except UserNotParticipant:                
        return 400
    except Exception:        
        return 400
    return 200
