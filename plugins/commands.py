from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
from helper.database import insert, getid
from helper.utils import not_subscribed
from variables import STAT_STICK, PICS, ADMIN
from pyrogram import enums
import asyncio
import random

WAIT_MSG = """"<b>Processing ...</b>"""

@Client.on_message(filters.private & filters.create(not_subscribed))
async def is_not_subscribed(client, message):
    await message.reply_text(
       text="**⚠️Sorry bro,You didn't Joined Our Updates Channel Join now and start again🙏**",
       reply_markup=InlineKeyboardMarkup([
           [ InlineKeyboardButton(text="📢𝙹𝚘𝚒𝚗 𝙼𝚢 𝚄𝚙𝚍𝚊𝚝𝚎 𝙲𝚑𝚊𝚗𝚗𝚎𝚕📢", url=client.invitelink)]
           ])
       )

@Client.on_message(filters.command("start"))
async def start_message(bot, message):
    insert(int(message.chat.id))
    await message.reply_chat_action(enums.ChatAction.TYPING)
    await asyncio.sleep(1)
    m=await message.reply_sticker(STAT_STICK)
    await asyncio.sleep(2)
    await m.delete()             
    await message.reply_photo(
        photo=random.choice(PICS),
        caption=f"Hello {message.from_user.mention}👋🏻 I'am A Multi Bot with many usefull features. You can see My commands by below button",
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("❣️ 𝐒𝐔𝐏𝐏𝐎𝐑𝐓", url="https://t.me/BETA_BOTSUPPORT"),
            InlineKeyboardButton("📢 𝐔𝐏𝐃𝐀𝐓𝐄𝐒", url="https://t.me/BETA_UPDATES")
            ],[            
            InlineKeyboardButton("ℹ️ 𝐇𝐄𝐋𝐏", callback_data="help"),
            InlineKeyboardButton("😉 𝐅𝐔𝐍", callback_data="fun")
            ],[
            InlineKeyboardButton("👨‍💻 𝐃𝐄𝐕𝐒 👨‍💻 ", callback_data="devs"),
            InlineKeyboardButton("🤖 𝐀𝐁𝐎𝐔𝐓", callback_data="about")
            ]]
            )
        )
         
@Client.on_message(filters.command("id"))
async def id_message(bot, message):
    await message.reply_text(
    text = f"""<i>
<u>👁️‍🗨️DETAILS</u>

♂️ID : <code>{message.from_user.id}</code>
♀️FIRST NAME : {message.from_user.first_name}
⚡️LAST NAME : {message.from_user.last_name}
⚜️USERNAME : @{message.from_user.username}
🔅MENTION : {message.from_user.mention}

THANK YOU FOR USING BETA❣️</i>""")


@Client.on_message(filters.command(["stickerid"]))
async def stickerid(bot, message):   
    if message.reply_to_message.sticker:
       await message.reply(f"**Sticker ID is**  \n `{message.reply_to_message.sticker.file_id}` \n \n ** Unique ID is ** \n\n`{message.reply_to_message.sticker.file_unique_id}`", quote=True)
    else: 
       await message.reply("Oops !! Not a sticker file")


@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["broadcast"]))
async def broadcast(bot, message):
 if (message.reply_to_message):
   ms = await message.reply_text("Geting All ids from database ...........")
   ids = getid()
   tot = len(ids)
   await ms.edit(f"Starting Broadcast .... \n Sending Message To {tot} Users")
   for id in ids:
     try:
     	await message.reply_to_message.copy(id)
     except:
     	pass


@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["users"]))
async def get_users(client: Client, message: Message):    
    msg = await client.send_message(chat_id=message.chat.id, text=WAIT_MSG)
    ids = getid()
    tot = len(ids)
    await msg.edit(f"Total uses = {tot}")
