# Рядом с программой находится файл со списком продуктов products.txt.
# Напишите программу, которая добавляет в этот файл два новых продукта: Масло и Мясо.
# Записи должны добавляться с новой строки каждая.
# В исходном файле продукты также записаны с новой строки, при этом после последней записи перевода строки нет.
#
# Пример запуска программы:
# > python program.py
# После того как программа выполнится, система сама откроет файл products.txt и проверит его содержимое.

products_file = open("1_products.txt", "a", encoding="utf8")
products_file.write("\nМасло\nМясо")