# Рядом с программой находится файл template.txt, в котором хранится шаблон текста.
# В шаблоне есть текст вида {{ name }}, который нужно заменить на реальное имя пользователя.
#
# Напишите программу, которая принимает из первого аргумента командной строки имя пользователя, а затем подставляет его в шаблон и выводит результат.
#
# Если в файле будет содержаться «Привет, {{ name }}!», то программа должна отработать так:
#
# > python program.py Никита
# > Привет, Никита!

import sys
username = sys.argv[1]
file = open("4_template.txt", encoding="utf8")
text = file.read().replace("{{ name }}", str(username))
print(text)
