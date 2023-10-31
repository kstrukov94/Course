"""ЦЕЛЕВАЯ АУДИТОРИЯ"""
# Сайт предназначен для мужчин от 20 до 30 лет включительно.
# Отфильтруйте список people, чтобы в нем осталась только целевая аудитория сайта.
#
# Результат должен быть помещен в переменную my_people.

people = [
    {"sex": "m", "age": 12},
    {"sex": "w", "age": 12},
    {"sex": "m", "age": 15},
    {"sex": "m", "age": 20},
    {"sex": "m", "age": 13},
    {"sex": "m", "age": 27},
    {"sex": "w", "age": 31},
    {"sex": "m", "age": 17},
    {"sex": "w", "age": 17},
    {"sex": "m", "age": 12},
    {"sex": "m", "age": 42},
    {"sex": "w", "age": 25}
]


def men_20_30(d):
    return d["sex"] == "m" and d["age"] in range(20, 30)


my_people = filter(men_20_30, people)

print(my_people)
