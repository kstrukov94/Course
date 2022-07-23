"""ПРОВЕРКА ДЛИНЫ ПАРОЛЯ, ЧАСТЬ 2_Strings"""
# В переменной password содержится пароль введенный пользователем.
# Выведите фразу «Пароль слишком короткий» (без кавычек), если длина пароля меньше 6 символов.
# Если длина от 6 до 8 символов, то выведите «Хорошо, но можно и лучше».
# Если длина более 8 символов — «Пароль подходит».

import sys
password = sys.argv[1]

if len(password) > 8:
    print("Пароль подходит")
elif len(password) >= 6:
    print("Хорошо, но можно и лучше")
else:
    print("Пароль слишком короткий")

# # Используем функцию len()
# if len(password) < 6:
#     print("Пароль слишком короткий")
# # Используем метод __len__()
# elif password.__len__() <= 8:
#     print("Хорошо, но можно и лучше")
# else:
#     print("Пароль подходит")
#
# # Функция len() и метод __len__() равнозначны