"""ЦЕЛЬСИИ В ФАРЕНГЕЙТЫ"""
# Напишите функцию c_to_f, которая принимает один аргумент — градусы по Цельсию и возвращает градусы по Фаренгейту.
# Результат должен быть вещественным числом, округленным до одного знака после десятичной точки.
#
# Пример использования функции:
# result = c_to_f(0)
# print(result)
# 32.0

def c_to_f(degree_c):
    template = "{result:.1f}"
    if type(degree_c) == str and degree_c.isdigit():
        degree_c = float(degree_c)
    if type(degree_c) not in [int,float]:
        return TypeError
    return round(degree_c * 9 / 5 + 32, 1)

print(c_to_f(36.6))
