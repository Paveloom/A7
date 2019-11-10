"""
Модуль, содержащий функции для подсчета
числа живых соседей у клеток на доске
"""

import numpy as np  # Тип матриц


def count_alive_neighbors_inside(matrix: np.ndarray, i: int, j: int):
    """
    Функция, возвращающая число живых соседей текущей клетки,
    расположенной во внутреннем прямоугольнике доски
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
    расположенной на левой грани доски
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
    расположенной на правой грани доски
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


def count_alive_neighbors_top(matrix: np.ndarray, j: int):
    """
    Функция, возвращающая число живых соседей текущей клетки,
    расположенной на верхней грани доски
    :param matrix: Текущая доска
    :param j: Индекс столбца текущей клетки
    :return: Число живых соседей
    """

    count = 0

    # Проход по соседям снизу
    for k in range(3):
        if matrix[1, j - 1 + k]:
            count += 1

    # Проход по соседям сбоку

    if matrix[0, j - 1]:
        count += 1

    if matrix[0, j + 1]:
        count += 1

    return count


def count_alive_neighbors_bottom(matrix: np.ndarray, j: int, nm1: int):
    """
    Функция, возвращающая число живых соседей текущей клетки,
    расположенной на верхней грани доски
    :param matrix: Текущая доска
    :param j: Индекс столбца текущей клетки
    :param nm1: Число строк доски - 1
    :return: Число живых соседей
    """

    count = 0

    # Проход по соседям сверху
    for k in range(3):
        if matrix[nm1 - 1, j - 1 + k]:
            count += 1

    # Проход по соседям сбоку

    if matrix[nm1, j - 1]:
        count += 1

    if matrix[nm1, j + 1]:
        count += 1

    return count


def count_alive_neighbors_c1(bcur: np.ndarray):
    """
    Функция, возвращающая число живых соседей текущей клетки,
    расположенной в верхнем левом углу доски
    :param bcur: Текущая доска
    :return: Число живых соседей
    """

    count = 0

    # Проход по соседям

    if bcur[0, 1]:
        count += 1

    if bcur[1, 0]:
        count += 1

    if bcur[1, 1]:
        count += 1

    return count


def count_alive_neighbors_c2(bcur: np.ndarray, mm1: int):
    """
    Функция, возвращающая число живых соседей текущей клетки,
    расположенной в верхнем правом углу доски
    :param bcur: Текущая доска
    :param mm1: Число столбцов доски - 1
    :return: Число живых соседей
    """

    count = 0

    # Проход по соседям

    if bcur[0, mm1 - 1]:
        count += 1

    if bcur[1, mm1]:
        count += 1

    if bcur[1, mm1 - 1]:
        count += 1

    return count


def count_alive_neighbors_c3(bcur: np.ndarray, nm1: int):
    """
    Функция, возвращающая число живых соседей текущей клетки,
    расположенной в нижнем левом углу доски
    :param bcur: Текущая доска
    :param nm1: Число строк доски - 1
    :return: Число живых соседей
    """

    count = 0

    # Проход по соседям

    if bcur[nm1 - 1, 0]:
        count += 1

    if bcur[nm1, 1]:
        count += 1

    if bcur[nm1 - 1, 1]:
        count += 1

    return count


def count_alive_neighbors_c4(bcur: np.ndarray, nm1: int, mm1: int):
    """
    Функция, возвращающая число живых соседей текущей клетки,
    расположенной в нижнем левом углу доски
    :param bcur: Текущая доска
    :param nm1: Число строк доски - 1
    :param mm1: Число столбцов доски - 1
    :return: Число живых соседей
    """

    count = 0

    # Проход по соседям

    if bcur[nm1, mm1 - 1]:
        count += 1

    if bcur[nm1 - 1, mm1]:
        count += 1

    if bcur[nm1 - 1, mm1 - 1]:
        count += 1

    return count
