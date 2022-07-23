# Рядом с программой находится файл language.txt, в котором содержится текст в кодировке cp1251.
# Напишите программу, которая читает файл и выводит его содержимое.
#
# Пример использования в командной строке Windows:
# > python program.py
# > English

import sys
language_file = open(sys.argv[1], encoding="cp1251")
text = language_file.read()
print(text)
