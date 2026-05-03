import os
from flask import Flask
from threading import Thread
from pyrogram import Client, idle
from cleanup import start_cleanup_scheduler

# 1. Flask Setup
app = Flask(__name__)

@app.route('/')
def status():
    return "Bot is Running! 🚀"

def run_flask():
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

# 2. Environment Variables
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

# 3. Client Setup
bot = Client(
    "my_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="Extractor/modules")
)

# 4. Main Function
async def start_services():
    # Flask start
    Thread(target=run_flask, daemon=True).start()
    
    # Scheduler start
    try:
        start_cleanup_scheduler()
        print("Cleanup Scheduler Started...")
    except Exception as e:
        print(f"Scheduler Error: {e}")

    # Bot start message
    print("////////////////////////////////////////")
    print("      EXTRACTOR BOT IS STARTING...      ")
    print("////////////////////////////////////////")
    
    await idle()

if __name__ == "__main__":
    # Pyrogram ka native run method jo event loop handle kar leta hai
    bot.run(start_services())
    
