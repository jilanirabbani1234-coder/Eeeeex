import os
import asyncio
from flask import Flask
from threading import Thread
from pyrogram import Client, idle

# Flask Setup (Render Health Check ke liye)
app = Flask(__name__)
@app.route('/')
def status(): return "Bot is Alive! 🚀"

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

# Background mein Flask chalu karein
Thread(target=run_flask, daemon=True).start()

# Client Setup
bot = Client(
    "my_bot",
    api_id=os.getenv("API_ID"),
    api_hash=os.getenv("API_HASH"),
    bot_token=os.getenv("BOT_TOKEN"),
    plugins=dict(root="Extractor/modules") # Folder name check kar lena
)

async def main():
    await bot.start()
    print("Bot Started Successfully!")
    await idle()

if __name__ == "__main__":
    # Naya event loop create karke bot run karna
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    
