""" Модуль, содержащий методы, описывающие игровые механики """

import numpy as np


def evolution_step(bcur: np.ndarray, bnext: np.ndarray, n: int, m: int):
    """
    Метод, реализующие переход от одного
    поколения к следующему
    :param bcur: Текущая доска
    :param bnext: Следующая доска
    :param n: Число строк досок
    :param m: Число столбцов досок
    """

    # Проход по внутреннему прямоугольнику (8 соседей)
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            
            # Подсчет числа живых соседей
            count = count_alive_neighbors_8(bcur, i, j)

            # Выполнение правил:
            apply_rules(bcur, bnext, count, i, j)


def count_alive_neighbors_8(matrix: np.ndarray, i: int, j: int):
    """
    Функция, возвращающая число живых соседей текущей клетки
    :param matrix: Текущая доска
    :param i: Индекс строки текущей клетки
    :param j: Индекс столбца текущей клетки
    :return: Число живых соседей
    """

    count = 0

    for k in range(3):

        # Проход по соседям сверху
        if matrix[i - 1, j - 1 + k]:
            count += 1

        # Проход по соседям снизу
        if matrix[i + 1, j - 1 + k]:
            count += 1

    # Проход по соседям сбоку

    if matrix[i, j - 1]:
        count += 1

    if matrix[i, j + 1]:
        count += 1

    return count


def apply_rules(bcur: np.ndarray, bnext: np.ndarray, count: int, i: int, j: int):
    """
    Метод, реализующий правила перехода
    между поколениями для клеток
    :param bcur: Текущая доска
    :param bnext: Следующая доска
    :param count: Число живых соседей
    :param i: Индекс строки текущей клетки
    :param j: Индекс столбца текущей клетки
    """

    # Если клетка живая
    if bcur[i, j]:
        if count not in range(2, 4):
            bnext[i, j] = False
    # Если клетка мертвая
    else:
        if count == 3:
            bnext[i, j] = True
