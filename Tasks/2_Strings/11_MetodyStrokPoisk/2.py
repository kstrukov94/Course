# Напишите программу, которая получает из первого аргумента командной строки HTML-текст,
# а после извлекает из него содержание <H1>-заголовка.
# <p>текст</p><h1>Заголовок</h1><p>еще текст</p>

import sys
text = sys.argv[1]
header_start = text.find("<h1>") + 4
header_end = text.find("</h1>")
print(text[header_start:header_end])
