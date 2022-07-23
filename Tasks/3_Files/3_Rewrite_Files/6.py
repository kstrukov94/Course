# Рядом с программой находится файл products.txt в кодировке cp1251.
# Напишите программу, которая перекодирует его в кодировку utf-8.
#
# После того как программа выполнится, система сама откроет файл products.txt и проверит его содержимое.
file = open("6_products.txt", "r", encoding="cp1251")
products = file.read()
file.close()
file = open("6_products.txt", "w", encoding="utf8")
file.write(products)
file.close()