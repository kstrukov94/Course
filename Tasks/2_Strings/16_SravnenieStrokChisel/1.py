# Начинающий разработчик написал программу, которая выводит максимальное из трех чисел,
# однако код работает не так как было задумано. Исправьте ошибку, чтобы программа работала правильно.
#
# Пример использования в командной строке Windows:
# > python program.py 9 11 7
# > 11

import sys

d1 = int(sys.argv[1])
d2 = int(sys.argv[2])
d3 = int(sys.argv[3])

print(max([d1, d2, d3]))
