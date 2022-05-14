from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
from helper.database import insert, getid
from helper.utils import not_subscribed
from variables import STAT_STICK, PICS, ADMIN
import asyncio
import random

WAIT_MSG = """"<b>Processing ...</b>"""

@Client.on_message(filters.private & filters.create(not_subscribed))
async def is_not_subscribed(client, message):
    await message.reply_text(
       text="**sorry bro നിങ്ങൾ ഞങ്ങളുടെ ചാനലിൽ ജോയിൻ ചെയ്തിട്ടില്ല താഴെയുള്ള ബട്ടനിൽ ക്ലിക്ക് ചെയ്ത് join ചെയ്യൂ എന്നിട്ട് വീണ്ടും start കൊടുക്കൂ 🙏**",
       reply_markup=InlineKeyboardMarkup([
           [ InlineKeyboardButton(text="📢𝙹𝚘𝚒𝚗 𝙼𝚢 𝚄𝚙𝚍𝚊𝚝𝚎 𝙲𝚑𝚊𝚗𝚗𝚎𝚕📢", url=client.invitelink)]
           ])
       )

@Client.on_message(filters.command("start"))
async def start_message(bot, message):
    insert(int(message.chat.id))
    m=await message.reply_sticker(STAT_STICK)
    await asyncio.sleep(2)
    await m.delete()             
    await message.reply_photo(
        photo=random.choice(PICS),
        caption=f"Hello {message.from_user.mention}👋🏻 How are you Iam The official BETA BOT Type /bots to see our bot list",
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("Support", url="https://t.me/BETA_BOTSUPPORT"),
            InlineKeyboardButton("Updates", url="https://t.me/BETA_UPDATES")
            ],[
            InlineKeyboardButton("Developer", url="https://t.me/JP_Jeol"),
            InlineKeyboardButton("commands", callback_data="commands"),
            InlineKeyboardButton("about", callback_data="about")
            ]]
            )
        )
         
@Client.on_message(filters.command("help"))
async def help_message(bot, message):
    await message.reply_photo(
        photo="https://telegra.ph//file/e937426b58e31a881c25f.jpg",
        caption="""Hey how can i help You. 
To see our bot list type /bots
If you have any questions join support
Group and ask🤍❤️
Thank you for using Beta"""
    )


@Client.on_message(filters.command("id"))
async def id_message(bot, message):
    await message.reply_text(
    text = f"""
👁️‍🗨️DETAILS
○ID : <code>{message.from_user.id}</code>
○FIRST NAME : {message.from_user.first_name}
○LAST NAME : {message.from_user.last_name}
○USERNAME : @{message.from_user.username}
○MENTION : {message.from_user.mention}
THANK YOU FOR USING BETA🤍""")

@Client.on_message(filters.command("dice"))
async def roll_dice(bot, message):
    await bot.send_dice(message.chat.id, "🎲")

@Client.on_message(filters.command("bots"))
async def bots_message(bot, message):
    await message.reply_text(
        text=f"""Hey {message.from_user.mention}
👇🏻👇🏻👇🏻HERE IS OUR BOTS LIST👇🏻👇🏻👇🏻""",
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("INFO BOT", url="https://t.me/get_id_beta_bot"),
            InlineKeyboardButton("MUSIC BOT", url="https://t.me/Kochirajavu_musicbot")
            ],[
            InlineKeyboardButton("GROUP MANAGER", url="https://t.me/BETA_GROUPMANAGBOT")
            ]]
            )
        )

@Client.on_message(filters.command(["stickerid"]))
async def stickerid(bot, message):   
    if message.reply_to_message.sticker:
       await message.reply(f"**Sticker ID is**  \n `{message.reply_to_message.sticker.file_id}` \n \n ** Unique ID is ** \n\n`{message.reply_to_message.sticker.file_unique_id}`", quote=True)
    else: 
       await message.reply("Oops !! Not a sticker file")


@Client.on_message(filters.command("broadcast") filters.private & filters.user(ADMIN))
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


@Client.on_message(filters.command("users") filters.private & filters.user(ADMIN))
async def get_users(client: Client, message: Message):    
    msg = await client.send_message(chat_id=message.chat.id, text=WAIT_MSG)
    ids = getid()
    tot = len(ids)
    await msg.edit(f"Total uses = {tot}")
