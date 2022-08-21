# ЧПУ
# ЧПУ — на языке web-разработчиков означает «Человекопонятный URL», такой вид адреса интернет-страницы,
# когда вместо идентификаторов используются понятные слова, записанные особым образом.
# Как правило ЧПУ адреса записываются в нижнем регистре с заменой пробелов черточками.
#
# Например для статьи с названием «Intro to the Python Walrus Operator»,
# ЧПУ может быть таким: intro-to-the-python-walrus-operator.
#
# Напишите программу, которая первым аргументом командной строки получает название статьи,
# а после выводит для неё ЧПУ. При выводе нужно учитывать следующие правила:
#
# Пробелы должны заменяться на черточки (-).
# Если подряд стоит несколько пробелов, то черточка должна быть одна. +
# Все слова должны быть приведены к нижнему регистру +
# Точки, запятые, восклицательные и вопросительные знаки, двоеточия, а также точки с запятыми должны быть удалены. +
# Пример использования
# > python program.py "Intro? to the! Python Walrus Operator"
# > intro-to-the-python-walrus-operator

import sys
url = sys.argv[1]
url_list = url.lower().replace(".", " ").replace(",", " ").replace("!", " ")\
    .replace("?", " ").replace(":", " ").replace(";", " ").split()

url_new = "-".join(url_list)
print(url_new)