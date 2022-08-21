"""ПЕРВЫЙ ПОДХОДЯЩИЙ ПРОГРАММИСТ"""
# В редакторе ниже содержится список программистов.
# Каждый программист представлен словарем и одним из ключей является lang, который хранит информацию о языке, с которым работает разработчик.
#
# Напишите программу, которая получает из первого аргумента командной строки название языка программирования,
# а затем выводит имя и фамилию первого программиста, который на нем пишет.
#
# Программа гарантированно будет получать только те названия языков, которые есть в списке.
#
# Пример использования:
# > python program.py java
# > Алёна Гордеева

users = [
    {"id": 17, "first_name": "Дмитрий", "last_name": "Иванов", "lang": "python"},
    {"id": 156, "first_name": "Виктор", "last_name": "Осипов", "lang": "php"},
    {"id": 23, "first_name": "Алёна", "last_name": "Гордеева", "lang": "java"},
    {"id": 84, "first_name": "Семён", "last_name": "Васильев", "lang": "python"},
    {"id": 21, "first_name": "София", "last_name": "Зинько", "lang": "java"},
    {"id": 55, "first_name": "Антон", "last_name": "Ватутин", "lang": "python"},
    {"id": 287, "first_name": "Виталий", "last_name": "Новиков", "lang": "c++"}
]

import sys
lang_to_find = sys.argv[1]

i = 0
while i < len(users):
    if users[i].get("lang") == lang_to_find:
        print("{} {}".format(users[i].get("first_name"), users[i].get("last_name")))
        break
    i += 1