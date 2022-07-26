# НОВЫЕ ТОВАРЫ
# Ниже в редакторе кода содержится список товаров — products.
# Напишите программу, которая принимает из первого аргумента командной строки один параметр — строку продуктов разделенных запятой с пробелом.
# Эти продукты нужно добавить в исходный список, а затем отсортировать его и напечатать.
#
# Пример использования:
# > python program.py "апельсины, ватрушки"
# > ['ананас', 'апельсины', 'ватрушки', 'макароны', 'помидоры', 'яблоки']

products = ["ананас", "макароны", "помидоры", "яблоки"]

import sys
products_new = sys.argv[1].split(", ")
products.extend(products_new)
products.sort(key=str.upper)
print(products)