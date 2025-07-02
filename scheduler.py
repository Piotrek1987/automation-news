import schedule
import time
from fetch_and_cache_news import fetch_and_cache

# Schedule it every day at 07:00
schedule.every().day.at("07:00").do(fetch_and_cache)

print("⏰ Scheduler is running...")

while True:
    schedule.run_pending()
    time.sleep(60)
