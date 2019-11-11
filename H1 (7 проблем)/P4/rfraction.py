""" Модуль, содержащий класс рациональных дробей """

import sys  # Системно-зависимые параметры и функции


class Rfraction(object):
    """
    Класс, описывающий рациональные дроби
    """

    def __init__(self, a, b):
        """
        Конструктор
        :param a: Числитель
        :param b: Знаменатель
        """

        self.a = a
        self.b = b

        if self.b == 0:
            sys.exit("Делитель не может быть равен нулю")
        else:
            self.__simplify__()

    def __simplify__(self):
        """
        Метод сокращения дробей
        :return: Сокращенная дробь
        """

        # Реализация алгоритма Евклида для поиска НОД
        if self.a != 0:

            a_abs = abs(self.a)
            b_abs = abs(self.b)

            if a_abs == b_abs:  # Если числитель и знаменатель равны

                self.a = 1
                self.b = 1

            elif a_abs > b_abs:  # Если числитель больше знаменателя

                while True:

                    r = a_abs % b_abs

                    if r == 0:

                        self.a = self.a // b_abs
                        self.b = self.b // b_abs
                        break

                    else:

                        a_abs = b_abs
                        b_abs = r

            else: # Если числитель меньше знаменателя

                while True:

                    r = b_abs % a_abs

                    if r == 0:

                        self.a = self.a // a_abs
                        self.b = self.b // a_abs
                        break

                    else:

                        b_abs = a_abs
                        a_abs = r

    def show(self):
        """
        Метод для вывода рационального числа в консоль
        """

        if self.a == 0: # Если числитель равен 0

            print(self.a)

        elif self.a == 1 and self.b == 1:  # Если дробь равна единице

            print(self.a)

        else:

            print(self.a, "/", self.b)

    def __add__(self, other):
        """
        Переопределения операции сложения для рациональных дробей
        :return: Рациональная дробь (сумма аргументов)
        """

        if self.b == other.b: # Если знаменатели дробей равны

            new_a = self.a + other.a
            new_b = self.b

        elif self.b % other.b == 0:  # Если знаменатель первой дроби делится
                                     # на знаменатель второй дроби без остатка

            tmp = self.b // other.b
            new_b = self.b
            new_a = self.a + other.a * tmp

        elif other.b % self.b == 0:  # Если знаменатель второй дроби делится
                                     # на знаменатель первой дроби без остатка

            tmp = other.b // self.b
            new_b = other.b
            new_a = self.a * tmp + other.a

        else:

            new_b = self.b * other.b
            tmp_1 = new_b // self.b
            tmp_2 = new_b // other.b
            new_a = self.a * tmp_1 + other.a * tmp_2

        res = Rfraction(new_a, new_b) # Создание объекта
        res.__simplify__() # Упрощение дроби

        return res # Возвращение результата

    def __sub__(self, other):
        """
        Переопределения операции вычитания для рациональных дробей
        :return: Рациональная дробь (разность аргументов)
        """

        # Взятие дроби other с отрицательным числителем
        mother = Rfraction(-other.a, other.b)

        # Сложение дробей
        return self + mother

    def __mul__(self, other):
        """
        Переопределения операции умножения для рациональных дробей
        :return: Рациональная дробь (произведение аргументов)
        """

        new_a = self.a * other.a
        new_b = self.b * other.b

        res = Rfraction(new_a, new_b) # Создание объекта
        res.__simplify__() # Упрощение дроби

        return res # Возвращение результата

    def __truediv__(self, other):
        """
        Переопределения операции деления для рациональных дробей
        :return:
        """

        # Взятие перевернутой дроби other
        rother = Rfraction(other.b, other.a)

        # Перемножение дробей
        return self * rother
