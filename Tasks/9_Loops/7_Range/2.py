"""ФАКТОРИАЛ С ПОМОЩЬЮ FOR"""
# Перепишите решение задачи «Факториал» с использованием цикла for и функции range.
#
# Пример использования:
# > python program.py 5
# 120

import sys
n = int(sys.argv[1])

result_new = 1
for num in range(1, n + 1):
    result_new *= num
print(result_new)

# import sys
#
# n = int(sys.argv[1])
#
# # Задаем начальное значение factorial.
# factorial = 1
# # Запускаем цикл.
# for i in range(2, n + 1):
#     factorial *= i
#
# print(factorial)