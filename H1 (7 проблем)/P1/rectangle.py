""" Модуль, содержащий класс Rectangle """


class Rectangle(object):
    """
    Класс, определяющий прямоугольник
    """

    def __init__(self, w, h):
        """ 
        Конструктор
        :param w: (weight) — ширина;
        :param h: (height) — высота
        """
        self.w = w
        self.h = h

    def info(self):
        """
        Метод для вывода информации о прямоугольнике
        """
        print("Ширина прямоугольника:", self.w)
        print("Высота прямоугольника:", self.h)

    def area(self):
        """
        Функция для вычисления площади прямоугольника
        :return: Площадь прямоугольника
        """
        return self.w * self.h

    def area_print(self):
        """
        Процедура для вычисления и вывода на экран площади прямоугольника
        """
        print("Площадь прямоугольника:", self.area())

    def perimeter(self):
        """
        Функция для вычисления периметра прямоугольника
        :return: Периметр прямоугольника
        """
        return self.w * 2 + self.h * 2

    def per_print(self):
        """
        Метод для вычисления и вывода на экран периметра прямоугольника
        """
        print("Периметр прямоугольника:", self.perimeter())

    def draw(self, filled):
        """
        Метод для вывода прямоугольника в консоль (символами решетки)
        :param filled: закрашивать прямоугольник?
        """

        print("\nИзображение прямоугольника:\n")

        if filled:
            for i in range(self.h):
                for j in range(self.w):
                    print("#", end='')
                print()
        else:
            for i in range(self.h):
                if i == 0 or i == self.h - 1:
                    for j in range(self.w):
                        print("#", end='')
                    print()
                else:
                    print("#", end='')
                    for j in range(self.w - 2):
                        print(" ", end='')
                    print("#")
