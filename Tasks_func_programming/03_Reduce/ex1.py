"""СКЛЕЙКА"""
# Склейте элементы списка whoami в строку с помощью функции reduce.

from functools import reduce

whoami = ['Я', ' ', 'п', 'р', 'о', 'г', 'р', 'а', 'м', 'м', 'и', 'с', 'т']


def concatenate(str1, str2):
    return str1 + str2


whoami = reduce(concatenate, whoami)

# print(whoami)