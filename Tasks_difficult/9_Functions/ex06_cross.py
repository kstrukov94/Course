"""#84: ПЕРЕСЕЧЕНИЕ ПРЯМОУГОЛЬНИКОВ"""
# Сложность: 2 из 10
# Напишите функцию is_cross, которая принимает два списка.
# Каждый из списков содержит по 4 числа – координаты левого верхнего (x1, y1) и правого нижнего (x2, y2) углов прямоугольника.
#
# Функция должна возвращать True если прямоугольники пересекаются и False в противном случае.
#
# Прямоугольники считаются пересекающимися, если у них есть хотя бы одна общая точка.
# Под точками прямоугольника следует понимать не только вершины и точки находящиеся на отрезках соединяющих вершины.
# Но и все точки, которые лежат внутри прямоугольника.
#
# Стороны прямоугольников параллельны осям координат.

# Пример вызова функции:
# result = is_cross([-5, 2, 3,-2], [2, 6, 5, 1])
# print(result)
# True

def is_cross(rectangle1, rectangle2):
    if max(rectangle1[1], rectangle1[3]) < min(rectangle2[1], rectangle2[3]) \
        or max(rectangle2[1], rectangle2[3]) < min(rectangle1[1], rectangle1[3]) \
            or min(rectangle1[0], rectangle1[2]) > max(rectangle2[0], rectangle2[2]) \
                or min(rectangle2[0], rectangle2[2]) > max(rectangle1[0], rectangle1[2]):
        return False
    else:
        return True

# проверки

# print(is_cross([-5, 2, 3, -2], [2, 6, 5, 1])) # True
#
# print(is_cross([-5, 2, 3, -2], [2, 6, 5, 4])) # False
#
# print(is_cross([-5, 2, 3, -2], [2, 6, -10, 1])) # True
#
# print(is_cross([1, 4, 4, 2], [1, 1, 4, -1])) # False
#
# print(is_cross([-5, 4, -1, 1], [1, -1, 5, -4])) # False


# def is_cross(r1, r2):
#     # Изначально считаем, что прямоугольники пересекаются.
#     cross = True
#
#     # Разделяем координаты
#     r1x1, r1y1, r1x2, r1y2 = r1
#     r2x1, r2y1, r2x2, r2y2 = r2
#
#     # Логически проверяем варианты, когда прямоугольники не пересекаются
#     if (r2x1 > r1x2) or (r2x2 < r1x1) or (r2y2 > r1y1) or (r2y1 < r1y2):
#         cross = False
#
#     return cross