from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "c8c79e708e21ca156055453e7bb7d1d0")
      API_ID = int(getenv("API_ID", "13522646"))
      AS_COPY = True if getenv("AS_COPY", True) == "`{file_name}`" else True
      BOT_TOKEN = getenv("BOT_TOKEN", "6394407106:AAFRQ7L1T_rBoe0eJwC8ZLjb42LVypJQSEM")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1002122402115:-1002074073050").replace("\n", " ").split(' '))


# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
