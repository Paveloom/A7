"""
Модуль, содержащий стартовые функции, позволяющие
задать начальное поколение на досках
"""

import numpy as np


def blinker(board: np.ndarray):
    """ Функция, создающая на доске осциллятор blinker """

    board[2, 1:4] = True
    return board


def pulsar(board: np.ndarray):
    """ Функция, создающая на доске осциллятор pulsar """

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