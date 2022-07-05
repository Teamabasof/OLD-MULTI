import asyncio
from pyrogram import Client
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from variables import FORCE_SUB


async def ForceSub(bot: Client, cmd: Message):
    if not FORCE_SUB:
      return False
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
        invite_link = await bot.create_chat_invite_link(chat_id=(int(FORCE_SUB) if FORCE_SUB.startswith("-100") else FORCE_SUB))
        await bot.send_message(                               
            chat_id=cmd.from_user.id,
            text="**Please Join My Updates Channel to use this Bot!**\n\nDue to Overload, Only Channel Subscribers can use the Bot!",
            reply_markup=InlineKeyboardMarkup( [[
                InlineKeyboardButton(text='📢 Join Updates Channel 📢', url=invite_link)
                ],[
                InlineKeyboardButton('🔄 𝚃𝚛𝚢 𝙰𝚐𝚊𝚒𝚗 🔄', url=f'https://t.me/{bot.username}?start=start')                            
                ]]
            ),
            parse_mode="markdown"
        )
        return 400
    except Exception:        
        return 400
    return 200
