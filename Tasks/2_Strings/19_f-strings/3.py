"""ФОРМИРУЕМ URL"""
# Если вы решите поискать на сайте auto.ru автомобиль Audi A6 выпуска 2018 и позже,
# то сайт сформирует следующий URL адрес: https://auto.ru/cars/audi/a6/all/?year_from=2018
# - жирным шрифтом выделены ключевые параметры поиска.
#
# Напишите программу, которая получает из аргументов командной строки три параметра:
# марку, модель и год, а затем на базе них формирует URL-адрес по аналогии с примером выше.
#
# Марка и модель могу быть переданы в любом регистре, но в адресе они должны быть в нижнем.
# Если марка или модель содержат пробелы, то их надо заменить на подчеркивания.
#
# Пример использования:
# > python program.py Audi A6 2018
# > https://auto.ru/cars/audi/a6/all/?year_from=2018

import sys

a_tm, a_model, a_year = list(sys.argv[1:])
a_tm = a_tm.lower().replace(" ", "_")
a_model = a_model.lower().replace(" ", "_")
string_template = f"https://auto.ru/cars/{a_tm}/{a_model}/all/?year_from={a_year}"
print(string_template)

