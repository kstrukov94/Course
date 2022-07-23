# Рядом с программой находится файл book.txt, в котором содержится название книги.
# Напишите программу, которая читает файл и выводит его содержимое.
#
# Пример использования в командной строке Windows:
# > python program.py
# > Название книги

import sys
filename = sys.argv[1]
book_file = open(filename, encoding="utf8")
text = book_file.read()
print(text)
