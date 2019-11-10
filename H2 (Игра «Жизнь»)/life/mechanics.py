""" Модуль, содержащий методы, описывающие игровые механики """

import numpy as np  # Тип матриц
from life import counts as cs  # Функции для подсчета живых соседей


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
            count = cs.count_alive_neighbors_inside(bcur, i, j)

            # Применение правил:
            apply_rules(bcur, bnext, count, i, j)

    # Проход по боковым граням (без углов; 5 соседей)
    for i in range(1, nm1):

        # Проход по левой грани

        # Подсчет числа живых соседей у клеток на левой грани
        count = cs.count_alive_neighbors_left(bcur, i)

        # Применение правил
        apply_rules(bcur, bnext, count, i, 0)

        # Проход по правой грани

        # Подсчет числа живых соседей у клеток на правой грани
        count = cs.count_alive_neighbors_right(bcur, i, mm1)

        # Применение правил
        apply_rules(bcur, bnext, count, i, mm1)

    # Проход по верхней и нижней граням доски (без углов; 5 соседей)
    for j in range(1, mm1):

        # Проход по верхней грани

        # Подсчет числа живых соседей у клеток на верхней грани
        count = cs.count_alive_neighbors_top(bcur, j)

        # Применение правил
        apply_rules(bcur, bnext, count, 0, j)

        # Проход по нижней грани

        # Подсчет числа живых соседей у клеток на нижней грани
        count = cs.count_alive_neighbors_bottom(bcur, j, nm1)

        # Применение правил
        apply_rules(bcur, bnext, count, nm1, j)

    # Проход по углам (3 соседа)

        # Подсчет числа живых соседей в левом верхнем углу
        count = cs.count_alive_neighbors_c1(bcur)

        # Применение правил
        apply_rules(bcur, bnext, count, 0, 0)

        # Подсчет числа живых соседей в правом верхнем углу
        count = cs.count_alive_neighbors_c2(bcur, mm1)

        # Применение правил
        apply_rules(bcur, bnext, count, 0, mm1)

        # Подсчет числа живых соседей в левом нижнем углу
        count = cs.count_alive_neighbors_c3(bcur, nm1)

        # Применение правил
        apply_rules(bcur, bnext, count, nm1, 0)

        # Подсчет числа живых соседей в правом нижнем углу
        count = cs.count_alive_neighbors_c4(bcur, nm1, mm1)

        # Применение правил
        apply_rules(bcur, bnext, count, nm1, mm1)


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
        if count in range(2, 4):
            bnext[i, j] = True
        else:
            bnext[i, j] = False
    # Если клетка мертвая
    else:
        if count == 3:
            bnext[i, j] = True
        else:
            bnext[i, j] = False
