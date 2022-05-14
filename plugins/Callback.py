from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton                              
from pyrogram.types import CallbackQuery
import asyncio


@Client.on_callback_query()
async def callback(bot, msg):
   data = msg.data
   if data == "commands":
       await msg.message.edit(
           text="""HEY HERE YOU CAN FIND THE BASIC COMMANDS OF MINE.IF YOU DON'T KNOW HOW TO USE COMMAND JOIN SUPPORT GROUP AND ASK.
COMMANDS - /start /help /id /info /bots THESE WERE OUR COMMANS WE HAVE PUBLISHED"""
       )
   elif data == "about":
         await msg.message.edit(
             text=""""
╔════❰ 𝙼𝚄𝙻𝚃𝙸 𝙱𝙾𝚃 ❱═❍
║╭━━━━━━━━━━━━━━━➣
║┣⪼👦ᴄʀᴇᴀᴛᴏʀ : ᴊᴇᴏʟᴘᴀᴜʟ
║┣⪼📡ʜᴏsᴛᴇᴅ ᴏɴ : ʜᴇʀᴏᴋᴜ
║┣⪼🗣️ʟᴀɴɢᴜᴀɢᴇ : ᴘʏᴛʜᴏɴ3
║┣⪼📚ʟɪʙʀᴀʀʏ : ᴘʏʀᴏɢʀᴀᴍ 
║┣⪼🗒️ᴠᴇʀsɪᴏɴ : 1.0.3  
║╰━━━━━━━━━━━━━━━➣
╚══════════════════❍  
"""
         )     



























