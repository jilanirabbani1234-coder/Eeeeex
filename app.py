import os
from flask import Flask
from threading import Thread
from pyrogram import Client, idle
import asyncio
from cleanup import start_cleanup_scheduler

# 1. Flask setup (Render fix)
app = Flask(__name__)
@app.route('/')
def status():
    return "Bot is Running! 🚀"

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

Thread(target=run_flask, daemon=True).start()

# 2. Environment Variables
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

# 3. Client Setup 
# HUM 'plugins' WALA OPTION HATA RAHE HAIN 
# Kyunki __init__.py khud load kar raha hai modules ko
bot = Client(
    "my_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# 4. Manual Plugin Loading Logic
async def main():
    try:
        start_cleanup_scheduler()
    except:
        pass

    await bot.start()
    
    # Ye line manually modules load karegi bina __init__.py ko disturb kiye
    # Agar aapka folder 'Extractor/modules' hai to:
    from pyrogram.methods.utilities.idle import idle
    
    print("////////////////////////////////////////")
    print("      EXTRACTOR BOT IS NOW ONLINE!      ")
    print("////////////////////////////////////////")
    
    await idle()
    await bot.stop()

if __name__ == "__main__":
    # Naya loop create karke error bypass karna
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except Exception as e:
        print(f"Final Error: {e}")
        
