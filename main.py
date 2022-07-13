from GetConfig import getConfig
from Loguru import my_logger
from Watchdog import mymonitor
from ScheduleTask import scheduleTask
import traceback


if __name__ == "__main__":
    try:
      configfile = getConfig("./config.ini")
      config = configfile.getconfig()
      watchdog = mymonitor(config)
      watchdog.start()
      schedule = scheduleTask(config)
      schedule.start()
    except KeyboardInterrupt:
        my_logger.error(traceback.print_exc())
        watchdog.stop()
    watchdog.join()