import os
from pyrogram import Client, filters
from pyrogram.types import Message
from plugins.helper_functions.font_script import Fonts
from plugins.helper_functions.cust_p_filters import f_onw_fliter
from helper.utils import not_subscribed
from helper.ban import BanChek
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery 
import random


RUN_STRINGS = (
    "ഓ.. ധിക്കാരം... പഴേപോലെ തന്നെ....ഒരു മാറ്റോമില്ല.....ചുമ്മാതല്ല ഗതി പിടിക്കാത്തത്....!!!",
    "അള്ളാ... പിള്ളേരുടെ ഓരോ... പെഷനെ...",
    "എനിക്ക് എഴുതാൻ അല്ലെ അറിയൂ സാറേ.... വായിക്കാൻ അറിയില്ലല്ലോ....",
    "ഇന്ന് ഇനി നീ മിണ്ടരുത്... ഇന്നത്തെ കോട്ട കഴിഞ്ഞ്.....",
    "ചാരമാണെന്ന് കരുതി ചെകയാൻ നിൽക്കണ്ട കനൽ കെട്ടിട്ടില്ലെങ്കിൽ പൊള്ളും.",
    "ഒറ്റ ജീവിതമേ ഉള്ളു മനസിലാക്കിക്കോ, സ്വർഗ്ഗമില്ല നരകമില്ല, 'ഒറ്റ ജീവിതം', അത് എവിടെ എങ്ങനെ വേണമെന്ന് അവനവൻ തീരുമാനിക്കും",
    "വാട്ട് എ ബോംബെസ്റ്റിക് എക്സ്പ്ലോഷൻ! സച് എ ടെറിഫിക് ഡിസ്ക്ലോസ്!!",
    "ഗോ എവേ സ്ടുപ്പിഡ് ഇൻ ദി ഹൗസ് ഓഫ് മൈ വൈഫ്‌ ആൻഡ് ഡോട്ടർ യൂവിൽ നോട്ട് സി എനി മിനിറ്റ് ഓഫ് ദി ടുഡേ... ഇറങ്ങി പോടാ..",
    "ഐ കാൻ ഡു ദാറ്റ്‌ ഡു കാൻ ഐ ദാറ്റ്‌",
    "ക്രീം ബിസ്കറ്റിൽ ക്രീം ഉണ്ടന്ന് കരുതി ടൈഗർ ബിസ്കറ്റിൽ ടൈഗർ ഉണ്ടാകണമെന്നില്ല. പണി പാളും മോനെ...",
    "പട പേടിച്ചു പന്തളത്തു ചെന്നപ്പോ പന്തോം കുത്തി പട പന്തളത്തോട്ടെന്ന് പറഞ്ഞ പോലെ ആയല്ലോ.",
    "എന്റ കർത്താവെ.... എന്നെ നീ നല്ലവനാകാൻ സമ്മതിക്കൂല്ല അല്ലെ.",
    "കാർ എൻജിൻ ഔട്ട് കംപ്ലീറ്റ്‌ലി......",
    "തള്ളെ കലിപ്പ് തീരണില്ലല്ലോ!!",
    "പാതിരാത്രിക്ക് നിന്റെ അച്ഛൻ ഉണ്ടാക്കി വെച്ചിരിക്കുന്നോ പൊറോട്ടയും ചിക്കനും....",
    "ഓ പിന്നെ നീ ഒക്കെ പ്രേമിക്കുമ്പോൾ അത് പ്രണയം.... നമ്മൾ ഒക്കെ പ്രേമിക്കുമ്പോൾ അത് കമ്പി....",
    "ദൈവമേ എന്നെ മാത്രം രക്ഷിക്കണേ....",
    "അവളെ ഓർത്ത് കുടിച്ച കള്ളും നനഞ്ഞ മഴയും വേസ്റ്റ്....",
    "ഇത്രേം കാലം എവിടെ ആയിരുന്നു....!",
    "ഇൻഗ്ലീഷ് തീരെ പിടി ഇല്ല അല്ലെ....",
    "ആൾ ദി ഡ്രീംസ്‌ ലൈക്‌ ട്വിങ്കിൽ സ്റ്റാർസ്...",
    "എന്റെ പ്രാന്തൻ മുത്തപ്പാ അവനെ ഒരു വഴിയാക്കി തരണേ",
    "പെങ്ങളെ കെട്ടിയ സ്ത്രീധന തുക തരുമോ അളിയാ",
    "നീ വല്ലാതെ ക്ഷീണിച്ചു പൊയി",
    "കണ്ണിലെണ്ണയൊഴിച്ചു കാത്തിരിക്കുവായിരുന്നളിയാ.",
    "ചെല്ലാക്കണ്ടു എന്നിച്ചു പോടാ തടി.യാ .\
    ഷട്ട് ഉഒ യുവർ മൗത് ബ്ലഡി gramavasis.",
    "പോയി ചാവട .\
    നിന്നെ കൊണ്ട് ചാവാൻ patto.",
    "നിന്നെ കൊണ്ട് നാട്ടുകാർക്കും ഗുണോല്ല്യ വിട്ടുകാർക്കും ഗുണോല്ല്യ എന്തിനാ ഇങ്ങനെ നാണം കേട്ടു ജീവിക്കുന്നട പാട് വാഴെ ചെങ്കതളി വാഴ .", 
)


