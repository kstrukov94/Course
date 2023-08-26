"""#70: ФОРМАТИРОВАНИЕ ВРЕМЕНИ"""
# Сложность: 5 из 10
# Напишите программу time.py, которая получает из первого аргумента командной строки количество секунд, которое прошло с начала дня.
# Программа должна выводить отформатированное время в формате HH:MM:SS.
#
# SS – число секунд от 0 до 59.
# MM – число минут от 0 до 59.
# HH – число часов от 0 до 23.
# Все значения времени должны выводится в двузначном формате, если число занимает один знак, то перед ним должен быть 0.
#
# Если прошло меньше одного часа, то часы выводить не нужно.
#
# Если прошло меньше одной минуты, то минуты выводить не нужно.
#
# Пример использования:
# > python time.py 17
# 17
# > python time.py 79
# 01:19
# > python time.py 4589
# 01:16:29

import sys
num = int(sys.argv[1])
# num = 4589
hours = num // 3600
mins = (num // 60) - hours * 60
secs = num - (hours * 3600) - (mins * 60)
if num >= 3600:
    result = f"{hours:0>2}:{mins:0>2}:{secs:0>2}"
elif num >= 60:
    result = f"{mins:0>2}:{secs:0>2}"
else:
    result = f"{secs:0>2}"
print(result)


# TODO ознакомиться с вариантами преподавателя
# # Вариант 1
# import sys
#
# # Получаем количество секунд и объявляем переменную t для хранения результата.
# seconds = int(sys.argv[1])
# t = ""
#
# # Вычисляем часы
# h = int(seconds / 3600)
# if h:
#     # Если часы меньше 9, то добавляем в начале 0.
#     if h <= 9:
#         t += "0{}:".format(h)
#     else:
#         t += "{}:".format(h)
#
#
# # Вычисляем минуты
# m = int((seconds - h * 3600) / 60)
# if m or (not m and h):
#     # Если минуты меньше 9, то добавляем в начале 0.
#     if m <= 9:
#         t += "0{}:".format(m)
#     else:
#         t += "{}:".format(m)
#
# # Вычисляем секунды
# s = (seconds - h * 3600 - m * 60)
# # Если секунды меньше 9, то добавляем в начале 0.
# if s <= 9:
#     t += "0{}".format(s)
# else:
#     t += "{}".format(s)
#
# print(t)
#
# #
# # Вариант 2: используем продвинутое форматирование и однострочный if
# #
# import sys
#
# # Получаем количество секунд и объявляем переменную t для хранения результата.
# seconds = int(sys.argv[1])
# t = ""
#
# # Вычисляем часы
# h = seconds // 3600
# t += "{:02d}:".format(h) if h else ""
#
# # Вычисляем минуты
# m = (seconds - h * 3600) // 60
# t += "{:02d}:".format(m) if m or (not m and h) else ""
#
# # Вычисляем секунды
# s = seconds - h * 3600 - m * 60
# t += "{:02d}".format(s)
#
# print(t)
#
# #
# # Вариант 3: используем модуль time для получения и форматирования времени
# #
# import sys
# import time
#
# seconds = int(sys.argv[1])
#
# # Получаем структурированное время
# struct_time = time.gmtime(seconds)
#
# # Получаем форматированное время
# format_time = time.strftime("%H:%M:%S", struct_time)
#
# # Вырезаем начальные 00:
# zero = format_time.startswith("00:")
# while zero:
#     format_time = format_time[3:]
#     zero = format_time.startswith("00:")
#
# print(format_time)
#
# #
# # Вариант 4: используем модуль time для получения и форматирования времени
# #
# import sys
# import time
#
# seconds = int(sys.argv[1])
#
# # Получаем структурированное время
# struct_time = time.gmtime(seconds)
#
# # В зависимости от количества секунд подбираем форматирование
# if seconds < 60:
#     time_format = "%S"
# elif seconds < 3600:
#     time_format = "%M:%S"
# else:
#     time_format = "%H:%M:%S"
#
# # Получаем форматированное время
# format_time = time.strftime(time_format, struct_time)
#
# print(format_time)
