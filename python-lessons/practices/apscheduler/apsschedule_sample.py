# -*- coding:utf-8 -*-

# cron job samples
import datetime
import os
import subprocess
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()
current_folder = os.getcwd()


def schedule_job():
    print("job started at " + str(datetime.datetime.now()))
    try:
        subprocess.call(["python", current_folder + "/apscheduler/print_job.py"])
    except Exception as e:
        print(e)


sched.add_job(schedule_job,
              'cron',
              hour=18, id='crawl job')
sched.start()
