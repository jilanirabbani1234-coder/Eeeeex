import os
import asyncio
from flask import Flask
from threading import Thread
from pyrogram import Client, idle
from cleanup import start_cleanup_scheduler

# 1. Flask App Setup (Render ko 'Live' dikhane ke liye)
app = Flask(__name__)

@app.route('/')
def status():
    return "Bot is Running and Extractor Modules are Loaded! 🚀"

def run_flask():
    # Render hamesha port 8080 ya 10000 maangta hai
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8080)))

# Flask ko background thread mein start karein
Thread(target=run_flask, daemon=True).start()

# 2. Environment Variables (Credentials)
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

# 3. Pyrogram Client Setup with Plugins
# Hum 'root="Extractor/modules"' isliye de rahe hain taaki downloader files load hon
bot = Client(
    "my_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="Extractor/modules"), 
    sleep_threshold=60
)

async def main():
    # Cleanup scheduler start (Agar 'cleanup' file sahi hai to)
    try:
        start_cleanup_scheduler()
        print("Cleanup Scheduler Started...")
    except Exception as e:
        print(f"Cleanup Error: {e}")

    try:
        # Bot start karna
        await bot.start()
        print("////////////////////////////////////////")
        print("      EXTRACTOR BOT IS NOW LIVE!        ")
        print("////////////////////////////////////////")
        
        # Bot ko chalu rakhne ke liye
        await idle()
        
    except Exception as e:
        print(f"Bot Crash Error: {e}")
    finally:
        # Properly band karna taaki error na aaye
        await bot.stop()

if __name__ == "__main__":
    # Event loop ke saath bot run karna
    try:
        asyncio.get_event_loop().run_until_complete(main())
    except KeyboardInterrupt:
        pass
        
