# НОВАЯ ТРОЙКА ПОБЕДИТЕЛЕЙ
# Напишите программу, которая принимает из аргументов командной строки список из трех спортсменов,
# а затем заменяет первую тройку в списке athletes новыми значениями.
#
# Пример использования:
# > python program.py Зидан Анри Пети
# > ['Зидан', 'Анри', 'Пети', 'Зинько', 'Сидоров', 'Васильев', 'Литвинов']

athletes = ['Иванов', 'Ильин', 'Петров', 'Зинько', 'Сидоров', 'Васильев', 'Литвинов']

import sys
new_athletes = sys.argv[1:4]
athletes[0:3] = new_athletes
print(athletes)



