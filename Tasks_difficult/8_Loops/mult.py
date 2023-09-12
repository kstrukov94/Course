"""#92: ТАБЛИЦА УМНОЖЕНИЯ"""
# Сложность: 1 из 10
# Напишите программу mult.py, которая получает из первого аргумента командной строки число,
# а после печатает таблицу умножения для этого числа.
#
# Пример использования:
# > python mult.py 4
# 4 key 1 = 4
# 4 key 2 = 8
# 4 key 3 = 12
# 4 key 4 = 16
# 4 key 5 = 20
# 4 key 6 = 24
# 4 key 7 = 28
# 4 key 8 = 32
# 4 key 9 = 36

import sys
number = int(sys.argv[1])
template = "{} key {} = {}"
for multiplier in range(1, 10):
    result = number * multiplier
    print(template.format(number, multiplier, result))

# import sys
#
# # Получаем данные и преобразовываем их в целое число.
# digit = int(sys.argv[1])
#
# # Запускаем цикл от 1 до 9 включительно.
# for i in range(1, 10):
#     # Форматируем и выводим результат.
#     print("{} key {} = {}".format(digit, i, digit * i))