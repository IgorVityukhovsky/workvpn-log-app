import time
import re
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Путь к файлу для анализа
file_path = '/tmp/openvpn-status.log'

def read_file_content():
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            #print(content)
    except FileNotFoundError:
        print(f"0")

def count_and_divide():
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            pattern = r'\b10\.244\.0\.1\b'  # Используем регулярное выражение для поиска строки
            count = len(re.findall(pattern, content))
            result = count // 2
            return result
    except FileNotFoundError:
        print(f"0")
        return None

# Использование функции и вывод результата
result = count_and_divide()
if result is not None:
    print(f"{result}")

class FileModifiedHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path == file_path and event.is_directory is False:
            count_and_divide()
            result = count_and_divide()
            if result is not None:
               print(f"{result}")

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