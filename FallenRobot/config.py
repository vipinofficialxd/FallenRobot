class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = "16051908"
    API_HASH = "abf9b83f9ca40cf9f5ba9bf6e6afaa8b"

    CASH_API_KEY = "V3GINZ5GSBYKPMF1"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgres://ncuydipp:ZyoDiKlPA_KiWW_9DxQw0LWwbU1bcx1z@berry.db.elephantsql.com/ncuydipp"  # A sql database url from elephantsql.com

    EVENT_LOGS = "-1001842160008"  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://starxrobo:starxrobo@cluster0.efstcnr.mongodb.net/?retryWrites=true&w=majority"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://te.legra.ph/file/0e20f2832a8a845dd9c2f.jpg"

    SUPPORT_CHAT = "TH3ONLYSUPPORT"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "6112798069:AAEGdT2gJwCDBzDf5E6YzWAOcq6Bp8xBs7A"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "G1VE375UCXVX"  # Get this value from https://timezonedb.com/api

    OWNER_ID = "5171357677"  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
