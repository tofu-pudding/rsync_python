from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler,FileSystemEventHandler
from Loguru import my_logger
import os

from Rsync import rsync_pool


class MyHandler(FileSystemEventHandler):
    def __init__(self,source, target):
        FileSystemEventHandler.__init__(self)
        self.source = source
        self.target = target

    def on_created(self, event):
        # 排除临时文件
        if event.is_directory or os.path.basename(event.src_path).startswith("."):
            pass
        else:
            print("文件创建触发")
            relative_path = os.path.relpath(event.src_path, self.source)
            if relative_path.endswith("/"):
                pass
            target_path = self.target + "/" +relative_path
            rsync_pool([(event.src_path,target_path,False)])
            my_logger.info(target_path + "file add")

class mymonitor():
    def __init__(self, config):
        observer = Observer()
        for dir in config:
            event_handler = MyHandler(dir['source'],dir['target'])
            watch = observer.schedule(event_handler, dir['source'], recursive=True)
        log_handler = LoggingEventHandler()
        observer.add_handler_for_watch(log_handler, watch)
        self.observer = observer

    def start(self):
        self.observer.start()

    def stop(self):
        self.observer.stop()

    def join(self):
        self.observer.join()
