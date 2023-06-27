from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

START_MSG = '''Hi {}. Hello from Pyrogram!'''

START_TEXT = """
✮ Hey {} ✮\n
<code>I am Telegram File To Link Bot</code>\n
<code>Use Help Command to Know how to Use me</code>\n
✮ Made By @Tellybots"""

HELP_TEXT = """
✮ Send Me Any File or Media\n
✮ I Will Provide You Instant Direct Download link as Well as Stream Link\n
✮ Add me in Your Channel as Admin To Get Direct Download link button and online Stream Link Button\n
"""

ABOUT_TEXT = """
🤖 My Name : Telly File Stream Bot\n
🚦 Version : <a href='https://telegram.me/tellybots'>3.0</a>\n
💫 Source Code : <a href='https://t.me/tellybots_digital'>Click Here</a>\n
🗃️ Library : <a href='https://pyrogram.org'>Click Here</a>\n
👲 Developer : <a href='https://telegram.me/tellybots'>TellyBots</a>\n
📦 Last Updated : <a href='https://telegram.me/tellybots'>[ 13-Jan-22 ] 09:00 AM</a>"""

# InlineKeyboard Buttons

START_MARKUP = InlineKeyboardMarkup(
    [[
    InlineKeyboardButton("Devloper", url="https://t.me/RUBANDURAI27"),
    InlineKeyboardButton("Support", callback_data="button2")
    ]]
)

START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('♻️ Update Channel', url='https://telegram.me/tellybots_4u'),
        InlineKeyboardButton('💬 Support Group', url='https://telegram.me/tellybots_support')
        ],[
        InlineKeyboardButton('♨️ Help', callback_data='help'),
        InlineKeyboardButton('🗑️ Close', callback_data='close')
        ]]
)
HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏤 Home', callback_data='home'),
        InlineKeyboardButton('🚴‍♂️ About', callback_data='about'),
        InlineKeyboardButton('🗑️ Close', callback_data='close')
        ]]
)
ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏤 Home', callback_data='home'),
        InlineKeyboardButton('♨️ Help', callback_data='help'),
        InlineKeyboardButton('🗑️ Close', callback_data='close')
        ]]
)
