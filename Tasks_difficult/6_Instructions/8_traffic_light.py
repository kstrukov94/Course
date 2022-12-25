"""#80: СВЕТОФОР"""
# Сложность: 3 из 10
# Работа светофора для пешеходов запрограммирована следующим образом, с начала каждого часа,
# в течение N минут горит зеленый сигнал, затем в течение M минут горит красный сигнал.
# Потом снова N минут горит зеленый и тд.
#
# Написать программу traffic_light.py, которая получает три аргумента из командной строки: N, M и T,
# где T время в минутах, прошедшее с начала очередного часа.
# После программа должна вывести green или red в зависимости от того, сигнал какого цвета горит для пешехода в этот момент.
#
# Пример использования:
# > python traffic_light.py 4 2 3
# green
# > python traffic_light.py 4 2 4
# red

import sys

n, m, t = map(int, sys.argv[1:])

time = 0
light_green = 0

while time <= t:
    if light_green:
        time += m
        light_green = 0
    else:
        time += n
        light_green = 1

print("green") if light_green else print("red")


# # Вариант 1: решение "В ЛОБ"
# import sys
#
# # Получаем значения
# green = int(sys.argv[1])
# red = int(sys.argv[2])
# time = int(sys.argv[3])
#
# # Устанавливаем зеленый сигнал
# signal = "green"
#
# # Длительность текущего сигнала
# current_signal_min = 0
#
# # Идем в часовом цикле от 0 до 59 включительно
# for i in range(0, 60):
#     current_signal_min += 1
#
#     # Прерываем цикл, если время кончилось
#     if i == time:
#         break
#
#     # Если текущий сигнал зеленый
#     if signal == "green":
#         # Если зеленый свет уже горит green секунд, то
#         # включаем красный и сбрасываем current_signal_min
#         if current_signal_min == green:
#             current_signal_min = 0
#             signal = "red"
#             continue
#
#     # Если текущий сигнал красный
#     if signal == "red":
#         # Если красный свет уже горит red секунд, то
#         # включаем зеленый и сбрасываем current_signal_min
#         if current_signal_min == red:
#             current_signal_min = 0
#             signal = "green"
#             continue
#
# print(signal)
#
# #
# # Вариант 2: решение с формулой
# #
# # Если немного подумать, то можно найти простое математическое решение,
# # для которого не требуются циклы.
# import sys
#
# # Получаем значения
# green_time = int(sys.argv[1])
# red_time = int(sys.argv[2])
# all_time = int(sys.argv[3])
#
# # Вычисляем один светофорный цикл.
# cycle = green_time + red_time
#
# # Вычисляем сколько времени прошло в последнем цикле.
# last_cycle = all_time - int(all_time / cycle) * cycle
#
# # Выводим red если время зеленого света уже прошло.
# print("red" if last_cycle >= green_time else "green")
#
# #
# # Вариант 3: используем остаток от деления
# #
# import sys
#
# # Получаем значения
# green_time = int(sys.argv[1])
# red_time = int(sys.argv[2])
# all_time = int(sys.argv[3])
#
# # Вычисляем последний цикл
# last_time = all_time % (green_time + red_time)
#
# # Если в последнем цикле прошло больше времени чем требуется для зеленого,
# # то значит у нас красный цвет.
# if last_time >= green_time:
#     print("red")
# else:
#     print("green")