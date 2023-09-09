"""ЧИСЛО С МАКСИМАЛЬНОЙ СУММОЙ ЦИФР"""
# Напишите программу, которая принимает из аргументов командной строки
# произвольное количество чисел, а затем выводит то, у которого максимальная сумма цифр.
#
# Пример работы программы (сумма цифр у 33 равна 6):
# > python program.py 111 2_Strings 33 41
# 33

import sys
numbers = sys.argv[1:]
sum_max = 0
num_max = 0
i = 0
while i < len(numbers):
    j = 0
    num_sum = 0
    while j < len(numbers[i]):
        num_sum += int(numbers[i][j])
        j += 1
    if num_sum > sum_max:
        num_max = int(numbers[i])
        sum_max = int(num_sum)
    i += 1
print(num_max)

# import sys
#
# numbers = sys.argv[1:]
#
# # Переменные для хранения максимального результата.
# max_sum = 0
# max_number = 0
#
# # Основной цикл, который обходит числа.
# number_i = 0
# while number_i < len(numbers):
#
#     # Вложенный цикл для обхода цифр числа и подсчета суммы.
#     digit_i = 0
#     current_sum = 0
#     while digit_i < len(numbers[number_i]):
#         current_sum += int(numbers[number_i][digit_i])
#         digit_i += 1
#
#     # Обновляем максимальное число.
#     if current_sum > max_sum:
#         max_sum = current_sum
#         max_number = numbers[number_i]
#
#     number_i += 1
#
# print(max_number)
#
# #
# # Альтернативный вариант (более классический, так как используется математика)
# #
#
# import sys
#
# numbers = sys.argv[1:]
#
# max_sum = 0
# max_number = 0
#
# # Основной цикл, который обходит числа.
# number_i = 0
# while number_i < len(numbers):
#     # Получаем число
#     number = int(numbers[number_i])
#
#     # Вложенный цикл для обхода цифр числа и подсчета суммы.
#     digit_i = 0
#     current_sum = 0
#     while number > 0:
#         current_sum += number % 10
#         number //= 10
#
#     # Обновляем максимальное число.
#     if current_sum > max_sum:
#         max_sum = current_sum
#         max_number = numbers[number_i]
#
#     number_i += 1
#
# print(max_number)


