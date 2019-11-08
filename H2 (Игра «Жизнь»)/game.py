""" Модуль, описывающий игровые механики игры «Жизнь» """

import numpy as np


def create_board(n, m=0):
    """
    Функция, возвращающая доску n x m
    :param n:
        Число строк доски
    :param m:
        Число столбцов доски
    :return:
    """

    # Создание квадратной матрицы
    if not m:
        return np.ascontiguousarray(np.zeros(shape=(n, n), dtype=bool))
    else:
        return np.ascontiguousarray(np.zeros(shape=(n, m), dtype=bool))
