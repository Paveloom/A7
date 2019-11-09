""" Скрипт, демонстрирующий реализацию игры «Жизнь» """

from board import Board  # Класс доски
import starters as st  # Стартовые функции


# Создание доски
board = Board(17, starter=st.pulsar)

# Вызов эволюции
board.evolve(120, 0.1)