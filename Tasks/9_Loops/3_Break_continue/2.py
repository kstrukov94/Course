"""ПОИСК ПОЛЬЗОВАТЕЛЯ"""
# В редакторе ниже содержится список пользователей.
# Каждый пользователь представлен словарем из трёх ключей: user_id, first_name и last_name.
# Напишите программу, которая получает user_id пользователя из первого аргумента командной строки, а затем выводит его имя и фамилию.
#
# Программа гарантированно будет получать только те user_id, которые есть в списке.
#
# Пример использования:
# > python program.py 156
# > Виктор Осипов

users = [
    {"user_id": 17, "first_name": "Дмитрий", "last_name": "Иванов"},
    {"user_id": 156, "first_name": "Виктор", "last_name": "Осипов"},
    {"user_id": 23, "first_name": "Алёна", "last_name": "Гордеева"},
    {"user_id": 84, "first_name": "Семён", "last_name": "Васильев"},
    {"user_id": 21, "first_name": "София", "last_name": "Зинько"},
    {"user_id": 55, "first_name": "Антон", "last_name": "Ватутин"},
    {"user_id": 287, "first_name": "Виталий", "last_name": "Новиков"}
]

import sys

user_id = int(sys.argv[1])
users_index = 0
while users_index < len(users):
    if user_id == users[users_index].get("user_id"):
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
#     # Проверяем user_id
#     if user["user_id"] == user_id:
#         # Выводим данные.
#         print("{} {}".format(user["first_name"], user["last_name"]))
#
#         # Завершаем цикл.
#         # Если его не завершить, то программа будет выполнять лишние итерации.
#         break
#
#     i += 1