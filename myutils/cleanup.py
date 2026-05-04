# utils/cleanup
import os
import time
from pathlib import Path
from apscheduler.schedulers.background import BackgroundScheduler

TEMP_DIR = Path("/app/tmp")

if not TEMP_DIR.exists():
    TEMP_DIR.mkdir(parents=True)

def clean_old_files():
    current_time = time.time()
    thirty_minutes_ago = current_time - (30 * 60)
    for file_path in TEMP_DIR.iterdir():
        if file_path.is_file():
            file_stat = file_path.stat()
            creation_time = file_stat.st_ctime
            if creation_time < thirty_minutes_ago:
                try:
                    file_path.unlink()
                    print(f"Deleted old file: {file_path}")
                except Exception as e:
                    print(f"Error deleting {file_path}: {e}")

def start_cleanup_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(clean_old_files, 'interval', minutes=10)
    scheduler.start()
    print("Cleanup scheduler started.")
    return scheduler

if __name__ == "__main__":
    scheduler = start_cleanup_scheduler()
    try:
        while True:
            time.sleep(60)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
