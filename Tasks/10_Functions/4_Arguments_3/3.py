"""ПРОЙДЕННОЕ РАССТОЯНИЕ"""
# В редакторе ниже содержится матрица расстояний между городами.
# Чтобы узнать расстояние между Москвой и Тверью, надо выбрать вторую по порядку строку и шестой столбец.
# Или шестую строку и второй столбец. В обоих случаях мы найдем значение 192.
#
# Напишите функцию calc_distance, которая принимает список, содержащий путь, по которому двигался автомобиль.
# Функция должна вернуть пройденное автомобилем расстояние.
#
# Пример использования функции (Казань - Калининград - Тверь):
# print(calc_distance([3, 0, 5]))
# 3447

import sys

# Список городов
cities = [
    # Клд  Мск   СПб,  Каз   Врж,  Тверь
    [0,    1337, 1103, 2192, 1855, 1255],  # Калининград
    [1337, 0,    712,  825,  522,  192],   # Москва
    [1103, 712,  0,    1526, 1337, 531],   # Санкт-Петербург
    [2192, 825,  1526, 0,    1080, 1006],  # Казань
    [1855, 522,  1337, 1080, 0,    815],   # Воронеж
    [1255, 192,  531,  1006, 815,  0]      # Тверь
]

# Напишите код функции тут.

def calc_distance(path):
    distance = 0
    start_point = path[0]
    for end_point in path[1:]:
        distance += cities[start_point][end_point]
        start_point = end_point
    return distance

# Получаем путь в виде списка: [0, 1, 2]
path = list(map(int, sys.argv[1:]))

print(calc_distance([3, 0, 5]))
# Выводим результат
# print(calc_distance(path))