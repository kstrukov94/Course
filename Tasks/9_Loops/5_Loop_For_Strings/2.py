"""РАЗДЕЛЯЕМ СИМВОЛЫ"""
# Напишите программу, которая первым аргументом командной строки получает строку символов,
# набранных в разных регистрах, а затем разделяет их на символы в нижнем регистре и символы в верхнем регистре.
#
# В конце программа должна вывести сперва все символы в нижнем регистре, а затем все символы в верхнем регистре.
# Порядок следования символов нужно сохранить.
#
# Пример использования:
# > python program.py aBcDeFGhiKL
# > acehiBDFGKL

import string
import sys

string_text = sys.argv[1]

upper = ""
lower = ""

for char in string_text:
    if char in string.ascii_uppercase:
        upper += char
    if char in string.ascii_lowercase:
        lower += char
print(lower+upper)

# import sys
#
# text = sys.argv[1]
#
# # Создаем переменные для храннения.
# lower_text = upper_text = ""
#
# # Перебираем текст.
# for c in text:
#     # Раскидываем по массиву.
#     if c.islower():
#         lower_text += c
#
#     if c.isupper():
#         upper_text += c
#
# print(lower_text + upper_text)