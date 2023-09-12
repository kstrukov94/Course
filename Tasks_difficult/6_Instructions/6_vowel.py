"""#10: ТОЛЬКО ГЛАСНЫЕ"""
# Сложность: 2 из 10
# Напишите программу vowel.py, которая получает из первого аргумента командной строки слово на английском языке,
# удаляет из него все согласные буквы и выводит оставшиеся гласные.
#
# Пример использования:
# > python vowel.py programming
# oai

import sys
word = sys.argv[1]

result = []
for i in word:
    if i in "aeioquyAEIOQUY":
        result.append(i)
print("".join(result))


# import sys
#
# # Определяем две строки с согласными
# abc_lowercase = 'bcdfghjklmnpqrstvwxz'
# abc_uppercase = 'BCDFGHJKLMNPQRSTVWXZ'
#
# # Получаем оригинальную строку и объявляем пустую для хранения результата.
# original = sys.argv[1]
# vowels = ""
#
# # Проходимся в цикле по всем буквам оригинальной строки.
# for i in original:
#     # Проверяем, что очередной символ не принадлежит к согласным
#     if i not in abc_lowercase and i not in abc_uppercase:
#         # Расширяем результат
#         vowels += i
#
# print(vowels)
#
# # Вариант 2
# # Используем алфавит гласных.
# abc = 'aueiyoAUEIYO'
#
# # Получаем оригинальную строку и объявляем пустую для хранения результата.
# original = sys.argv[1]
# vowels = ""
#
# # Проходимся в цикле по всем буквам оригинальной строки.
# for i in original:
#     # Проверяем, что очередной символ принадлежит к гласным
#     if i in abc:
#         # Расширяем результат
#         vowels += i
#
# print(vowels)
#
# # Вариант 3 (продвинутый).
# # Используем функциональное программирование.
# print("".join(list(filter(lambda key: key in "aueiyoAUEIYO", sys.argv[1]))))


