""" Модуль, содержащий класс Board """

import numpy as np
import mechanics as ms


class Board(object):
    """
    Класс, определяющий две доски, поочередно представляющие
    собой текущее и предыдущее поколения (две — в целях экономии
    на операциях выделения памяти)

    Элементы класса:

    n и m — числа строк и столбцов досок;
    b1 и b2 — доски, поочередно представляющие
    собой текущее и предыдущее поколения;
    switch — логическая переменная, указывающая,
    является ли первая доска текущей
    """

    def __init__(self, n: int, m: int = 0, starter=None):
        """
        Конструктор
        :param n: Число строк досок
        :param m: Число столбцов досок
        :param starter: Стартовая функция
        """

        # Запись числа строк
        self.n = n

        if m:
            # Запись числа столбцов
            self.m = m

            # Создание досок
            self.b1 = np.ascontiguousarray(np.zeros(shape=(n, m), dtype=bool))
            self.b2 = np.ascontiguousarray(np.zeros(shape=(n, m), dtype=bool))

            # Если указана, вызов стартовой функции
            if starter:
                starter(self.b1)
                starter(self.b2)
        else:
            # Запись числа столбцов
            self.m = n

            # Создание досок
            self.b1 = np.ascontiguousarray(np.zeros(shape=(n, n), dtype=bool))
            self.b2 = np.ascontiguousarray(np.zeros(shape=(n, n), dtype=bool))

            # Если указана, вызов стартовой функции
            if starter:
                starter(self.b1)
                starter(self.b2)

        # Присваивание стандартного значения
        # логической переменной
        self.switch = False

    def evolve(self, iters: int = 1):
        """
         Метод, получающий следующие поколения в смежных досках
        :param iters: Число итераций
        """

        # Вычисление вспомогательных переменных
        nm1 = self.n - 1
        mm1 = self.m - 1

        for _ in range(iters):

            # Текущая доска — b2
            if self.switch:

                # Выполнение перехода от одного поколения к следующему
                ms.evolution_step(self.b2, self.b1, nm1, mm1)

                # Переключение текущей доски
                self.switch = not self.switch

            # Текущая доска — b1
            else:

                # Выполнение перехода от одного поколения к следующему
                ms.evolution_step(self.b1, self.b2, nm1, mm1)

                # Переключение текущей доски
                self.switch = not self.switch

    def print(self):
        """ Метод для вывода текущей доски """

        if self.switch:
            print(self.b2)

        else:
            print(self.b1)

        print()
