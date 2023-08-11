"""ИСПРАВЛЯЕМ ШАБЛОН"""
# Начинающий программист написал программу для вывода данных о товаре.
# Однако он допустил несколько ошибок в шаблоне строки и программа теперь не запускается.
# Исправьте шаблон product_template, чтобы программа выводила данные как в примере ниже.
#
# Пример использования:
# > python program.py Garmin Часы 6990
# > Garmin (Часы), 6990 руб.

import sys

# Получаем данные.
name = sys.argv[1]
category = sys.argv[2]
price = sys.argv[3]

# Формируем словарь.
product = {
   "name": name,
   "category": category,
   "price": price
}

product_template = "{product[name]} ({product[category]}), {product[price]} руб."

# Форматируем строку данными из словаря.
print(product_template.format(product=product))