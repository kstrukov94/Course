"""#134: ПЕРЕСЕЧЕНИЕ КРУГОВ
Сложность: 4 из 10
Напишите функцию is_cross, которая принимает два списка.
Каждый из списков содержит по 3 числа – координаты центра круга (x, y) и его радиус (r).

Функция должна возвращать True если круги пересекаются и False в противном случае.

Круги считаются пересекающимися, если у них есть хотя бы одна общая точка.

Иллюстрация к задаче

Пример вызова функции:
result = is_cross([-2, 2, 3], [3, 0, 4])
print(result)
True"""


def is_cross(l1, l2):
    # вычисляем сумму радиусов
    r_sum = l1[2] + l2[2]
    # вычисляем расстояние между точками
    points = ((l1[0] - l2[0]) ** 2 + (l1[1] - l2[1]) ** 2) ** 0.5
    # return True if points <= r_sum else False - более длинный вариант
    return points <= r_sum


# print(is_cross([-2, 2, 3], [3, 0, 4]))