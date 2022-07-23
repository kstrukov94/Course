# СОРТИРОВКА ФАЙЛА
# Рядом с программой находится файл products.txt со списком товаров.
# Каждый товар записан с новой строки.
# Напишите код, который прочитает список товаров из файла, отсортирует его и запишет обратно.
#
# Пример файла до запуска программы и после:
#
# Яблоки
# Бананы
# Виноград
# Груши
# Сливы спелые
# Помидоры
# Ананас
#
# Ананас
# Бананы
# Виноград
# Груши
# Помидоры
# Сливы спелые
# Яблоки
# Пример использования (программа перезаписывает файл и ничего не выводит):
# > python program.py

products_file = open("5_products.txt", encoding="utf8")
products_list = products_file.read().split("\n")
products_list.sort()
products_file.close()
products_file = open("5_products.txt", "w", encoding="utf8")
products_file.write("\n".join(products_list))




