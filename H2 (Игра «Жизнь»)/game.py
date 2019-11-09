""" Модуль, описывающий игровые механики игры «Жизнь» """

import numpy as np


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

        for _ in range(iters):

            if not self.switch:

                # Проход по внутреннему прямоугольнику (8 соседей)
                for i in range(1, self.n - 1):
                    for j in range(1, self.m - 1):

                        # Подсчет числа живых соседей
                        count = __count_alive_neighbors__(self.b1, 8, i, j)

                        # Выполнение правил:
                        __apply_rules__(self.b1, self.b2, count, i, j)




def __count_alive_neighbors__(matrix: np.ndarray, num: int, i: int, j: int):
    """
    Функция, возвращающая число живых соседей текущей клетки
    :param num: Число соседей для проверки
    :param i: Индекс строки текущей клетки
    :param j: Индекс столбца текущей клетки
    :return: Число живых соседей
    """

    if num == 8:  # 8 соседей

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


def __apply_rules__(bcur: np.ndarray, bnext: np.ndarray, count: int, i: int, j: int):
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