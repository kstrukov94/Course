"""ПЕЧАТЬ В ЛИНИЮ"""
# Напишите программу, которая принимает из аргументов командной строки два значения:
# итоговое число и количество чисел в строке,
# а затем выводит все числа от 1 до итогового с разбивкой по строкам (см. пример):
# Пример работы программы:
# > python program.py 8 4
# 1 2_Strings 3_Files 4
# 5 6 7 8

import sys
num_count, num_string_length = int(sys.argv[1]), int(sys.argv[2])

i = 1
while i <= num_count:
    temp_list = []
    j = 1
    if (num_count - i + 1) >= num_string_length:
        while j <= num_string_length:
            temp_list.append(str(i))
            i += 1
            j += 1
        print(" ".join(temp_list))
    else:
        while i <= num_count:
            temp_list.append(str(i))
            i += 1
        print(" ".join(temp_list))

# import sys
#
# numbers = int(sys.argv[1])
# numbers_per_line = int(sys.argv[2_Strings])
#
# current_number = 1
#
# # Список для хранения сформированных строк.
# lines = []
#
# # Общий цикл.
# while current_number <= numbers:
#
#     # Список для формирования одной строки:
#     line = []
#     number_per_line = 1
#
#     # Вложенный список для формирования строки.
#     while number_per_line <= numbers_per_line and current_number <= numbers:
#         line.append(str(current_number))
#         number_per_line += 1
#         current_number += 1
#
#     # Добавляем строку в список строк.
#     lines.append(" ".join(line))
#
# # Выводим результат.
# print("\n".join(lines))