"""ПОИСК МАКСИМУМОВ"""
# Иногда в систему поступает много данных и нужно фиксировать только те, которые выросли в значении.
# Например, если в программу пришли числа 34, 56, 12, 55, 74, 58. То нужно оставить только 34, 56, и 74.
# То есть мы каждый раз оставляем только максимальное число относительно всех предыдущий значений.
#
# Напишите программу, которая получает из аргументов командной строки произвольное количество чисел, а затем выводит только максимумы.
# Выводимые числа нужно разделить запятой с пробелом.
#
# Пример использования:
# > python trend.py 34 56 12 55 74 58 59 74 75
# 34, 56, 74, 75

import sys
sys_list = list(map(int, sys.argv[1:]))
result = []
result.append(str(sys_list[0]))
i_max = sys_list[0]

for i in sys_list[1:]:
    if i > i_max:
        result.append(str(i))
        i_max = i
print(", ".join(result))


# import sys
#
# max_values = []
# max_value = float("-inf")  # Изначально считаем, что минимальное значение - это минус бесконечность
# for value in sys.argv[1:]:
#     value = int(value)
#     if value > max_value:
#         max_value = value
#         max_values.append(str(max_value))
#
# print(", ".join(max_values))
#
#
# # Альтернативный вариант с помощью reduce
# # Функциональное программирование мы изучаем в отдельном курсе.
# import sys
# from functools import reduce
#
# data = map(int, sys.argv[1:])
#
# def collect_max_values(result, value):
#     if value > result[0]:
#         return value, result[1] + [value]
#     return result[0], result[1]
#
# max_values = reduce(collect_max_values, data, (float("-inf"), []))
# max_values = map(str, max_values[1])
# print(", ".join(max_values))
#
#
# # Жесткий альтернативный вариант с помощью map и reduce
# # Так писать крайне не рекомендуется, но в целом можно
# import sys
# from functools import reduce
# print(", ".join(map(str, reduce(lambda r, v: (v, r[1] + [v]) if v > r[0] else (r[0], r[1]), map(int, sys.argv[1:]), (float("-inf"), []))[1])))
