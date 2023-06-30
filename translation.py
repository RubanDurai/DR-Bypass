from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

WELCOM_IMG = [
    "https://te.legra.ph/file/738609525d91dfd2a5182.jpg",
    "https://telegra.ph/file/821ca3f7b9b58d665e582.jpg",
    "https://telegra.ph/file/6c5ce18e3cf82d3dee973.jpg"
]

START_MSG = '''
<b> 𝖧𝖾𝗒 {}. 𝖨 𝖠𝗆 𝖴𝗋𝗅 𝖡𝗒𝗉𝖺𝗌𝗌 𝖡𝗈𝗍. 𝖲𝖾𝗇𝖽 𝖬𝖾 𝖲𝗁𝗈𝗋𝗍 𝖫𝗂𝗇𝗄 , 𝖸𝗈𝗎 𝗐𝗂𝗅𝗅 𝗀𝖾𝗍 𝖮𝗋𝗂𝗀𝗂𝗇𝖺𝗅 𝖫𝗂𝗇𝗄 \n
𝖣𝗎𝖾 𝖳𝗈 𝖲𝗈𝗆𝖾 𝖱𝖾𝖺𝗌𝗈𝗇 𝖶𝖾 𝖢𝖺𝗇'𝗍 𝖲𝗁𝗈𝗐 𝖲𝗎𝗉𝗉𝗈𝗋𝗍𝖾𝖽 𝖲𝗂𝗍𝖾𝗌 , 𝖲𝗈 𝖳𝗋𝗒 𝖸𝗈𝗎𝗋 𝖫𝗎𝖼𝗄 😜 \n
MADE BY @TN_LINKZZ.
</b>
'''

# Help message
HELP_MSG = """<b>--Available Commands:--\n
/start - Start the bot
/help - Get help
/about - About the bot
/info - Information about you\n
--How To Use-- 
 𝖩𝗎𝗌𝗍 𝗌𝖾𝗇𝖽 𝗆𝖾 𝖺𝗇𝗒 𝗌𝗎𝗉𝗉𝗈𝗋𝗍𝖾𝖽 𝗅𝗂𝗇𝗄𝗌 𝖺𝗇𝖽 𝗂 𝗐𝗂𝗅𝗅 𝗒𝗈𝗎 𝗀𝖾𝗍 𝗒𝗈𝗎 𝗋𝖾𝗌𝗎𝗅𝗍𝗌.</b>
 """

DISCLAIMER_MSG = """
<b>--Disclaimer--
☞ Please note that this bot does not guarantee the removal of any content.\n
☞ If you believe that your copyrighted content has been used inappropriately or without permission, please contact the owner of this bot.\n
☞ You can send a direct message to the owner with the details of the content and the reasons for its removal.
</b>
--**Contact**-- 
Owner : @RUBANDURAI27
Admin : @TEAM_TN_RIO
"""

# About message
ABOUT_MSG = """
<b>
𝙱𝙾𝚃 𝙽𝙰𝙼𝙴 : Url Bypass Bot
𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴 : Python
𝙻𝙸𝙱𝚁𝙰𝚁𝚈: Pyrogram
𝙲𝚁𝙴𝙰𝚃𝙾𝚁: @RUBANDURAI27
𝙳𝙰𝚃𝙰𝙱𝙰𝚂𝙴: Mongodb
𝚅𝙴𝚁𝚂𝙸𝙾𝙽: 𝚅1.0.0
</b>
"""

INFO_TEXT = """
 💫 Telegram Information

 🤹 First Name : <b>{}</b>

 🚴‍♂️ Second Name : <b>{}</b>

 🧑🏻 Username : <b>@{}</b>

 🆔 Telegram Id : <code>{}</code>

 📇 Profile Link : <b>{}</b>

 📡 Dc : <b>{}</b>

 📑 Language : <b>{}</b>

 👲 Status : <b>{}</b>
"""

DEVELOPERS_MSG = """<b>--Developers :--</b>
<b>♔ Creator : @RUBANDURAI27</b>
"""

# Start buttons
START_BUTTONS = InlineKeyboardMarkup(
    [[
    InlineKeyboardButton("♕ 𝖣𝖾𝗏𝗅𝗈𝗉𝖾𝗋", url="https://t.me/RUBANDURAI27"),
    ],[
    InlineKeyboardButton("♻️ 𝖴𝗉𝖽𝖺𝗍𝖾𝗌", url="https://t.me/JOKERBOTS"),
    InlineKeyboardButton("💬 𝖲𝗎𝗉𝗉𝗈𝗋𝗍", url="https://t.me/TAMILMIRROR"),
    ],[
    InlineKeyboardButton("🦋 𝖱𝖾𝗊𝗎𝖾𝗌𝗍 𝖲𝗂𝗍𝖾𝗌 🦋", url="https://t.me/ContentTNBot"),
    ],[
    InlineKeyboardButton("✨ 𝖧𝖾𝗅𝗉", callback_data="help"),
    InlineKeyboardButton("🚴‍♂️ 𝖠𝖻𝗈𝗎𝗍", callback_data="about"),
    ]]
)

# Help buttons
HELP_BUTTONS = InlineKeyboardMarkup(
    [[
    InlineKeyboardButton("🧑‍💻 𝖽𝖾𝗏𝗌", callback_data="devlopers"),
    ],[
    InlineKeyboardButton("⚠ 𝖣𝗂𝗌𝖼𝗅𝖺𝗂𝗆𝖾𝗋", callback_data="disclaimer"),
    InlineKeyboardButton("🚴‍♂️ 𝖠𝖻𝗈𝗎𝗍", callback_data="about"),
    ],[
    InlineKeyboardButton("🗑️ 𝖢𝗅𝗈𝗌𝖾", callback_data="delete"),
    ]]
)

# About buttons
ABOUT_BUTTONS = InlineKeyboardMarkup(
    [[
    InlineKeyboardButton("🎪 𝖧𝗈𝗆𝖾", callback_data="home"),
    InlineKeyboardButton("✨ 𝖧𝖾𝗅𝗉", callback_data="help"),
    ],[
    InlineKeyboardButton("🗑️ 𝖢𝗅𝗈𝗌𝖾", callback_data="delete"),
    ]]
)

DISCLAIMER_BUTTONS = InlineKeyboardMarkup(
    [[
    InlineKeyboardButton("🎪 𝖧𝗈𝗆𝖾", callback_data="home"),
    ]]
)

DEVELOPERS_BUTTONS = InlineKeyboardMarkup(
    [[
    InlineKeyboardButton("↵ 𝖡𝖺𝖼𝗄", callback_data="help"),
    ]]
)
