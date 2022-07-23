# Рядом с программой находится файл template.txt, в котором хранится шаблон текста.
# В шаблоне есть текст вида {{ name }}, который нужно заменить на реальное имя пользователя.
#
# Напишите программу, которая принимает из первого аргумента командной строки имя пользователя, а затем подставляет его в шаблон и записывает результат в файл.
#
# После того как программа выполнится, система сама откроет файл template.txt и проверит его содержимое.

import sys
name = sys.argv[1]
file = open("2_template.txt", "r", encoding="utf8")
string = file.read()
file.close()
print("до изменений " + string)
string = string.replace("{{ name }}", name)
print("после изменений " + string)
file = open("2_template.txt", "w", encoding="utf8")
file.write(string)
file.close()