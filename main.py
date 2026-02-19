import os
import sys
import random
import asyncio
from config import API_HASH, API_ID, BOT_TOKEN, SESSION_NAME, SESSION2, SESSION3, SESSION4, SESSION5
from pyrogram import Client
from pytgcalls import idle
from pytgcalls import PyTgCalls
from Zaid.Database.clientdb import get_assistant, save_assistant

# Timezone သတ်မှတ်ပါ
os.environ['TZ'] = 'Asia/Yangon'

bot = Client(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins={"root": "Zaid.Player"},
    sleep_threshold=120,
    workers=4,
    app_version="1.0.0",
    device_model="Railway"
)

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
    
    # Bot က run နေပြီးသားလားစစ်ပါ
    try:
        if bot.is_connected:
            print("[INFO]: Bot is already connected")
        else:
            # Retry logic without raising exception
            max_retries = 5
            bot_started = False
            
            for i in range(max_retries):
                try:
                    await asyncio.wait_for(bot.start(), timeout=30)
                    print(f"[INFO]: Bot started successfully on attempt {i+1}")
                    bot_started = True
                    break
                except asyncio.TimeoutError:
                    print(f"[WARN]: Bot start timeout, retrying... ({i+1}/{max_retries})")
                    await asyncio.sleep(10)
                except Exception as e:
                    if "already connected" in str(e).lower():
                        print("[INFO]: Bot is already connected")
                        bot_started = True
                        break
                    else:
                        print(f"[WARN]: Bot start error: {e}")
                        await asyncio.sleep(10)
            
            if not bot_started:
                print("[ERROR]: Bot could not start after all retries")
                return
    except Exception as e:
        print(f"[WARN]: Error checking bot connection: {e}")
    
    # Bot info ကိုရယူပါ - with retry logic
    try:
        global me_bot
        me_bot = None
        
        # get_me() ကို ၃ ကြိမ်အထိ ပြန်ကြိုးစားမယ်
        for j in range(3):
            try:
                me_bot = await bot.get_me()
                if me_bot:
                    break
            except Exception as e:
                print(f"[WARN]: get_me attempt {j+1}/3 failed: {e}")
                if j < 2:
                    await asyncio.sleep(5)
        
        if me_bot:
            print(f"[INFO]: Bot started as @{me_bot.username}")
        else:
            print("[WARN]: Could not get bot info after 3 attempts")
            me_bot = None
    except Exception as e:
        print(f"[WARN]: Failed to get bot info: {e}")
        me_bot = None
    
    # Assistant clients start (continue even if some fail)
    assistant_count = 0
    
    if SESSION_NAME != "None" and ASS_CLI_1:
       try:
           if not Test.is_connected:
               await Test.start()
           if call_py:
               await call_py.start()
           random_assistant.append(1)
           assistant_count += 1
           print("[INFO]: Assistant 1 started")
       except Exception as e:
           print(f"[WARN]: Assistant 1 failed to start: {e}")
       
    if SESSION2 != "None" and user:
       try:
           if not user.is_connected:
               await user.start()
           if call_py2:
               await call_py2.start()
           random_assistant.append(2)
           assistant_count += 1
           print("[INFO]: Assistant 2 started")
       except Exception as e:
           print(f"[WARN]: Assistant 2 failed to start: {e}")
       
    if SESSION3 != "None" and user3:
       try:
           if not user3.is_connected:
               await user3.start()
           if call_py3:
               await call_py3.start()
           random_assistant.append(3)
           assistant_count += 1
           print("[INFO]: Assistant 3 started")
       except Exception as e:
           print(f"[WARN]: Assistant 3 failed to start: {e}")
       
    if SESSION4 != "None" and user4:
       try:
           if not user4.is_connected:
               await user4.start()
           if call_py4:
               await call_py4.start()
           random_assistant.append(4)
           assistant_count += 1
           print("[INFO]: Assistant 4 started")
       except Exception as e:
           print(f"[WARN]: Assistant 4 failed to start: {e}")
       
    if SESSION5 != "None" and user5:
       try:
           if not user5.is_connected:
               await user5.start()
           if call_py5:
               await call_py5.start()
           random_assistant.append(5)
           assistant_count += 1
           print("[INFO]: Assistant 5 started")
       except Exception as e:
           print(f"[WARN]: Assistant 5 failed to start: {e}")
       
    random_assistant.append(6)
    
    print(f"[INFO]: Total assistants started: {assistant_count}")
    print("[INFO]: Your Bot Has been Started")
    print("[INFO]: Entering idle state...")
    
    # Idle မသွားခင် ခဏစောင့်ပါ
    await asyncio.sleep(2)
    
    # Pyrogram idle ကိုသုံးမယ်
    await idle()

def init_db():
    global db_mem
    db_mem = {}

init_db()
