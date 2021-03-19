from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime

def reminder():
	# what do you want to happen every time the job triggers
	# print(now.strftime("%d/%m/%Y %H:%M:%S"))
	
scheduler = BlockingScheduler()
scheduler.add_job(reminder, 'cron', hour='0-23') # available parameters at: https://apscheduler.readthedocs.io/en/stable/modules/triggers/cron.html
scheduler.start()