# САМОЕ ДЛИННОЕ СЛОВО
# Напишите программу, которая первым аргументом командной строки принимает строку со списком слов,
# разделенных пробелом, а после выводит самое длинное из этих слов.
#
# Пример использования:
# > python program.py "кошки собаки пингвины зебры"
# > пингвины

import sys
string = sys.argv[1]
list = string.split()
list.sort(key=len, reverse=True)
print(list[0])

# # лучше так
# list.sort(key=len)
# print(list[-1])

# # СОРТИРОВКА ДОРОГО, ПОЛЬЗУЕМСЯ MAX + LEN
# text = str(sys.argv[1]).lower().split()
# big = max(text, key=len)
# print(big)
