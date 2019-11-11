""" Модуль, содержащий метод для сортировки строк """


def sort_rows(if_name, of_name):
    """
    Метод для сортировки строк из файла if_name и
    вывода результата в файл of_name
    :param if_name: Имя входного файла
    :param of_name: Имя выходного файла
    """

    with open(if_name) as iff:
        # Считывание данных из файла iff
        data = iff.readlines()

    # Добавление управляющего символа новой
    # строки к последнему элементу списка
    data[-1] += "\n"

    # Сортировка строк
    data = sorted(data, key=str.lower)

    # Удаление управляющего символа новой
    # строки у последнего элемента списка
    data[-1] = data[-1][:-1]

    # Вывод данных в файл of
    with open(of_name, mode='w') as off:
        for line in data:
            off.write(line)
