"""58: СЛЕД МАТРИЦЫ"""
# Сложность: 2 из 10
# В файле matrix.txt содержится квадратная матрица N key N.
# Напишите программу sled.py, которая вычисляет след матрицы и выводит его на экран.
#
# Пример файла matrix.txt:
# 1 2
# 3 4
# Пример использования:
# > python sled.py
# 5

i = 0
result = 0
for line in open("matrix.txt", "r", encoding="utf-8"):
    result += int(list(line.strip().split())[i])
    i += 1
print(result)
