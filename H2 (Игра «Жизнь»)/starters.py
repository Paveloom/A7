"""
Модуль, содержащий стартовые функции, позволяющие
задать начальное поколение на досках
"""

import numpy as np


def blinker(board: np.ndarray):
    """ Метод, создающий на доске осциллятор blinker """
    board[2, 1:4] = True
    return board
