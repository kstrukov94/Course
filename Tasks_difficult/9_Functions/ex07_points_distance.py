"""#67: РАССТОЯНИЕ МЕЖДУ ТОЧКАМИ"""
# Сложность: 3 из 10
# Напишите функцию distance, которая вычисляет расстояние между двумя точками на плоскости или в пространстве.
#
# Функция принимает два аргумента.
# Каждый аргумент - это кортеж из двух или трех элементов: X и Y для точки на плоскости и X, Y, Z - для точки в пространстве.
#
# Пример использования функции:
# print(distance((-1, 3), (6, 2)))
# 7.0710678118654755
# print(distance((-1, 3, 3), (6, 2, -2)))
# 8.660254037844387

import math


def distance(tuple1: tuple, tuple2: tuple):
    if len(tuple1) == 2 and len(tuple1) == len(tuple2):
        x1, y1 = tuple1
        x2, y2 = tuple2
        return ((x1 - x2)**2 + (y1 - y2)**2)**0.5
    if len(tuple1) == 3 and len(tuple1) == len(tuple2):
        x1, y1, z1 = tuple1
        x2, y2, z2 = tuple2
        return ((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)**0.5


# print(distance((-1, 3), (6, 2)))
#
# print(distance((-1, 3, 3), (6, 2, -2)))

# def distance(a, b):
#     # Проверяем длину передаваемых списков.
#     # В зависимости от длины используем одну из двух формул.
#     if len(a) == 3:
#         result = (b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2 + (b[2] - a[2]) ** 2
#     else:
#         result = (b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2
#
#     # Извлекаем квадратный корень с помощью возведения в степень на 1/2
#     return result ** .5