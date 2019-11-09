""" Модуль, содержащий методы, описывающие игровые механики """

import numpy as np


def evolution_step(bcur: np.ndarray, bnext: np.ndarray, nm1: int, mm1: int):
    """
    Метод, реализующие переход от одного
    поколения к следующему
    :param bcur: Текущая доска
    :param bnext: Следующая доска
    :param nm1: Число строк досок - 1
    :param mm1: Число столбцов досок - 1
    """

    # Проход по внутреннему прямоугольнику (8 соседей)
    for i in range(1, nm1):
        for j in range(1, mm1):

            # Подсчет числа живых соседей
            count = count_alive_neighbors_inside(bcur, i, j)

            # Выполнение правил:
            apply_rules(bcur, bnext, count, i, j)

    # Проход по левой грани (без углов; 5 соседей)
    for i in range(1, nm1):

        # Подсчет числа живых соседей на левой грани
        count = count_alive_neighbors_left(bcur, i)

        # Выполнение правил
        apply_rules(bcur, bnext, count, i, 0)

    # Проход по правой грани (без углов; 5 соседей)
    for i in range(1, nm1):

        # Подсчет числа живых соседей на правой грани
        count = count_alive_neighbors_right(bcur, i, mm1)

        # Выполнение правил
        apply_rules(bcur, bnext, count, i, mm1)


def count_alive_neighbors_inside(matrix: np.ndarray, i: int, j: int):
    """
    Функция, возвращающая число живых соседей текущей клетки,
    расположенной во внутреннем прямоугольнике
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


def count_alive_neighbors_left(matrix: np.ndarray, i: int):
    """
    Функция, возвращающая число живых соседей текущей клетки,
    расположенной на левой грани
    :param matrix: Текущая доска
    :param i: Индекс строки текущей клетки
    :return: Число живых соседей
    """

    count = 0

    # Проход по соседям сбоку
    for k in range(3):
        if matrix[i - 1 + k, 1]:
            count += 1

    # Проход по соседям сверху и снизу

    if matrix[i - 1, 0]:
        count += 1

    if matrix[i + 1, 0]:
        count += 1

    return count


def count_alive_neighbors_right(matrix: np.ndarray, i: int, mm1: int):
    """
    Функция, возвращающая число живых соседей текущей клетки,
    расположенной на правой грани
    :param matrix: Текущая доска
    :param i: Индекс строки текущей клетки
    :param mm1: Число столбцов доски - 1
    :return: Число живых соседей
    """

    count = 0

    # Проход по соседям сбоку
    for k in range(3):
        if matrix[i - 1 + k, mm1 - 1]:
            count += 1

    # Проход по соседям сверху и снизу

    if matrix[i - 1, mm1]:
        count += 1

    if matrix[i + 1, mm1]:
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
