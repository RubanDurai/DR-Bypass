from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


START_MSG = '''Hi {}. Hello from Pyrogram!'''

# InlineKeyboard Buttons

START_MARKUP = InlineKeyboardMarkup(
    [[
    InlineKeyboardButton("Devloper", url="https://t.me/RUBANDURAI27"),
    InlineKeyboardButton("Support", callback_data="button2")
    ]]
)

HELP_MSG = '''
This Is Help Message
'''
