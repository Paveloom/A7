"""
Модуль, содержащий стартовые функции, позволяющие
задать начальное поколение на досках
"""

import numpy as np  # Тип матрицы


def blinker(board: np.ndarray):
    """
    Функция, создающая на доске осциллятор blinker
    Рекомендуемый размер тестовой доски: 5 x 5
    :param board: Текущая доска
    :return: Доска с осциллятором blinker
    """

    board[2, 1:4] = True


def pulsar(board: np.ndarray):
    """
    Функция, создающая на доске осциллятор pulsar
    Рекомендуемый размер тестовой доски: 17 x 17
    :param board: Текущая доска
    :return: Доска с осциллятором pulsar
    """

    board[1:4, 5] = True
    board[3, 6] = True

    board[1:4, 11] = True
    board[3, 10] = True

    board[5, 1:4] = True
    board[6, 3] = True

    board[5, 13:16] = True
    board[6, 13] = True

    board[5, 6:8] = board[5, 9:11] = True
    board[6, 5] = board[6, 7] = board[6, 9] = board[6, 11] = True
    board[7, 5:7] = board[7, 10:12] = True

    board[9, 5:7] = board[9, 10:12] = True
    board[10, 5] = board[10, 7] = board[10, 9] = board[10, 11] = True
    board[11, 6:8] = board[11, 9:11] = True

    board[10, 3] = True
    board[11, 1:4] = True

    board[10, 13] = True
    board[11, 13:16] = True

    board[13:16, 5] = True
    board[13, 6] = True

    board[13:16, 11] = True
    board[13, 10] = True


def hwss(board: np.ndarray):
    """
    Функция, создающая на доске тяжелый космический корабль
    Рекомендуемый размер тестовой доски: 9 x 33
    :param board: Текущая доска
    :return: Доска с тяжелым космическим кораблем
    """

    board[3, 3:9] = True
    board[4, 2] = board[4, 8] = True
    board[5, 8] = True
    board[6, 2] = board[6, 7] = True
    board[7, 4:6] = True


def glider_gun(board: np.ndarray):
    """
    Функция, создающая на доске планерную пушку
    :param board: Текущая доска
    :return: Доска с планерной пушкой
    """

    board[1, 25] = True
    board[2, 23] = board[2, 25] = True
    board[3, 13:15] = board[3, 21:23] = board[3, 35:37] = True
    board[4, 12] = board[4, 16] = board[4, 21:23] = board[4, 35:37] = True
    board[5, 1:3] = board[5, 11] = board[5, 17] = board[5, 21:23] = True
    board[6, 1:3] = board[6, 11] = board[6, 15] = board[6, 17:19] = board[6, 23] = board[6, 25] = True
    board[7, 11] = board[7, 17] = board[7, 25] = True
    board[8, 12] = board[8, 16] = True
    board[9, 13:15] = True