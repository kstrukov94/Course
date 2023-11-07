"""#291: MAPS"""
"""Сложность: 6 из 10
Оригинальная map позволяет применять только одну функцию к элементам последовательности. 
Однако часто нужно применить сразу несколько map подряд.

Напишите функцию maps, которая может принимать несколько функций. 
Функции должны применяться к последовательности в порядке их следования. 
Последним аргументом должна идти сама последовательность.

Пример использования
original_tags = [" python", "SQL", " PHP "]
tags = maps(str.strip, str.lower, original_tags)
# После выполнения кода в переменной tags будет список ["python", "sql", "php"]
"""
from functools import reduce


# решение в лоб
def maps(*args):
    obj = args[-1]
    result = []
    for o in obj:
        for func in args[:-1]:
            o = func(o)
        result.append(o)
    return result


# решение преподавателя
def maps2(*args):
    funcs, obj = args[:-1], args[-1]
    for func in funcs:
        obj = map(func, obj)
    return list(obj)


# решение "изящное" через генератр
# TODO доделоть через генератор

# def maps3(*args):
#     funcs, obj = args[:-1], args[-1]
#     return [func(o) for func in funcs for o in obj]

# original_tags = [" python", "SQL", " PHP "]
# print(maps(str.strip, str.lower, original_tags))
# print(maps2(str.strip, str.lower, original_tags))
# print(maps3(str.strip, str.lower, original_tags))
