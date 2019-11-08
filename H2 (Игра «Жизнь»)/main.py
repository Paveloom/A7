""" Скрипт, демонстрирующий реализацию игры «Жизнь» """

from game import Board  # Класс доски
import starters as st  # Стартовые функции


# Создание доски
board = Board(5, 5, starter=st.blinker)
