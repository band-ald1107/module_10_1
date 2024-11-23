import threading
from time import sleep, time

def write_words(word_count, file_name):
    with open(file_name, 'w', encoding = 'utf-8') as f:
        for i in range(1, word_count + 1):
            f.write(f"Какое-то слово № {i}\n")
            sleep(0.1)  # Пауза 0.1 секунды
    print(f"Завершилась запись в файл {file_name}")

# Измеряем время выполнения функции
start_time = time()

# Вызов функции с заданными аргументами
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

end_time = time()
print(f"Время выполнения функций: {end_time - start_time:.6f} секунд")

# Для запуска в потоках
def thread_function(word_count, file_name):
    write_words(word_count, file_name)

# Время начала работы потоков
start_time_threads = time()

# Создаем потоки
threads = [
    threading.Thread(target=thread_function, args=(10, 'example5.txt')),
    threading.Thread(target=thread_function, args=(30, 'example6.txt')),
    threading.Thread(target=thread_function, args=(200, 'example7.txt')),
    threading.Thread(target=thread_function, args=(100, 'example8.txt')),
]

# Запускаем потоки
for thread in threads:
    thread.start()

# Ждем завершения всех потоков
for thread in threads:
    thread.join()

end_time_threads = time()
print(f"Время работы потоков: {end_time_threads - start_time_threads:.6f} секунд")