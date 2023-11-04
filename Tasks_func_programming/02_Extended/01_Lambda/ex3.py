"""СКЛЕЙКА, 2"""
"""Склейте элементы списка whoami в строку с помощью функции reduce и lambda-функции."""

from functools import reduce

whoami = ['Я', ' ', 'п', 'р', 'о', 'г', 'р', 'а', 'м', 'м', 'и', 'с', 'т']

whoami = reduce(lambda x, y: x + y, whoami)

# print(whoami)