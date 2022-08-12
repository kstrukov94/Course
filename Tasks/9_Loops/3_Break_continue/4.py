"""ПЕРВЫЙ АКТИВНЫЙ ПРОГРАММИСТ"""
# В редакторе ниже содержится список программистов.
# Каждый программист представлен словарем из трёх элементов: id, язык (lang) и активность (active).
#
# Напишите программу, которая получает из первого аргумента командной строки название языка программирования,
# а затем выводит id первого активного программиста, который пишет на переданном языке.
#
# Программа гарантированно будет получать только те названия языков, которые есть в списке.
#
# Пример использования:
# > python program.py python
# > 84

users = [
    {"id": 17,  "lang": "python", "active": False},
    {"id": 156, "lang": "php",    "active": True},
    {"id": 23,  "lang": "java",   "active": True},
    {"id": 84,  "lang": "python", "active": True},
    {"id": 21,  "lang": "java",   "active": False},
    {"id": 55,  "lang": "python", "active": True},
    {"id": 88,  "lang": "python", "active": True},
    {"id": 287, "lang": "c++",    "active": False},
    {"id": 481, "lang": "php",    "active": False},
    {"id": 134, "lang": "c++",    "active": True}
]

import sys
lang_to_find = sys.argv[1]

i = 0
while i < len(users):
    if users[i].get("lang") == lang_to_find and users[i].get("active") == 1:
        print("{}".format(users[i].get("id")))
        break
    i += 1

# i = 0
# # Перебираем всех программистов
# while i < len(users):
#     # Получаем данные очередного программиста.
#     user = users[i]
#
#     # Проверяем языки и активность.
#     if user["lang"] == lang and user["active"]:
#         # Выводим данные и завершаем цикл.
#         print(user["id"])
#         break
#
#     i += 1