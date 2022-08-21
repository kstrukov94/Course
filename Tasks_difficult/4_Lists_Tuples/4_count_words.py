"""#37: КОЛИЧЕСТВО СЛОВ В ПРЕДЛОЖЕНИИ"""
# Сложность: 6 из 10
# Напишите программу count.py, которая получает из первого аргумента командной строки предложение, а затем выводит количество слов в этом предложении.
#
# В предложении могут быть двойные пробелы, а также неправильно расставленные знаки препинания (запятые, точки, восклицательный и вопросительный знаки).
#
# Примечание: если в программу передать набор слов заключенных в кавычки, то они будут восприняты как один аргумент.
#
# Пример использования:
#  "А вы действительно хотите узнать всю правду ???"
# > python count.py "Мы с Андреем пошли на рыбалку , а затем вернулись домой ! "
# > 10

import sys
line = sys.argv[1]

symbol_list = []
for symbol in line:
    if symbol in ".,!? ":
        symbol_list.append(" ")
    else:
        symbol_list.append(symbol)
# print(symbol_list)

new_line = "".join(symbol_list)
# print(new_line)

word_list = []
for word in new_line.strip().split():
        word_list.append(word)
# print(word_list)

print(len(word_list))

# import sys
#
# # Получаем строку.
# stroka = sys.argv[1]
#
# # Меняем все знаки препинания на пробелы, чтобы у нас остался один разделитель.
# stroka = stroka.\
#     replace(",", " ").\
#     replace(".", " ").\
#     replace("!", " ").\
#     replace("?", " ")
#
# # Разбиваем строку по пробелу.
# # После работы split() получится список вида ['word1', 'word2', '', '', 'word3'].
# words = stroka.split(" ")
#
# # Считаем количество пустых элементов.
# empty_cnt = words.count('')
#
# # Считаем общее количество элементов.
# all_cnt = words.__len__()
#
# # Считаем и выводим результат.
# print(all_cnt - empty_cnt)
#
# # Альтернативный вариант
# # Использование split() без передачи параметров
# # В этом случае метод будет разбивать строку по пробелам,
# # при этом серии последовательных пробелов будут рассматриваться как один.
# words = stroka.split()
#
# # Просто печатаем результат с помощью функции len
# print(len(words))
#
# #
# # Вариант с подсчетом слов
# # На основе решения ученика Ильи (https://shultais.education/lms/courses/python-3/tasks/37?thread=4610)
# #
# import sys
# text = sys.argv[1]
# words = 0
# new_word = True
# for i in text:
#     if i.isalpha():
#         # Если новое слово, или до этого были знаки препинания
#         if new_word or new_word is None:
#             words += 1
#             new_word = False
#     else:
#         # Если это не буква, то это и не новое слово
#         # и, вообще, не слово, поэтому None
#         new_word = None
#
# print(words)

