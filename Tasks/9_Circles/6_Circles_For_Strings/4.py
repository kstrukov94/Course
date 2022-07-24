"""СЛЕДИМ ЗА ТРЕНДАМИ"""
# В сервисе сквозной аналитики Roistat есть такой отчет:

# Этот отчет показывает ежедневное количество событий, которые приняла система.
# В случае если в определенный день данных пришло больше, чем в предыдущий, то столбец раскрашивается зеленым цветом.
# Если данных пришло меньше, то столбец раскрашивается в красный.
# Если данных столько же, сколько и вчера, то столбец раскрашивается в тот же цвет, что и в предыдущий день.
#
# Напишите программу, которая получает из аргументов командной строки произвольное количество аргументов,
# каждый из которых отвечает за количество событий, которые пришли за один день.
# Программа должна вывести цвета для раскраски столбцов для каждого полученного элемента.
#
# Для положительных трендов нужно выводить green, а для отрицательных red.
# Выводимые цвета надо разделить пробелом. Считаем что первый день всегда положительный.
#
# Пример использования:
# > python trend.py 129 130 135 110 109 123
# green green green red red green

import sys
event_number = sys.argv[1:]

event_colors = []
prev_num = 0

for num in event_number:
    num = int(num)
    if not event_colors:
        event_colors.append("green")
        prev_color = "green"
        continue
    if num == prev_num:
        event_colors.append(prev_color)
        continue
    if num > prev_num:
        event_colors.append("green")
        prev_color = "green"
    else:
        event_colors.append("red")
        prev_color = "red"
    prev_num = num
print(" ".join(event_colors))

# import sys
#
# # Получаем все элементы
# values = sys.argv[1:]
#
# colors = []
#
# # Считаем, что предыдущий элемент минус бесконечность.
# # Это значит, что любой другой элемент будет больше,
# # а значит первый гарантировано получит зеленый цвет.
# prev_value = float("-inf")
#
# # Перебираем элементы
# for value in values:
#     value = int(value)
#
#     # Сравниваем текущее значение с предыдущим
#     if value > prev_value:
#         colors.append("green")
#     elif value < prev_value:
#         colors.append("red")
#     else:
#         # Если данные равны, то ставим значение последнего элемента из colors
#         colors.append(colors[-1])
#
#     prev_value = value
#
# print(" ".join(colors))