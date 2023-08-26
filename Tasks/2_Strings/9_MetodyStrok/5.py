"""КОЛИЧЕСТВО ПОВТОРЕНИЙ БЕЗ УЧЕТА РЕГИСТРА"""
# Напишите программу, которая получает из первого аргумента командной строки слово, а из второго букву и выводит сколько раз эта буква встречается в переданном слове.
# В данной задаче одинаковые буквы в разном регистре считаются одной буквой: a и A - это одна буква
# Пример использования:
# > python count.py Python Y
# > 1

import sys

w, l = list(map(str, sys.argv[1:]))
syllables = 0
for char in w.lower():
    syllables += char in l.lower()
print(syllables)