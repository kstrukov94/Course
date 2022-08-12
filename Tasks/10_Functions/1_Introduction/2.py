"""ДЛИННАЯ ЛИНИЯ"""
# Создайте функцию line, которая принимает атрибут length и возвращает строку из черточек -, повторенных lenght раз.
#
# Пример использования такой функции:
# print(line(15))
# ---------------

def line(length):
    if type(length) == str and length.isdigit():
        length = int(length)
    if type(length) not in [int, float]:
        return TypeError
    return "-" * length
print(line(10))
