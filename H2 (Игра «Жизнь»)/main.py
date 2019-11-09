""" Скрипт, демонстрирующий реализацию игры «Жизнь» """

from board import Board  # Класс доски
import starters as st  # Стартовые функции


# Создание доски
board = Board(9, 33, starter=st.hwss)

# Вызов эволюции
board.evolve(60, 0.2)
