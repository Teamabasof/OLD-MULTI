from pyrogram.errors import UserNotParticipant

async def not_subscribed(_, client, message):
   if not client.force_channel:
      return False
   try:             
      user = await client.get_chat_member(client.force_channel, message.from_user.id)
   except UserNotParticipant:
      pass
   else:
      if user.status != "kicked":
          await client.send_message(
                chat_id=message.from_user.id,
                text="Access Denied ⚠. Contact my [Support Group](https://t.me/BETA_BOTSUPPORT).",
                parse_mode="markdown",
                disable_web_page_preview=True
            )
         return False 
   return True
