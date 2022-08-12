"""ОБМЕН БУКВ"""
# Напишите программу, которая из первого аргумента командной строки получает фразу,
# а затем меняет в ней местами рядом стоящие буквы.
#
# Если фраза имеет нечетное число символов,
# то последний символ остается на своём месте.
#
# Пример использования:
# > python program.py "ABCDEF"
# > BADCFE

import sys
text = sys.argv[1]
prev_char = None
result = []
for idx, char in enumerate(text):
    prev_char = text[idx - 1] if idx > 0 else None
    if idx == len(text) - 1 and not idx % 2:
        result.append(char)
    if idx > 0 and idx % 2:
        result.append(char)
        result.append(prev_char)
print("".join(result))

# import sys
#
# # Приводим к списку.
# text = list(sys.argv[1])
#
# # Перебираем индексы с шагом 2 до len - 1.
# for i in range(0, len(text) - 1, 2):
#     # Меняем местами текущий и следующей символы.
#     text[i], text[i + 1] = text[i + 1], text[i]
#
# # Собираем финальную строку и выводим результат.
# print("".join(text))
#
# # Обратите внимание, что в range() мы перебираем до len(text) - 1.
# # Так как range() не захватывает последнее значение,
# #     то мы дойдем до позиции len(text) - 2.
# # Если слово содержит четное число символов, например 6,
# #     то мы обработаем 0, 2, 4.
# # Если слово содержит нечетное число символов, например 7,
# #     то мы всё-равно обработаем 0, 2, 4.
# # То есть последний символ мы не затронем, что как раз и требуется по условию.
#
# #
# # Альтернативный вариант через while и строки.
# #
# import sys
#
# text = sys.argv[1]
#
# swapped = ""
# i = 0
# while i < len(text) - 1:
#     swapped += text[i+1] + text[i]
#     i += 2
#
# # Добавляем последний символ если строка нечетная
# if len(text) % 2 == 1:
#     swapped += text[-1]
#
# print(swapped)

