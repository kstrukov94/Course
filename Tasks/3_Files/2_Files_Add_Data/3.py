# Рядом с программой находятся два файла: products.txt и new_products.txt.
# Первый сохранен в кодировке cp1251, а второй в koi8-r.
#
# Напишите программу, которая копирует список продуктов из файла new_products.txt в products.txt.
# Все товары в  исходных файлах записаны с новой строки, при этом после последней записи также стоит перевод строки.
#
# Пример запуска программы:
# > python program.py
# После того как программа выполнится, система сама откроет файл products.txt и проверит его содержимое.

new_products_file = open("3_new_products.txt", encoding="koi8-r")
products_add = new_products_file.read()
new_products_file.close()
products_file = open("3_products.txt", "a", encoding="cp1251")
products_file.write(products_add)
products_file.close()


# # Открываем файл на дозапись.
# products_file = open("products.txt", "a", encoding="cp1251")
#
# # Открыаем файл на чтение
# new_products_file = open("new_products.txt", "r", encoding="koi8-r")
#
# # Получаем новые товары.
# new_products = new_products_file.read()
#
# # Записываем новые товары в файл.
# products_file.write(new_products)