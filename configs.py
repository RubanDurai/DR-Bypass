import os

class Config:
    API_ID = int(os.environ.get("API_ID", "6596420"))
    API_HASH = os.environ.get("API_HASH", "d052e942057719c009374ea083a1a57d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "2068606974:AAGB9d62iBllI8MpAPZAtll5goQ23TB0PKU")
    ADMINS = int(os.environ.get("ADMINS", "1389078939"))
    UPDATES_CHANNEL = int(os.environ.get("UPDATES_CHANNEL", "-1001582342980"))
