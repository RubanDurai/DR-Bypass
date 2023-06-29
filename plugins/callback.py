from pyrogram import Client, filters
from pyrogram.types import CallbackQuery
from pyrogram.errors import UserNotParticipant
import contextlib
from translation import *
from configs import Config

# @Client.on_callback_query(filters.regex("sub_refresh"))
# async def refresh_cb(c, m):
#     owner = c.owner
#     if Config.UPDATES_CHANNEL:
#         try:
#             user = await c.get_chat_member(Config.UPDATES_CHANNEL, m.from_user.id)
#             if user.status == "kicked":
#                 with contextlib.suppress(Exception):
#                     await m.message.edit("**Hey you are banned**")
#                 return
#         except UserNotParticipant:
#             await m.answer(
#                 "You have not yet joined our channel. First join and then press refresh button",
#                 show_alert=True,
#             )

#             return
#         except Exception as e:
#             print(e)
#             await m.message.edit(
#                 f"Something Wrong. Please try again later or contact {owner.mention(style='md')}"
#             )

#             return
#     await m.message.delete()


@Client.on_callback_query()
async def handle_callback(bot : Client, query : CallbackQuery):

    if query.data == "home":
        await query.edit_message_text(
            text=START_TEXT.format(query.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=START_BUTTONS
        )
    elif query.data == "help":
        await query.edit_message_text(
            text=HELP_TEXT,
            disable_web_page_preview=True,
            reply_markup=HELP_BUTTONS
        )
    elif query.data == "about":
        await query.edit_message_text(
            text=ABOUT_TEXT,
            disable_web_page_preview=True,
            reply_markup=ABOUT_BUTTONS
        )

