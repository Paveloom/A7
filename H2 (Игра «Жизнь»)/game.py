""" Модуль, описывающий игровые механики игры «Жизнь» """

import numpy as np


class Board(object):
    """
    Класс, определяющий две доски, поочередно представляющие
    собой текущее и предыдущее поколения (две — в целях экономии
    на операциях выделения памяти)

    Элементы класса:

    b1 и b2 — доски, поочередно представляющие
    собой текущее и предыдущее поколения;
    c1 — логическая переменная, указывающая,
    является ли первая доска текущей

    """

    def __init__(self, n: int, m: int = 0, starter=None):
        """
        Конструктор
        :param n: Число строк досок
        :param m: Число столбцов досок
        :param starter: Стартовая функция
        """

        if m:
            self.b1 = np.ascontiguousarray(np.zeros(shape=(n, m), dtype=bool))
            if starter:
                starter(self.b1)
        else:
            self.b1 = np.ascontiguousarray(np.zeros(shape=(n, n), dtype=bool))
            if starter:
                starter(self.b1)

        self.b2 = self.b1
        self.switch = False

    def evolve(self, iters: int):
        """
         Метод, получающий следующие поколения в смежных досках
        :param iters: Число итераций
        """
