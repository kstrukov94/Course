"""#85: МНОЖЕСТВЕННОЕ ЧИСЛО"""
# Сложность: 2 из 10
# В русском языке, если нужно рассказать о нескольких предметах, люди используют множественное число.
# В зависимости от количества предметов, форма существительного после числа может меняться.
#
# Например, один ананас, два ананаса, пять ананасов.
# Как видите, количество предметов меняется (один, два, пять) и у слова ананас изменяется окончание (ананас, ананаса, ананасов).
#
# Напишите функцию choose_plural, которая принимает два аргумента:
# целое число (количество предметов) и строку содержащую три слова разделенных запятыми,
# которые представляют собой формы множественного числа.
#
# Функция должна возвращать правильную форму множественного числа в зависимости от переданного первым аргументом значения.
#
# Пример использования функции:
# print(choose_plural(7, "ананас,ананаса,ананасов"))
# ананасов
# print(choose_plural(21, "ананас,ананаса,ананасов"))
# ананас

# 1, 21, 31 ... 101, 121, ... - ананас
# 2 - 4, 22 - 24, 32 - 34 ... - ананаса
# 5 - 20, 25 - 30, 35 - 40 ... - ананасов


def choose_plural(number: int, forms: str) -> str:
    forms_list = forms.split(',')
    num_str = str(number)
    last1 = num_str[-1]
    last2 = num_str[-2:]
    if len(num_str) == 1:
        if num_str in '234':
            return forms_list[1]
        elif num_str in '56789':
            return forms_list[2]
        else:
            return forms_list[0]
    # [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    if len(num_str) > 1:
        if int(last2) in range(10, 21) or last2 == '00':
            return forms_list[2]
        elif int(last1) in range(2, 5):
            return forms_list[1]
        elif int(last1) in range(6, 10):
            return forms_list[2]
        else:
            return forms_list[0]


print(choose_plural(100, "ананас,ананаса,ананасов"))


def choose_plural(amount, variants):
    # Разбиваем варианты
    variants = variants.split(",")

    # Далее просто вычисляем последние 2 цифры и в зависимости
    # от результата выбираем variant
    if amount % 10 == 1 and amount % 100 != 11:
        variant = 0
    elif amount % 10 >= 2 and amount % 10 <= 4 and \
         (amount % 100 < 10 or amount % 100 >= 20):
        variant = 1
    else:
        variant = 2

    return variants[variant]