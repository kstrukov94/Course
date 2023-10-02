"""#1218: СУММА ЭЛЕМЕНТОВ ВОКРУГ
Сложность: 7 из 10
Рядом с программой находится файл data.txt следующего содержания:

1  2  3  4  5  9
6  7  8  9  0  8
1  7  4  3  1  7
2  5 13  1  2  1
3  2  4  0  4  2
5  9  7  0 16  0
8  0 19  3  4  3
7  4  6  1  0 21

Это обычная матрица NxM с числами. Обратите внимание, что в реальном файле между числами стоит один пробел,
а в примере выше для наглядности, мы в некоторых местах добавили два пробела.

Напишите программу, которая получает из аргументов командной строки номер строки и номер столбца в матрице,
затем находит элемент на пересечении переданных координат,
а после вычисляет сумму значений элементов вокруг найденного элемента.
Номера элементов в строках и столбцах следует отсчитывать с нуля.

Пример расчета. Программа получает значения 1 (строка) и 5 (столбец).
По данным координатам находится число 8.
Вокруг него находятся элементы: 9, 5, 0, 1, 7.
Их сумма равна 22 — это и есть ответ.

Пример использования:
> python program.py 1 5
22
> python program.py 3 4
19
"""

import sys


def sum_elem(n, m):
    # читаем файл, записываем в массив
    matrix = []
    with open('data.txt', 'r', encoding='utf-8') as file:
        for line in file:
            matrix.append(list(map(int, line.strip().split(' '))))
    # print(matrix)

    # ищем сумму, проверяя границы матрицы
    result = 0

    # проверка на столбцы 1-4
    if n == 0:
        if m == len(matrix[n]) - 1:
            for i in range(0, n + 2):
                for j in range(m - 1, len(matrix[n])):
                    result += matrix[i][j]
        elif m == 0:
            for i in range(0, n + 2):
                for j in range(0, m + 2):
                    result += matrix[i][j]
        else:
            for i in range(0, n + 2):
                for j in range(m - 1, m + 2):
                    result += matrix[i][j]
    elif n == len(matrix) - 1:
        if m == len(matrix[n]) - 1:
            for i in range(n - 1, len(matrix)):
                for j in range(m - 1, len(matrix[n])):
                    result += matrix[i][j]
        elif m == 0:
            for i in range(n - 1, len(matrix)):
                for j in range(0, m + 2):
                    result += matrix[i][j]
        else:
            for i in range(n - 1, len(matrix)):
                for j in range(m - 1, m + 2):
                    result += matrix[i][j]
    else:
        if m == len(matrix[n]) - 1:
            for i in range(n - 1, n + 2):
                for j in range(m - 1, len(matrix[n])):
                    result += matrix[i][j]
        elif m == 0:
            for i in range(n - 1, n + 2):
                for j in range(0, m + 2):
                    result += matrix[i][j]
        else:
            for i in range(n - 1, n + 2):
                for j in range(m - 1, m + 2):
                    result += matrix[i][j]

    result -= matrix[n][m]
    return result


y, x = map(int, sys.argv[1:])
print(sum_elem(y, x))


"""
import sys

# Получаем координаты:
row = int(sys.argv[1])     # Строка
column = int(sys.argv[2])  # Столбец

# Размер матрицы
WIDTH = 6
HEIGHT = 8

# Читаем файл и преобразуем в матрицу
matrix = []
data_file = open("data.txt", "r")
for line in data_file:
    # Заводим список для хранения элементов одной строки файла.
    line_list = []
    for number in line.split(" "):
        line_list.append(int(number))

    # Альтернативный вариант в одну строку:
    # line_list = list(map(int, line.split()))
    matrix.append(line_list)


# Основной алгоритм.
# Считаем для каждого варианта.
result = 0
if row - 1 >= 0:
    result += matrix[row - 1][column]
if (row - 1) >= 0 and (column - 1 >= 0):
    result += matrix[row - 1][column - 1]
if (row - 1) >= 0 and (column + 1 < WIDTH):
    result += matrix[row - 1][column + 1]
if column - 1 >= 0:
    result += matrix[row][column - 1]
if column + 1 < WIDTH:
    result += matrix[row][column + 1]
if row + 1 < HEIGHT:
    result += matrix[row + 1][column]
if (row + 1 < HEIGHT) and (column - 1 >= 0):
    result += matrix[row + 1][column - 1]
if (row + 1 < HEIGHT) and (column + 1 < WIDTH):
    result += matrix[row + 1][column + 1]

print(result)"""

""" САМОЕ КРАСИВОЕ РЕШЕНИЕ
num_list = []
M_0 = - 1
for each in open("data.txt", "r").readlines():
    num_list_tmp = []
    for each_2 in each.strip().split():
        num_list_tmp.append(int(each_2))
    num_list.append(num_list_tmp)
    M_0 += 1
    
N_0 = len(num_list[0]) - 1

import sys
M, N = map(int, sys.argv[1:3])

res_list = []
for n in range(N-1 if N!=0 else N, N+2 if N<N_0 else N+1):
    for m in range(M-1 if M!=0 else M, M+2 if M<M_0 else M+1):
        res_list.append(num_list[int(m)][int(n)])
print(sum(res_list) - num_list[M][N])
"""