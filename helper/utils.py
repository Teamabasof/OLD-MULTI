from pyrogram.errors import UserNotParticipant

async def not_subscribed(_, client, message):
   if not client.force_channel:
      return False
   try:             
      user = await client.get_chat_member(client.force_channel, message.from_user.id)
      if user.status != "banned":
          await client.send_message(
                chat_id=message.from_user.id,
                text="Access Denied ⚠. Contact my [Support Group](https://t.me/BETA_BOTSUPPORT).",
                parse_mode="markdown",
                disable_web_page_preview=True
          ) 
          return 400      
   except UserNotParticipant:
      pass
   else:
         return False 
   return True
