import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "6435225"))
    API_HASH = os.environ.get("API_HASH", "4e984ea35f854762dcde906dce426c2d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5876413751:AAGYXCkhdXAdA-G_L9O4CMCYNyNzTizQL_I")
    STRING_SESSION = os.environ.get("STRING_SESSION", "BQBwd8ps81uh4QyuYWDY0H_SMkBZMn_344912d8hskYeZ_Bdy9Xvq5cgdx1Y2YON_QrLGGoD6YPx-0IEn5aNNgBNoGIL1E-7aBnr40QPoZDLE9fjrGnWRxqlNoK8zQgGSGlK9lHPS6YSf1ZanN1jHrLzTIQlKSL42xVLu_EHyyYbzCzZaTcOJ5KLx-0EHbGvGvxbh1_R_vBVbWdIZHpiBzSo_lnoxYdsESJPfMyWSRGK7IYDrnVoRDWVoTQ3I-lXdEPu1W4ZAFVsAGQu4UrAd1Sw2qp9dkscB6azhRQ-JO2WJO_scJrqgOjp8sQdxnx1nk7JAWbD5TpU6JpMPMUhUBJiAAAAAUTIe4gA")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "NixaVcBot")
    SUPPORT = os.environ.get("SUPPORT", "SankiWorldMF") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "NixaWorld") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5448956808")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', True) # Change it to "True"
