# ЧИСЛА НА РУССКОМ И АНГЛИЙСКОМ
# Ниже в редакторе находится словарь digits, который содержит набор чисел и их названия на русском и английском языках.
# Обратите внимание, что ключами словаря выступают целые числа (так тоже можно), а значениями вложенные словари.
#
# Напишите программу, которая принимает из аргументов командной строки два параметра:
# цифру и язык, а затем выводит название цифры на этом языке.
#
# Учитывайте, что если ключ словаря задан числом, то при доступе по ключу,
# в квадратных скобках нужно также указывать число.
#
# Пример использования:
# > python program.py 4 ru
# > четыре

digits = {
    1: {"ru": "один", "en": "one"},
    2: {"ru": "два", "en": "two"},
    3: {"ru": "три", "en": "three"},
    4: {"ru": "четыре", "en": "four"},
    5: {"ru": "пять", "en": "five"},
    6: {"ru": "шесть", "en": "six"},
    7: {"ru": "семь", "en": "seven"},
    8: {"ru": "восемь", "en": "eight"},
    9: {"ru": "девять", "en": "nine"},
    0: {"ru": "ноль", "en": "zero"}
}

import sys
number, lang = int(sys.argv[1]), sys.argv[2]
print(digits[number][lang])