import os
from pyrogram import Client
from configs import Config

class Bot(Client):
    def __init__(self):
        super().__init__(
            "my_bot",
            bot_token=Config.BOT_TOKEN,
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            plugins=dict(root="plugins")
        )
    
    async def start_bot(self):
        await self.start()
        await self.idle()

if __name__ == "__main__":
    print("Bot Started ..")
    bot = Bot()
    bot.run()