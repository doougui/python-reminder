from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
from plyer import notification
from playsound import playsound
from pathlib import Path

def reminder():
	now = datetime.now()
	notification.notify(
	    title = "Reality checker at {}".format(now.strftime("%d/%m/%Y %H:%M:%S")),
	    message = "Are you dreaming? Is this real? Pull your finger to find out.",
	    timeout  = 30
	)
	try:
		playsound('{}/assets/sound/time-is-now-585.mp3'.format(Path(__file__).parent.absolute()))
	except Exception as e:
		notification.notify(
		    title = "Failed to play audio",
		    message = "It was not possible to play the audio file. Please check the source code to fix the problem. Error: {}".format(e),
		    timeout  = 30
		)


scheduler = BlockingScheduler()
scheduler.add_job(reminder, 'cron', hour='0-23') # available parameters at: https://apscheduler.readthedocs.io/en/stable/modules/triggers/cron.html
scheduler.start()