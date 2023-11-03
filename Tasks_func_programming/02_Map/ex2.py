"""ТОЛЬКО ЧИСЛА"""
# В списке digits содержатся строки с числами.
# Эти строки содержат ошибки: лишние пробелы, а также неправильные разделители целой и десятичной части.
#
# Создайте функцию, которая сначала исправит ошибки в строках, а затем преобразует каждую строку в вещественное число.
# Примените эту функцию ко всем элементам digits с помощью map.

digits = ["12", "145", "  45", "12.4", "45,14", "15 645"]


def clean_nums(number_str: str):
    return float(number_str.replace(",", ".").replace(" ", ""))


right_digits = map(float, map(clean_nums, digits))

print(list(right_digits))


def clean_num_old(num: str):
    return num.replace(",", ".").replace(" ", "")