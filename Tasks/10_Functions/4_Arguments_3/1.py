"""ДЛИННАЯ ЛИНИЯ, 2"""
# Создайте функцию line, которая принимает аргументы fill и length и возвращает строку из символов fill, повторенных lenght раз.
# Если аргумент length не передан, то символы fill должны повторятся 10 раз.
#
# Пример использования такой функции:
# print(line('-', 15))
# ---------------
# print(line('+'))
# ++++++++++

def line(fill, length = 10):
     return str(fill * length)

print(line("-", 3))
