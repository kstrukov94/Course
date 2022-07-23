# Напишите программу, которая создает файл index.html и добавляет в него следующую строку:
# <html><head></head><body></body></html>.
#
# После того как программа выполнится, система сама откроет файл index.html и проверит его содержимое.

file = open("1_index.html", "w", encoding="utf8")
file.write("<html><head></head><body></body></html>")
file.close()