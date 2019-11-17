"""
Модуль, содержащий главные методы для
построения вертикальных срезов
по изображениям галактик
"""

import os  # Работа с путями
import fitsio  # Считывание .fits файлов
import numpy as np  # Работа с массивами

from inspect import signature  # Получения числа аргументов функции
from matplotlib import pyplot as plt, rcParams as rcP  # Графики
from scipy import optimize as so  # Вписывание кривой

# Значение по умолчанию для isens
isens_default = 1.5e3

# Настройки графиков

rcP["savefig.dpi"] = 300
rcP["figure.dpi"] = 300

rcP["font.size"] = 13
rcP["legend.fontsize"] = 10
rcP["font.family"] = "sans"
rcP["font.sans-serif"] = ["DejaVu Sans"]


# Определение функции для вписывания по умолчанию
def fit_function_default(x, a, b, c):
    """
    Функция для вписывания по умолчанию
    (функция Гаусса)

    Параметры:
        a, b, c: Параметры функции Гаусса.
    """

    # Получение результата функции
    return a * np.exp(- (x - b) ** 2 / (2 * c ** 2))


def supportive_fit_function_default(x: np.ndarray, params: np.ndarray):
    """
    Вспомогательная функция для вписывания
    по умолчанию (функция Гаусса)

    Параметры:
        params: Параметры функции Гаусса.
    """

    # Создание массива
    result = np.zeros(len(x))

    # Получение результата функции
    for i in range(len(x)):
        result[i] = params[0] * np.exp(- (x[i] - params[1]) ** 2 / (2 * params[2] ** 2))

    # Возвращение результата
    return result


#  Значение по умолчанию для списка начальных параметров
def get_priors_default(x: np.ndarray, y: np.ndarray):
    """
    Функция по умолчанию для получения начальных значений

    Параметры:
        x: Массив аргументов;
        y: Массив значений функции.
    """

    return [y.max(), len(x) / 2, len(x) / 4]


def slice_data(path_to_data: str, path_to_output: str, isens: float = isens_default, clean: bool = False,
               fit_function=fit_function_default, supportive_fit_function=supportive_fit_function_default,
               priors_function=get_priors_default):
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
               предыдущих результатов для найденных файлов;
        fit_function: Функция, описывающая кривую,
                      которая будет вписана.
        supportive_fit_function: Вспомогательная функция,
                                 описывающая кривую,
                                 которая будет вписана;
        priors_function: Функция для получения начальных
                         значений для заданной функции.
    """

    # Рекурсивный проход по всем данным в path_to_data
    for cur, folders, files in os.walk(path_to_data):
        for file in files:

            # Если найден .fits файл:
            if file.lower().endswith(".fits"):

                # Вызов функции для работы с этим файлом
                slice_file(path_to_data, os.path.join(cur, file)[len(path_to_data) + 1:], path_to_output, isens, clean,
                           fit_function, supportive_fit_function, priors_function)


def slice_file(path_to_data: str, path_to_file: str, path_to_output: str, isens: float = isens_default,
               clean: bool = False, fit_function=fit_function_default,
               supportive_fit_function=supportive_fit_function_default, priors_function=get_priors_default):
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
               предыдущих результатов для текущего файла;
        fit_function: Функция, описывающая кривую,
                      которая будет вписана;
        supportive_fit_function: Вспомогательная функция,
                                 описывающая кривую,
                                 которая будет вписана;
        priors_function: Функция для получения начальных
                         значений для заданной функции.
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
    rows_inds = np.r_[1:rows_num + 1]

    # Определение списка индексов значимых срезов
    imp_inds = []

    # Проход по вертикальным срезам (определение значимых срезов)
    for j in range(cols_num):

        # Проверка на значимость текущего среза
        if np.all(f[:, j] <= isens):
            continue

        # Дополнение текущего индекса вертикального
        # среза к списку индексов значимых срезов
        imp_inds.append(j)

    # Получение параметров в виде листа строк
    params_str = str(signature(fit_function)).replace("(", "").replace(")", "").replace(",", "").split()[1:]

    # Получение числа зависимых параметров функции fit_function
    params_num = len(params_str)

    # Определение длины списка индексов значимых срезов
    imp_inds_len = len(imp_inds)

    # Создание массива параметров
    params = np.zeros((imp_inds_len, params_num))

    # Обнуление вспомогательной переменной
    k = 0

    # Проход по значимым вертикальным срезам
    # (построение графиков срезов и вписывание функции)
    for j in imp_inds:

        # Вписывание функции
        fit_params = so.curve_fit(fit_function, rows_inds, f[:, j], p0=priors_function(rows_inds, f[:, j]))

        # Добавление полученных параметров к общему массиву
        params[k, :] = fit_params[0]

        # Увеличение вспомогательной переменной на единицу
        k += 1

        # Построение графика среза
        plt.plot(rows_inds, f[:, j], label="Данные")

        # Построение графика вписанной функции
        plt.plot(rows_inds, supportive_fit_function(rows_inds, fit_params[0]), label="Вписанная функция")

        # Добавление легенды
        plt.legend(loc="upper right")

        # Добавление названий осей
        plt.xlabel("$y$")
        plt.ylabel("$I$")

        # Добавление заголовка
        plt.title("Вертикальный срез " + str(j + 1))

        # Сохранение графика
        plt.savefig(os.path.join(path_to_output_directory, str(j + 1)), bbox_inches="tight")

        # Очистка графика
        plt.close()

    # Построение полотна для подграфиков
    fig, axes = plt.subplots(params_num, sharex="col")

    # Построение графиков параметров по всем срезам
    for m in range(params_num):
        axes[m].plot(range(1, imp_inds_len + 1), params[:, m], color="orange", label="Параметр " + params_str[m])
        axes[m].legend()

    # Получение индексов значимых
    # срезов в виде списка строк

    imp_inds_str = []
    for k in range(imp_inds_len):
        imp_inds_str.append(str(imp_inds[k] + 1))

    # Изменение меток для значений абсциссы

    if imp_inds_len < 10:
        axes[-1].set_xticks(np.arange(1, imp_inds_len + 1, 1))
        axes[-1].set_xticklabels(imp_inds_str)
    elif 10 <= imp_inds_len < 22:
        axes[-1].set_xticks(np.arange(1, imp_inds_len + 1, 2))
        axes[-1].set_xticklabels(imp_inds_str[::2])
    else:
        axes[-1].set_xticks(np.arange(1, imp_inds_len + 1, 4))
        axes[-1].set_xticklabels(imp_inds_str[::4])

    # Добавление заголовка
    axes[0].set_title("Мастер-график по всем срезам")

    # Добавление названия абсциссы
    axes[-1].set_xlabel("Номер вертикального среза")

    # Сохранение графика
    fig.savefig(os.path.join(path_to_output_directory, "master"), bbox_inches="tight")

    # Освобождение памяти из-под фигуры
    plt.close(fig)
