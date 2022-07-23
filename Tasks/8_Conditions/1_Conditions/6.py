"""ПРОВЕРКА ДЛИНЫ ПАРОЛЯ"""
# В переменной password содержится пароль введенный пользователем.
# Выведите фразу «Пароль слишком короткий» (без кавычек),
# если длина пароля меньше 6 символов и фразу «Пароль подходит» в противном случае.

import sys
password = sys.argv[1]

if len(password) >= 6:
    print("Пароль подходит")
else:
    print("Пароль слишком короткий")

