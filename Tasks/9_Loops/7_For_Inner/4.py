"""НЕАКТИВНЫЕ ПРОГРАММИСТЫ"""
# В редакторе ниже содержится список программистов. Каждый программист представлен словарем из трёх элементов: id, языки (langs) и активность (active).
# Обратите внимание, что языки — это список языков, на которых разработчик программирует.
#
# Напишите программу, которая получает из первого аргумента командной строки название языка программирования,
# а затем выводит идентификаторы неактивных программистов, которые пишут на переданном языке.
# Идентификаторы нужно выводить в том порядке, в котором они стоят в списке users (дополнительная сортировка не нужна).
# Идентификаторы нужно разделять запятыми.
#
# Пример использования:
# > python program.py python
# > 17, 481

users = [
    {"id": 17,  "active": False, "langs": ["python", "javascript"]},
    {"id": 156, "active": True,  "langs": ["php"]},
    {"id": 23,  "active": True,  "langs": ["java", "c++"]},
    {"id": 84,  "active": True,  "langs": ["python", "c++"]},
    {"id": 28,  "active": False, "langs": ["java", "php"]},
    {"id": 21,  "active": True,  "langs": ["java", "javascript"]},
    {"id": 55,  "active": True,  "langs": ["python", "c#"]},
    {"id": 88,  "active": True,  "langs": []},
    {"id": 287, "active": False, "langs": ["c++", "c#", "java"]},
    {"id": 481, "active": False, "langs": ["php", "javascript", "python"]},
    {"id": 134, "active": True,  "langs": ["c++", "python"]},
    {"id": 65,  "active": True,  "langs": ["php", "python"]},
    {"id": 7,  "active": False,  "langs": ["javascript", "c#"]}
]

import sys
lang = sys.argv[1]

found_ids = []

for user in users:
    if lang in user["langs"] and not user["active"]:
        found_ids.append(user["id"])
i = 0
for this_id in found_ids:
    found_ids[i] = str(found_ids[i])
    i += 1
print(", ".join(found_ids))



