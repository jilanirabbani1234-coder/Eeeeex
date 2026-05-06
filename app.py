import os
from flask import Flask
from threading import Thread
import asyncio
import importlib
from pyrogram import idle
from Extractor import app
from Extractor.modules import ALL_MODULES
from myutils.cleanup import start_cleanup_scheduler

# Start cleanup scheduler
scheduler = start_cleanup_scheduler()

# Flask app
flask_app = Flask(__name__)

@flask_app.route('/')
def hello_world():
    return 'Hello from Tech VJ'

def run_flask():
    flask_app.run(host='0.0.0.0', port=8080)

# Start Flask in separate thread
Thread(target=run_flask).start()

# Bot startup
async def main():
    await app.start()
    for module in ALL_MODULES:
        importlib.import_module("Extractor.modules." + module)
        print(f"Loaded module: {module}")
    print("Bot is running...")
    await idle()
    await app.stop()

if __name__ == "__main__":
    asyncio.run(main())
