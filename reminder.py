from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
from plyer import notification
from playsound import playsound

def reminder():
	now = datetime.now()
	notification.notify(
	    title = "Reality checker at {}".format(now.strftime("%d/%m/%Y %H:%M:%S")),
	    message = "Are you dreaming? Is this real? Pull your finger to find out.",
	    timeout  = 30
	)
	playsound('assets/sound/time-is-now-585.mp3')

scheduler = BlockingScheduler()
scheduler.add_job(reminder, 'cron', hour='0-23') # available parameters at: https://apscheduler.readthedocs.io/en/stable/modules/triggers/cron.html
scheduler.start()