"""46: ПРОВЕРКА СКОБОК"""
# Сложность: 2 из 10
# Напишите программу skobki.py, которая получает из первого аргумента командной строки строку, содержащую скобки,
# а затем проверяет правильно ли они расставлены.
#
# Рассматривайте только круглые скобки.
# Программа должна выводить 1 если скобки расставлены правильно, и 0 если порядок скобок нарушен
#
# Пример использования:
# > python skobki.py (2+3)()
# 1

import sys
line_symbols = list(sys.argv[1])
bracket_list = []
for symbol in line_symbols:
    if symbol in "()":
        bracket_list.append(symbol)
# print(bracket_list)

result = 1
prev_bracket = bracket_list[0]
for bracket in bracket_list[1:]:
    if bracket == ")" and prev_bracket != "(":
        result = 0
    prev_bracket = bracket
print(result)


