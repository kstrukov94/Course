# ПОСЛЕДНЯЯ ТРОЙКА
# Напишите программу, которая принимает из аргументов командной строки список спортсменов, а затем выводит последнюю тройку.
#
# Пример использования:
# > python program.py Ильин Петров Зинько Сидоров Васильев Литвинов
# > ['Сидоров', 'Васильев', 'Литвинов']

import sys
list = sys.argv[1:]
print(list[-3:])