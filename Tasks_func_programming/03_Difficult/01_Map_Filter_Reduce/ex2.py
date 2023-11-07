"""#123: СОБСТВЕННАЯ ФУНКЦИЯ MAP"""
"""Сложность: 5 из 10
Создайте функцию mymap, которая будет работать так же как и оригинальная map, но возвращать список.

Учитывайте, что map может принимать сразу несколько последовательностей.

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result)) # [5, 7, 9] 1 + 4, 2 + 5, 3 + 6
Если последовательности имеют разную длину, то за основную будет браться самая короткая.

numbers1 = [1, 2, 3]
numbers2 = [4, 5]

result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result)) # [5, 7] 1 + 4, 2 + 5"""


def mymap(func, *lists) -> list:
    return [func(*args) for args in zip(*lists)]


# установочные данные для проверок
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6, 7]
numbers3 = [1, 2, 3]
numbers4 = [4, 5]

#TODO изучить код подробно

# проверки
# print(mymap(int, ["1", "2", "3"]))
# print(mymap(lambda x, y, z: x * y * z, [1, 2, 3, 4], [5, 6], numbers3))

