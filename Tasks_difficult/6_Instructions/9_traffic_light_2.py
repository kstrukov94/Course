"""#88: СВЕТОФОР - 2"""
# Сложность: 4 из 10
# Работа светофора для автомобилей запрограммирована следующим образом, с начала каждого часа,
# в течение N минут горит зеленый сигнал, затем в течение M минут горит желтый сигнал,
# а потом в течение L минут — красный. После снова загорается зеленый и тд.
#
# Напишите программу traffic_light.py, которая получает четыре аргумента из командной строки: N, M, L и T,
# где T время в минутах, прошедшее с начала очередного часа.
# После программа должна вывести green, yellow или red в зависимости от того,
# сигнал какого цвета горит для автомобиля в этот момент.
#
# Пример использования:
# > python traffic_light.py 3 1 2 2
# green

import sys
n, m, l, t = map(int, sys.argv[1:])

lights = {0: "green", 1: "yellow", 2: "red"}

period = n + m + l

remainder = t % period

if remainder < n:
    print(lights[0])
elif remainder < (n+m):
    print(lights[1])
elif remainder < (n+m+l):
    print(lights[2])


# # Вариант 1. Решение "В ЛОБ" (не рекомендуется)
# import sys
#
# # Получаем значения
# green = int(sys.argv[1])
# yellow = int(sys.argv[2])
# red = int(sys.argv[3])
# time = int(sys.argv[4])
#
# # Устанавливаем зеленый сигнал
# signal = "green"
#
# # Определяем продолжительность текущего сигнала
# current_signal_min = 0
#
# i = -1
# while i < (time - 1):
#     i += 1
#     current_signal_min += 1
#
#     # Если сигнал зеленый:
#     if signal == "green":
#         # Если его время истекло, то переключаемся на желтый и сбрасываем current_signal_min
#         if current_signal_min == green:
#             current_signal_min = 0
#             signal = "yellow"
#             continue
#
#     # Если сигнал желтый:
#     if signal == "yellow":
#         # Если его время истекло, то переключаемся на красный и сбрасываем current_signal_min
#         if current_signal_min == yellow:
#             current_signal_min = 0
#             signal = "red"
#             continue
#
#     # Если сигнал красный:
#     if signal == "red":
#         # Если его время истекло, то переключаемся на зеленый и сбрасываем current_signal_min
#         if current_signal_min == red:
#             current_signal_min = 0
#             signal = "green"
#             continue
#
# print(signal)
#
#
# # Вариант 2. С помощью математики.
# import sys
#
# # Получаем значения
# green_time = int(sys.argv[1])
# yellow_time = int(sys.argv[2])
# red_time = int(sys.argv[3])
# all_time = int(sys.argv[4])
#
# # Вычисляем один светофорный цикл.
# cycle = green_time + yellow_time + red_time
#
# # Вычисляем сколько времени прошло в последнем цикле.
# last_cycle = all_time - int(all_time / cycle) * cycle
#
# # Выводим red если время зеленого и желтого света уже прошло.
# if last_cycle >= yellow_time + green_time:
#     print("red")
# # Выводим yellow если время зеленого света уже прошло.
# elif last_cycle >= green_time:
#     print("yellow")
# # Выводим green если его время еще не прошло.
# else:
#     print("green")
#
#
# # Вариант 3. Тоже с помощью математики, но немного другой подход.
#
# import sys
#
# time = int(sys.argv[4])
#
# # Время работы светофоров
# green = int(sys.argv[1])
# yellow = int(sys.argv[2])
# red = int(sys.argv[3])
#
# # Находим время последнего цикла
# last = time % (green + yellow + red)
#
# # Финальные условия
# if 0 <= last < green:
#     print('green')
# elif green <= last < green + yellow:
#     print('yellow')
# else:
#     print('red')