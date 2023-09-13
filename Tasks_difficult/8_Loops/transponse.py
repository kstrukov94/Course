"""#56: ТРАНСПОНИРУЕМ МАТРИЦУ
Сложность: 6 из 10
В файле matrix.txt содержится матрица M x N.
Напишите программу transpose.py, которая транспонирует матрицу и сохраняет результат в файл transpose_matrix.txt.

Пример файла matrix.txt:
1 2
3 4
5 6
Пример файла transpose_matrix.txt (после транспонирования матрицы из matrix.txt):
1 3 5
2 4 6
"""

# представляем матрицу в виде вложенного списка
lines = []
for data in open('matrix.txt', 'r', encoding='UTF-8'):
    line = data.strip().split(' ')
    lines.append(line)
temp = []
# print(lines)

# создаем пустую матрицу и заполняем ее значениями, иначе получим exc: index out of range
result = []
for i in range(len(lines[0])):
    temp = []
    for j in range(len(lines)):
        temp.append(0)
    result.append(temp)
# print(result)

# переворачиваем значения в матрице
for i in range(len(lines[0])):
    for j in range(len(lines)):
        result[i][j] = lines[j][i]
# print(result)

# записываем в файл
file = open('transponse_matrix.txt', 'w', encoding='UTF-8')
for elems in result:
    file.write(f'{" ".join(elems)}\n')



"""РЕШЕНИЕ ПРЕПОДАВАТЕЛЯ"""
# Открываем файл и объявляем переменную для хранения матирцы
matrix_file = open("matrix.txt", "r")
matrix = []

# Заполняем матрицу данными.
for line in matrix_file.readlines():
    matrix.append(line.strip().split(" "))

# Создаем пустую развернутую матрицу.
transpose_matrix = []
for k in range(matrix[0].__len__()):
    transpose_matrix.append([None] * matrix.__len__())

# Транспонируем (заполняем значениями)
i = 0
for line in matrix:
    j = 0
    for col in line:
        transpose_matrix[j][i] = matrix[i][j]
        j += 1
    i += 1

# Записываем результат в файл.
transpose_matrix_file = open("transpose_matrix.txt", "w")
for line in transpose_matrix:
    transpose_matrix_file.write("{}\n".format(" ".join(line)))
transpose_matrix_file.close()


# Вариант 2 (продвинутый)

# Заполняем переменную matrix данными из файла.
# Используем генератор списков из мини-курса
# по Функциональному программированию на Python 3.
matrix = [line.strip().split(" ") for line in open("matrix.txt").readlines()]

# Создаем пустую развернутую матрицу.
# Используем генератор списков.
transpose_matrix = [[None] * len(matrix) for k in range(len(matrix[0]))]

# Транспонируем (заполняем значениями).
# Используем enumerate вмемсто собственных счетчиков.
for i, line in enumerate(matrix):
    for j, _ in enumerate(line):
        transpose_matrix[j][i] = matrix[i][j]

# Записываем результат в файл.
# Используем менеджер контекста with.
# Записываем с помощью функции print()
with open("transpose_matrix.txt", "w") as transpose_matrix_file:
    for line in transpose_matrix:
        print(" ".join(line), file=transpose_matrix_file)