IKKA_STRINGS = (
    "CAACAgUAAxkBAAIDUmIN8bqiD5DYQLjQzUwH7-1AsH0eAAJGBAAClj7wVxJlL3v8QuaoHgQ",
    "CAACAgUAAxkBAAIDVmIN8cCiVJZl05m0wiggUJaOvYarAAL5BAACo7lRVClze9Et3bCJHgQ",
    "CAACAgUAAxkBAAIDV2IN8cSKz20_0T-f7BlHVQfQYPu_AAKfAwACA4rwV01BOgyNllX1HgQ",
    "CAACAgUAAxkBAAIDWGIN8coT1jTnXpetiFOKVGZVCX78AAJLBAACrXgAAVTcB_E8ndEu0h4E",
    "CAACAgUAAxkBAAIDWWIN8c-GSo6HX8bmIvJOwDXG1pJ-AAJkBAACbYZIVIF7psBskaRiHgQ",
    "CAACAgUAAxkBAAIDWmIN8dfwrILfwAABBczAR4DoYxpkvAACvwUAAlNOSFRraTuQ8L5Qzx4E",
    "CAACAgUAAxkBAAIDXGIN8eN4RRZPSvKW5OcDhBGnF_qIAAJtBQACwq0JVAnAmIgTMZr6HgQ",
    "CAACAgUAAxkBAAIDeGIN8ke0Qm7S8rWAp5XRHtG21RP1AAJzBQACg5tAVL8bVAS2wafYHgQ",
    "CAACAgUAAxkBAAIDfGIN8lvvH0C9VGSLMV7fvxJ9L_r9AAIlBgACf4hJVA_SXDgpTipeHgQ",
    "CAACAgUAAxkBAAIDf2IN8nL54y-xsW_PGMX5T96e_ErnAAJiAwACjh3YV6f4T7ZwQqExHgQ",
    "CAACAgUAAxkBAAIDgmIN8oZFf70SfKUOl9nnk0Q0uIGPAAJjAwAC3-lRVqPrbp8AAeUBch4E",
    "CAACAgUAAxkBAAIDj2IN86K_5xEpxc00sVRoFLgNgvh_AALeAgACh49oVh2VB0KUEX3zHgQ",
    "CAACAgUAAxkBAAIDkmIN87LWn-56jo9wHTdifHsdBCAiAAJPAwACK4yZVlCyU1tXbk2YHgQ",
) 


@Client.on_message(filters.private & filters.create(not_subscribed))
async def is_not_subscribed(client, message):
    await message.reply_text(
       text="**⚠️Sorry bro,You didn't Joined Our Updates Channel Join now and start again🙏**",
       reply_markup=InlineKeyboardMarkup( [[
           InlineKeyboardButton(text="📢𝙹𝚘𝚒𝚗 𝙼𝚢 𝚄𝚙𝚍𝚊𝚝𝚎 𝙲𝚑𝚊𝚗𝚗𝚎𝚕📢", url=client.invitelink)
           ],[
           InlineKeyboardButton("🔄 𝚃𝚛𝚢 𝙰𝚐𝚊𝚒𝚗 🔄", url=f"https://t.me/{client.username}?start=start")            
           ]]
           )
       )

@Client.on_message(filters.command("dice"))
async def roll_dice(bot, message):
    kikked = await BanChek(bot, message)
    if kikked == 400:
        return 
    await bot.send_dice(message.chat.id, "🎲")

@Client.on_message(filters.command("arrow"))                                      
async def roll_arrow(bot, message):
    kikked = await BanChek(bot, message)
    if kikked == 400:
        return 
    await bot.send_dice(message.chat.id, "🎯")

@Client.on_message(filters.command("goal"))
async def roll_goal(bot, message):
    kikked = await BanChek(bot, message)
    if kikked == 400:
        return 
    await bot.send_dice(message.chat.id, "⚽️")

@Client.on_message(filters.command("luck"))
async def roll_luck(bot, message):
    kikked = await BanChek(bot, message)
    if kikked == 400:
        return 
    await bot.send_dice(message.chat.id, "🎰")

@Client.on_message(filters.command("throw"))
async def roll_throw(bot, message):
    kikked = await BanChek(bot, message)
    if kikked == 400:
        return 
    await bot.send_dice(message.chat.id, "🏀")

