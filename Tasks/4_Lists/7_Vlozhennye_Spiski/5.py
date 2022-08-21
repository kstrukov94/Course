# РАСШИРЯЕМ СПИСОК
# Ниже содержится список products с товарами разбитыми по категориям. Каждая категория товаров помещена в отдельный вложенный список.
#
# Напишите программу, которая принимает из аргументов командной строки список товаров и помещает его как вложенный список в products,
# а после выводит конечную последовательность.
#
# Пример использования:
# > python program.py яблоки груши
# > [['молоко', 'кефир'], ['котлеты', 'курица', 'говядина'], ['яблоки', 'груши']]


import sys

products = [
    ["молоко", "кефир"],  # молочка
    ["котлеты", "курица", "говядина"]  # мясо
]

new_list = sys.argv[1:]
products.append(new_list)
print(products)