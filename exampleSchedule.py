import schedule
import time

def job():
    print("Running scheduled task...")

#schedule.every(10).seconds.do(job)
#schedule.every().hour.do(job)
#schedule.every().day.at("12:39").do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
