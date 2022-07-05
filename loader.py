import os
import logging 
from pyrogram import Client
import re

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

API_ID = int(os.environ.get("API_ID", ""))

API_HASH = os.environ.get("API_HASH", "")

class App(Client):

    def __init__(self):
        super().__init__(
            "tgbot",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            plugins={"root": "plugins"},
        )

    async def start(self):
       await super().start()
       me = await self.get_me() 
       self.mention = me.mention
       self.username = me.username        
       
print("Bot Started...")
bot = App()
bot.run()


        










