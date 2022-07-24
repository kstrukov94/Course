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
    # print(list(user.items()))
    for user_data in list(user.items()):
            print(user_data)

            # if user_data[0] == str_email.lower():
            #     if user_data[1] == str_password:
            #         print("Доступ открыт")
            #         i += 1
            #         break
            #     else:
            #         print("Доступ закрыт")
            #         i += 1
            #         break
if not i:
    print("Пользователь не найден")




