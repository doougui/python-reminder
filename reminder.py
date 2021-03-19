from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
from plyer import notification

def reminder():
	now = datetime.now()
	notification.notify(
	    title = "Reality checker at {}".format(now.strftime("%d/%m/%Y %H:%M:%S")),
	    message = "Are you dreaming? Is this real? Pull your finger to find out.",
	    timeout  = 30
	)

scheduler = BlockingScheduler()
scheduler.add_job(reminder, 'cron', second='0-59') # available parameters at: https://apscheduler.readthedocs.io/en/stable/modules/triggers/cron.html
scheduler.start()