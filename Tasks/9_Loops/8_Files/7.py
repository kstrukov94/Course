"""ЧТЕНИЕ RAID 0"""
# RAID — это технология, которая позволяет разбивать данные на несколько частей и хранить каждую часть на отдельном жестком диске.
# Например, если у нас есть два диска и файл в 1Гб, то мы можем разбить его на две части по 500Мб и записать каждую на свой диск,
# что в 2 раза увеличит скорость записи.
#
# Попробуем реализовать чтение RAID 0 на Python. Рядом с программой находится N текстовых файлов в кодировке utf-8.
# Каждый файл имеет имя data-1.txt, data-2.txt, ..., data-N.txt. При записи данных, первый символ текста был помещен в файл data-1.txt,
# второй в data-2.txt и тд. В случае если длина текста больше N, то алгоритм записывает данные по кругу.
# Например, для трёх файлов и текста «Программирование» данные распределяются так:
#
# Файл data-1.txt: «Пгмрае». Файл data-2.txt: «ррмон» . data-3.txt: «оаиви» .
#
# Напишите программу, которая из первого аргумента командной строки принимает количество файлов,
# которые были использованы для записи, а из второго количество символов, которе нужно из них прочитать.
# Результатом программа должна вернуть восстановленный текст.
#
# Пример использования (на примере данных из текста условия):
# > python program.py 3 16
# > Программирование
# > python program.py 3 7
# > Програм

import sys
n_files, n_symbols = list(map(int, sys.argv[1:]))

result = []
full_cycles = round(n_symbols / n_files)
rest = n_symbols % n_files

line_symbol_index = 0
for cycles_counter in range(1, full_cycles + 1):
    for file_index in range(1, n_files + 1):
        for line in open(f"data-{file_index}.txt", "r", encoding="utf-8"):
            if line_symbol_index < len(line):
                result.append(line[line_symbol_index])
    line_symbol_index += 1
    file_index = 1

for file_index in range(1, rest + 1):
        for line in open(f"data-{file_index}.txt", "r", encoding="utf-8"):
            result.append(line[line_symbol_index])
print("".join(result))


# import sys
# n_files, n_symbols = list(map(int, sys.argv[1:]))
#
# result = []
# full_cycles = round(n_symbols / n_files)
# rest = n_symbols % n_files
#
# line_symbol_index = 0
# cycles_counter = 1
# while cycles_counter <= full_cycles:
#     for file_index in range(1, n_files + 1):
#         for line in open(f"data-{file_index}.txt", "r", encoding="utf-8"):
#             if line_symbol_index < len(line):
#                 result.append(line[line_symbol_index])
#     line_symbol_index += 1
#     file_index = 1
#     cycles_counter += 1
#
# for file_index in range(1, rest + 1):
#         for line in open(f"data-{file_index}.txt", "r", encoding="utf-8"):
#             result.append(line[line_symbol_index])
# print("".join(result))