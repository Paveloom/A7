from T1.rectangle import Rectangle # Задание #1
from T2.show_file_info import show_file_info # Задание #2
from T3.sort_rows import sort_rows # Задание #3
from T4.rfraction import Rfraction # Задание #4
from T5.get_nth_prime import get_nth_prime # Задание #5
from T6.top_5_words import show_top_5_words # Задание #6

# Задание #1
print("\nЗадание #1\n")

## Инициализация объекта
a = Rectangle(14, 5)

## Вывод информации о прямоугольнике
a.info()

## Вычисление и вывод площади прямоугольника
a.area_print()

## Вычисление и вывод периметра прямоугольника
a.per_print()

## Вывод прямоугольника в консоль
a.draw(filled = False)


# Задание #2
print("\n\nЗадание #2\n")

## Вывод информации о файле
show_file_info("./T2/text")


# Задание #3

## Вызов метода для сортировки строк в файле
sort_rows("./T3/in", "./T3/out")

# Задание #4
print("\nЗадание #4\n")

## Инициализация объекта
a = Rfraction(2, 12)
b = Rfraction(2, 5)

## Вывод дробей в консоль
print("Дроби a и b:")
a.show()
b.show()

## Сложение дробей
print("\nСложение дробей:")
c = a + b
c.show()

## Вычитание дробей
print("\nВычитание дробей:")
c = a - b
c.show()

## Умножение дробей
print("\nУмножение дробей:")
c = a * b
c.show()

## Деление дробей
print("\nДеление дробей:")
c = a / b
c.show()

# Задание #5
print("\nЗадание #5\n")

n = 25
print("Просто число под номером", n, ":", get_nth_prime(n))

# Задание #6
print("\nЗадание #6\n")

show_top_5_words("./T6/text")

