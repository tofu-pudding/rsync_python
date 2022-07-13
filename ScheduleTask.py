import datetime
from Loguru import my_logger
import time
import schedule

from Rsync import rsync_pool


class scheduleTask():
    def __init__(self, config):
        self.config = config

    def rsync_whole(self):
        list = []
        for dir in self.config:
            list.append((dir['source'], dir['target'],True))
        rsync_pool(list)

    def start(self):
        self.rsync_whole()
        schedule.every(7).days.do(self.rsync_whole)
        while True:
            schedule.run_pending()
            time.sleep(2)
