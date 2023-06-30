from pyrogram import Client, filters
from configs import Config
import asyncio
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.private & filters.incoming)
async def force_subscribe(c: Client, m: Message):
    try:
        # Check if the user is a member of the force subscribe channel
        chat_member = await c.get_chat_member(int(Config.UPDATES_CHANNEL), m.from_user.id)
        if chat_member.status == "kicked":
            # If the user is kicked, send a message
            await m.reply_text("Sorry, you have been kicked and cannot access this bot's features.")
            return
 
    except FloodWait as e:
        await asyncio.sleep(e.x)
        return 400
    
    except UserNotParticipant:
        # If the user is not a member, send a force subscribe message
        invite_link = await c.create_chat_invite_link(int(Config.UPDATES_CHANNEL))
        
        # Create an inline keyboard with the invite link button
        inline_keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("Join Channel", url=invite_link.invite_link)]])
        
        await c.send_message(
            chat_id=m.chat.id,
            text="Please join the force subscribe channel to access this bot's features:",
            reply_markup=inline_keyboard
        )
        return
    except Exception as error:
        await c.send_message(
            chat_id=m.chat.id,
            text=f"An error occurred: {error}"
        ) 
        return

# # Define the function to generate the primary invite link
# def generate_primary_invite_link():
#     # Check if a primary invite link already exists
#     chat = c.get_chat(Config.UPDATES_CHANNEL)
#     if chat.invite_link is not None:
#         return chat.invite_link
    
#     # Generate a new primary invite link
#     invite_link = c.export_chat_invite_link(Config.UPDATES_CHANNEL).invite_link
#     return invite_link

# # Get the primary invite link
# primary_invite_link = generate_primary_invite_link()

# # Print the primary invite link
# print(primary_invite_link)