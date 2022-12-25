"""СКЛЕЙКА"""
# Склейте элементы списка whoami в строку с помощью функции reduce.

from functools import reduce

whoami = ['Я', ' ', 'п', 'р', 'о', 'г', 'р', 'а', 'м', 'м', 'и', 'с', 'т']

def string_merge(str1: str, str2: str):
    return str1 + str2

whoami = reduce(string_merge, whoami)

# print(whoami)
