"""#1206: ЁЛОЧКА"""
# Сложность: 3 из 10
# Напишите программу, которая из первого аргумента командной строки принимает число, а затем выводит «ёлочку» в таком виде (для числа 17):
#
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
# 16 17
# Внимание! Перед отправкой решения, хорошо протестируйте программу с разными числами на своём компьютере.
# В данной задаче очень просто войти в бесконечный цикл и если вы отправите на проверку решение с бесконечным циклом, сайт на какое-то время заблокирует доступ.
# Мы, конечно, его разблокируем, но зачем рисковать :)
#
# Пример работы программы:
# > python program.py 17
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
# 16 17

import sys


def spruce(end_number):
    current_number = 1
    numbers_per_line = 1
    # Список для хранения сформированных строк.
    lines = []

    # Общий цикл.
    while current_number <= end_number:

        # Список для формирования одной строки:
        line = []

        # Вложенный список для формирования строки.
        while len(line) < numbers_per_line and current_number <= end_number:
            line.append(str(current_number))
            current_number += 1
        numbers_per_line += 1

        # Добавляем строку в список строк.
        lines.append(" ".join(line))

    # Выводим результат.
    return "\n".join(lines)


num = int(sys.argv[1])
print(spruce(num))


# import sys
# numbers = int(sys.argv[1])
#
# number = 1
# numbers_in_line = 1
#
# # В данной задаче используем вложенные друг в друга while циклы
# while number <= numbers:
#     number_in_line = 1
#     line = []
#
#     # Важно проверять как формирование очередной строки,
#     # так и следить за общим количеством чисел
#     while number_in_line <= numbers_in_line and number <= numbers:
#         line.append(str(number))
#         number_in_line += 1
#         number += 1
#
#     print(" ".join(line))
#
#     numbers_in_line += 1
