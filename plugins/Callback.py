from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton                              
from pyrogram.types import CallbackQuery
import asyncio


@Client.on_callback_query()
async def callback(bot, msg):
   data = msg.data
   if data == "help":
       await msg.message.edit(       
           text="""HEY HERE YOU CAN FIND THE BASIC COMMANDS OF MINE.IF YOU DON'T KNOW HOW TO USE COMMAND JOIN SUPPORT GROUP AND ASK.

<b><u>COMMANDS</u></b>

◉ send channel last message with
  forwerd tag to get the channel id 💯

◉ /id - your tg id & info

◉ /telegraph - reply to below 5Mb media
  to get telegraph link💯

◉ /stickerid - Reply To Any Sticker to get sticker id

🤩THANKS FOR USING ME😍
""",       
           reply_markup=InlineKeyboardMarkup( [[
                  InlineKeyboardButton("🤖 𝐌𝐘 𝐁𝐎𝐓𝐒", callback_data="botz")
                  ],[
                  InlineKeyboardButton("↩️ 𝐁𝐀𝐂𝐊", callback_data="start"),
                  InlineKeyboardButton("🔒 𝐂𝐋𝐎𝐒𝐄", callback_data="close")
                  ]]
                  )
           )
   elif data == "about":
         await msg.message.edit(
             text=f""" 
╔════❰ 𝙼𝚄𝙻𝚃𝙸 𝙱𝙾𝚃 ❱═❍
║╭━━━━━━━━━━━━━━━➣
║┣⪼🤖ᴍʏ ɴᴀᴍᴇ : {bot.mention}
║┣⪼👦ᴅᴇᴠ 1 : <a href=https://t.me/JP_Jeol>ᴊᴇᴏʟᴘᴀᴜʟ</a>
║┣⪼👨‍💻ᴅᴇᴠ 2 : <a href=https://t.me/mr_MKN>ᴍʀ.ᴍᴋɴ ᴛɢ</a>
║┣⪼❣️sᴏᴜʀᴄᴇ ᴄᴏᴅ : <a href=https://github.com/Jeolpaul/TG-MULTI-BOT>ᴛɢ-ᴍᴜʟᴛɪ-ʙᴏᴛ</a>
║┣⪼📡ʜᴏsᴛᴇᴅ ᴏɴ : <a href=https://dashboard.heroku.com>ʜᴇʀᴏᴋᴜ</a>
║┣⪼🗣️ʟᴀɴɢᴜᴀɢᴇ : <a href=https://www.python.org>ᴘʏᴛʜᴏɴ3</a>
║┣⪼📚ʟɪʙʀᴀʀʏ : <a href=https://github.com/pyrogram>ᴘʏʀᴏɢʀᴀᴍ</a> 
║┣⪼🗒️ᴠᴇʀsɪᴏɴ : 1.0.3  
║╰━━━━━━━━━━━━━━━➣
╚══════════════════❍ """,
              disable_web_page_preview = True,
              reply_markup=InlineKeyboardMarkup( [[
                  InlineKeyboardButton("↩️ 𝐁𝐀𝐂𝐊", callback_data="start"),
                  InlineKeyboardButton("🔒 𝐂𝐋𝐎𝐒𝐄", callback_data="close")
                  ]]
                  )
         )        
   elif data == "start":
         await msg.message.edit(
             text=f"Hello {msg.from_user.mention}👋🏻\nI'am A Multi use Bot with many usefull features.\neg:- Telegarph, Channel ID, User ID, Fun, Group Id etc...\nYou can see My commands by below button... \n\n◉ send channel last message with forwerd tag to get the channel id 💯",          
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
   elif data == "devs":
         await msg.message.edit(
             text=f"This Bot will be made @JP_Jeol & @mr_MKN ",
             reply_markup=InlineKeyboardMarkup( [[
                  InlineKeyboardButton("👨‍💻 𝐃𝐄𝐕𝐒 1", url="https://t.me/JP_Jeol"),
                  InlineKeyboardButton("👨‍💻 𝐃𝐄𝐕𝐒 2", url="https://t.me/mr_MKN")
                  ],[
                  InlineKeyboardButton("❣️ 𝐒𝐎𝐔𝐑𝐂𝐄 𝐂𝐎𝐃𝐄 ❣️", url="https://github.com/Jeolpaul/TG-MULTI-BOT"),
                  ],[
                  InlineKeyboardButton("↩️ 𝐁𝐀𝐂𝐊", callback_data="start"),
                  InlineKeyboardButton("🔒 𝐂𝐋𝐎𝐒𝐄", callback_data="close")
                  ]]
                  )
             )
   elif data == "fun":
         await msg.message.edit(
             text=f"""<b><u>JUS TEST THIS COMMANDS 😉</u></b>

◉ /runs         
◉ /ikka      
◉ /dice     
◉ /arrow    
◉ /goal    
◉ /luck    
◉ /throw     
◉ /bowling  
◉ /tenpins    
""",      
             reply_markup=InlineKeyboardMarkup( [[
                 InlineKeyboardButton("↩️ 𝐁𝐀𝐂𝐊", callback_data="start"),
                 InlineKeyboardButton("🔒 𝐂𝐋𝐎𝐒𝐄", callback_data="close")
                 ]]
                 )
             )
   elif data == "botz":
         await msg.message.edit(
             text="🤖 This is My botz 😁",
                 reply_markup=InlineKeyboardMarkup( [[
                     InlineKeyboardButton("ℹ️ 𝐈𝐍𝐅𝐎 𝐁𝐎𝐓", url="https://t.me/get_id_beta_bot"),
                     InlineKeyboardButton("🎵 𝐌𝐔𝐒𝐈𝐂 𝐁𝐎𝐓", url="https://t.me/Kochirajavu_musicbot")
                     ],[
                     InlineKeyboardButton("🎖️ 𝐆𝐑𝐎𝐔𝐏 𝐌𝐀𝐍𝐀𝐆𝐄𝐑 🎖️", url="https://t.me/BETA_GROUPMANAGBOT")
                     ],[                   
                     InlineKeyboardButton("↩️ 𝐁𝐀𝐂𝐊", callback_data="start"),
                     InlineKeyboardButton("🔒 𝐂𝐋𝐎𝐒𝐄", callback_data="close")
                     ]]
                     )
                 )
   elif data == "close":
        await msg.message.delete()
        try:
            await msg.message.reply_to_message.delete()
        except:
            pass
























