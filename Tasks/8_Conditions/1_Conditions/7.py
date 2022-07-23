"""НОВЫЙ ТОВАР"""
# Чтобы проверить, есть ли в списке элемент, нужно воспользоваться оператором in или not in:
#
# values = [1, 2_Strings, 3_Files, 5, 8, 13]
# print(1 in values)
# True
# print(4 in values)
# False
# print(1 not in values)
# False
# print(4 not in values)
# True
# Так как оператор in возвращает True или False, то всё выражение value in values можно использовать в условиях:
#
# if value in values:
#     ...
# В редакторе ниже находится список products с товарами.
# Напишите программу, которая первым аргументом командной строки принимает название товара,
# а затем, если переданного товара в списке нет, то добавляет его туда. Если переданный товар уже есть в списке, то ничего делать не надо.
#
# В конце программа должна отсортировать список и вывести все товары через запятую с пробелом.
#
# Пример использования:
# > python program.py Огурцы
# > Масло, Молоко, Овсянка, Огурцы, Хлеб, Яйца

products = ["Молоко", "Масло", "Хлеб", "Овсянка", "Яйца"]

import sys
product = sys.argv[1]
if product not in products:
    products.append(product)
products.sort()
print(", ".join(products))