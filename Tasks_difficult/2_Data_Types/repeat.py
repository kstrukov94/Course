# #9: ПОВТОРЕНИЕ СТРОКИ
# Сложность: 2_Strings из 10
# Напишите программу repeat.py, которая получает из первого аргумента командной строки слово,
# а из второго число N, а после повторяет полученное слово N раз.
#
# Пример использования:
# > python repeat.py AA 5
# > AAAAAAAAAA


import sys
word, times = str(sys.argv[1]), int(sys.argv[2])
result = word * times
print(result)

