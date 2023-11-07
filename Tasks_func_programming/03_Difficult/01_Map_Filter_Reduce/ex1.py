"""#126: НОМЕР ТЕЛЕФОНА"""

"""Сложность: 3 из 10
Напишите функцию normalize_phone, которая принимает номер телефона в произвольной форме, 
а затем возвращает строку, которая содержит только цифры этого номера.

Используйте возможности функционального программирования.
Попробуйте записать тело функции в одну строку.

Пример использования:
phone = normalize_phone("+7 (981) 452-79-72")
print(phone)
79814527972"""

from functools import reduce


# решение через join:
# оборачивать в листь нет необходимости, так как join умеет работать с итератором, встроенным в filter
def normalize_phone2(tel_num):
    return "".join(filter(lambda x: x.isdecimal(), tel_num))


# решение через генератор списка:
def normalize_phone3(tel_num):
    return "".join([s for s in tel_num if s.isdecimal()])


# решение через reduce:
def normalize_phone1(tel_num):
    return reduce(lambda a, b: a + b, filter(lambda x: x.isdecimal(), tel_num))


print(normalize_phone1("+7 (981) 452-79-72"))
print(normalize_phone2("+7 (981) 452-79-72"))
print(normalize_phone3("+7 (981) 452-79-72"))
