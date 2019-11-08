def show_file_info(file_name):
    '''
    Метод для получения следующей информации о файле:
    число строк, число слов, число символов
    :param file_name: Имя файла
    '''
    with open(file_name, mode = 'r') as f:

        # Считывание данных из файла
        data = f.read()

        # Вывод информации о файле
        print("Число строк в файле", file_name, ":", len(data.splitlines()))
        print("Число слов в файле", file_name, ":", len(data.split()))
        print("Число символов в файле", file_name, ":", len(data))