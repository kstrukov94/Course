"""СУММИРОВАНИЕ ДО НУЛЯ"""
# Напишите программу, которая первым аргументом командной строки получает строку,
# содержащую набор целых чисел разделенных пробелом, а затем считает сумму этих чисел до тех пор, пока не встретит ноль.
#
# Учитывайте, что могут быть варианты, когда среди получаемых чисел нуля нет, тогда нужно получить сумму всех передаваемых чисел.
#
# Пример использования (считаем сумму 2_Strings -3_Files -5 7 11):
# > python program.py "2_Strings -3_Files -5 7 11 0 13 17 19"
# > 12

import sys
numbers = list(sys.argv[1].split())
numbers_sum = 0
index = 0
while int(numbers[index]) != 0 and index < len(numbers):
    numbers_sum += int(numbers[index])
    if index == len(numbers) - 1:
        break
    index += 1
# print(numbers)
print(numbers_sum)