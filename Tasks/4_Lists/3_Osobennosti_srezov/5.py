# ДИСКВАЛИФИКАЦИЯ
# В переменной athletes хранится список спортсменов. Организаторы соревнований решили дисквалифицировать одного из участников.
# Напишите программу, которая принимает из аргументов командной строки индекс спортсмена, удаляет его из списка, а затем выводит оставшийся список.
#
# Пример использования:
# > python program.py 0
# > ['Ильин', 'Петров', 'Зинько', 'Сидоров', 'Васильев', 'Литвинов']

athletes = ['Иванов', 'Ильин', 'Петров', 'Зинько', 'Сидоров', 'Васильев', 'Литвинов']

import sys
index = int(sys.argv[1])
del athletes[index]
#либо athletes[index:index] = []
print(athletes)





