"""СУММА ПРОИЗВЕДЕНИЙ ЭЛЕМЕНТА НА ИНДЕКС"""
# Напишите функцию sum_mult_index, которая принимает список, а затем проходится по каждому его элементу,
# умножает элемент на его индекс, суммирует все полученные результаты и возвращает итоговый ответ.
#
# Например, если у нас список [5, 6, 7, 8],
# то нужно посчитать 0x5 + 1x6 + 2x7 + 3x8 = 44 (где 0, 1, 2, 3 - это индексы элементов, а 5, 6, 7, 8 - значения).
#
# Используйте функцию enumerate.
#
# Пример использования функции:
# result = sum_mult_index([11, 22, 33, 44, 55])
# print(result)
# 440

import sys
def sum_mult_index(list):
    result = []
    for index, value in enumerate(list):
        result.append(index * value)
    return sum(result)

print(sum_mult_index([11, 22, 33, 44, 55]))

# Так как первый элемент имеет индекс 0,
# то начинать можно со второго элемента.

# # Вариант 1
# def sum_mult_index(lst):
#     result = 0
#     for e, i in enumerate(lst[1:], 1):
#         result += e * i
#     return result
#
#
# # Вариант 2
# def sum_mult_index(lst):
#     return sum(e * i for e, i in enumerate(lst[1:], 1))