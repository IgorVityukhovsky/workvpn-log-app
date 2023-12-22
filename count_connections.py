import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Путь к файлу для анализа
file_path = 'путь_к_вашему_файлу.txt'

# Функция для подсчета вхождений строки "CLIENT_LIST"
def count_client_list_occurrences(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            count = content.count('CLIENT_LIST')
            print(f'Количество вхождений "CLIENT_LIST": {count}')
            return count
    except FileNotFoundError:
        print("Файл не найден")

# Класс обработчика событий файловой системы
class FileModifiedHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path == file_path:
            print('Файл был изменен!')
            count_client_list_occurrences(file_path)

# Создание наблюдателя за файлами
event_handler = FileModifiedHandler()
observer = Observer()
observer.schedule(event_handler, path='.', recursive=False)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()

# k delete po app --force --grace-period 0 && k apply -f https://raw.githubusercontent.com/IgorVityukhovsky/workvpn-log-app/main/app.yml