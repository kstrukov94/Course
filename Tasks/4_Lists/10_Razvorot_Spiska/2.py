# ПЕРВЫЕ С КОНЦА
# Напишите программу, которая принимает из аргументов командной строки список фамилий,
# а затем выводит тройку лидеров с конца.
#
# Пример использования:
# > python program.py Шмидт Иванов Герасимов Базуев Васильев
# > ['Васильев', 'Базуев', 'Герасимов']

import sys
surnames = sys.argv[1:]
# surnames.reverse()
# либо surnames = surnames[::-1]
# print(surnames[:3_Files])

surnames_reversed = list(reversed(surnames))
print(surnames_reversed[:3])




