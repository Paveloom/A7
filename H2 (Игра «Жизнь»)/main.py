""" Скрипт, демонстрирующий реализацию игры «Жизнь» """

from board import Board  # Класс доски
import starters as st  # Стартовые функции

# Создание доски
board = Board(22, 38, starter=st.glider_gun)

# Вызов эволюции
board.evolve(sleep_time=0.05)
