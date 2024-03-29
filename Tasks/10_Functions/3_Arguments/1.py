"""БУХГАЛТЕРСКИЙ СТИЛЬ ЗАПИСИ"""


# Напишите функцию buh(), которая принимает целое число, а затем возвращает строку,
# в которой переданное число записано в бухгалтерском стиле:
#
# Цифры разделены пробелами на классы единиц, тысяч, миллионов и тд;
# Отрицательные числа записаны без знака «минус», но в скобках.
# Пример вызова функции:
# result = buh(987)
# print(result)
# 987
# result = buh(-1987)
# print(result)
# (1 987)

# Напишите вашу функцию тут

def buh(num):
    result = f'{num:,}'.replace(',', ' ')
    if result[0] == '-':
        result = f'({result.lstrip("-")})'
    return result


# Не удаляйте строки нижи, они нужны для проверки вашей функции
import sys

print(buh(int(sys.argv[1])))
