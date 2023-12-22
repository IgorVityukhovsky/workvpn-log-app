import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Путь к файлу для анализа
file_path = '/tmp/openvpn-status.log'

def read_file_content():
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")

class FileModifiedHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path == file_path and event.is_directory is False:
            print(f"Файл {file_path} был изменен.")
            read_file_content()

if __name__ == "__main__":
    read_file_content()

    event_handler = FileModifiedHandler()
    observer = Observer()
    observer.schedule(event_handler, path='/tmp', recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()