@Client.on_message(filters.command(["bowling", "tenpins"]))
async def roll_bowling(bot, message):
    kikked = await BanChek(bot, message)
    if kikked == 400:
        return 
    await bot.send_dice(message.chat.id, "🎳")


@Client.on_message(filters.command("runs") &
    f_onw_fliter
)
async def runs(bot, message):
    kikked = await BanChek(bot, message)
    if kikked == 400:
        return 
    """ /runs strings """
    effective_string = random.choice(RUN_STRINGS)
    if message.reply_to_message:
        await message.reply_to_message.reply_text(effective_string)
    else:
        await message.reply_text(effective_string)

@Client.on_message(filters.command("ikka") &
    f_onw_fliter
)
async def ikka(bot, message):
    kikked = await BanChek(bot, message)
    if kikked == 400:
        return 
    """ /ikka strings """
    effective_string = random.choice(IKKA_STRINGS)
    if message.reply_to_message:
        await message.reply_to_message.reply_sticker(effective_string)
    else:
        await message.reply_sticker(effective_string)


@Client.on_message(filters.private & filters.command("font"))
async def style_buttons(c, m, cb=False):
    buttons = [[
        InlineKeyboardButton('𝚃𝚢𝚙𝚎𝚠𝚛𝚒𝚝𝚎𝚛', callback_data='style+typewriter'),
        InlineKeyboardButton('𝕆𝕦𝕥𝕝𝕚𝕟𝕖', callback_data='style+outline'),
        InlineKeyboardButton('𝐒𝐞𝐫𝐢𝐟', callback_data='style+serif'),

        ],[

        InlineKeyboardButton('𝑺𝒆𝒓𝒊𝒇', callback_data='style+bold_cool'),
        InlineKeyboardButton('𝑆𝑒𝑟𝑖𝑓', callback_data='style+cool'),
        InlineKeyboardButton('Sᴍᴀʟʟ Cᴀᴘs', callback_data='style+small_cap'),

        ],[

        InlineKeyboardButton('𝓈𝒸𝓇𝒾𝓅𝓉', callback_data='style+script'),
        InlineKeyboardButton('𝓼𝓬𝓻𝓲𝓹𝓽', callback_data='style+script_bolt'),
        InlineKeyboardButton('ᵗⁱⁿʸ', callback_data='style+tiny'),

        ],[

        InlineKeyboardButton('ᑕOᗰIᑕ', callback_data='style+comic'),
        InlineKeyboardButton('𝗦𝗮𝗻𝘀', callback_data='style+sans'),
        InlineKeyboardButton('𝙎𝙖𝙣𝙨', callback_data='style+slant_sans'),

        ],[

        InlineKeyboardButton('𝘚𝘢𝘯𝘴', callback_data='style+slant'),
        InlineKeyboardButton('𝖲𝖺𝗇𝗌', callback_data='style+sim'),
        InlineKeyboardButton('Ⓒ︎Ⓘ︎Ⓡ︎Ⓒ︎Ⓛ︎Ⓔ︎Ⓢ︎', callback_data='style+circles'),

        ],[

        InlineKeyboardButton('🅒︎🅘︎🅡︎🅒︎🅛︎🅔︎🅢︎', callback_data='style+circle_dark'),
        InlineKeyboardButton('𝔊𝔬𝔱𝔥𝔦𝔠', callback_data='style+gothic'),
        InlineKeyboardButton('𝕲𝖔𝖙𝖍𝖎𝖈', callback_data='style+gothic_bolt'),

        ],[

        InlineKeyboardButton('C͜͡l͜͡o͜͡u͜͡d͜͡s͜͡', callback_data='style+cloud'),
        InlineKeyboardButton('H̆̈ă̈p̆̈p̆̈y̆̈', callback_data='style+happy'),
        InlineKeyboardButton('S̑̈ȃ̈d̑̈', callback_data='style+sad'),

        ],[

        InlineKeyboardButton('Next ➡️', callback_data="nxt")
    ]]
    if not cb:
        await m.reply_text(m.text, reply_markup=InlineKeyboardMarkup(buttons), quote=True)
    else:
        await m.answer()
        await m.message.edit_reply_markup(InlineKeyboardMarkup(buttons))


