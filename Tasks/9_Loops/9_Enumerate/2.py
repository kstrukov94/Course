"""ЗАПИСЬ RAID 0"""
# Ранее вы уже создавали программу для чтения данных из массива файлов в соответствии с технологией RAID 0.
# Теперь проведем обратную операцию.
#
# Напишите программу, которая принимает два аргумента: количество файлов, по которым нужно распределить текст и сам текст.
# После программа должна распределить весь текст по файлам по кругу, записывая в каждый файл по одному символу.
# Так, если нам нужно записать текст «Программирование» в три файла, то данные в них распределяются следующим образом:
#
# Файл data-1.txt: «Пгмрае». Файл data-2.txt: «ррмон» . data-3.txt: «оаиви» .
#
# Программа должна только создавать файлы и записывать в них данные. Ничего выводить не нужно.
# Система проверки сама прочитает данные в этих файлах и сравнит с образцом.
#
# Пример использования (на примере данных из текста условия):
# > python program.py 3 "Программирование"

import sys
files_counter, text = int(sys.argv[1]), sys.argv[2]
writing_list = []
# пишем текст в список с 2 уровнями вложенности
for n in range(0, files_counter):
    writing_list.append([])
    for symbol in list(text)[n::files_counter]:
        writing_list[n].append(symbol)
print(writing_list)
# раскидываем каждый из списков по файлам
for n in range(0, files_counter):
    file = open(f"data-{n+1}.txt", "w+", encoding="utf-8")
    file.write("".join(writing_list[n]))
















# # создаем файлы
# for file_index in range(1, n_files + 1):
#     open(f"data-{file_index}.txt", "w", encoding="utf-8")
#
# full_loops = len(text) // n_files
# rest_in_loop = len(text) % n_files

# записываем массивы данных

# for file_index in range(1, n_files + 1):
#     result.append([])
#     for symbol_index, symbol in enumerate(text):
#         result[file_index - 1].append(symbol)

# for file_index in range(1, n_files + 1):
#     result.append([])
#     for symbol_index, symbol in enumerate(text):
#         for symbol_index in range(0, len(text) - 1, n_files - 1):
#             result[file_index - 1].append(symbol)
# print(result)

# symbol_counter = 0
#
# result = []
# symbol_counter = 0
# for loop_counter in range(0, full_loops):
#     result.append([])
#     for symbol_index, symbol in enumerate(text):
#         result[loop_counter].append(symbol)
