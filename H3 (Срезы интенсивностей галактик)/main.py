"""
Скрипт, строящий графики вертикальных
срезов по изображениям галактик
"""

from gslices import clear as cl  # Удаления содержимого указанной папки
from gslices import slices as sl  # Вертикальные срезы
from gslices import dgaussian as dg  # Двойная функция Гаусса

# Удаления содержимого указанной папки
cl.clear_dir("output")

# Получение результатов для data/20
sl.slice_data("data/20", "output/20")

# Получение результатов для data/130
sl.slice_data("data/130", "output/130",
              fit_function=dg.double_gaussian, supportive_fit_function=dg.s_double_gaussian,
              priors_function=dg.p_double_gaussian)

# Получение результатов для data/149
sl.slice_data("data/149", "output/149", isens=400)

# Получение результатов для data/216
sl.slice_data("data/216", "output/216", isens=1100)

# Получение результатов для data/236
sl.slice_data("data/236", "output/236")

# Получение результатов для data/274
sl.slice_data("data/274", "output/274",
              fit_function=dg.double_gaussian, supportive_fit_function=dg.s_double_gaussian,
              priors_function=dg.p_double_gaussian)

# Получение результатов для data/283
sl.slice_data("data/283", "output/283")

# Получение результатов для data/305
sl.slice_data("data/305", "output/305")

# Получение результатов для data/305
sl.slice_data("data/305", "output/305")

# Получение результатов для data/325
sl.slice_data("data/325", "output/325")
