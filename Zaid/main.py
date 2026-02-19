import os
import sys
import random
import asyncio
from config import API_HASH, API_ID, BOT_TOKEN, SESSION_NAME, SESSION2, SESSION3, SESSION4, SESSION5
from pyrogram import Client
from pytgcalls import idle
from pytgcalls import PyTgCalls
from Zaid.Database.clientdb import get_assistant, save_assistant

bot = Client(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins={"root": "Zaid.Player"},
)

# Assistant clients
if not SESSION_NAME:
   ASS_CLI_1 = None
else:   
   ASS_CLI_1 = Client(SESSION_NAME, api_id=API_ID, api_hash=API_HASH)

if not SESSION2:
   user = None
else:
   user = Client(SESSION2, api_id=API_ID, api_hash=API_HASH)

if not SESSION3:
   user3 = None
else:
   user3 = Client(SESSION3, api_id=API_ID, api_hash=API_HASH)

if not SESSION4:
   user4 = None
else:
   user4 = Client(SESSION4, api_id=API_ID, api_hash=API_HASH)

if not SESSION5:
   user5 = None
else:
   user5 = Client(SESSION5, api_id=API_ID, api_hash=API_HASH)

# ဒီအောက်က ":umm:" ဆိုတဲ့ Client ကိုဖျက်ပစ်လိုက်ပါ
# with Client(":umm:", API_ID, API_HASH, bot_token=BOT_TOKEN) as app:
#    me_bot = app.get_me()

Test = ASS_CLI_1
ASS_CLI_2 = user
call_py = PyTgCalls(ASS_CLI_1) if ASS_CLI_1 else None
call_py2 = PyTgCalls(user) if user else None
call_py3 = PyTgCalls(user3) if user3 else None
call_py4 = PyTgCalls(user4) if user4 else None
call_py5 = PyTgCalls(user5) if user5 else None

ASSIDS = []
ASSID1 = 0
ASSNAME1 = ""
ASSUSERNAME1 = ""
ASSMENTION1 = ""
ASSID2 = 0
ASSNAME2 = ""
ASSUSERNAME2 = ""
ASSMENTION2 = ""
ASSID3 = 0
ASSNAME3 = ""
ASSUSERNAME3 = ""
ASSMENTION3 = ""
ASSID4 = 0
ASSNAME4 = ""
ASSUSERNAME4 = ""
ASSMENTION4 = ""
ASSID5 = 0
ASSNAME5 = ""
ASSUSERNAME5 = ""
ASSMENTION5 = ""
random_assistant = []

async def start_bot():
    print("[INFO]: STARTING BOT CLIENT")
    await bot.start()
    
    # Bot info ကိုရယူပါ
    global me_bot
    me_bot = bot.get_me()
    print(f"[INFO]: Bot started as @{me_bot.username}")
    
    if SESSION_NAME != "None" and ASS_CLI_1:
       await Test.start()
       if call_py:
           await call_py.start()
       random_assistant.append(1)
    if SESSION2 != "None" and user:
       await user.start()
       if call_py2:
           await call_py2.start()
       random_assistant.append(2)
    if SESSION3 != "None" and user3:
       await user3.start()
       if call_py3:
           await call_py3.start()
       random_assistant.append(3)
    if SESSION4 != "None" and user4:
       await user4.start()
       if call_py4:
           await call_py4.start()
       random_assistant.append(4)
    if SESSION5 != "None" and user5:
       await user5.start()
       if call_py5:
           await call_py5.start()
       random_assistant.append(5)
    random_assistant.append(6)
    print("[INFO]: Your Bot Has been Started")
    await idle()

def init_db():
    global db_mem
    db_mem = {}

init_db()
