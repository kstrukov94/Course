"""ПОВТОРЯЕМ СТРОКИ"""
# Напишите программу, которая принимает первым аргументом командной строки множитель N, а после произвольное количество строк.
# Программа должна повторить каждую принятую строку N раз и вывести финальные данные разделенные пробелом (см. пример ниже).
#
# Пример использования:
# > python program.py 3 a C xy
# a a a C C C xy xy xy

import sys
N = int(sys.argv[1])
strings = sys.argv[2:]
res = []
strings_i = 0
while strings_i < len(strings):
    n = 1
    while n <= N:
        res.append(strings[strings_i])
        n += 1
    strings_i += 1
print(" ".join(res))

