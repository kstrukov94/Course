# Числа, которые содержат много цифр, удобно разбивать на классы по три цифры.
# Так их гораздо удобнее и быстрее считывать:
#
# Напишите программу, которая получает из первого аргумента командной строки число, после разбивает это число пробелами на классы, а затем печатает результат.
#
# Иногда такая операция называется «Разбиение числа на разряды». Это неправильно с точки зрения математики, тем не менее такая формулировка часто используется программистами.
#
# Спецификатор для разбития числа на классы найдите в официальной документации.
#
# Пример использования:
# > python th.py 12345678
# > 12 345 678

import sys
number = int(sys.argv[1])
number = "{:,}".format(number).replace(",", " ")
print(number)
