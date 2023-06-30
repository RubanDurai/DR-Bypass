from pyrogram import Client
from pyrogram.types import CallbackQuery
from translation import *

# Handler for inline keyboard button callbacks
@Client.on_callback_query()
async def handle_callback_query(client, query: CallbackQuery):
    # Get the callback data
    callback_data = query.data

    if callback_data == "home":
        # Handle the "home" callback
        if query.message:
            await query.message.edit_text(
                text=START_MSG.format(query.from_user.mention),
                disable_web_page_preview=True,
                reply_markup=START_BUTTONS
            )
    elif callback_data == "help":
        # Handle the "help" callback
        if query.message:
            await query.message.edit_text(
                text=HELP_MSG,
                disable_web_page_preview=True,
                reply_markup=HELP_BUTTONS
            )
    elif callback_data == "about":
        # Handle the "about" callback
        if query.message:
            await query.message.edit_text(
                text=ABOUT_MSG,
                disable_web_page_preview=True,
                reply_markup=ABOUT_BUTTONS
            )
    elif callback_data == "disclaimer":
        # Handle the "disclaimer" callback
        if query.message:
            await query.message.edit_text(
                text=DISCLAIMER_MSG,
                disable_web_page_preview=True,
                reply_markup=DISCLAIMER_BUTTONS
            )
    elif callback_data == "devlopers":
        # Handle the "devlopers" callback
        if query.message:
            await query.message.edit_text(
                text=DEVELOPERS_MSG,
                disable_web_page_preview=True,
                reply_markup=DEVELOPERS_BUTTONS
            )

    elif callback_data == "delete":
        if query.message:
            await query.message.delete()
