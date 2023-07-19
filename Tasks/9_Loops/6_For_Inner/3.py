"""СПИСОК ПОДХОДЯЩИХ ПРОГРАММИСТОВ"""
# В редакторе ниже содержится список программистов.
# Каждый программист представлен словарем из трёх элементов: user_id, язык (lang) и активность (active).
#
# Напишите программу, которая получает из первого аргумента командной строки название языка программирования, а
# затем выводит идентификаторы активных программистов, которые пишут на переданном языке.
# Идентификаторы должны быть отсортированы в порядке возрастания и разделены запятыми.
#
# Программа гарантированно будет получать только те названия языков, которые есть в списке.
#
# Пример использования:
# > python program.py python
# > 55, 84, 88

users = [
    {"user_id": 17,  "lang": "python", "active": False},
    {"user_id": 156, "lang": "php",    "active": True},
    {"user_id": 23,  "lang": "java",   "active": True},
    {"user_id": 84,  "lang": "python", "active": True},
    {"user_id": 28,  "lang": "java",   "active": False},
    {"user_id": 21,  "lang": "java",   "active": True},
    {"user_id": 55,  "lang": "python", "active": True},
    {"user_id": 88,  "lang": "python", "active": True},
    {"user_id": 287, "lang": "c++",    "active": False},
    {"user_id": 481, "lang": "php",    "active": False},
    {"user_id": 134, "lang": "c++",    "active": True},
    {"user_id": 65, "lang": "php",    "active": True},
]

import sys
lang = sys.argv[1]

result_ids = []

for user in users:
    if user["lang"] == lang and user["active"]:
        result_ids.append(user["user_id"])
result_ids.sort()
i = 0
for this_id in result_ids:
    result_ids[i] = str(this_id)
    i += 1
print(", ".join(result_ids))






