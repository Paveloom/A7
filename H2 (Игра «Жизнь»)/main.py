""" Скрипт, демонстрирующий реализацию игры «Жизнь» """

from board import Board  # Класс доски
import starters as st  # Стартовые функции


# Создание доски
board = Board(5, 5, starter=st.blinker)

board.print()

board.evolve(300)

board.print()
