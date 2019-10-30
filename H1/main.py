from P1.rectangle import Rectangle # Проблема #1
from P2.show_file_info import show_file_info # Проблема #2
from P3.sort_rows import sort_rows # Проблема #3
from P4.rfraction import Rfraction # Проблема #4
from P5.get_nth_prime import get_nth_prime # Проблема #5
from P6.top_5_words import show_top_5_words # Проблема #6
from P7.pi_est import est_pi # Проблема 7

# Проблема #1
print("\nПроблема #1\n")

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


# Проблема #2
print("\n\nПроблема #2\n")

## Вывод информации о файле
show_file_info("./P2/text")


# Проблема #3

## Вызов метода для сортировки строк в файле
sort_rows("./P3/in", "./P3/out")

# Проблема #4
print("\nПроблема #4\n")

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

# Проблема #5
print("\nПроблема #5\n")

n = 25
print("Просто число под номером", n, ":", get_nth_prime(n))

# Проблема #6
print("\nПроблема #6\n")

show_top_5_words("./P6/text")

# Проблема #7
print("\nПроблема #7\n")

N = 60000
dN = 10000

print("     N | pi     ")
for i in range(1, N, dN):
    print('%6d   %e' % (i, est_pi(i)))