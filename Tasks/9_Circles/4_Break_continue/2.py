"""ПОИСК ПОЛЬЗОВАТЕЛЯ"""
# В редакторе ниже содержится список пользователей.
# Каждый пользователь представлен словарем из трёх ключей: id, first_name и last_name.
# Напишите программу, которая получает id пользователя из первого аргумента командной строки, а затем выводит его имя и фамилию.
#
# Программа гарантированно будет получать только те id, которые есть в списке.
#
# Пример использования:
# > python program.py 156
# > Виктор Осипов

users = [
    {"id": 17, "first_name": "Дмитрий", "last_name": "Иванов"},
    {"id": 156, "first_name": "Виктор", "last_name": "Осипов"},
    {"id": 23, "first_name": "Алёна", "last_name": "Гордеева"},
    {"id": 84, "first_name": "Семён", "last_name": "Васильев"},
    {"id": 21, "first_name": "София", "last_name": "Зинько"},
    {"id": 55, "first_name": "Антон", "last_name": "Ватутин"},
    {"id": 287, "first_name": "Виталий", "last_name": "Новиков"}
]

import sys

user_id = int(sys.argv[1])
users_index = 0
while users_index < len(users):
    if user_id == users[users_index].get("id"):
        print("{} {}".format(users[users_index].get("first_name"), users[users_index].get("last_name")))
        break
    else:
        users_index += 1
        continue

# i = 0  # Переменная-счетчик.
#
# # Перебираем всех пользователей
# while i < len(users):
#     # Получаем данные очередного пользователя.
#     user = users[i]
#
#     # Проверяем id
#     if user["id"] == user_id:
#         # Выводим данные.
#         print("{} {}".format(user["first_name"], user["last_name"]))
#
#         # Завершаем цикл.
#         # Если его не завершить, то программа будет выполнять лишние итерации.
#         break
#
#     i += 1