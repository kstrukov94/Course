"""ЛОГИН / ПАРОЛЬ"""
# Программа ниже уже полностью готова. Перепишите её с использованием f-строк:
#
# Пример использования:
# > python program.py user user@domain.com 123456
# > Логин: user
# > E-mail: user@domain.com
# > Пароль: ******

import sys

# Получаем данные аккаунта
login = sys.argv[1]
email = sys.argv[2]
password = sys.argv[3]

# Формируем строку
# info = "Логин: {login}\n".format(login=login) + \
#        "E-mail: {e}\nПароль: {p}".format(e=email, p='*' * len(password))

info = f"Логин: {login}\nE-mail: {email}\nПароль: {'*' * len(password)}"

print(info)


