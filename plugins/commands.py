from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from database import Database
from translation import *

db = Database()

# Define a command handler for /start
@Client.on_message(filters.command("start"))
async def start_command(c: Client, m: Message):
    user_id = m.from_user.id
    await db.save_user(user_id)

    s = START_TEXT.format(
        m.from_user.mention,
    )
    # keyboard = InlineKeyboardMarkup(
    #     [[
    #         InlineKeyboardButton("Button 1", callback_data="button1"),
    #         InlineKeyboardButton("Button 2", callback_data="button2"),
    #         InlineKeyboardButton("Button 3", callback_data="button3")
    #     ]]
    # )

    await m.reply_text(
        s, START_TEXT, reply_markup=START_BUTTONS
        )

@Client.on_message(filters.command("stat") & filters.private)
async def stats_handler(c: Client, m: Message):
    try:
        txt = await m.reply("`Fetching stats...`")
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
