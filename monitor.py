import datetime
import time

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer


######################################################
# This script does not work with mounting/unmounting #
######################################################


class Watcher:
    # TODO: DENNE MÅ ENDRES:
    DIRECTORY_TO_WATCH = "/media/pi/744E-C88C"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except Exception as e:
            self.observer.stop()
            print(f"Error: {e}")

        self.observer.join()


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            # Take any action here when a file is first created.
            print(f"Received created event - {event.src_path}.")
            with open('log.txt', 'a') as file:
                filename = event.src_path.split('/')[-1]
                dt = datetime.datetime.now()
                coords = "123,123"
                file.write(f'{"file": "{filename}", "time": "{dt}", "coords": "{coords}"}\n')

        elif event.event_type == 'modified':
            # Taken any action here when a file is modified.
            print(f"Received modified event - {event.src_path}.")


if __name__ == '__main__':
    w = Watcher()
    w.run()
