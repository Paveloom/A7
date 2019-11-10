"""
Модуль, содержащий функции для проверки
на случаи окончания игры
"""

import numpy as np  # Тип матриц


def the_board_is_empty(matrix: np.ndarray):
    """
    Функция, проверяющая, пуста ли доска
    :param matrix: Текущая доска
    :return: Да / нет
    """

    if matrix.any():
        return False
    else:
        print("Доска пуста.")
        return True


def the_board_repeated(boards_stack: list):
    """
    Функция, проверяющая, повторилась
    ли доска, и определяющая,
    если она повторилась, её период
    :param boards_stack: Текущая стопка досок
    :return: Да / нет
    """

    for i in range(len(boards_stack[:-1]) - 1, -1, -1):
        if np.array_equal(boards_stack[-1], boards_stack[i]):
            print("Обнаружено повторение конфигурации с периодом " + str(len(boards_stack) - i - 1) + ".")
            return True

    else:
        return False
