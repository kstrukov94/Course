"""СПИСОК ПОДХОДЯЩИХ ПРОГРАММИСТОВ"""
# В редакторе ниже содержится список программистов.
# Каждый программист представлен словарем из трёх элементов: id, язык (lang) и активность (active).
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
    {"id": 17,  "lang": "python", "active": False},
    {"id": 156, "lang": "php",    "active": True},
    {"id": 23,  "lang": "java",   "active": True},
    {"id": 84,  "lang": "python", "active": True},
    {"id": 28,  "lang": "java",   "active": False},
    {"id": 21,  "lang": "java",   "active": True},
    {"id": 55,  "lang": "python", "active": True},
    {"id": 88,  "lang": "python", "active": True},
    {"id": 287, "lang": "c++",    "active": False},
    {"id": 481, "lang": "php",    "active": False},
    {"id": 134, "lang": "c++",    "active": True},
    {"id": 65, "lang": "php",    "active": True},
]

import sys
lang = sys.argv[1]

result_ids = []

for user in users:
    if user["lang"] == lang and user["active"]:
        result_ids.append(user["id"])
result_ids.sort()
i = 0
for this_id in result_ids:
    result_ids[i] = str(this_id)
    i += 1
print(", ".join(result_ids))






