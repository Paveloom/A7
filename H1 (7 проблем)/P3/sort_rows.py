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

    # Сортировка строк
    data = sorted(data, key=str.lower)

    # Вывод данных в файл of
    with open(of_name, mode='w') as off:
        for line in data:
            off.write(line)
