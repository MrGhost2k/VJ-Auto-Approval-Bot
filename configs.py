# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "27665094"))
    API_HASH = getenv("API_HASH", "7ac316483449a74fba1102491fbf34b7")
    BOT_TOKEN = getenv("BOT_TOKEN", "5829825871:AAGedDyMziJ_gwBVWeO-wPYBQpGqYXCsxdU")
    FSUB = getenv("FSUB", "VJ_Botz")
    CHID = int(getenv("CHID", "-1001623633000"))
    SUDO = list(map(int, getenv("SUDO", "1957293487").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://sushankm16:4i1WAfPYKWyqPIDD@cluster0.sngp9pz.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
