"""ЗАПОЛНЯЕМ ПРОМЕЖУТКИ, ЧАСТЬ 2"""
# Напишите программу, которая из аргументов командной строки принимает два вещественных числа:
# начальное и конечное, а после заполняет промежуток между этими числами с шагом 0.1 в возрастающем порядке.
#
# Используйте функцию range().
#
# Пример использования:
# > python program.py 0.7 1.5
# > 0.7 0.8 0.9 1.0 1.1 1.2 1.3 1.4 1.5

import sys

n_start, n_end = sys.argv[1:]
n_start = int(float(n_start) * 10)
n_end = int(float(n_end) * 10) + 1
nums = []

for n in range(n_start, n_end):
    nums.append(str(n / 10))
print(" ".join(nums))

# import sys
# start = float(sys.argv[1])
# end = float(sys.argv[2])
#
# # Приводим к целым числам
# start = int(start * 10)
# # Не забываем добавить 1, чтобы захватить конечное число
# end = int(end * 10) + 1
#
# values = []
# # Перебираем числа и заполняем список values.
# for val in range(start, end):
#     values.append(str(val / 10))
#
# print(" ".join(values))

# TODO переписать без step (он лишний)
# from sys import argv
#
# numA = int(float(argv[1]) * 10)
# numB = int(float(argv[2]) * 10)
# step = 0
# if numA > numB:
#     step = -1
#     for i in range(numB, numA + 1, step):
#         print(round(i / 10, 1), end=' ')
# else:
#     step = 1
#     for i in range(numA, numB + 1, step):
#         print(round(i / 10, 1), end=' ')
