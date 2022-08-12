"""#40: ПРЯМОЙ И ОБРАТНЫЙ ПОРЯДОК"""
# Сложность: 1 из 10
# Напишите программу reverse.py, которая получает из первого аргумента командной строки текст и меняет в нем порядок букв в словах на обратный.
# Порядок слов должен быть сохранен.
#
# Пример использования:
# > python reverse.py "яблоки вкусные"
# иколбя еынсукв

import sys
word = sys.argv[1]

result = []
for word in word.split():
    result.append("".join(word[::-1]))
print(" ".join(result))

# import sys
# text = sys.argv[1]
#
# words = []
# # Разбиваем текст на слова и проходим по ним в цикле
# for word in text.split(" "):
#     # Каждое отдельное слово разворачиваем с помощью среза [::-1]
#     # и добавляем в список words
#     words.append(word[::-1])
#
# # Склеиваем все слова обратно с помощью join
# print(" ".join(words))
#
# #
# # Альтернативный (продвинутый) вариант
# # с использованием функции map и lambda.
# # Подробнее в курсе по функциональному программированию
# #
# import sys
# print(" ".join(map(lambda w: w[::-1], sys.argv[1].split())))
