"""СУММА ЧИСЕЛ"""
# Создайте функцию sum_num, которая принимает целое число N, а затем возвращает сумму всех чисел от 1 до N.
# Например, если число N=4, то нужно считать так: 1 + 2 + 3 + 4 = 10.
#
# Обрабатывать аргументы командной строки не нужно.
# Достаточно создать рабочую функцию, а система сама её проверит.
#
# Пример использования функции:
# result = sum_num(4)
# print(result)
# 10

def sum_num(num):
    if type(num) == str and num.isdigit():
        num = int(num)
    if type(num) not in [int, float]:
        return TypeError
    result = 0
    for n in range(1, num + 1):
        result += n
    return result

# # Вариант 1: с помощью while
# def sum_num(num):
#     result = 0
#     while num >= 1:
#         result += num
#         num -= 1
#     return result
#
# # Вариант 2: рекурсивное решение
# def sum_num_rec(num):
#     if num <= 1:
#         return num
#     return num + sum_num_rec(num - 1)
#
# # Вариант 3: используем формулу для арифметической прогрессии.
# # https://ru.wikipedia.org/wiki/Арифметическая_прогрессия
# def sum_num_gauss(num):
#     return int(num * (num + 1) / 2)


