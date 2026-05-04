import os
import sys
import random
import asyncio
from flask import Flask
from threading import Thread
from config import API_HASH, API_ID, BOT_TOKEN, SESSION_NAME, SESSION2, SESSION3, SESSION4, SESSION5
from pyrogram import Client
from pytgcalls import idle
from pytgcalls import PyTgCalls
from Zaid.Database.clientdb import get_assistant, save_assistant

# --- Render အတွက် Web Server စတင်ခြင်း (ဒီအပိုင်းကို အသစ်ထည့်ပါ) ---
app = Flask('')

@app.route('/')
def home():
    return "Bot is Running"

def run():
    # Render က Port 10000 သို့မဟုတ် 8080 ကို သုံးလေ့ရှိပါတယ်
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run)
    t.start()
# ---------------------------------------------------------

# Timezone သတ်မှတ်ပါ
os.environ['TZ'] = 'Asia/Yangon'

# Bot Client များ သတ်မှတ်ချက် (သင့် code အတိုင်း)
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

# ... (သင့်ရဲ့ Sessions code တွေ ဒီကြားထဲမှာ ရှိမယ်) ...

async def start_bot():
    print("[INFO]: STARTING BOT CLIENT")
    
    # Render အတွက် Web Server ကို ဒီနေရာမှာ စတင်လိုက်ပါ
    print("[INFO]: Starting Web Server for Render...")
    keep_alive() 

    # --- သင့်ရဲ့ ကျန်တဲ့ bot start logic တွေ အောက်မှာ ဆက်သွားမယ် ---
    try:
        if not bot.is_connected:
            await bot.start()
            print("[INFO]: Bot started successfully")
    except Exception as e:
        print(f"[ERROR]: {e}")

    # ... (ကျန်တဲ့ Assistant client code များ) ...

    await idle()

# Bot စတင်ရန်
if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(start_bot())
