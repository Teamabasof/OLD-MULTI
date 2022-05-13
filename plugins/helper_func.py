from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
from pyrogram.types import CallbackQuery
from config import FORCE_SUB
import asyncio


@Client.on_message(filters.command("start"))
async def start_message(bot, message):
    if FORCE_SUB:   
        try:             
            user = await bot.get_chat_member(FORCE_SUB, message.from_user.id)
            if user.status == "kicked":
               await message.reply_text("Sorry, You're Banned")
               return
        except UserNotParticipant:
            await message.reply_text(
                text="**sorry bro നിങ്ങൾ ഞങ്ങളുടെ ചാനലിൽ ജോയിൻ ചെയ്തിട്ടില്ല താഴെയുള്ള ബട്ടനിൽ ക്ലിക്ക് ചെയ്ത് join ചെയ്യൂ എന്നിട്ട് വീണ്ടും start കൊടുക്കൂ 🙏**",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text="📢𝙹𝚘𝚒𝚗 𝙼𝚢 𝚄𝚙𝚍𝚊𝚝𝚎 𝙲𝚑𝚊𝚗𝚗𝚎𝚕📢", url=f"https://t.me/{FORCE_SUB}")]
              ])
            )
            return
        else:
             m=await message.reply_sticker("CAACAgUAAxkBAAIBU2J-N7WIdJobwDnajHerWD7aD-IwAAKeBAACf7TwVxZUQiDRe7p1JAQ")
             await asyncio.sleep(4)
             await m.delete()             
             await message.reply_text(
                 text=f"Hello {message.from_user.mention}👋🏻 How are you Iam The official BETA BOT Type /bots to see our bot list",
                 reply_markup=InlineKeyboardMarkup( [[
                     InlineKeyboardButton("Support", url="https://t.me/BETA_BOTSUPPORT"),
                     InlineKeyboardButton("Updates", url="https://t.me/BETA_UPDATES")
                     ],[
                     InlineKeyboardButton("Developer", url="https://t.me/JP_Jeol"),
                     InlineKeyboardButton("commands", callback_data="commands")
                     ]]
                     )
                 )

@Client.on_message(filters.command("help"))
async def help_message(bot, message):
    if FORCE_SUB:   
        try:             
            user = await bot.get_chat_member(FORCE_SUB, message.from_user.id)
            if user.status == "kicked":
               await message.reply_text("Sorry, You're Banned")
               return
        except UserNotParticipant:
            await message.reply_text(
                text="**sorry bro നിങ്ങൾ ഞങ്ങളുടെ ചാനലിൽ ജോയിൻ ചെയ്തിട്ടില്ല താഴെയുള്ള ബട്ടനിൽ ക്ലിക്ക് ചെയ്ത് join ചെയ്യൂ എന്നിട്ട് വീണ്ടും start കൊടുക്കൂ 🙏**",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text="📢𝙹𝚘𝚒𝚗 𝙼𝚢 𝚄𝚙𝚍𝚊𝚝𝚎 𝙲𝚑𝚊𝚗𝚗𝚎𝚕📢", url=f"https://t.me/{FORCE_SUB}")]
              ])
            )
            return
        else:
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
    if FORCE_SUB:   
        try:             
            user = await bot.get_chat_member(FORCE_SUB, message.from_user.id)
            if user.status == "kicked":
               await message.reply_text("Sorry, You're Banned")
               return
        except UserNotParticipant:
            await message.reply_text(
                text="**sorry bro നിങ്ങൾ ഞങ്ങളുടെ ചാനലിൽ ജോയിൻ ചെയ്തിട്ടില്ല താഴെയുള്ള ബട്ടനിൽ ക്ലിക്ക് ചെയ്ത് join ചെയ്യൂ എന്നിട്ട് വീണ്ടും start കൊടുക്കൂ 🙏**",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text="📢𝙹𝚘𝚒𝚗 𝙼𝚢 𝚄𝚙𝚍𝚊𝚝𝚎 𝙲𝚑𝚊𝚗𝚗𝚎𝚕📢", url=f"https://t.me/{FORCE_SUB}")]
              ])
            )
            return
        else:
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
async def dice_message(bot, message):
    await message.reply_text(
    text = "🎲")

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



@Client.on_callback_query()
async def callback(bot, msg):
   if msg.data == "commands":
       await msg.message.edit(
           text="""HEY HERE YOU CAN FIND THE BASIC COMMANDS OF MINE.IF YOU DON'T KNOW HOW TO USE COMMAND JOIN SUPPORT GROUP AND ASK.
COMMANDS - /start /help /id /info /bots THESE WERE OUR COMMANS WE HAVE PUBLISHED"""
       )
