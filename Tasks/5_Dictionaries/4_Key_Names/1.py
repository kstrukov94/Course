# ОЛЕГ ИВАНОВ
# Начинающий разработчик написал программу, которая принимает первым аргументом командной строки ключ словаря user,
# а затем выводит значение этого словаря.
# Однако что-то пошло не так и программа не работает. Исправьте все ошибки.
#
# Пример использования:
# > python program.py last_name
# > Иванов
# import sys
#
# key = sys.argv[0]
#
# user = {
#     first_name: 'Олег',
#     'last_name': 'Иванов',
#     'last_name': 'Петров',
#     age: 28
# }
#
# print(users['key'])


import sys

key = sys.argv[1]

user = {
    'first_name': 'Олег',
    'last_name': 'Иванов',
    'age': 28
}

print(user[key])