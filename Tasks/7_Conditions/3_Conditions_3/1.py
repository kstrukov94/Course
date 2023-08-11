"""СОЗДАЕМ ФАЙЛ"""
# При создании новых файлов в PyCharm, мы можем выбрать его тип (например, Python file), а также указать название:
#
# 1. Если указать название файла без расширения, то PyCharm добавит расширение на основе типа.
# Например, для типа "Python file", файл с названием "program" будет сохранен как "program.py".
#
# 2. Если указать название файла с расширением, то PyCharm не будет добавлять расширение на основе типа.
# Например, для типа "Python file" файл с названием "program.py" будет сохранен как "program.py",
# а файл "file.html" будет сохранен как "file.html.py" (добавляем расширение .py, так как изначально было .html).
#
# Напишите программу, которая принимает из аргументов командной строки два параметра, расширение,
# которое привязано к типу, а также имя файла, которое ввел пользователь.
#
# Программа должна сформировать финальное имя файла, которое будет использоваться для сохранения.
#
# Пример использования:
# > python program.py .py filename
# > filename.py
# > python program.py .py filename.py
# > filename.py

import sys
file_ext, file_name = sys.argv[1:]
# file_ext, file_name = ".html", "html.html"
if file_name.endswith(file_ext):
    file_ext = ""
print(f"{file_name}{file_ext}")

# import sys
#
# # Получаем данные
# ext = sys.argv[1]
# filename = sys.argv[2]
#
# if not filename.endswith(ext):
#     filename += ext
#
# print(filename)