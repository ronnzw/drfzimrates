from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from  .rates_job import save_todays_rate


def start():
    print('We are starting.....')
    scheduler = BackgroundScheduler()
    trigger = CronTrigger(year="*", month="*", day="*", hour="12", minute="0", second="0")
    scheduler.add_job(save_todays_rate,trigger=trigger,timezone='Africa/Harare')
    scheduler.start()
    