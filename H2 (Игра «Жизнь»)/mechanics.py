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

            # Подсчет числа живых соседей у клеток во
            # внутреннем прямоугольнике
            count = count_alive_neighbors_inside(bcur, i, j)

            # Применение правил:
            apply_rules(bcur, bnext, count, i, j)

    # Проход по боковым граням (без углов; 5 соседей)
    for i in range(1, nm1):

        # Проход по левой грани

        # Подсчет числа живых соседей у клеток на левой грани
        count = count_alive_neighbors_left(bcur, i)

        # Применение правил
        apply_rules(bcur, bnext, count, i, 0)

        # Проход по правой грани

        # Подсчет числа живых соседей у клеток на правой грани
        count = count_alive_neighbors_right(bcur, i, mm1)

        # Применение правил
        apply_rules(bcur, bnext, count, i, mm1)

    # Проход по верхней и нижней граням доски (без углов; 5 соседей)
    for j in range(1, mm1):

        # Проход по верхней грани

        # Подсчет числа живых соседей у клеток на верхней грани
        count = count_alive_neighbors_top(bcur, j)

        # Применение правил
        apply_rules(bcur, bnext, count, 0, j)

        # Проход по нижней грани

        # Подсчет числа живых соседей у клеток на нижней грани
        count = count_alive_neighbors_bottom(bcur, j, nm1)

        # Применение правил
        apply_rules(bcur, bnext, count, nm1, j)

    # Проход по углам (3 соседа)

        # Подсчет числа живых соседей в левом верхнем углу
        count = count_alive_neighbors_c1(bcur)

        # Применение правил
        apply_rules(bcur, bnext, count, 0, 0)

        # Подсчет числа живых соседей в правом верхнем углу
        count = count_alive_neighbors_c2(bcur, mm1)

        # Применение правил
        apply_rules(bcur, bnext, count, 0, mm1)

        # Подсчет числа живых соседей в левом нижнем углу
        count = count_alive_neighbors_c3(bcur, nm1)

        # Применение правил
        apply_rules(bcur, bnext, count, nm1, 0)

        # Подсчет числа живых соседей в правом нижнем углу
        count = count_alive_neighbors_c4(bcur, nm1, mm1)

        # Применение правил
        apply_rules(bcur, bnext, count, nm1, mm1)


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
