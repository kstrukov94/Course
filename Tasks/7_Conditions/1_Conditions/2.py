"""ПРОВЕРКА РЕАЛЬНОГО ПАРОЛЯ"""
# TODO Надо перечитать заново и разобраться с хэшированием md5
# В реальных программах пароли хранят в зашифрованном виде, чтобы в случае утечки их было сложно взломать.
# Когда пользователь пытается авторизоваться на сайте, то его пароль сперва зашифровывается,
# а затем этот шифр сравнивается с зашифрованным паролем в программе или в базе данных.
#
# Простейшая схема шифрования с помощью алгоритма md5* выглядит так:
#
# # Импортируем в программу библиотеку для шифрования.
# import hashlib
#
# # Задаем "сырой" (незашифрованный) пароль.
# raw_password = 'password'
#
# # Кодируем "сырой" пароль.
# # Нужно для того, чтобы воспользоваться md5.
# raw_password = raw_password.encode()
#
# # Получаем шифр-объект.
# hash_password = hashlib.md5(raw_password)
#
# # Получаем зашифрованный пароль.
# hash_password = hash_password.hexdigest()
#
# # Выводим зашифрованный пароль.
# print(hash_password)
# 5f4dcc3b5aa765d61d8327deb882cf99
#
# # Именно строка вида "5f4dcc3b5aa765d61d8327deb882cf99"
# # обычно хранится в программе или базе данных.
# В редакторе ниже в переменной hash_password хранится зашифрованный пароль.
# Напишите программу, которая первым аргументом командной строки принимает "сырой" пароль пользователя,
# а затем, проверяет, верный ли он.
#
# Если переданный пароль верный, то программа должна вывести "Доступ открыт", а если пароль неверный, то "Доступ закрыт".
#
# Пример использования:
# > python program.py admin
# > Доступ закрыт
# Примечание. В настоящий момент алгоритм md5 является небезопасным. Не используйте его в реальных программах.

import sys
import hashlib

hash_password = 'c8b667f4e6953d59b6ae9b9659772333'

raw_password = sys.argv[1]
raw_password = raw_password.encode()
hash_user_password = hashlib.md5(raw_password)
hash_user_password = hash_user_password.hexdigest()

if raw_password == hash_password:
    print("Доступ открыт")
else:
    print("Доступ закрыт")
