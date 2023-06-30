from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from database import Database
from configs import Config
from translation import *
from bot import Bot

import random

db = Database()

# Define a command handler for /start
@Client.on_message(filters.command("start"))
async def start_command(c: Client, m: Message):
    user_id = m.from_user.id
    await db.save_user(user_id)

    s = START_MSG.format(
        m.from_user.mention,
    )
    await m.reply_photo(
        caption=s,
        photo=random.choice(WELCOM_IMG),
        reply_markup=START_BUTTONS,
    )
    # Send a message to the log channel
    await c.send_message(Config.LOG_CHANNEL, f"User {m.from_user.mention} has started the bot.")

@Bot.on_message(filters.command("help") & filters.private)
async def help_cmd(c: Client, m: Message):
    await m.reply_photo(
        caption=HELP_MSG,
        photo=random.choice(WELCOM_IMG),
        reply_markup=HELP_BUTTONS,
    )

@Bot.on_message(filters.command("about") & filters.private)
async def about_cmd(c: Client, m: Message):
    await m.reply_photo(
        caption=ABOUT_MSG,
        photo=random.choice(WELCOM_IMG),
        reply_markup=ABOUT_BUTTONS,
    )

@Client.on_message(filters.command("status") & filters.private & filters.user(Config.ADMINS))
async def stats_handler(c: Client, m: Message):
    try:
        txt = await m.reply("`Fetching stats...`", quote=True)
        # Create an instance of the Database class
        db = Database()

        # Call the count_users() method to get the total number of users
        total_users = await db.count_users()

        msg = f"""
        **- Total Users:** `{total_users}`
        """
        # Send the stats message
        return await txt.edit(msg)
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")

@Client.on_message(filters.command("info") & filters.private)
async def info_handler(bot, m: Message):

    if m.from_user.last_name:
        last_name = m.from_user.last_name
    else:
        last_name = "None"

    await m.reply_text(  
        text=INFO_TEXT.format(m.from_user.first_name, last_name, m.from_user.username, m.from_user.id, m.from_user.mention, m.from_user.dc_id, m.from_user.language_code, m.from_user.status),             
        disable_web_page_preview=True,
        quote=True
    )

