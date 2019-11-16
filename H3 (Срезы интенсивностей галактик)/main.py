"""
Скрипт, строящий графики вертикальных
срезов по изображениям галактик
"""

import time  # Время выполнения скрипта

from gslices import clear as cl  # Удаления содержимого указанной папки
from gslices import slices as sl  # Вертикальные срезы

# Включение таймера
start = time.time()

# Удаления содержимого указанной папки
cl.clear_dir("output")

# Получение вертикальных срезов
sl.slice_data("data", "output", clean=False)

# Получения вертикальных срезов (понижена чувствительность)
sl.slice_data("data/149", "output/149", isens=400)

# Выключение таймера
end = time.time()

# Вывод времени выполнения скрипта
print("Время выполнения: " + str(end - start))
