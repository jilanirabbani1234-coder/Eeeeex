import os
from flask import Flask
from threading import Thread
from pyrogram import Client, idle
from cleanup import start_cleanup_scheduler

# 1. Flask setup (Render ke liye zaroori)
app = Flask(__name__)

@app.route('/')
def status():
    return "Bot is Running! 🚀"

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

# Flask ko background thread mein start karein
Thread(target=run_flask, daemon=True).start()

# 2. Env Variables
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

# 3. Client Setup
# Agar __init__.py mein lambe codes hain, to hum root ko 'Extractor' tak rakhte hain
# Taaki wo poore package ko sahi se scan kare
bot = Client(
    "my_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="Extractor/modules")
)

async def main():
    try:
        start_cleanup_scheduler()
    except:
        pass

    await bot.start()
    print("////////////////////////////////////////")
    print("      BOT IS SUCCESSFULLY STARTED!      ")
    print("////////////////////////////////////////")
    
    await idle()
    await bot.stop()

if __name__ == "__main__":
    # Native method to avoid loop conflict
    bot.run(main())
    
