"""АВТОРИЗАЦИЯ ПО EMAIL"""
# В редакторе ниже находится список users, состоящий из словарей. Каждый словарь содержит email и пароль пользователя.
#
# Напишите программу, которая первым аргументом командной строки принимает email пользователя, а вторым — его пароль.
# Далее программа должна проверить переданные данные и вывести "Доступ открыт" если пароль верный
# и "Доступ закрыт" если пароль ошибочный.
#
# Если пользователя, который передается в программу, в списке нет, то нужно вывести "Пользователь не найден".
# Обратите внимание, что email может передаваться в программу в любом регистре, но в словаре он всегда хранится в нижнем.
#
# Пример использования:
# > python program.py User2@domain.com abcde
# > Доступ открыт

users = [
    {"email": "user1@domain.com", "password": "password1"},
    {"email": "user2@domain.com", "password": "abcde"},
    {"email": "user3@domain.com", "password": "123456"},
    {"email": "user4@domain.com", "password": "lovelove"},
    {"email": "user5@domain.com", "password": "kdmUdmk84M"},
    {"email": "user7@domain.com", "password": "123456"},
    {"email": "user8@domain.com", "password": "123456"},
    {"email": "user9@mail.com.ru", "password": "password9"}
]

import sys
str_email, str_password = sys.argv[1:]
i = 0
for user in users:
    if user["email"] == str(str_email).lower():
        if user["password"] == str_password:
            print("Доступ открыт")
            break
        else:
            print("Доступ закрыт")
            break
    i += 1
if i == len(users):
    print("Пользователь не найден")


# import sys
#
# # Получаем данные пользователя.
# email = sys.argv[1].lower()
# password = sys.argv[2]
#
# # Задаем доступ: None - пользователь не найден, True - доступ есть, False - доступа нет.
# has_access = None
#
# # Перебираем всех пользователей в цикле:
# for user in users:
#     if user["email"] == email:
#         if user["password"] == password:
#             has_access = True
#         else:
#             has_access = False
#
#         break
#
# # Выводим результат.
# if has_access is None:
#     print("Пользователь не найден")
# elif has_access:
#     print("Доступ открыт")
# else:
#     print("Доступ закрыт")



