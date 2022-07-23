"""
 СОРТИРОВКА ПО АЛФАВИТУ
"""

# Сложность: 2_Strings из 10
# Напишите программу sort.py, которая получает из первого аргумента командной строки слово,
# а затем выводит все буквы слова в алфавитном порядке.

import sys
word = sys.argv[1]
word_list = list(word)
word_list.sort()
word = "".join(word_list)
print(word)

