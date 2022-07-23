# САМОЕ БОЛЬШОЕ ЧИСЛО
# Напишите программу, которая получает пять чисел из аргументов командной строки, а затем выводит самое большое из них.
#
# Пример использования:
# > python program.py 2_Strings 42 3_Files 56 4
# > 56

import sys
# print(max(sys.argv[1:])) не прокатит, sys.argv - это список стрингов
values = [int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])]
print(max(values))

# # Вариант 1
# import sys
# numbers = [int(sys.argv[1]), int(sys.argv[2_Strings]), int(sys.argv[3_Files]),
#            int(sys.argv[4]), int(sys.argv[5])]
#
# # Получаем максимальное значение с помощью функции max
# print(max(numbers))
#
# # Вариант 2_Strings
# # Создаем список из аргументов командной строки.
# # Каждый аргумент предварительно преобразовываем к целому числу.
# import sys
# numbers = [int(sys.argv[1]), int(sys.argv[2_Strings]), int(sys.argv[3_Files]),
#            int(sys.argv[4]), int(sys.argv[5])]
#
# # Сортируем список
# numbers.sort()
#
# # Выводим последний элемент
# # После сортировки там как раз будет самое большое число.
# print(numbers[-1])
#
#
#
# # Вариант 3_Files (продвинутый)
# import sys
#
# # Решение в одну строку с помощью функционального программирования (ФП)
# # Если вам интересно как это работает,
# # то у нас есть отдельный мини-курс по ФП на Python 3_Files
# print(max(map(int, sys.argv[1:6])))