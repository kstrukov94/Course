# Напишите программу, которая принимает первым аргументом командной строки номер лицевого счета, состоящий из 8 цифр.
# Если номер короткий, то в начале проставляются нули, например 00001451.
# В результате работы программа должна вывести номер без лидирующих нулей.
#
# Воспользуйтесь методом lstrip, который работает также как и strip, но очищает только левую часть строки.
#
# Пример использования:
# > python program.py 00123456
# > 123456
# python program.py 05550600
# > 5550600

import sys
card_number = sys.argv[1]
print(card_number.lstrip("0"))
