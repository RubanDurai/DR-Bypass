from pyrogram import Client, filters
from configs import Config
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.private & filters.incoming)
async def forcesub_handler(c: Client, m: Message):
    owner = c.owner
    if Config.UPDATES_CHANNEL:
        invite_link = c.invite_link
        try:
            user = await c.get_chat_member(Config.UPDATES_CHANNEL, m.from_user.id)
            if user.status == "kicked":
                await m.reply_text("**Hey you are banned 😜**", quote=True)
                return
        except UserNotParticipant:
            buttons = [
                [
                    InlineKeyboardButton(
                        text="Updates Channel", url=invite_link.invite_link
                    )
                ]
            ]
            buttons.append(
                [InlineKeyboardButton("🔄 Refresh", callback_data="sub_refresh")]
            )

            await m.reply_text(
                f"Hey {m.from_user.mention(style='md')} you need join My updates channel in order to use me\n\n"
                "Press the Following Button to join Now ",
                reply_markup=InlineKeyboardMarkup(buttons),
                quote=True,
            )
            return
        except Exception as e:
            print(e)
            await m.reply_text(
                f"Something Wrong. Please try again later or contact {owner.mention(style='md')}",
                quote=True,
            )
            return
    await m.continue_propagation()