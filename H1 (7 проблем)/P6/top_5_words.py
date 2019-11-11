""" Модуль, содержащий метод для вывода на экран пяти наиболее часто встречаемых слов """


def show_top_5_words(filename):
    """
    Метод для вывода на экран пяти
    наиболее часто встречаемых слов
    в файле filename
    :param filename: Имя файла для считывания
    """

    ls = []

    with open(filename) as f:

        # Считывание данных из файла (строками)
        data = f.readlines()

        # Заполнение листа
        for line in data:
            words = line.split()

            # Одновременно: удаление специальных символов
            for word in words:
                ls.append(''.join(filter(str.isalnum, word.lower())))

        # Начальные значения
        top_words = ["", "", "", "", ""]
        counts = [0, 0, 0, 0, 0]

        # Проверка каждого слова
        for item in ls:

            # Вычисление числа совпадений в списке
            count = ls.count(item)

            # Проверка на максимум по списку counts
            for i in range(4):

                # Проверка на максимум i-ой компоненты списка counts
                if count > counts[i]:

                    # Сдвиг среза (i:4) списка counts вправо
                    for j in range(3 - i + 1):
                        counts[4 - j] = counts[3 - j]

                    # Присвоение значения нового максимума
                    counts[i] = count

                    # Сдвиг среза (i:4) списка top_words вправо
                    for j in range(3 - i + 1):
                        top_words[4 - j] = top_words[3 - j]

                    # Запись нового слова
                    top_words[i] = item

                    break

            # Удаление всех совпадений со словом item в списке
            ls = list(filter(lambda a: a != item, ls))

        # Вывод результата
        print("Пять наиболее часто встречаемых слов в файле", filename)
        print("и соответствующие количества найденных слов:\n")
        print(top_words)
        print(counts)
