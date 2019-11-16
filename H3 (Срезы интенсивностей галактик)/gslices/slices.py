"""
Модуль, содержащий главные методы для
построения вертикальных срезов
по изображениям галактик
"""

import os  # Работа с путями
import fitsio  # Считывание .fits файлов
import numpy as np  # Работа с массивами

from matplotlib import pyplot as plt, rcParams as rcP  # Графики

# Значение по умолчанию для isens
isens_default = 1.5e3

# Настройки графиков

rcP["savefig.dpi"] = 300
rcP["figure.dpi"] = 300

rcP["font.size"] = 16
rcP["font.family"] = "sans"
rcP["font.sans-serif"] = ["DejaVu Sans"]


def slice_data(path_to_data: str, path_to_output: str, isens: float = isens_default, clean: bool = True):
    """
    Функция для построения вертикальных срезов
    по всем данным, найденным рекурсивно в path_to_data

    Параметры:
        path_to_data: Строка, содержащая путь к данным;
        path_to_output: Строка, содержащая путь к каталогу,
                        где будут храниться результаты
                        (директория будет иметь ту же
                        иерархию файлов, что и path_to_data);
        isens: Вещественное число, указывающее нижний предел
               для интенсивностей, при которых текущий
               вертикальный срез еще будет считаться значимым;
        clean: Логическая переменная, отвечающая за удаление
               предыдущих результатов для найденных файлов
    """

    # Рекурсивный проход по всем данным в path_to_data
    for cur, folders, files in os.walk(path_to_data):
        for file in files:

            # Если найден .fits файл:
            if file.lower().endswith(".fits"):

                # Вызов функции для работы с этим файлом
                slice_file(path_to_data, os.path.join(cur, file)[len(path_to_data) + 1:], path_to_output, isens, clean)


def slice_file(path_to_data: str, path_to_file: str, path_to_output: str, isens: float = isens_default,
               clean: bool = True):
    """
    Функция для построения вертикального среза
    по данным из файла path_to_file

    Параметры:
        path_to_data: Строка, содержащая путь к данным;
        path_to_file: Строка, содержащая путь к .fits файлу
                      относительно path_to_data;
        path_to_output: Строка, содержащая путь к каталогу,
                        где будут храниться результаты;
        isens: Вещественное число, указывающее нижний предел
               для интенсивностей, при которой текущий
               вертикальный срез еще будет считаться значимым;
        clean: Логическая переменная, отвечающая за удаление
               предыдущих результатов для текущего файла
    """

    # Сборка пути к зеркальной
    # директории в path_to_output

    path_to_output_directory = os.path.join(path_to_output, path_to_file[:-5])

    # Создание, если необходимо,
    # директории в path_to_output

    if not os.path.isdir(path_to_output_directory):
        os.makedirs(path_to_output_directory)

    # Удаление результатов предыдущего
    # пропуска для этого файла
    elif clean:
        for cur, folders, files in os.walk(path_to_output_directory):
            for file in files:
                os.remove(os.path.join(cur, file))

    # Считывание данных из файла
    f = fitsio.read(os.path.join(path_to_data, path_to_file))

    # Определение числа столбцов
    cols_num = len(f[0, :])

    # Определение числа строк
    rows_num = len(f[:, 0])

    # Получения массива из индексов строк
    rows_ind = np.r_[1:rows_num + 1]

    # Проход по вертикальным срезам
    for j in range(cols_num):

        # Проверка на значимость текущего среза
        if np.all(f[:, j] <= isens):
            continue

        # Построение графика среза
        plt.plot(rows_ind, f[:, j])

        # Добавление названий осей
        plt.xlabel("$y$")
        plt.ylabel("$I$")

        # Добавление заголовка
        plt.title("Вертикальный срез " + str(j + 1))

        # Сохранение графика
        plt.savefig(os.path.join(path_to_output_directory, str(j + 1)), bbox_inches="tight")

        # Очистка графика
        plt.clf()
