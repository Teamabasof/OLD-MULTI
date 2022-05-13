from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import CallbackQuery
import asyncio


Jeol=Client(
    "Jeol Bot",
    bot_token="5235245424:AAGt8l7zfDUxXoG7NMnM5ejcAX-gxnWO6zI",
    api_id="11271918",
    api_hash="1cd29c2b7e1df5f18aeaeafbf7ebf7cd"
)


@Jeol.on_message(filters.command("start"))
async def start_message(bot, message):
    await message.reply_sticker(
        sticker="CAACAgUAAxkBAAIBU2J-N7WIdJobwDnajHerWD7aD-IwAAKeBAACf7TwVxZUQiDRe7p1JAQ"
    )
    await asyncio.sleep(1)
    await m.delete(6)
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

@Jeol.on_message(filters.command("help"))
async def help_message(bot, message):
    await message.reply_photo(
        photo="https://telegra.ph//file/e937426b58e31a881c25f.jpg",
        caption="""Hey how can i help You. 
To see our bot list type /bots
If you have any questions join support
Group and ask🤍❤️
Thank you for using Beta"""
    )



@Jeol.on_message(filters.command("id"))
async def id_message(bot, message):
    await message.reply_text(
    text = f"""
👁️‍🗨️DETAILS
○ID : {message.from_user.id}
○FIRST NAME : {message.from_user.first_name}
○LAST NAME : {message.from_user.last_name}
○USERNAME : @{message.from_user.username}
○MENTION : {message.from_user.mention}

THANK YOU FOR USING BETA🤍""")

@Jeol.on_message(filters.command("dice"))
async def dice_message(bot, message):
    await message.reply_text(
    text = "🎲")

@Jeol.on_message(filters.command("bots"))
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



@Jeol.on_callback_query()
async def callback(bot, msg):
   if msg.data == "commands":
       await msg.message.edit(
           text="""HEY HERE YOU CAN FIND THE BASIC COMMANDS OF MINE.IF YOU DON'T KNOW HOW TO USE COMMAND JOIN SUPPORT GROUP AND ASK.
COMMANDS - /start /help /id /info /bots THESE WERE OUR COMMANS WE HAVE PUBLISHED"""
       )




Jeol.run()
