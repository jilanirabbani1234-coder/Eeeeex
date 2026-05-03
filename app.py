import os
import asyncio
from flask import Flask
from threading import Thread
from pyrogram import Client, idle, filters # filters add kiya
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton # buttons ke liye
from cleanup import start_cleanup_scheduler

# Flask setup
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello from Tech VJ'

def run_flask():
    app.run(host='0.0.0.0', port=8080)

# Environment Variables
api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("BOT_TOKEN")

bot = Client(
    "my_bot",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token,
    sleep_threshold=60,
)

# Start Command with Buttons
@bot.on_message(filters.command("start") & filters.private)
async def start_handler(client, message):
    await message.reply_text(
        f"Hello {message.from_user.mention}!\nWelcome to Tech VJ Bot.",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("Help", callback_data="help"),
             InlineKeyboardButton("About", callback_data="about")]
        ])
    )

# Baaki messages ke liye alag handler (Optionally)
@bot.on_message(filters.text & ~filters.command("start"))
async def echo(client, message):
    await message.reply("Aapne message bheja, par main abhi sirf /start samajhta hoon!")

async def main():
    # Flask ko yahan start karein
    t = Thread(target=run_flask)
    t.daemon = True # Taaki main program band hone par ye bhi band ho jaye
    t.start()
    
    # Cleanup scheduler start
    scheduler = start_cleanup_scheduler()
    
    try:
        await bot.start()
        print("Bot is running...")
        await idle()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Shutdown logic (RuntimeError se bachne ke liye)
        if scheduler.running:
            scheduler.shutdown()
        await bot.stop()

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
    
