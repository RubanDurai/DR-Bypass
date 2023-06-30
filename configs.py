import os

class Config:
    API_ID = int(os.environ.get("API_ID", "6596420"))
    API_HASH = os.environ.get("API_HASH", "d052e942057719c009374ea083a1a57d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5743961840:AAGduam3pC0xP4JZlClmO3GwfDqbzkc7yV0")
    ADMINS = [int(admins) for admins in os.environ.get("ADMINS", "1389078939").split()]
    UPDATES_CHANNEL = int(os.environ.get("UPDATES_CHANNEL", "-1001582342980"))
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001190658285"))