@Client.on_callback_query(filters.regex('^nxt'))
async def nxt(c, m):
    if m.data == "nxt":
        buttons = [[
            InlineKeyboardButton('🇸 🇵 🇪 🇨 🇮 🇦 🇱 ', callback_data='style+special'),
            InlineKeyboardButton('🅂🅀🅄🄰🅁🄴🅂', callback_data='style+squares'),
            InlineKeyboardButton('🆂︎🆀︎🆄︎🅰︎🆁︎🅴︎🆂︎', callback_data='style+squares_bold'),
            ],[
            InlineKeyboardButton('ꪖꪀᦔꪖꪶꪊᥴ𝓲ꪖ', callback_data='style+andalucia'),
            InlineKeyboardButton('爪卂几ᘜ卂', callback_data='style+manga'),
            InlineKeyboardButton('S̾t̾i̾n̾k̾y̾', callback_data='style+stinky'),
            ],[
            InlineKeyboardButton('B̥ͦu̥ͦb̥ͦb̥ͦl̥ͦe̥ͦs̥ͦ', callback_data='style+bubbles'),
            InlineKeyboardButton('U͟n͟d͟e͟r͟l͟i͟n͟e͟', callback_data='style+underline'),
            InlineKeyboardButton('꒒ꍏꀷꌩꌃꀎꁅ', callback_data='style+ladybug'),
            ],[
            InlineKeyboardButton('R҉a҉y҉s҉', callback_data='style+rays'),
            InlineKeyboardButton('B҈i҈r҈d҈s҈', callback_data='style+birds'),
            InlineKeyboardButton('S̸l̸a̸s̸h̸', callback_data='style+slash'),
            ],[
            InlineKeyboardButton('s⃠t⃠o⃠p⃠', callback_data='style+stop'),
            InlineKeyboardButton('S̺͆k̺͆y̺͆l̺͆i̺͆n̺͆e̺͆', callback_data='style+skyline'),
            InlineKeyboardButton('A͎r͎r͎o͎w͎s͎', callback_data='style+arrows'),
            ],[
            InlineKeyboardButton('ዪሀክቿነ', callback_data='style+qvnes'),
            InlineKeyboardButton('S̶t̶r̶i̶k̶e̶', callback_data='style+strike'),
            InlineKeyboardButton('F༙r༙o༙z༙e༙n༙', callback_data='style+frozen')
            ],[
            InlineKeyboardButton('⬅️ Back', callback_data='nxt+0')
        ]]
        await m.answer()
        await m.message.edit_reply_markup(InlineKeyboardMarkup(buttons))
    else:
        await style_buttons(c, m, cb=True)


@Client.on_callback_query(filters.regex('^style'))
async def style(c, m):
    await m.answer()
    cmd, style = m.data.split('+')

    if style == 'typewriter':
        cls = Fonts.typewriter
    if style == 'outline':
        cls = Fonts.outline
    if style == 'serif':
        cls = Fonts.serief
    if style == 'bold_cool':
        cls = Fonts.bold_cool
    if style == 'cool':
        cls = Fonts.cool
    if style == 'small_cap':
        cls = Fonts.smallcap
    if style == 'script':
        cls = Fonts.script
    if style == 'script_bolt':
        cls = Fonts.bold_script
    if style == 'tiny':
        cls = Fonts.tiny
    if style == 'comic':
        cls = Fonts.comic
    if style == 'sans':
        cls = Fonts.san
    if style == 'slant_sans':
        cls = Fonts.slant_san
    if style == 'slant':
        cls = Fonts.slant
    if style == 'sim':
        cls = Fonts.sim
    if style == 'circles':
        cls = Fonts.circles
    if style == 'circle_dark':
        cls = Fonts.dark_circle
    if style == 'gothic':
        cls = Fonts.gothic
    if style == 'gothic_bolt':
        cls = Fonts.bold_gothic
    if style == 'cloud':
        cls = Fonts.cloud
    if style == 'happy':
        cls = Fonts.happy
    if style == 'sad':
        cls = Fonts.sad
    if style == 'special':
        cls = Fonts.special
    if style == 'squares':
        cls = Fonts.square
    if style == 'squares_bold':
        cls = Fonts.dark_square
    if style == 'andalucia':
        cls = Fonts.andalucia
    if style == 'manga':
        cls = Fonts.manga
    if style == 'stinky':
        cls = Fonts.stinky
    if style == 'bubbles':
        cls = Fonts.bubbles
    if style == 'underline':
        cls = Fonts.underline
    if style == 'ladybug':
        cls = Fonts.ladybug
    if style == 'rays':
        cls = Fonts.rays
    if style == 'birds':
        cls = Fonts.birds
    if style == 'slash':
        cls = Fonts.slash
    if style == 'stop':
        cls = Fonts.stop
    if style == 'skyline':
        cls = Fonts.skyline
    if style == 'arrows':
        cls = Fonts.arrows
    if style == 'qvnes':
        cls = Fonts.rvnes
    if style == 'strike':
        cls = Fonts.strike
    if style == 'frozen':
        cls = Fonts.frozen
    new_text = cls(m.message.reply_to_message.text)
    try:
        await m.message.edit_text(new_text, reply_markup=m.message.reply_markup)
    except:
        pass










#end😁






