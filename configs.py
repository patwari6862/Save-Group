# (c) @AbirHasan2005

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 12345))
    API_HASH = os.environ.get("API_HASH", None)
    STRING_SESSION = os.environ.get("STRING_SESSION", ""
    FORCE_SUB_CHANNEL = os.environ.get("FORCE_SUB_CHANNEL", None)
    MONGODB_URI = os.environ.get("MONGODB_URI", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
